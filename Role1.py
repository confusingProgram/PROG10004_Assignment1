"""This module contains Role 1, AKA the Pizza Driver, including the object class, its variables, and methods"""
class Pizza:
    """This class contains the Pizza Driver object, with the attributes Strength, Dexterity, and Charisma"""
    def __init__(self, name):
        self._name = name
        self._role = "pd"
        self._str = 0
        self._dex = 0
        self._chr = 1
        self._challenge_1_result = 0
        self._challenge_2_result = 0
        self._challenge_3_result = 0
    
    def __str__(self):
        """This method returns the string representation the Pizza Driver object."""
        return f"{self._name}: {self._str} Strength, {self._dex} Dexterity, {self._chr} Charisma)"

    def mod_stat(self, stat, inc):
        """This method changes the stat by the amount indicated."""
        if stat == "str":
            self._str = self._str + inc
        elif stat == "dex":
            self._dex = self._dex + inc
        elif stat == "chr":
            self._chr = self._chr + inc

    def challenge_result(self, chal_num, result):
        """This method will keep track of the status of completed or failed challenges."""
        # chal_num refers to the challenge number, result is the result of the challenge,
        # where 0 == failure, and 1 == success
        if chal_num == 1: 
            self._challenge_1_result = result
        elif  chal_num == 2:
            self._challenge_2_result = result
        else:
            self._challenge_3_result = result

