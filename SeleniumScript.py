from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

# CONFIG
Github_UserName = "kerollos-saad"
URL = f"https://profile-counter.glitch.me/{{{Github_UserName}}}/count.svg"
REFRESH_COUNT = 1500
DELAY_SECONDS = 0.1

#Already Install Edge WebDriver
# Start Edge WebDriver
service = Service()  # Will look for msedgedriver in PATH
driver = webdriver.Edge(service=service)

# Setup Edge with automatic WebDriver installation For First Time
# driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

# Open the webpage
driver.get(URL)

# Refresh the page X times
for i in range(REFRESH_COUNT):
    print(f"Refreshing {i + 1}/{REFRESH_COUNT}")
    time.sleep(DELAY_SECONDS)
    driver.refresh()

# Optional: Close the browser after completion
driver.quit()

