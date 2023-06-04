# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop['name']

def get_total_cash(cash):
    return (cash["admin"]["total_cash"])

def add_or_remove_cash(pet_shop, num):
    pet_shop["admin"]["total_cash"] += num

def get_pets_sold(pets_sold):
    return pets_sold["admin"]["pets_sold"]

def increase_pets_sold(sold, num):
    sold["admin"]["pets_sold"] += num

def get_stock_count(stock):
    return len(stock["pets"])
    
def get_pets_by_breed(pet_shop, breed):
    ret_list = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            ret_list.append(pet)
    return ret_list

def find_pet_by_name(list_of_pets, pet_name):
    found_pet = None
    for pet in list_of_pets["pets"]:
        if pet["name"] == pet_name:
           found_pet = pet
    return found_pet
    
def remove_pet_by_name(list_of_pets, pet_name):
    for pet in list_of_pets["pets"]:
        if pet["name"] == pet_name:
            list_of_pets["pets"].remove(pet)
        
def add_pet_to_stock(list_of_pets, new_pet_name):
    list_of_pets["pets"].append(new_pet_name)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)