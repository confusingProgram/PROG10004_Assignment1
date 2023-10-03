"""This module contains Role 1, AKA the Pizza Driver, including the object class, its variables, and methods"""
class Pizza:
    """This class contains the Pizza Driver object,  with the attributes Strength, Dexterity, and Charisma"""
    def __init__(self, name, str, dex, chr):
        self.name = name
        self.str = 0
        self.dex = 0
        self.chr = 1
    
    def __str__(self):
        """This method returns the string representation the object"""
        return f"{self.name})"

    def mod_stat(stat, inc):
        """This method changes the stat by the amount indicated"""
        if stat == "str":
            str = str + inc
        elif stat == "dex":
            dex = dex + inc
        elif stat == "chr":
            chr = chr + inc