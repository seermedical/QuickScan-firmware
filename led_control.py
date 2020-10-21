import smbus

class LED:
    def __init__(self, addr = 0x30, bus =1):
        self.i2c_addr = addr
        self.bus = smbus.SMBus(bus)
    

    
    def led_init(self):     
        # need this initialization at power up
        # need to confirm if unlocking needed at all step
 
        self.bus.write_i2c_block_data(self.i2c_addr, 0xFE, [0xC5])
        self.bus.write_i2c_block_data(self.i2c_addr, 0xFD, [0x04])
        #set config reg
        self.bus.write_i2c_block_data(0x30, 0x00, [0x41])

        self.bus.write_i2c_block_data(self.i2c_addr, 0xFE, [0xC5])
        self.bus.write_i2c_block_data(self.i2c_addr, 0xFD, [0x04])
        #set GCM
        self.bus.write_i2c_block_data(self.i2c_addr, 0x01, [0xFF])
        
        self.bus.write_i2c_block_data(self.i2c_addr, 0xFE, [0xC5])
        self.bus.write_i2c_block_data(self.i2c_addr, 0xFD, [0x04])
        #set pullup/down
        self.bus.write_i2c_block_data(self.i2c_addr, 0x02, [0x00])


    def all_leds_off(self):
        self.bus.write_i2c_block_data(self.i2c_addr, 0xFE, [0xC5])
        self.bus.write_i2c_block_data(self.i2c_addr, 0xFD, [0x04])
        #set GCM
        self.bus.write_i2c_block_data(self.i2c_addr, 0x01, [0x00])
                
    def all_leds_off_single(self, Blue_led, Green_led, Red_led):
        for key in self.Blue_led:
            self.led_off(Blue_led[key])
            
        for key in self.Green_led:
            self.led_off(Green_led[key])
        for key in self.Red_led:
            self.led_off(Red_led[key])
        
    def led_on(self, led_addr, scaling, pwm):
        #self.unlock_command_reg()
        # set scaling of led_addrss 
        self.bus.write_i2c_block_data(self.i2c_addr, 0xFE, [0xC5])
        self.bus.write_i2c_block_data(self.i2c_addr, 0xFD, [0x02])

        self.bus.write_i2c_block_data(self.i2c_addr, led_addr, [scaling])
        
        #self.unlock_command_reg()
        #set pwm of led_adrss 
        self.bus.write_i2c_block_data(self.i2c_addr, 0xFE, [0xC5])
        self.bus.write_i2c_block_data(self.i2c_addr, 0xFD, [0x00])

        self.bus.write_i2c_block_data(self.i2c_addr, led_addr, [pwm])
    
    def led_off(self, led_addr):
        self.bus.write_i2c_block_data(self.i2c_addr, 0xFE, [0xC5])
        self.bus.write_i2c_block_data(self.i2c_addr, 0xFD, [0x02])
        # set scaling of addrss 1
        self.bus.write_i2c_block_data(self.i2c_addr, led_addr, [0x00])
        
        self.bus.write_i2c_block_data(self.i2c_addr, 0xFE, [0xC5])
        self.bus.write_i2c_block_data(self.i2c_addr, 0xFD, [0x00])
        #set pwm of adrss 0
        self.bus.write_i2c_block_data(self.i2c_addr, led_addr, [0x00])
    Blue_led = {
        1:0x00,
        2:0x03,
        3:0x06,
        4:0x09,
        5:0x0C,
        6:0x1E,
        7:0x21,
        8:0x24,
        9:0x27,
        10:0x2A,
        11:0x3C,
        12:0x3F,
        13:0x42,
        14:0x45,
        15:0x48,
        16:0x5A,
        17:0x5D,
        18:0x60,
        19:0x63,
        20:0x66,
        21:0x78,
        22:0x7B,
        23:0x7E,
        24:0x81,
        25:0x84,
        }
    Green_led = {
        1:0x01,
        2:0x04,
        3:0x07,
        4:0x0A,
        5:0x0D,
        6:0x1F,
        7:0x22,
        8:0x25,
        9:0x28,
        10:0x2B,
        11:0x3D,
        12:0x40,
        13:0x43,
        14:0x46,
        15:0x49,
        16:0x5B,
        17:0x5E,
        18:0x61,
        19:0x64,
        20:0x67,
        21:0x79,
        22:0x7C,
        23:0x7F,
        24:0x82,
        25:0x85,
        }
    Red_led = {
        1:0x02,
        2:0x05,
        3:0x08,
        4:0x0B,
        5:0x0E,
        6:0x20,
        7:0x23,
        8:0x26,
        9:0x29,
        10:0x2C,
        11:0x3E,
        12:0x41,
        13:0x44,
        14:0x47,
        15:0x4A,
        16:0x5C,
        17:0x5F,
        18:0x62,
        19:0x65,
        20:0x68,
        21:0x7A,
        22:0x7D,
        23:0x80,
        24:0x83,
        25:0x86,
        }