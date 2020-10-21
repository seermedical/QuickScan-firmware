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
sense_elecs = [24,25,27,26,30,31,29,28,0,1,2,3,7,6,5,4,8,9,11,10,14,15,13,12,22]
#sense_elecs = [7]
ext_elec = 1 #list(range(25))
gpio.set_mux_pin(ext_elec, excitation_sel)
        
LED.led_init()  # should be init func of led
gpio.set_pwm(pwm_pin, pwm_freq, pwm_duty)
reading_max = 0
LED.all_leds_off_single(LED.Blue_led,LED.Green_led,LED.Red_led)
with open('data_sense_elec4.csv', 'w') as f:
    for idx, sense_elec in enumerate(sense_elecs):
        gpio.set_mux_pin(sense_elec, sense_sel)
        LED.led_on(LED.Blue_led[idx+1], 0xF0, 0xF0)
        gpio.set_pin(26)  # clear cap
        time.sleep(0.1)
        gpio.clear_pin(26)
        time.sleep(0.1)
        reading = 0
        for i in range(5):
            print(ADC.read_adc())
            reading = reading+ADC.read_adc()
            time.sleep(0.05)
        reading =reading/len(range(5))
        print(reading)
        if reading>reading_max:
            reading_max = reading
            idx_max = idx
        f.write("%s,%s,%s\n" % (idx+1, ext_elec, reading))
        LED.led_off(LED.Blue_led[idx+1])
    LED.led_on(LED.Green_led[idx_max+1], 0xF0, 0xF0)
       
        
        
