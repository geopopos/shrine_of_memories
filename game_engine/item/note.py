from textwrap import dedent
from item import Item


class Note(Item):
    """ This is a child of the Item Class """

    def __init__(self, name, description, text):
        """ An Altered form of the Item classes init method """
        self.text = text
        super(Note, self).__init__(name, description)

    def read(self):
        """ An overrided version of the Item classes read method """
        print(dedent("{} reads:\n\t{}".format(self.name, self.text)))
