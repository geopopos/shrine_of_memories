"""
A potion Item class the amount of hp a potion restored can be specified
in the __init__ method
"""
from . import item

class Potion(item.Item):
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
