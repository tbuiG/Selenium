from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://youtu.be/j3qgmlwMsQI")
driver.maximize_window()
driver.implicitly_wait(10)

driver.execute_script(
    "window.open('https://box.live/upcoming-fights-schedule/','secondtab');")
driver.switch_to.window("secondtab")
# driver.get("https://neetcode.io/")

# element = driver.find_element(By.XPATH, "//button[@routerlink='/practice']")
# element.click()

driver.execute_script(
    "window.open('https://www.google.com/search?q=ufc&rlz=1C1CHBF_enUS744US744&oq=ufc&aqs=chrome.0.69i59j69i60l4.487j0j7&sourceid=chrome&ie=UTF-8','thirdtab');")
driver.switch_to.window("thirdtab")
# driver.get("https://box.live/")

# bschedule = driver.find_element(By.PARTIAL_LINK_TEXT, 'View ')
# bschedule.click()
