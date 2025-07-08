from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import io
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=chrome_options)

ticker = "AAPL"
options_url = f"https://sg.finance.yahoo.com/quote/AAPL/options/?date=1766102400"

driver.get(options_url)
time.sleep(5)
tables = pd.read_html(io.StringIO(driver.page_source))
date_button = driver.find_element(By.XPATH, '//button[@data-type="date"]')
expiry = date_button.get_attribute("aria-label")
driver.quit()

calls = tables[0]
puts = tables[1]
calls['expiry'] = expiry
puts['expiry'] = expiry
calls.to_csv(f"{ticker}_call_options_{expiry}.csv", index = False)
puts.to_csv(f"{ticker}_put_options_{expiry}.csv", index = False)
