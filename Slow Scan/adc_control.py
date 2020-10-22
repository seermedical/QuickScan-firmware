import gpio_control
import spidev

class ADC():
    def __init__(self, bus =0, CS = 0, mode = 0b00, freq = 7629):
        self.spi = spidev.SpiDev()
        self.spi.open(0,0)
        self.spi.mode = mode
        self.spi.max_speed_hz = freq
        self.spi.xfer2([0xD0, 0x14, 0x00, 0x0B])
    
    def read_adc(self):
        self.spi.xfer2([0x00, 0x00,0x00,0x00])        
        adc = self.spi.xfer2([0x00, 0x00,0x00,0x00])
        return ((adc[0]<<8)+ adc[1])/65535.0*5.3
    
    def read_adc_raw(self): 
        self.spi.xfer2([0x00, 0x00,0x00,0x00])
        adc = self.spi.xfer2([0x00, 0x00,0x00,0x00])
        return adc  
