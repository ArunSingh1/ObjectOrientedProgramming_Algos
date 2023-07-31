from Menu import Menu
from Payment import Payment

class Orders(Menu, Payment):

    all_orders = []

    def __init__(self, orders_list) -> None:
 
        self.orders_list = orders_list
        # self.all_orders.extend(orders_list)
        Menu.__init__(self, [])
        Payment.__init__(self, [])
        # super().__init__([])
        Orders.all_orders.append(self)

    @classmethod    
    def print_all_order_info(cls):
        
        for order_items in cls.all_orders:
            # print(order_items.orders_list)
            # print(type(order_items.orders_list))

            res = []
            if len(order_items.orders_list) > 0:            
                for i in range(0,len(order_items.orders_list)):
                    print('Created Orders', order_items.orders_list[i])   
            else:
                return False

        return True
    
    @classmethod
    def find_specific_order_detail(cls, orderid_tofind) :

        for order_items in cls.all_orders:
            res = []
            if len(order_items.orders_list) > 0:            
                for i in range(0, len(order_items.orders_list)):
                    if order_items.orders_list[i].get('Order_id') == orderid_tofind:
                        res = order_items.orders_list[i]

                        print(res)
                        print(f"{'Order_id': <15}: {order_items.orders_list[i].get('Order_id') }")
                        print(f"{'Order_Details': <15}: {order_items.orders_list[i].get('Order_Details') }")
                        print(f"{'Order_Time': <15}: {order_items.orders_list[i].get('Order_Time')}")
                        print(f"{'Ordered_Menu_ID': <15}: {order_items.orders_list[i].get('Ordered_Menu_ID') }")
                        print(f"{'Customer_ID': <15}: {order_items.orders_list[i].get('Customer_ID') }")
                    
                        break

                for menu in cls.allmenuitem:
                    # print(menus)

                    if menu.get('Menu_item_id') ==  order_items.orders_list[i].get('Ordered_Menu_ID') :
                        res = menu
                        print(res)
                        print(f"Menu Item ID   : {menu['Menu_item_id']}")
                        print(f"Menu Item Name : {menu['Menu_item_name']}")
                        print(f"Menu Item Desc : {menu['Menu_item_desc']}")
                        print(f"Menu Item Prize: {menu['Menu_item_prize']}")
                        print()
                        break
                
                for payment in cls.all_payments:
                     if payment.get('Order_id') == order_items.orders_list[i].get('Order_id'):
                        print(payment)
                        print(f"Payment reference   : {payment['Payment_ref']}")
                        print(f"Payment time : {payment['Payment_time']}")
                        print(f"Is_Payment_processed : {payment['Is_Payment_processed']}")
                        print(f"Customer_ID : {payment['Customer_ID']}")
                        print()
                        break
                


        return  res
    


    def __repr__(self) -> str:
        return  f"Order created - '{self.orders_list}'"
    





ordersbulk = Orders([{'Order_id':'ORD3243', 'Order_Details':'Pizza', 'Order_Time':'12.21am','Ordered_Menu_ID': 1, 'Customer_ID': 'CUST1235' },
               {'Order_id': 'ORDWFEA', 'Order_Details': 'Pizza MWLI', 'Order_Time': '10.32am', 'Ordered_Menu_ID': 1, 'Customer_ID': 'CUSTBEFA'},
                {'Order_id': 'ORDEHRR', 'Order_Details': 'Pizza FBTZ', 'Order_Time': '05.43am', 'Ordered_Menu_ID': 2, 'Customer_ID': 'CUSTWTIE'},
                {'Order_id': 'ORDRKQO', 'Order_Details': 'Pizza QFPI', 'Order_Time': '09.20pm', 'Ordered_Menu_ID': 3, 'Customer_ID': 'CUSTUBBQ'},
                {'Order_id': 'ORDGQIY', 'Order_Details': 'Pizza EVQT', 'Order_Time': '08.34pm', 'Ordered_Menu_ID': 4, 'Customer_ID': 'CUSTMAEF'},
                {'Order_id': 'ORDTYEL', 'Order_Details': 'Pizza RHSD', 'Order_Time': '07.39pm', 'Ordered_Menu_ID': 5, 'Customer_ID': 'CUSTXIDC'},
                {'Order_id': 'ORDADWI', 'Order_Details': 'Pizza MUVV', 'Order_Time': '08.39pm', 'Ordered_Menu_ID': 6, 'Customer_ID': 'CUSTNGSC'}])


# Orders.print_all_order_info()
Orders.find_specific_order_detail('ORDADWI')


# print(Orders.all_orders)

# print(ordersbulk.find_menu_detail())