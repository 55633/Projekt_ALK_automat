from tests.base_test import BaseTest

from time import sleep
import unittest

#TC5
from tests.test_data import TestData


class AddBasketTest(BaseTest):
    """
     Dodaje produkt do koszyka
    """

    def test_no_name(self):
        """
        TC 005: dodanie do koszyka
        """
        home_page = self.home_page

        # 1. wpisanie produktuw polewyszukiawnia
        home_page.search_area(TestData.search_prod)

        # 2. Klikniecie Szukaj
        search_list = home_page.clc_search()

        # wybierz pierwszy produkt
        first_item_click = search_list.click_first_item()





