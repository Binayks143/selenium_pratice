import requests
from selenium import webdriver

driver=webdriver.Chrome()

driver.get(url)
# Set the URL of the page you want to record the response from
url = "https://www.scaler.com/topics/append-to-file-python/"

# Send a GET request to the URL
response = requests.get(url)

# Get the status code of the response
status_code = response.status_code

# Print the status code to the console
print("Status code:", status_code)

# Write the response content to a file
with open("response.txt", "w") as f:
    f.write(response.text)
