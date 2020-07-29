#!/usr/bin/env python3
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
#driver = webdriver.Chrome('/usr/bin/chromedriver')

'''
# If extensions are needed
extension_dir = '/location/'
extensions = [ 
             "whatever.xpi"
            ]
for extension in extensions:
    driver.install_addon(extension_dir+extension,temporary=True)
'''

driver.get("https://login.synack.com/")
assert "Synack" in driver.title

#driver.switch_to.window(handles)
#driver.window_handles)



# I would hope I could log in within 120 seconds otherwise this errors..
time.sleep(120)
session = driver.execute_script("return sessionStorage.getItem('shared-session-com.synack.accessToken')")
print(session)
with open('/tmp/synacktoken',"w") as f:
    f.write(session)
    

accept_num = 1 
while True:
    
    try:
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        text = alert.text
        alert.accept()
        print(f"{session} extended {accept_num} \r",end="")
        accept_num += 1 
    except:
        pass
