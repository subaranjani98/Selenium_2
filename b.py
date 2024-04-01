from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()

# Open URL
driver.get("https://www.cowin.gov.in/")

# Wait for the "FAQ" link to be clickable
faq_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'FAQ')]")))
faq_link.click()

# Wait for the "Partners" link to be clickable
partners_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Partners')]")))
partners_link.click()

# Get window handles for all open windows
window_handles = driver.window_handles

# Display window IDs and frame IDs
for handle in window_handles:
    driver.switch_to.window(handle)
    print("Window ID:", handle)

    # Fetch and display frame IDs
    frame_elements = driver.find_elements(By.TAG_NAME,'frame') + driver.find_elements(By.TAG_NAME,'iframe')
    if frame_elements:
        for frame in frame_elements:
            print("Frame ID:", frame.get_attribute("id"))
    else:
        print("No frames found in this window.")

# Close the new windows
for handle in window_handles:
    driver.switch_to.window(handle)
    if handle != driver.current_window_handle:
        driver.close()

# Switch back to the main window
driver.switch_to.window(window_handles[0])

# Close the browser
driver.quit()


import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to create a folder if it doesn't exist
def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# Initialize WebDriver
driver = webdriver.Chrome()

# Open URL
driver.get("https://labour.gov.in/")

# Task 1: Download Monthly Progress Report from "Documents" menu
try:
    documents_menu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Documents']")))
    documents_menu.click()

    # Find and click on "Monthly Progress Report" link
    monthly_report_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Monthly Progress Report')]")))
    monthly_report_link.click()

    # Download the report
    report_url = driver.current_url
    response = requests.get(report_url)
    with open("Monthly_Progress_Report.pdf", "wb") as file:
        file.write(response.content)

    print("Monthly Progress Report downloaded successfully.")
    
except Exception as e:
    print("Error downloading Monthly Progress Report:", str(e))

# Task 2: Download 10 photos from "Photo Gallery" under "Media" menu
try:
    # Navigate to "Media" menu
    media_menu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Media']")))
    media_menu.click()

    # Navigate to "Photo Gallery" submenu
    photo_gallery_submenu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Photo Gallery']")))
    photo_gallery_submenu.click()

    # Create a folder to store downloaded photos
    folder_name = "Labour_Department_Photos"
    create_folder(folder_name)

    # Download 10 photos
    photo_elements = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".owl-item img")))
    for i, photo_element in enumerate(photo_elements[:10], start=1):
        photo_url = photo_element.get_attribute("src")
        photo_filename = f"photo_{i}.jpg"
        photo_path = os.path.join(folder_name, photo_filename)
        response = requests.get(photo_url)
        with open(photo_path, "wb") as file:
            file.write(response.content)
        print(f"Downloaded photo {i}.")

    print("Photos downloaded successfully.")

except Exception as e:
    print("Error downloading photos:", str(e))

# Close the browser
driver.quit()