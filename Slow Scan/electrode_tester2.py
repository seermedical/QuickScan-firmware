import gpio_control
import adc_control
import time
import tkinter as tk
import numpy as np

gpio = gpio_control.gpio()
ADC = adc_control.ADC()

gpio.set_pin(18)

ext_sel = [25, 12, 16, 20, 21]
#ext_elecs = [24,25,27,26,30,31,29,28,0,1,2,3,7,6,5,4,8,9,11,10,14,15,13,12,22]
ext_elecs = np.arange(0,26)
Elec_names = ['Cz','F3','Fp2','P4','C3','Fp1','F4','Fz','T3','F7','REF1','GND1','F8','A2','A1','T5','O2','C4','T4','','P3','O1','Pz','T6','']
cal_val = [404.0, 403.0, 403.0, 407.0, 405.0, 405.0, 404.0, 404.0, 402.5, 403.0, 403.0, 402.5, 403.0, 403.0, 402.5, 404.0, 403.0, 403.0, 402.5, 403.0, 0.0, 403.0, 403.0, 403.0, 403.0,0.0]



def test_electrode(idx):
    Vout = ADC.read_adc()
    R= 360.0*((Vin/(Vout+0.000001))-1)-cal_val[idx]
    print(idx)
    if (R<10000.0) & (R>0.0) & (idx!=19):
        Ext_Elecs[idx].set(str(R))
        Ext_elec_print[idx].set(str(R))
def stop_test():
    global start_test
    start_test = 0
    error.set("No error")

def rerun_electrode_sweep():
    global start_test
    for i in range(25):
        Ext_Elecs[i].set(str(10000.0))
    if start_test==1:
        run_test()

def run_test():
    global start_test
    start_test = 1
    for idx, ext_elec in enumerate(ext_elecs):
        gpio.set_mux_pin(ext_elec, ext_sel)
        root.after(10, test_electrode(idx))
    on_elec = 0
    for i in range(25):
        if float(Ext_Elecs[i].get())<10000.0:
            on_elec = on_elec + 1
    if (on_elec>1):
         error.set("Error")
    root.after(1000,rerun_electrode_sweep)

Vin = 3.42
root = tk.Tk()
root.title("Electrode tester")
strt = tk.Button(root, text  = "start test", command = run_test)
stop = tk.Button(root, text  = "stop test", command = stop_test)
strt.grid(row = 0, column = 0)
stop.grid(row = 0, column = 1)

Ext_Elecs = []
Ext_elec_print = []

global error
error =tk.StringVar()
tk.Label(root, textvariable = error).grid(row = 0, column = 2)
for i in range(25):
    if i<13:
        tk.Button(root, text  = Elec_names[i]).grid(row = i+1, column = 0)
    else:
        tk.Button(root, text  = Elec_names[i]).grid(row = i-12, column = 2)
    
    
    var = tk.StringVar()
    var1 = tk.StringVar()
    var.set(str(10000.0))
    var1.set(str(20000.0))    
    Ext_Elecs.append(var)
    Ext_elec_print.append(var1)

    if i<13:
        tk.Label(root, textvariable = Ext_elec_print[i]).grid(row=i+1,column=1)
    else:
        tk.Label(root, textvariable = Ext_elec_print[i]).grid(row=i-12,column=3)


root.mainloop()

       
        
        



