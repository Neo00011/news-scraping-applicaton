import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import csv
from os import system
haberler=[]
dosya="C:/Users/yakup/OneDrive/Desktop/projeler/proje5/haberler.csv"
news=[]
control=False
while True:
    url = "https://tr.euronews.com/son-haberler"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    print(requests.get(url).status_code)
    # Haber kartları
    cards = soup.select("div.o-timeline__main li.js-timeline-item.c-timeline-items__content")
    system("cls")
    print("— SON HABERLER —".center(60, "-"))
    print()
    
    
    
    time.sleep(1.5)
    for card in cards[:15]:                            # ilk 15 haber
        # Başlık
        h2 = card.find("h2", class_="c-timeline-items__article__title")
        if not h2:
            continue
        title = h2.get_text(strip=True)

        # Link
        a_tag = card.find("a",class_="c-timeline-items__article__link")
        link  = urljoin(url, a_tag["href"]) if a_tag else "—"

        # Saat & tarih
        time_tag = card.find("p", class_="c-item-time")
        date_tag = card.find("p", class_="c-item-date")

        time1 = time_tag.get_text(strip=True) if time_tag else "?"
        date = date_tag.get_text(strip=True) if date_tag else "?"
        print(f"Haber: {title}\nSaat: {time1}  Tarih: {date}\nLink: {link}\n")

        haberler.append([title, time1, date, link])
        time.sleep(0.2)
    
    with open(dosya,"w",newline="",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerow(["Haber","Saat","Tarih","Link"])
        writer.writerows(haberler)
    
    time.sleep(10)