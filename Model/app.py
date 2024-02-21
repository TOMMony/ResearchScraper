from scraper import ICSScraper
scraper = ICSScraper()
scraper.open_site('https://ics.uci.edu/people/')
scraper._load_people_pages()
for item in scraper.get_valid_website():
    print(item.get_attribute('href'))