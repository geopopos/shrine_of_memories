from . import item

class Sword(item.Item):

    def __init__(self, name, description, attack):
        super(Sword, self).__init__(name, description)
        self.attack = attack

    def equip(self, entity):
        if isinstance(entity.equipped_item) == item.Item:
            return ('You already have a {} equipped, you can only equip one item at a time'.
                    format(entity.equipped_item.name))
        else:
            entity.equipped_item = self
            entity.attack += self.attack
            return 1
