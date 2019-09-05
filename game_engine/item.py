"""
Items module. Contains Base Items class and all children classes
"""

from textwrap import dedent

class Item(object):
    """ Base class for Items
        Parameters
        __________
        name : is the displayable name of the item

        description : this is the description of an
                      items capabilities and physcial attributes
    """

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self, entity):
        """
        The base implementation of the use method
        This removes the item from the entities inventory
        The use method allows a game 'entity' (Player, Enemy) to
        use an items ability
        """
        print("I don't Know how you expected to use a ", self.name)

    def equip(self, entity):
        """
        The base implementation of the equip method

        This removes the item from the players inventory
        The equip method allows a game entity (Player, Enemy) to
        equip an item and inherit it's ability
        """
        print("I don't know how you expected to equip a ", self.name)

    def unequip(self, entity):
        """
        The base implementation of the unequip method

        The equip method allows a game entity (Player, Enemy) to
        unequip an item and uninherit it's ability
        it also adds this item back to the players inventory
        """
        print("I don't know how you expected to unequip a ", self.name)

    def read(self):
        """
        The base implementatin of the read method

        The equip method allows a game entity (Player, Enemy) to
        read an items contents
        """
        print("I don't know how you expected to read a ", self.name)


class Key(Item):
    """
    The class used to specify a key object.
    The key object has no actions.
    """
    pass


class Note(Item):
    """ This is a child of the Item Class """

    def __init__(self, name, description, text):
        """ An Altered form of the Item classes init method """
        self.text = text
        super(Note, self).__init__(name, description)

    def read(self):
        """ An overrided version of the Item classes read method """
        print(dedent("{} reads:\n\t{}".format(self.name, self.text)))


class Potion(Item):
    """
    The class used to specify a potion object. The potion can be 'used'
    by a game entity (Player, Enemy)
    """
    def __init__(self, name, description, hp):
        super(Potion, self).__init__(name, description)
        self.hp = hp

    def use(self, entity):
        """ this method allows a game entity to use a potion object

        Parameters
        __________
        entity : the game entity to apply the potion to
        __________
        """
        if entity.hp + self.hp > entity.max_hp:
            entity.hp = entity.max_hp
        else:
            entity.hp = entity.hp + self.hp
        print('{} HP raised to {}'.format(entity.name, entity.hp))


class Sword(Item):

    def __init__(self, name, description, attack):
        super(Sword, self).__init__(name, description)
        self.attack = attack

    def equip(self, entity):
        if isinstance(entity.equipped_item) == Item:
            return ('You already have a {} equipped, you can only equip one item at a time'.
                    format(entity.equipped_item.name))
        else:
            entity.equipped_item = self
            entity.attack += self.attack
            return 1
