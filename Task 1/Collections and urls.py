import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Set the path to the Microsoft Edge browser executable file
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# Set the path to the Edge webdriver executable file
edge_driver_path = r"C:\edgedriver_win64\msedgedriver.exe"

# Set the options for the Edge webdriver
options = webdriver.EdgeOptions()
options.binary_location = edge_path

# Set the service for the Edge webdriver
service = Service(executable_path=edge_driver_path)

# Create a new instance of the Edge webdriver
driver = webdriver.Edge(service=service, options=options)

# Navigate to the URL
url = "https://raritysniper.com/nft-collections"
driver.get(url)

# Wait for the page to load and for the "loading" overlay to disappear
wait = WebDriverWait(driver, 30)
wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "loading-overlay")))

# Scroll to the bottom of the page to load more collections
scroll_pause_time = 10
scroll_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)
    new_scroll_height = driver.execute_script("return document.body.scrollHeight")
    if new_scroll_height == scroll_height:
        break
    scroll_height = new_scroll_height

# Wait for the dynamic content to be fully loaded
try:
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "hit")))
except TimeoutException:
    print("Timeout waiting for element to appear")

# Extract the HTML content of the page
html = driver.page_source

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find all the NFT collection divs with class "hit"
nft_collections = soup.find_all("div", {"slot": "hit"})

# Extract the collection name and URL for each NFT collection
collection_names = []
collection_urls = []
for collection in nft_collections:
    name = collection.find("h4").text.strip()
    url = "https://raritysniper.com" + collection.find("a")["href"]
    collection_names.append(name)
    collection_urls.append(url)

# Print the collection names and URLs along with their length
print("Collection Names:", len(collection_names))
print(collection_names)
print("\nCollection URLs:", len(collection_urls))
print(collection_urls)

# Close the browser
driver.quit()
