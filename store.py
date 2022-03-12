
class Store :

    def __init__(self):
        self.list_of_products = []
        self.list_of_users = []
        self.total_asset = 0 


    def add_product(self , product):
        self.list_of_products.append(product.info)
        self.total_asset += product.info['price'] * product.info['number_of_remain']

    def remove_product(self ,product):
        self.list_of_products.remove(product.info)
        self.total_asset -= product.info['price'] * product.info['number_of_remain']


    def add_user(self , user):

        if self.list_of_users :

            if self.is_exist(user):
                self.list_of_users.append(user.info)

        else :
            self.list_of_users.append(user.info)


    def is_exist(self,user):

        for i in range(len(self.list_of_users)): 
                if self.list_of_users[i]['user'] == user.info['user']:
                    return 0 
        return 1 



    def get_my_products(self) :
        return self.list_of_products

    def get_my_users(self):
        return self.list_of_users


    def get_total_asset(self):
        return self.total_asset



    pass

