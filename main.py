import led_control
import gpio_control
import adc_control
import time

LED = led_control.LED()
gpio = gpio_control.gpio()
ADC = adc_control.ADC()
pwm_pin =18
pwm_freq = 10000
pwm_duty = 500000
sense_sel = [5, 6, 13, 23, 24]
excitation_sel = [25, 12, 16, 20, 21]
#sense_elecs = [24,25,27,26,30,31,29,28,0,1,2,3,7,6,5,4,8,9,11,10,14,15,13,12,22]
sense_elecs = [7]
ext_elecs = list(range(25))

LED.led_init()  # should be init func of led
gpio.set_pwm(pwm_pin, pwm_freq, pwm_duty)
with open('data.csv', 'w') as f:
    for idx, sense_elec in enumerate(sense_elecs):
        gpio.set_mux_pin(sense_elec, sense_sel)
        LED.led_on(LED.blue_led[idx+1], 0xF0, 0xF0)
        for ext_elec in ext_elecs:
            gpio.set_pin(26)  # clear cap
            time.sleep(0.5)
            gpio.clear_pin(26)
            gpio.set_mux_pin(ext_elec, excitation_sel)
            time.sleep(0.5)
            reading = ADC.read_adc()
            f.write("%s,%s,%s\n" % (sense_elec, ext_elec, reading))
        LED.led_off(LED.blue_led[idx+1])
        
        
        
        