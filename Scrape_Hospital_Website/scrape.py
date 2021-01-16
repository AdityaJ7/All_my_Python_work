import requests
from bs4 import BeautifulSoup

all_links = set()
all_names = set()

number_of_pages_to_scrape = 1
# Total no of pages are 188 which can be put here


def get_links():
    i = 1
    while i <= number_of_pages_to_scrape:
        url = f"https://doctors.ololrmc.com/search?sort=networks&page={i}"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        links = soup.find_all(
            'h2', class_="css-1yi8h8m-ProviderName e16v8r6n5")
        for link in links:
            all_links.add(link.a['href'])
        i += 1


def get_names():
    for link in all_links:
        r_2 = requests.get("https://doctors.ololrmc.com"+link)
        soup_2 = BeautifulSoup(r_2.text, 'html.parser')
        name = soup_2.find('h1', class_="fw-6 fs-l").span.text
        position = name.find("About")
        all_names.add(name[position+6:])




if __name__ == "__main__":
    get_links()
    get_names()
    
    for name in all_names:
        print(name)
