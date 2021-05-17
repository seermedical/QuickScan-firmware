import pigpio
import time
import subprocess

subprocess.run(["sudo","pigpiod"])
class gpio():
    def __init__(self):
        self.pi = pigpio.pi()
    
    def pin_set_mode(self, pin_no, state):
        if state == 'output':        #is this the right way?
            self.pi.set_mode(pin_no, pigpio.OUTPUT)
        else:
             self.pi.set_mode(pin_no, pigpio.INPUT)
    
    def set_pin(self, pin_no):
        self.pin_set_mode(pin_no, 'output')
        self.pi.write(pin_no, 1)
    
    def clear_pin(self, pin_no):
        self.pin_set_mode(pin_no, 'output')
        self.pi.write(pin_no, 0)
    
    def set_pwm(self, pwm_pin, pwm_freq, pwm_duty):
        self.pi.hardware_PWM(pwm_pin, pwm_freq, pwm_duty)
        
    def pwm_off(self, pwm_pin):
        self.pi.hardware_PWM(pwm_pin, 0, 0)

    def set_mux_pin(self, mux_pin, sel_bits):
        for sel_bit in sel_bits:
            self.pin_set_mode(sel_bit, 'output')

        for i in range(len(sel_bits)):
            self.pi.write(sel_bits[i], mux_pin>>i&1)

