from inventory import Inventory

class Player(object):
    """ 
    The class that defines a Player and it's attributes 
    
    Parameters
    __________
    hp : The players HitPoints. How much damage can a player take.

    attack : the players attack power. this is used in the damage
             equation to determine how much damage the player deals
    
    defense : the players defense power. this is used in the damage
              calculation equation to determine how much damage the
              Player takes.
    
    inventory : A list of all the players acquired items. of the class
                Inventory

    equipped_item : the item the player currently has equipped. the
                    player will inherit this items attributes
    __________
    """
    def __init__(self, name, max_hp, attack, defense, inventory, equipped_item):
        self.name = name
        self.hp = self.max_hp = max_hp
        self.attack = attack
        self.defense = defense
        self.inventory = inventory
        self.equipped_item = equipped_item

    def use_item(self, item_name):
        """ use an items from the players inventory

        Parameters
        __________
        item_name : a string matching the name attribute of an item
        __________
        """

        items = self.inventory.has_item(item_name)
        if not items:
            print("{} does not have item {} in their inventory".format(self.name, item_name))
        else:
            print("{} used {}".format(self.name, item_name))
            items[0].use(self)
            self.inventory.remove_item(items[0])

    def equip_item(self, item_name):
        """
        Add an item to the players equipped_item slot
        Only one item may be equipped at a time
        equipping and item removes it from the players inventory
        
        Parameters
        __________
        item_name : a string matching the name attribute of an item
        __________
        """

        items = self.inventory.has_item(item_name)
        if not items:
            print("{} does not have item {} in their inventory".format(self.name, item_name))
        else:
            equip_success = items[0].equip(self)
            if equip_success == 1:
                print("{} equipped {}".format(self.name, item_name))
                self.inventory.remove_item(items[0])
            else:
                print(equip_success)
