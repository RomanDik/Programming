import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
if not os.path.exists('dataset'):
    os.mkdir('dataset')
if not os.path.exists('dataset/polar_bear'):
    os.mkdir('dataset/polar_bear')
if not os.path.exists('dataset/brown_bear'):
    os.mkdir('dataset/brown_bear')
def driver_scroller(driver, pix):
    
    sroll_range = 0
    while sroll_range < pix:
        driver.execute_script(f"window.scrollTo(0, {sroll_range});") 
        sroll_range += 4


full_list_polar_bear=[]
full_list_brown_bear=[]

def make_driver_with_link(link, path_name, name):
    global full_list_polar_bear,  full_list_brown_bear
    driver = webdriver.Opera()
    driver.get(link)
    time.sleep(4)
    driver_scroller(driver, 20000)
    list_pictures = driver.find_elements(By.XPATH, path_name)
    if name=="polar_bear":
        full_list_polar_bear += list_pictures
    if name=="brown_bear":
        full_list_brown_bear += list_pictures
    print(len(full_list_polar_bear),len(full_list_brown_bear))
    for i in range(6):
     if len(full_list_polar_bear) < 1010:
        make_driver_with_link(f"https://yandex.ru/images/search?p={i}&from=tabbar&text=polar bear&lr=51&rpt=image", "//img[@class='serp-item__thumb justifier__thumb']","cat")
        time.sleep(10)
    for i in range(6):        
     if len(full_list_brown_bear) < 1010:
        make_driver_with_link(f"https://yandex.ru/images/search?p={i}&from=tabbar&text=brown bear&lr=51&rpt=image", "//img[@class='serp-item__thumb justifier__thumb']", "dog")
        time.sleep(10)


def make_name(value):
    return '0'*(4-len(str(value))) + str(value)

def save_pictures():
    global full_list_polar_bear,  full_list_brown_bear
    directory_polar_bear = "dataset/polar_bear"
    directory_dog = "dataset/brown_bear"
    print(f'lens: {len(full_list_polar_bear)}, {len(full_list_brown_bear)}')
    for elem in range(len(full_list_polar_bear)):
        img = urllib.request.urlopen(full_list_polar_bear[elem].get_attribute('src')).read()
        out = open(f"{directory_polar_bear}/{make_name(elem)}.jpg", "wb")
        out.write(img)
        out.close
    for elem in range(len(full_list_brown_bear)):
        img = urllib.request.urlopen(full_list_brown_bear[elem].get_attribute('src')).read()
        out = open(f"{directory_dog}/{make_name(elem)}.jpg", "wb")
        out.write(img)
        out.close
if __name__ == "__main__":
    save_pictures()