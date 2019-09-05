class Inventory(object):

    def __init__(self, inventory_list=[], capacity=10):
        self.inventory_list = inventory_list
        self.capacity = capacity

    def add_item(self, item):
        if len(self.inventory_list) <= self.capacity:
            self.inventory_list.append(item)
        else:
            return -1

    def remove_item(self, item):
        if item in self.inventory_list:
            print("{} removed".format(item.name))
            self.inventory_list.remove(item)

    def has_item(self, item_name):
        items = [item for item in self.inventory_list if item.name == item_name]
        return items
