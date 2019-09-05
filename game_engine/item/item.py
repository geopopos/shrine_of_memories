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
