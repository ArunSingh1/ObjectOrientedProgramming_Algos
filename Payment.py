class Payment():

    all_payments =[]
    def __init__(self, payments_list):

        self.payment_list = payments_list
        self.all_payments.extend(payments_list) 


    def __repr__(self) -> str:
        
        return  f"Payments created '{self.payment_list}'"



payments = Payment([{'Order_id':'ORD3243', 'Payment_ref':'LKHL', 'Payment_time':'12.21am','Is_Payment_processed': 'YES', 'Customer_ID': 'CUST1235' },
               {'Order_id': 'ORDWFEA', 'Payment_ref': 'MWLI', 'Payment_time': '10.32am', 'Is_Payment_processed': 'YES', 'Customer_ID': 'CUSTBEFA'},
                {'Order_id': 'ORDEHRR', 'Payment_ref': 'FBTZ', 'Payment_time': '05.43am', 'Is_Payment_processed': 'YES', 'Customer_ID': 'CUSTWTIE'},
                {'Order_id': 'ORDRKQO', 'Payment_ref': 'QFPI', 'Payment_time': '09.20pm', 'Is_Payment_processed': 'NO', 'Customer_ID': 'CUSTUBBQ'},
                {'Order_id': 'ORDGQIY', 'Payment_ref': 'EVQT', 'Payment_time': '08.34pm', 'Is_Payment_processed': 'YES', 'Customer_ID': 'CUSTMAEF'},
                {'Order_id': 'ORDTYEL', 'Payment_ref': 'RHSD', 'Payment_time': '07.39pm', 'Is_Payment_processed': 'YES', 'Customer_ID': 'CUSTXIDC'},
                {'Order_id': 'ORDADWI', 'Payment_ref': 'MUVV', 'Payment_time': '08.39pm', 'Is_Payment_processed': 'NO', 'Customer_ID': 'CUSTNGSC'}])

        

# print(payments.__repr__())