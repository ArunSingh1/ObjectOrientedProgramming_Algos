import unittest
from Resturant import Resturant
from Menu import Menu

class Test_Restraunt(unittest.TestCase):

    def setUp(self):
        self.res = Resturant('Arun Restraunt', '119  Villejuif Paris')
        self.menu = Menu([{'Menu_item_id': 99, 'Menu_item_name': 'Vegetable Stir-Fry', 'Menu_item_desc': 'Assorted sushi rolls with fresh fish and rice', 'Menu_item_prize': 5.5}])

    def test_name_description(self):
        self.assertEqual(self.res.name_restraunt, "Arun Restraunt")
        self.assertEqual(self.res.address_restraunt,  '119  Villejuif Paris')

    def test_private_params(self):
        with self.assertRaises(AttributeError):
            name_restraunt = self.res.__name_restraunt
            address_restraunt = self.res.__address_restraunt

    def test_find_menuitem_detail(self):
        menuitem_tofind= 99
        result = self.menu.find_menuitem_detail(menuitem_tofind)
        expected_menuitem = {'Menu_item_id': 99, 'Menu_item_name': 'Vegetable Stir-Fry', 'Menu_item_desc': 'Assorted sushi rolls with fresh fish and rice', 'Menu_item_prize': 5.5}
        self.assertEqual(result, expected_menuitem) 







if __name__ == '__main__':
    unittest.main()