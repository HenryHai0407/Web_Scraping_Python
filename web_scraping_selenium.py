from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

name = "Hoang Hai"

# Initialize WebDriver (Make sure to specify the correct path to your ChromeDriver)
driver = webdriver.Chrome() 

#Open a website from your choice
driver.get("https://books.toscrape.com/catalogue/page-2.html")

# Wait for JavaScript to load (optional)
time.sleep(4)

products = driver.find_elements(By.CSS_SELECTOR, "h3 a")

# Prepare data to save to targeted file
product_titles = [product.get_attribute('title') for product in products]

csv_file = 'product_titles.csv'

# Write data to CSV files
with open(csv_file, mode='w', newline= '', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['The title of products'])
    for title in product_titles:
        writer.writerow([title])

# Close the browser
driver.quit()

print(f'Successfully saved {len(product_titles)} titles of product to {csv_file}.')