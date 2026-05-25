from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import os

options = webdriver.ChromeOptions()
options.add_argument("--headless") 
driver = webdriver.Chrome(options=options)

# Open CricSheet matches page
url = "https://cricsheet.org/matches/"
driver.get(url)

# Absolute XPaths for the JSON download links
json_xpaths = {
    "ODI": "/html/body/div[3]/div/div[3]/dl/dd[4]/a[1]",
    "T20": "/html/body/div[3]/div/div[3]/dl/dd[6]/a[1]",
    "Test": "/html/body/div[3]/div/div[3]/dl/dd[2]/a[1]",
}

# Create a folder to save JSON files
download_folder = "cricsheet_json"
os.makedirs(download_folder, exist_ok=True)

# Function to download JSON files
def download_json(match_type, xpath):
    try:
        element = driver.find_element(By.XPATH, xpath)
        file_url = element.get_attribute("href")  # Get the direct JSON link
        file_name = file_url.split("/")[-1]

        response = requests.get(file_url)
        if response.status_code == 200:
            with open(os.path.join(download_folder, file_name), "wb") as file:
                file.write(response.content)
            print(f"Downloaded: {file_name}")
        else:
            print(f"Failed to download {match_type} JSON")
    except Exception as e:
        print(f"Error fetching {match_type}: {e}")

# Download JSON files for each match type
for match_type, xpath in json_xpaths.items():
    print(f"Downloading {match_type} JSON file...")
    download_json(match_type, xpath)

# Close the browser session
driver.quit()
print("\nAll JSON files downloaded successfully!")

