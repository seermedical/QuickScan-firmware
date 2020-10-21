import led_control
import gpio_control
import adc_control
import time

LED = led_control.LED()
gpio = gpio_control.gpio()
ADC = adc_control.ADC()

gpio.set_pin(18)

pwm_pin =18
pwm_freq = 10000
pwm_duty = 500000
sense_sel = [5, 6, 13, 23, 24]
excitation_sel = [25, 12, 16, 20, 21]
sense_elecs = [24,25,27,26,30,31,29,28,0,1,2,3,7,6,5,4,8,9,11,10,14,15,13,12,22]
#sense_elecs = [7]
ext_elec = 1#list(range(25))
gpio.set_mux_pin(ext_elec, excitation_sel)
        
#LED.led_init()  # should be init func of led
#gpio.set_pwm(pwm_pin, pwm_freq, pwm_duty)
reading_max = 0
#LED.all_leds_off_single(LED.Blue_led,LED.Green_led,LED.Red_led)

##set elec no.
idx = 17

Vin = 3.3
gpio.set_mux_pin(sense_elecs[idx-1], sense_sel)
#LED.led_on(LED.Blue_led[idx], 0xF0, 0xF0)
gpio.set_pin(26)  # clear cap
time.sleep(0.2)
gpio.clear_pin(26)
time.sleep(.1)
while (1):
    Vout = ADC.read_adc()
    R= 360.0*((Vin/(Vout+0.000001))-1)
    print(R)
    time.sleep(0.1)


       
        
        

