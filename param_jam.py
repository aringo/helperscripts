#!/usr/bin/env python3

## requires pyscreenshot in addition to selenium for firefox

import sys 
import argparse
from time import sleep
from selenium import webdriver
import pyscreenshot as ImageGrab
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


report_results=""


def generate_test_urls(url):
    urls_to_test = {}
    try:
        params=url.split('?')[1]
    except:
        print("Could not find parameters")
        sys.exit()
    params_url=params.split('&')
    print(f'Testing the following params {params_url}')
    for param in params_url:
        base_param,param_arg = param.split("=")
        new_param = base_param+'=XSS'
        meh = f"{url.replace(param,new_param)}"
        urls_to_test[base_param]=meh
    return urls_to_test


def document(payload,canary,param,time_to_wait):
    global report_results
    results_image = f"{param}.png"
    options = webdriver.FirefoxOptions()
    options.headless = False
    driver = webdriver.Firefox(options=options)
    driver.set_window_rect(x=5, y=17, width=1200, height=800)
    payload = payload.replace(canary,"document.domain")
    document_param = f"It was found that the {param} parameter was vulnerable to reflected cross-site scripting.  "
    document_param += f"To verify this vulnerability clicking on the link at \'{payload}\' will show the domain the code is executing in.  "
    document_param += f"This results of this action can be seen in the attached {results_image} image.\n"
    report_results += document_param
    driver.get(payload)
    sleep(time_to_wait)
    webbox = (5, 17, 1200, 800)
    im = ImageGrab.grab(webbox)
    im.save(results_image)
    im.close()
    driver.quit()



def main(args):
    options = webdriver.FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    time_to_wait = args.time_to_wait
    canary = args.canary
    test_urls = generate_test_urls(args.url)
    for param,generated_url in test_urls.items():
        print(f"Testing {param} with {generated_url}")
        payload = generated_url.replace("=XSS",f"=<script>alert({canary})</script>")
        driver.get(payload)   
        try:
            sleep(time_to_wait)
            try:
                alert = driver.switch_to.alert
                if alert.text == canary:
                    alert.accept()
                    document(payload,canary,param,time_to_wait)
                driver.quit()
            except:
                driver.quit()
                pass
        except:
            pass
    if report_results:
        with open("XSS_report.txt",'w') as f:
            f.write(report_results)
    else:
        print("No XSS found in parameters")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="XSS check to documentation")
    parser.add_argument("-u",action="store",dest="url",help="url")
    parser.add_argument("-c",action="store",dest="canary",help="what it looks for in alert",default="99")
    parser.add_argument("-t",action="store",type=int,dest="time_to_wait",help="time to wait on DOM",default=5)
 
    args = parser.parse_args()
    main(args)
