from settings import email, password
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('C:\git\chromedriver.exe')

   pytest.driver.implicitly_wait(10)
   pytest.driver.get('http://petfriends.skillfactory.ru/login')
   yield
   pytest.driver.quit()

def test_show_my_pets():

   pytest.driver.find_element_by_id('email').send_keys(email)

   pytest.driver.find_element_by_id('pass').send_keys(password)

   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"


   pytest.driver.implicitly_wait(10)
   images = pytest.driver.find_elements_by_css_selector('div#all_my_pets>table>tbody>tr>th>img')
   pytest.driver.implicitly_wait(10)
   names = pytest.driver.find_elements_by_xpath('//tr/th/following-sibling::td[1]')
   pytest.driver.implicitly_wait(10)
   types = pytest.driver.find_elements_by_xpath('//tr/th/following-sibling::td[2]')
   pytest.driver.implicitly_wait(10)
   ages = pytest.driver.find_elements_by_xpath('//tr/th/following-sibling::td[3]')


   user_stat_element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "html>body>div>div>div")))
   user_pets_count = int(user_stat_element.text.split("\n")[1].split(":")[1].strip())
   #user_pets_count = int(pytest.driver.find_element_by_css_selector('html>body>div>div>div').text.split("\n")[1].split(":")[1].strip())


   assert len(data_my_pets) == all_my_pets


   m = 0
   for i in range(len(image_my_pets)):
       if image_my_pets[i].get_attribute('src') != '':
           m += 1
   assert m >= all_my_pets / 2

   for i in range(len(name_my_pets)):
       assert name_my_pets[i].text != ''

   for i in range(len(type_my_pets)):
       assert type_my_pets[i].text != ''

   for i in range(len(age_my_pets)):
       assert age_my_pets[i].text != ''


   list_name_my_pets = []
   for i in range(len(name_my_pets)):
      list_name_my_pets.append(name_my_pets[i].text)
   set_name_my_pets = set(list_name_my_pets)
   assert len(list_name_my_pets) == len(set_name_my_pets)


   list_data_my_pets = []
   for i in range(len(data_my_pets)):
      list_data = data_my_pets[i].text.split("\n")
      list_data_my_pets.append(list_data[0])
   set_data_my_pets = set(list_data_my_pets)
   assert len(list_data_my_pets) == len(set_data_my_pets)