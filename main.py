from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path="/home/abhigyan/Desktop/chrome_driver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.python.org/")
# price = driver.find_element(By.XPATH, "/html/body/div/div[3]/div/section/div[3]/div[2]/div/ul/li[1]/a")
# print(price.text)

# driver.get("https://www.python.org/")
# event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
# events = {}
# for time in event_times:
#     print(time.text)
#
# for name in event_names:
#     print(name.text)

# for n in range(len(event_times)):
#     events[n] = {
#         "time": event_times[n].text,
#         "names":event_names[n].text,
#     }
#
# print(events)

# driver.close()
driver.quit()