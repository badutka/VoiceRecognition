from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from voice_recognition import speak, get_query
import time


def get_links(driver):
    driver.find_element_by_css_selector("button.style-scope.ytd-searchbox#search-icon-legacy").click()
    return [my_href.get_attribute("href") for my_href in WebDriverWait(driver, 5).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR,
                                               "a.yt-simple-endpoint.style-scope.ytd-video-renderer#video-title")))]


def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(executable_path='/home/bartosz/Pobrane/chromedriver_linux64/chromedriver',
                              chrome_options=chrome_options)
    return driver


def type_to_yt_searchbar(driver, query):
    # inputElement = driver.find_element_by_id("search")
    # inputElement = driver.find_element_by_id("search")
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#search"))).send_keys(query) #bez dropdownu
    searchbar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "search"))) # z dropdownem
    searchbar.send_keys(query)
    # inputElement.send_keys(query)
    searchbar.send_keys(Keys.ENTER)
    # inputElement.send_keys(Keys.ENTER)
    '''
    links = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, "video-title")))
    print(links)
    for x in links:
        print(x.get_attribute("href"))
    '''


def handle_youtube(engine):
    driver = get_driver()
    driver.get('https://www.youtube.com/?hl=pl&gl=PL')
    speak(engine, "What do you want to search for?")
    query = get_query(engine)
    # if 'go to sleep' in query.lower():
    #     speak(engine, "Initializing sleep mode.")
    #     return
    type_to_yt_searchbar(driver, query)
    time.sleep(1)
    links = get_links(driver)
    speak(engine, "Please tell me the number of a video you would like to watch.")
    print(links)
    query = get_query(engine)
    # if 'go to sleep' in query.lower():
    #     speak(engine, "Initializing sleep mode.")
    #     return
    # print(int(query[-1]))
    driver.get(links[int(query[-1]) - 1])
