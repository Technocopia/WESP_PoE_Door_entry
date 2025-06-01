import time

class DoorStrike:
    def __init__(self,strike_gpio, polarity = True):
        self.strike_gpio = strike_gpio
        self.polarity = polarity
        self.strike_gpio.value(not self.polarity)
        pass
    
    def open_door(self, duration=5):
        self.strike_gpio.value(self.polarity)
        time.sleep(duration)
        self.strike_gpio.value(not self.polarity)
        
    def __repr__(self):
        return f"<DoorStrike on GPIO: {self.strike_gpio}>"