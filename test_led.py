import led_control
import gpio_control
import adc_control

LED = led_control.LED()
gpio = gpio_control.gpio()
ADC = adc_control.ADC()

LED.led_init()  # should be init func of led
LED.led_off(6)
#LED.led_off(3)
LED.led_on(9, 0x0F, 0x0F)


