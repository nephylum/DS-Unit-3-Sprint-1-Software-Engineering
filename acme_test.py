#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, adj_list, noun_list


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_product_flammability(self):
        """Test default product flammability being 0.5"""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)


class AcmeReportTests(unittest.TestCase):
    """Testing the Methods"""

    def test_default_num_products(self):
        """Check if the list generated is proper length"""
        p_list = generate_products()
        self.assertEqual(len(p_list), 30)

    def test_legal_names(self):
        p_list = generate_products()
        self.assertIn(' ', p_list[0].name)


if __name__ == '__main__':
    unittest.main()
