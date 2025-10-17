import requests, sqlite3
from bs4 import BeautifulSoup
from datetime import datetime

r = requests.get("https://meteofor.com.ua/weather-chernihiv-4923/", headers={"User-Agent":"Mozilla/5.0"})
t = BeautifulSoup(r.text, "html.parser").find("div", class_="weather-now-temperature").text.strip()
d = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

conn = sqlite3.connect("weather.db")
conn.execute("CREATE TABLE IF NOT EXISTS weather(datetime TEXT, temperature TEXT)")
conn.execute("INSERT INTO weather VALUES(?,?)", (d, t))
conn.commit()
conn.close()

print(d, t)
