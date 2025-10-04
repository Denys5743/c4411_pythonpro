from bs4 import BeautifulSoup
import requests
res_parse_list = []
response = requests.get("https://coinmarketcap.com/")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    soup_list = soup.find_all(name="divs", attrs={"class": "sc-fa25c04c-0"})


    res = soup_list[0].find("span")
    print(res.text)
