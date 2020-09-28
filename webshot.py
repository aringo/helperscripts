#!/usr/bin/env python3
# I wanted a screenshot that showed URL and browser area

import sys 
import argparse
from time import sleep
from selenium import webdriver
import pyscreenshot as ImageGrab
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options



def main(args):

    tag_count = 0
    results_image = args.tag
    time_to_wait = args.time_to_wait
    urls = args.urls
    driver = webdriver.Firefox()
    driver.set_window_rect(x=5, y=17, width=1200, height=800)
    for url in urls:
        driver.get(url)
        sleep(time_to_wait)
        webbox = (5, 17, 1200, 800)
        im = ImageGrab.grab(webbox)
        if tag_count >= 1:
            save_image =  f"{results_image}_{tag_count}.png"
        else:
            save_image = f"{results_image}.png"
        print(f"Saved {url} : {save_image}")
        im.save(save_image)
        im.close()
        tag_count += 1
    driver.quit()
       

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Screenshots URLs")
    parser.add_argument("urls",nargs='*')
    parser.add_argument("-tag",action="store",dest="tag",help="What to tag",default="screenshot")
    parser.add_argument("-s",action="store",type=int,dest="time_to_wait",help="time to wait on DOM",default=3)
    args = parser.parse_args()
    main(args)
