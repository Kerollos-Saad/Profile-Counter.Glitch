from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time

# CONFIG
Github_UserName = "kerollos-saad"
URL = f"https://profile-counter.glitch.me/{{{Github_UserName}}}/count.svg"
REFRESH_COUNT = 1500
DELAY_SECONDS = 0.1

# Set up the Chrome driver
# Start Edge WebDriver
service = Service()  # Will look for msedgedriver in PATH
driver = webdriver.Edge(service=service)

# Open the webpage
driver.get(URL)

# Refresh the page X times
for i in range(REFRESH_COUNT):
    print(f"Refreshing {i + 1}/{REFRESH_COUNT}")
    time.sleep(DELAY_SECONDS)
    driver.refresh()

# Optional: Close the browser after completion
driver.quit()

