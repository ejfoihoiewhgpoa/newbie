class Toppings:
    def __init__(self, topping_type, weight):
        self.__topping_type = topping_type
        self.__weight = weight

    def get_topping_type(self):
        return self.__topping_type
    def get_weight(self):
        return self.__weight
    
    def set_topping_type(self, topping_type):
        self.__topping_type = topping_type
    def set_weight(self, weight):
        self.__weight = weight


class Dough:
    def __init__(self, flour_type, baking_technique, weight):
        self.__flour_type = flour_type
        self.__baking_technique = baking_technique
        self.__weight = weight
    
    def get_flour_type(self):
        return self.__flour_type
    def get_baking_technique(self):
        return self.__baking_technique
    def get_weight(self):
        return self.__weight
    
    def set_flour_type(self, flour_type):
        self.__flour_type = flour_type
    def set_baking_technique(self, baking_technique):
        self.__baking_technique = baking_technique
    def set_weight(self, weight):
        self.__weight = weight

class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.__name = name
        self.__dough = dough
        self.__toppings_capacity = toppings_capacity
        self.__toppings = {}
    
    def get_name(self):
        return self.__name
    def get_dough(self):
        return self.__dough
    def get_toppings_capacity(self):
        return self.__toppings_capacity
    def get_toppings(self):
        return self.__toppings
    
    def set_name(self, name):
        self.__name = name
    def set_dough(self, dough):
        self.__dough = dough
    def set_toppings_capacity(self, toppings_capacity):
        self.__toppings_capacity = toppings_capacity
    def set_toppings(self, toppings):
        self.__toppings = toppings
    
    def add_topping(self, topping):
        if len(self.__toppings) >= self.__toppings_capacity and topping.get_topping_type() not in self.__toppings:
            raise ValueError("Not enough space for another topping")
        
        if topping.get_topping_type() in self.__toppings:
            self.__toppings[topping.get_topping_type()] += topping.get_weight()
        else:
            self.__toppings[topping.get_topping_type()] = topping.get_weight()

    def calculate_total_weight(self):
        total = self.__dough.get_weight() + sum(self.__toppings.values())
        return total
