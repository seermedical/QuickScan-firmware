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
ext_elecs = np.arange(0,24)
Elec_names = ['Cz','F3','Fp2','P4','C3','Fp1','F4','Fz','T3','F7','REF1','GND1','F8','A2','A1','T5','O2','C4','T4','P3','O1','Pz','T6']
#cal_val = [404.0, 404.0, 404.0, 407.0, 405.0, 405.0, 404.0, 404.0, 403.5, 404.0, 404.0, 403.5, 404.0, 404.0, 403.5, 404.0, 404.0, 404.0, 403.5, 404.0, 404.0, 404.0, 404.0, 404.0, 404.0,0.0]
cal_val = 404
def calibrate_test():
    global cal_val
    cal_val = 10000
    gpio.set_mux_pin(23, ext_sel)
    time.sleep(0.1)
    while (cal_val>450):
        cal_avg = 0
        for i in range(10):
            cal_avg = cal_avg+360.0*((Vin/(ADC.read_adc()+0.000001))-1)
        cal_val = cal_avg/10
    print("calibration done")
def show_channel_active(idx):
    for channel in Ext_elec_labels:
        channel.config(background=default_label_color)
    Ext_elec_labels[idx].config(background='green')
    root.update()
def test_electrode(idx):
    global er
    R = 0
    for i in range(3):
        Vout = ADC.read_adc()
        R= R+360.0*((Vin/(Vout+0.000001))-1)-cal_val
        #print(cal_val)
    R=R/3
    #print(R)
    if (R<10000.0):
        if R<0.0:
            R=0.0
        R_str = f"{R:.2f}"
        if idx>19:
            R_old = float(Ext_Elecs[idx-1].get())        
            if (R<R_old):
                Ext_Elecs[idx-1].set(R_str)
                Ext_elec_print[idx-1].set(R_str)
            show_channel_active(idx-1)
        else:
            R_old = float(Ext_Elecs[idx].get())
            if (R<R_old):
                Ext_Elecs[idx].set(R_str)
                Ext_elec_print[idx].set(R_str)
            show_channel_active(idx)
    #print(idx,"=",R)
def stop_test():
    global er
    global start_test
    print("Test stopped")
    start_test = 0
    error.set("No error")
    for i in range(24):
        Ext_elec_print[i].set("Not connected")
def rerun_electrode_sweep():
    global er
    global start_test
    for i in range(23):
        Ext_Elecs[i].set(str(10000.0))
    if start_test==1:
        run_test()
def run_test():
    global er
    global start_test
    start_test = 1
    print("Test running")
    for idx, ext_elec in enumerate(ext_elecs):
        if idx!=19:
            gpio.set_mux_pin(ext_elec, ext_sel)
            root.after(10, test_electrode(idx))
    on_elec = 0
    for i in range(23):
        if float(Ext_Elecs[i].get())<10000.0:
            on_elec = on_elec + 1
    if (on_elec>1):
         error.set("Electrodes Shorted")
         color.set('red')
         #root.update()
    root.after(10,rerun_electrode_sweep)
Vin = 3.32
root = tk.Tk()
root.title("Electrode tester")
strt = tk.Button(root, text  = "start test", command = run_test)
stop = tk.Button(root, text  = "stop test", command = stop_test)
calibrate = tk.Button(root, text  = "Calibrate", command = calibrate_test)
strt.grid(row = 0, column = 0)
stop.grid(row = 0, column = 1)
calibrate.grid(row = 0, column = 2)
Ext_Elecs = []
Ext_elec_print = []
Ext_elec_labels = []
global error
#global er
color=tk.StringVar()
color.set('green')
error =tk.StringVar()
er = tk.Label(root, textvariable = error,bg=color.get()).grid(row = 13, column = 0)
var = tk.StringVar()
var1 = tk.StringVar()
var.set(str(10000.0))
var1.set(str("Not connected"))    
Ext_Elecs.append(var)
Ext_elec_print.append(var1)
for i in range(23):
    if i<12:
        tk.Button(root, text  = Elec_names[i]).grid(row = i+1, column = 0)
    else:
        tk.Button(root, text  = Elec_names[i]).grid(row = i-11, column = 2)
    var = tk.StringVar()
    var1 = tk.StringVar()
    var.set(str(10000.0))
    var1.set(str("Not connected"))    
    Ext_Elecs.append(var)
    Ext_elec_print.append(var1)
    label = tk.Label(root, textvariable = Ext_elec_print[i])
    Ext_elec_labels.append(label)
    if i<12:
        label.grid(row=i+1,column=1)
    else:
        label.grid(row=i-11,column=3)
default_label_color = Ext_elec_labels[0].cget('background')
root.mainloop()