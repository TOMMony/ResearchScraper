from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class ICSScraper:
    def __init__(self) -> None:
        cOptions = Options()
       # cOptions.add_experimental_option("detach", True)
        cService = webdriver.chrome.service.Service(executable_path = 'C:/Users/theor/Downloads/chromedriver-win64/chromedriver.exe')
        self.driver = webdriver.Chrome(service = cService, )
        self.people_pages = []

    def open_site(self, url) -> None:
        self.driver.get(url)

    def _load_people_pages(self) -> None:
        directory_page = 1
        while directory_page == 1 or len(pages) > 0:
            pages = self.driver.find_elements(By.XPATH, '//a[@class=" item__link"]')
            self.people_pages += [page.get_attribute('href') for page in pages]
            self.driver.get(f'https://ics.uci.edu/people/page/{directory_page + 1}/')
            directory_page += 1
        print(len(self.people_pages))
    
    def get_valid_website(self) -> str:
        for people in self.people_pages:
            self.driver.get(people)
            try:
                personal_page = self.driver.find_element(By.XPATH, '//a[@class=" person__link c-text-btn"]') 
            except:
                continue
            yield personal_page
        