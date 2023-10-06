"""This module contains Role 2, AKA the Mail Courier, including the object class, its variables, and methods."""
class Mail:
    """This class contains the Mail Courier object, with the attributes Strength, Dexterity, and Intelligence."""
    def __init__(self, name):
        """This method executes when a Mail Courier object is created, and sets default values."""
        self._name = name # Name of the character.
        self._role = "mc" # Short-hand of their role.
        self._str = 0 # Strength stat.
        self._dex = 0 # Dexterity stat.
        self._chr = 1 # Charisma stat.
        self._challenge_1_result = 0 # Tracks result of Challenge 1, where 0 == failure, 1 == success
        self._challenge_2_result = 0 # Tracks result of Challenge 2, where 0 == failure, 1 == success
        self._challenge_3_result = 0 # Tracks result of Challenge 3, where 0 == failure, 1 == success
    
    def __str__(self):
        """This method returns the string representation the Mail Courier object."""
        return f"{self.name}: {self._str} Strength, {self._dex} Dexterity, {self._iq} Intelligence)"

    def mod_stat(self, stat, inc):
        """This method changes the stat indicated by the amount indicated."""
        if stat == "str":
            self._str = self._str + inc
        elif stat == "dex":
            self._dex = self._dex + inc
        elif stat == "int":
            self._int = self._int + inc

    def challenge_result(self, chal_num, result):
        """This method will keep track of the status of completed or failed challenges."""
        # chal_num refers to the challenge number, result is the result of the challenge,
        # where 0 == failure, and 1 == success
        if chal_num == 1:
            self._challenge_1_result = result
        elif  chal_num == 2:
            self._challenge_2_result = result
        elif  chal_num == 3:
            self._challenge_3_result = result