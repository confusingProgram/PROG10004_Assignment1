"""This module contains Role 2, AKA the Mail Courier, including the object class, its variables, and methods"""
class Mail:
    """This class contains the Mail Courier object,  with the attributes Strength, Dexterity, and Intelligence"""
    def __init__(self, name):
        self._name = name
        self._role = "pd"
        self._str = 0
        self._dex = 0
        self._Int = 1
    
    def __str__(self):
        """This method returns the string representation the object"""
        return f"{self.name}: {self._str} Strength, {self._dex} Dexterity, {self._chr} Charisma)"

    def mod_stat(self, stat, inc):
        """This method changes the stat by the amount indicated"""
        if stat == "str":
            self._str = self._str + inc
        elif stat == "dex":
            self._dex = self._dex + inc
        elif stat == "chr":
            self._chr = self._chr + inc