"""This module contains Role 2, AKA the Mail Courier, including the object class, its variables, and methods"""
class Mail:
    """This class contains the Mail Courier object,  with the attributes Strength, Dexterity, and Intelligence"""
    def __init__(self, name):
        self._name = name
        self._role = "mc"
        self._str = 1
        self._dex = -1
        self._int = 1
    
    def __str__(self):
        """This method returns the string representation the object"""
        return f"{self.name}: {self._str} Strength, {self._dex} Dexterity, {self._int} Intelligence)"

    def mod_stat(self, stat, inc):
        """This method changes the stat by the amount indicated"""
        if stat == "str":
            self._str = self._str + inc
        elif stat == "dex":
            self._dex = self._dex + inc
        elif stat == "int":
            self._Int = self._int + inc