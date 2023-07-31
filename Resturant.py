
class Resturant():
    
    def __init__(self, name_restraunt:str, address_restraunt:str):
        """
        Setting name and address params to private 
        """
        
        self.__name_restraunt = name_restraunt 
        self.__address_restraunt = address_restraunt

    @property
    def name_restraunt(self):  
        return self.__name_restraunt
    
    @property
    def address_restraunt(self):
        return self.__address_restraunt

    def __repr__(self) -> str:
        return f"The name and address of the restaunt are '{self.__name_restraunt}' and '{self.__address_restraunt}'"
    