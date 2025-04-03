import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth

r_clean = re.compile(r'[^\d,]+')

options = Options()
options.add_argument('--headless')  # běží bez GUI
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36')
options.add_argument("--window-size=1920,915")
options.headless = False

driver = webdriver.Chrome(options=options)

from selenium_stealth import stealth
stealth(driver, languages=["en-US"], vendor="Google Inc.", platform="Win32",
        webgl_vendor="Intel Inc.", renderer="Intel Iris OpenGL Engine", fix_hairline=True)

from_iata = 'VIE'
to_iata = 'TFS'
departure_date = '2025-04-03'
return_date = '2025-04-08'


#url = f'https://www.ryanair.com/cz/cs/booking/home/{from_iata}/{to_iata}/{departure_date}/{return_date}/1/0/0/0'
url = f'https://www.wizzair.com/en-gb/booking/select-flight/{from_iata}/{to_iata}/{departure_date}/{return_date}/1/0/0/null'
driver.get(url)

#time.sleep(5)

print(driver.title)

try:
    try:
        cookie_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "onetrust-reject-all-handler"))
        )
        print("Klikám na 'Odmítnout všechny cookies'...")
        cookie_button.click()
    except:
        print("Tlačítko 'Odmítnout cookies' se nezobrazilo.")

    time.sleep(5)
    driver.save_screenshot("screenshot.png")


    # test if there is departure element
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "current-price"))
    )

    print("Načteny ceny...")

    prices = driver.find_elements(By.CLASS_NAME, "current-price")

    if prices:
        print(f"Nalezeno {len(prices)} cen:")
        for i, p in enumerate(prices, 1):
            text = p.text.strip()
            if text:
                print(f"Cena #{i}: {text}")
    else:
        print("Žádné ceny nebyly nalezeny.")

except Exception as e:
    print("Chyba při získávání dat:", e)

driver.quit()