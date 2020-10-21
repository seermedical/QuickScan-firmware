import gpio_control
import adc_control
import time
import tkinter as tk
import numpy as np

gpio = gpio_control.gpio()
ADC = adc_control.ADC()

gpio.set_pin(18)

ext_sel = [25, 12, 16, 20, 21]
ext_elecs = [24,25,27,26,30,31,29,28,0,1,2,3,7,6,5,4,8,9,11,10,14,15,13,12,22]

#sense_elecs = [7]
#ext_elec = 13 #list(range(25))
ext_elecs = np.arange(1,24)
def test_electrode():
    Vout = ADC.read_adc()
    R= 360.0*(Vin-Vout)/(Vout+0.0000001)
    print(R)
    #time.sleep(0.1)
    extElec1val.set(str(R))
def stop_test():
    start_test = 0
def run_test():
    start_test = 1
    for idx, ext_elec in enumerate(ext_elecs):
        gpio.set_mux_pin(ext_elec, ext_sel)
        root.after(100, test_electrode)


Vin = 3.42
start_test = 0

time.sleep(.1)
root = tk.Tk()
root.title("Electrode tester")
strt = tk.Button(root, text  = "start test", command = run_test)
stop = tk.Button(root, text  = "stop test", command = stop_test)
strt.grid(row = 0, column = 0)
stop.grid(row = 0, column = 1)

extElec1 = tk.Button(root, text  = "extElec1")
extElec2 = tk.Button(root, text  = "extElec2")
extElec3 = tk.Button(root, text  = "extElec3")
extElec4 = tk.Button(root, text  = "extElec4")
extElec5 = tk.Button(root, text  = "extElec5")
extElec1.grid(row = 1, column = 0)
extElec2.grid(row = 2, column = 0)
extElec3.grid(row = 3, column = 0)
extElec4.grid(row = 4, column = 0)
extElec5.grid(row = 5, column = 0)

extElec1val = tk.StringVar()
extElec2val = tk.StringVar()
extElec3val = tk.StringVar()
extElec4val = tk.StringVar()
extElec5val = tk.StringVar()



extElec1label= tk.Label(root, textvariable = extElec1val)
extElec2label= tk.Label(root, textvariable = extElec2val)
extElec3label= tk.Label(root, textvariable = extElec3val)
extElec4label= tk.Label(root, textvariable = extElec4val)
extElec5label= tk.Label(root, textvariable = extElec5val)
extElec1label.grid(row = 1, column = 1)
extElec2label.grid(row = 2, column = 2)
extElec3label.grid(row = 3, column = 3)
extElec4label.grid(row = 4, column = 4)
extElec5label.grid(row = 5, column = 5)

root.mainloop()

       
        
        


