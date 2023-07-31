# class Customer():

#     customer_all = []


#     def __init__(self, customer_data) :
#         self.customer_data = customer_data
        
#         Customer.customer_all.append(self)


#     def __repr__(self) -> str:
#         return  f" created customer '{self.customer_data}'"
    

#     # @classmethod
#     # def display_customer_details_from_id(cls, customer_id):      
#     #     res = None
#     #     for customer_item in cls.customer_all:
#     #         if customer_item.customer_data.get('customer_id') == customer_id:
#     #             res = customer_item.customer_data
#     #             break
 
#     #     return res





# # print(Customer.display_customer_details_from_id( 2))
# # print(customer1.__repr__())


class Customer():
    customer_all = []

    def __init__(self, customer_data):
        self.customer_data = customer_data
        Customer.customer_all.append(self)

    def __repr__(self) -> str:
        return f"Created customer '{self.customer_data}'"

    @classmethod
    def display_customer_details_from_id(cls, customer_id):
        res = None
        for customer_item in cls.customer_all:
            # print(customer_item)
            # print(type(customer_item))
            # print(customer_item.__dict__)

            # cls.customer__all has all the instances stored in it 
            if customer_item.customer_data.get('customer_id') == customer_id:
                res = customer_item.customer_data
                break
        return res


customer1_data = {'customer_id':1 , 'customer_name':'ali', 'customer_address':'villejuif paris', 'lastorderdate': '2022-12-12'}
customer2_data = {'customer_id':2 , 'customer_name':'alission', 'customer_address':' paris', 'lastorderdate': '2021-12-12'}

customer3_data = {'customer_id':3 , 'customer_name':'baggy', 'customer_address':' paris', 'lastorderdate': '2021-07-12'}
customer4_data = {'customer_id':4 , 'customer_name':'carl', 'customer_address':' paris', 'lastorderdate': '2021-02-12'}
customer5_data =  {'customer_id':5 , 'customer_name':'remy', 'customer_address':' paris', 'lastorderdate': '2022-102-12'}

customer1 = Customer(customer1_data)
customer2 = Customer(customer2_data)
customer3 = Customer(customer3_data)
customer4 = Customer(customer4_data)
customer5 = Customer(customer5_data)


# Retrieve customer details for customer_id = 1
customer_id_to_find = 4
found_customer = Customer.display_customer_details_from_id(customer_id_to_find)
print(found_customer) 
print(found_customer.get('lastorderdate'))

