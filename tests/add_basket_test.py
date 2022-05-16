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

        # wpisanie produktuw polewyszukiawnia
        home_page.search_area(TestData.search_prod)





