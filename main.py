
from product import Product
from store import Store
from user import User



store = Store()


product1 = Product('soda', 100 , 4 )
product2 = Product('rise' , 40 , 2)
# product3 = Product('suger', 67 , 23)

store.add_product(product1)
store.add_product(product2)
# store.add_product(product3)

# user1 = User("shsamiei" , "#abcslddkf")
# user2 = User("hosein_samiei" , "12343141")



# store.add_user(user1)
# store.add_user(user2)


# print("__________")
# print("\n")
# print(store.get_my_users())

print(store.get_total_asset())





