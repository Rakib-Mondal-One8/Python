from food_item import FoodItem


class Menu:
    items = [] # list of Food Items

    def add_menu_item(self,item_name,price,quantity):
        item = FoodItem(item_name,price,quantity)
        self.items.append(item)

    def find_item(self,item_name):
        for item in self.items:
            if(item_name.lower() == item.name.lower()):
                return item
        return None

    def remove_item(self,item_name):
        item = self.find_item(item_name)
        if(item):
            self.items.remove(item)
            print("Item Deleted")
        else:
            print("Item Not Found")

    def view_menu(self):
        print("*****Menu*****")
        print(f"Item Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t\t{item.price}\t\t{item.quantity}")

    def take_order(self,item_name,quantity):
        for item in self.items:
            if(item_name == item.name):
                if(quantity <= item.quantity):
                    item.quantity -= quantity
                    return (item.name,item.price,quantity)
                else:
                    print("Quantity Out of Stock!!")
                    return None
            else:
                print("Invalid Item!!")
                return None

