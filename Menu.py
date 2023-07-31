class Menu():    

    allmenuitem = []

    def __init__(self, listall_menus) -> None:
        self.listall_menus = listall_menus
        self.allmenuitem.extend(listall_menus)  
        # Menu.all_menus.append(self)

    def display_all_menus(self):
        for menu_item in self.listall_menus:
            print(f"Menu Item ID   : {menu_item['Menu_item_id']}")
            print(f"Menu Item Name : {menu_item['Menu_item_name']}")
            print(f"Menu Item Desc : {menu_item['Menu_item_desc']}")
            print(f"Menu Item Prize: {menu_item['Menu_item_prize']}")
            print()

    def add_new_menu(self,  newmenu:dict):
       
        self.listall_menus.append(newmenu)
        print("New menu added successfully." , newmenu)


    def find_menuitem_detail(self, menuitem_tofind:int):
     
        res = None
        for menu in self.listall_menus:
            if menu.get('Menu_item_id') ==  menuitem_tofind:
                res = menu
                # print(res)
                break

        else:
            print('Menu not Available')
        return res

    
    def find_priceof_menu(self, menuitem_pricetofind):

        res = None
        for menu in self.listall_menus:
            if menu.get('Menu_item_name') ==  menuitem_pricetofind:
                # print(menu)
                # print(menu.get('Menu_item_prize'))
                res = menu.get('Menu_item_prize')
            #     # print(res)
                break

        else:
            print('Menu not Available')
        return  f"price of '{menuitem_pricetofind}' is '{res}'"
            
    def __repr__(self) -> str:
        return f" Menus - '{self.listall_menus}' "


menus = Menu([{'Menu_item_id': 1, 'Menu_item_name': 'Caesar Salad', 'Menu_item_desc': 'Delicious spaghetti with Bolognese sauce', 'Menu_item_prize': 7.5},
{'Menu_item_id': 2, 'Menu_item_name': 'Pad Thai', 'Menu_item_desc': 'Grilled salmon with lemon and herbs', 'Menu_item_prize': 6.0},
{'Menu_item_id': 3, 'Menu_item_name': 'Grilled Salmon', 'Menu_item_desc': 'Tender BBQ ribs with BBQ sauce', 'Menu_item_prize': 14.5},
{'Menu_item_id': 4, 'Menu_item_name': 'Sushi Roll', 'Menu_item_desc': 'Healthy stir-fried vegetables with soy sauce', 'Menu_item_prize': 9.5},
{'Menu_item_id': 5, 'Menu_item_name': 'Chicken Alfredo', 'Menu_item_desc': 'Creamy mushroom risotto with parmesan', 'Menu_item_prize': 9.0},
{'Menu_item_id': 6, 'Menu_item_name': 'Cheeseburger', 'Menu_item_desc': 'Traditional Margherita pizza with tomato and cheese', 'Menu_item_prize': 13.99},
{'Menu_item_id': 7, 'Menu_item_name': 'BBQ Ribs', 'Menu_item_desc': 'Flavorful Pad Thai with noodles and veggies', 'Menu_item_prize': 9.0},
{'Menu_item_id': 8, 'Menu_item_name': 'Cheeseburger', 'Menu_item_desc': 'Grilled salmon with lemon and herbs', 'Menu_item_prize': 12.5},
{'Menu_item_id': 9, 'Menu_item_name': 'Vegetable Stir-Fry', 'Menu_item_desc': 'Classic cheeseburger with fries', 'Menu_item_prize': 9.5},
{'Menu_item_id': 10, 'Menu_item_name': 'Sushi Roll', 'Menu_item_desc': 'Delicious spaghetti with Bolognese sauce', 'Menu_item_prize': 14.5},
{'Menu_item_id': 11, 'Menu_item_name': 'Grilled Salmon', 'Menu_item_desc': 'Assorted sushi rolls with fresh fish and rice', 'Menu_item_prize': 5.5},
{'Menu_item_id': 12, 'Menu_item_name': 'BBQ Ribs', 'Menu_item_desc': 'Classic cheeseburger with fries', 'Menu_item_prize': 14.5},
{'Menu_item_id': 13, 'Menu_item_name': 'Mushroom Risotto', 'Menu_item_desc': 'Assorted sushi rolls with fresh fish and rice', 'Menu_item_prize': 9.0},
{'Menu_item_id': 14, 'Menu_item_name': 'Spaghetti Bolognese', 'Menu_item_desc': 'Tender BBQ ribs with BBQ sauce', 'Menu_item_prize': 14.5},
{'Menu_item_id': 15, 'Menu_item_name': 'Cheeseburger', 'Menu_item_desc': 'Fresh Caesar salad with dressing', 'Menu_item_prize': 9.5},
{'Menu_item_id': 16, 'Menu_item_name': 'Grilled Salmon', 'Menu_item_desc': 'Fresh Caesar salad with dressing', 'Menu_item_prize': 10.5},
{'Menu_item_id': 17, 'Menu_item_name': 'Margherita Pizza', 'Menu_item_desc': 'Classic cheeseburger with fries', 'Menu_item_prize': 13.99},
{'Menu_item_id': 18, 'Menu_item_name': 'Sushi Roll', 'Menu_item_desc': 'Tender BBQ ribs with BBQ sauce', 'Menu_item_prize': 9.5},
{'Menu_item_id': 19, 'Menu_item_name': 'Cheeseburger', 'Menu_item_desc': 'Assorted sushi rolls with fresh fish and rice', 'Menu_item_prize': 8.99},
{'Menu_item_id': 20, 'Menu_item_name': 'Vegetable Stir-Fry', 'Menu_item_desc': 'Assorted sushi rolls with fresh fish and rice', 'Menu_item_prize': 5.5}])




# newmenu = {'Menu_item_id': 21, 'Menu_item_name': 'NON Spicy Vegetable Stir-Fry', 'Menu_item_desc': 'Assorted sushi rolls with fresh fish and rice', 'Menu_item_prize': 5.5}
# menus.add_new_menu(newmenu)
# print(menus.display_all_menus())


print(menus.find_menuitem_detail(14))

# print(menus.find_priceof_menu('BBQ Ribs'))
