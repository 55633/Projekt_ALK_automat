import unittest
from pages.searched_basket_page import Searched_Basket_Page
from tests.base_test import BaseTest
from pages.home_page import HomePage
from tests.test_data import TestData
from pages.authentication_page import AuthenticationPage
from pages.base_page import BasePage
from pages.create_an_account_page import CreateAnAccountPage
from time import sleep
from selenium import webdriver


class AddBasketTest(BaseTest):
    """
     Dodaje produkt do koszyka
    """

    def test_add_basket(self):
        """
        TC 006: dodanie do koszyka
        """
        home_page = self.home_page

        # 1. wpisanie produktu w polewyszukiawnia
        wpisanie_produktu = home_page.search_area(TestData.item)

        # 2. Klikniecie Szukaj
        search_list = home_page.clc_search()

        # 3. wybierz pierwszy produkt
        first_prod_click = Searched_Basket_Page.first_item(self)

        # 4. Pobranie nazwy do późniejszego porównania
        product_name = Searched_Basket_Page.pull_product_name(self)
        sleep(3)
        #5. Dodanie do koszyka

        add_to_basket = Searched_Basket_Page.add_product(self)
        sleep(3)
        # 6. przejdź do koszyka

        jump_to_basket = Searched_Basket_Page.jump_to_basket(self)
        sleep(3)
        # 7. Zapisz nazwę produktu z koszyka do porównania
        prod_basket_name = Searched_Basket_Page.name_product_basket(self)

        # Oczekiwany rezultat:
        # 1. weryfikacja, czy produkt  dodany do i w  koszyku to ten sam produkt

    def assertion_product_name(self):
        # pobranie i porównanie nazwy produktu z pierwszego i drugiego pliku

        file = open("pull_product_name.txt")
        product1 = file.read()
        print(f'Produkt zakupiony:', product1)

        file2 = open('product_name_in.txt')
        product2 = file2.read()
        print(f'Produkt w koszyku:', product2)

        assert product1 == product2

        file.close()
        file2.close()









