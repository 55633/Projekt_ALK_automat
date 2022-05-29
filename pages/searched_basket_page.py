from pages.base_page import BasePage
from pages.locators import ProduktsLocators

class Searched_Basket_Page(BasePage):

    def first_item(self):
        fp = self.driver.find_element(*ProduktsLocators.FIRST_PROD)
        fp.click()


    def pull_product_name(self):
        pu = self.driver.find_element(*ProduktsLocators.PROD_NAME_P)
        product_name = pu.get_attribute("innerText")
        print(f'Produkt dodany do koszyka to:', product_name)
    # Zapisanie do późniejszego porównania do pliku
        file = open("pull_product_name.txt", "w")
        file.write(product_name)
        file.close()

    def add_product(self):
        ap = self.driver.find_element(*ProduktsLocators.ADD_BTN)
        ap.click()

    def jump_to_basket(self):
        jb = self.driver.find_element(*ProduktsLocators.BASKET_BTN)
        jb.click()

    def name_product_basket(self):
        ni = self.driver.find_element(*ProduktsLocators.IN_BASKET_PROD_NAME)
        product_name = ni.get_attribute("innerText")
        print(f'Produkt w koszyku to:', product_name)
        file1 = open("product_name_in.txt", "w")
        file.write(product_name)
        file.close()










