"""This module contains Role 2, AKA the Mail Courier, including the object class, its variables, and methods"""
class Mail:
    """This class contains the Mail Courier object, with the attributes Strength, Dexterity, and Intelligence"""
    def __init__(self, name):
        self._name = name
        self._role = "mc"
        self._str = 1
        self._dex = -1
        self._iq = 1
        self._challenge_1_success = 0
        self._challenge_2_success = 0
        self._challenge_3_success = 0

    
    def __str__(self):
        """This method returns the string representation the object"""
        return f"{self.name}: {self._str} Strength, {self._dex} Dexterity, {self._iq} Intelligence)"

    def mod_stat(self, stat, inc):
        """This method changes the stat indicated by the amount indicated"""
        if stat == _str:
            self._str = self._str + inc
        elif stat == _dex:
            self._dex = self._dex + inc
        elif stat == _iq:
            self._iq = self._iq + inc

    def challenge_result(self, chal_num, result):
        """This method will keep track of the status of completed or failed challenges"""
        # chal_num refers to the challenge number, result is the result of the challenge,
        # where 0 == failure, and 1 == success
        if chal_num == 1:
            self._challenge_1_success = result
        elif  chal_num == 2:
            self._challenge_2_success = result
        else:
            self._challenge_3_success = result