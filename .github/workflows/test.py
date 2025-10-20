from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service("/usr/bin/chromedriver")  # Chromium driver pat#h
#driver = webdriver.Chrome(service=service, options=options)
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.get("https://example.com")
print(driver.title)
driver.quit()
