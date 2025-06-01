
def bits_to_num(bits):
    num=0
    for i,b in enumerate(bits):
        num += (2**i)*b
    return num

class Card:
    def __repr__(self):
        return f"<{self.__class__.__name__} id: {self.id} site: {self.site} parity: {self.parity}>"

class TekCard33(Card):
    def __init__(self,bits):
        self.id = bits_to_num(bits[8:32][::-1])
        self.parity = bits_to_num(bits[32:32][::-1])
        self.site = bits_to_num(bits[0:8][::-1])
        