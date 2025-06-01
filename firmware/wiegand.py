import machine
import time
from card_formats import TekCard33

class WiegandDecoder:
    def __init__(self,wie_gpio_0,wie_gpio_1):
        self.wie_digits = []
        self.wie_decode_in_progress_timer=50
        
        self.wie_gpio_0 = wie_gpio_0
        self.wie_gpio_1 = wie_gpio_1
        # setup timer
        timer = machine.Timer(3)
        timer.init(mode=machine.Timer.PERIODIC)
        timer.init(period=10, mode=machine.Timer.PERIODIC, callback=self.callback_timer_interrupt)
        
        # Register Interrupt handlers for GPIO
        self.wie_gpio_0.irq(trigger=machine.Pin.IRQ_FALLING, handler=self.callback_wie_0)
        self.wie_gpio_1.irq(trigger=machine.Pin.IRQ_FALLING, handler=self.callback_wie_1)
        

        
    
    def has_scanned_code(self):
        # if a code is getting scanned in, chill untill its done.
        while self.wie_decode_in_progress_timer<50:
            continue
        return len(self.wie_digits)!=0 
    
    def get_scanned_code(self):
        # if a code is getting scanned in, chill untill its done.
        while self.wie_decode_in_progress_timer<50:
            continue
        # actually decode the code at some point.. idk.
        r = TekCard33(self.wie_digits)
        self.wie_digits = []
        return r
        
    def callback_wie_0(self,p):
        self.wie_decode_in_progress_timer = 0
        self.wie_digits.append(0)

    def callback_wie_1(self,p):
        self.wie_decode_in_progress_timer = 0
        self.wie_digits.append(1)
        
    def callback_timer_interrupt(self,t):
        if self.wie_decode_in_progress_timer<50:
            self.wie_decode_in_progress_timer += 1
        else:
            pass
    
    def __repr__(self):
        return f"<WiegandDecoder on GPIO: ( 1:{self.wie_gpio_1} 0:{self.wie_gpio_0} )>"
        