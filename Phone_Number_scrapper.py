import requests
from bs4 import BeautifulSoup
import re


url = "https://www.netapp.com/company/contact-us/"  
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    phone_pattern = re.compile(r"\+?\(?\d{1,4}\)?[\s.-]?\(?\d{1,4}\)?[\s.-]?\d{1,4}[\s.-]?\d{1,4}")
    phone_numbers = set(re.findall(phone_pattern, soup.get_text()))

    if phone_numbers:
        print("Phone numbers found:")
        for number in phone_numbers:
            print(number)
    else:
        print("No phone numbers found.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
