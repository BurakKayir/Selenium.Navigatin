import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.sahibinden.com")
time.sleep(10)

#time.sleep(15)
#alert1= driver.find_element(By.XPATH,"//*[@id='onetrust-reject-all-handler']")
#alert1.click()
#alert2=driver.find_element(By.XPATH,"//*[@id='btn-continue']")
#alert2.click()

#time.sleep(5)
alert1= driver.find_element(By.XPATH,"//*[@id='onetrust-reject-all-handler']")
alert1.click()
time.sleep(5)

try:
    search_box= driver.find_element(By.XPATH, "//*[@id='searchText']")
    search_box.click()
    search_box.send_keys("RCZ")
    time.sleep(2)
    search_box.clear()
    search_box.send_keys("GTI")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    cat= driver.find_element(By.XPATH, "//*[@id='wideContainer']/div/div[2]/ul/li[2]/ul/li[1]/a")
    cat.click()
    time.sleep(2)
    gallery = driver.find_element(By.XPATH, "//*[@id='searchResultsSearchForm']/div/div[3]/div[1]/div[3]/ul/li[3]/a")
    gallery.click()
    time.sleep(2)
    #search_box.send_keys(Keys.RETURN)
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    while True:
        # scroll to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # wait for the page to load
        time.sleep(2)

        # get the new page height
        new_height = driver.execute_script("return document.body.scrollHeight")

        # check if the page height has changed
        if new_height == last_height:
            # if the page height has not changed, we have reached the bottom
            break

        # set the last height to the new height and continue the loop
        last_height = new_height

        time.sleep(5)
        driver.save_screenshot('myshot.png')
    print("Found it and clicked it")
except:
    print("No such element, Sooooory")

driver.quit()
