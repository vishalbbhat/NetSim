from tkinter import *
from tkinter import ttk
from tkinter import messagebox
## Calculation

def result():
    result_Entry.delete(0, 'end')
    ps=float(var_entry.get())
    iat=float(var2_entry.get())
    result=(ps*8)/iat
    result_Entry.insert(END, str(result))

def value():
    Value_Entry.delete(0, 'end')
    ps=float(Packet_Entry.get())
    gen=float(Gen_Entry.get())
    result=(ps*8)/gen
    Value_Entry.insert(END, str(result)) 

root = Tk()
root.title('NetSim Calculator')
root.geometry("300x400")
root.maxsize(width=300,height=400)
root.minsize(width=300,height=400)

my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=5)

Generation_rate = Frame(my_notebook, width=480, height = 600)
InterArrivaltime = Frame(my_notebook, width=480, height = 480)

Generation_rate.pack(fill="both",expand =1)
InterArrivaltime.pack(fill="both",expand = 1)

my_notebook.add(Generation_rate, text = "Generation Rate")
my_notebook.add(InterArrivaltime, text = "Inter Arrival Time")

   

variable1 = LabelFrame(Generation_rate, text = "Size of the Packet(in Bytes)")
variable1.pack(pady=10)
var_entry = Entry(variable1, font=("Helvetica",10))
var_entry.insert(0, 1460)
var_entry.pack(pady=10,padx=10)


#IAT
variable2 = LabelFrame(Generation_rate, text = "Inter Arrival Time(µs)")
variable2.pack(pady=10)

var2_entry = Entry(variable2, font=("Helvetica",10))
var2_entry.pack(pady=10,padx=10)

#result
res = LabelFrame(Generation_rate, text = "Generation Rate(Mbps)")
res.pack(pady=10)

result_Entry = Entry(res, font=("Helvetica",10))
result_Entry.pack(pady=10,padx=10)

button_frame = Frame(Generation_rate)
button_frame.pack(pady=10)


Result_Button = Button(button_frame,text= 'Result',command = result)
Result_Button.grid(row=0,column=0,padx=10)


Packet_size = LabelFrame(InterArrivaltime, text = "Packet Size(Bytes)")
Packet_size.pack(pady=10)
Packet_Entry = Entry(Packet_size, font=("Helvetica",10))
Packet_Entry.insert(0, 1460)
Packet_Entry.pack(pady=10,padx=10)


#GENERATION RATE
Gen = LabelFrame(InterArrivaltime, text = "Generation Rate(Mbps)")
Gen.pack(pady=10)

Gen_Entry = Entry(Gen, font=("Helvetica",10))
Gen_Entry.pack(pady=10,padx=10)

#result
res = LabelFrame(InterArrivaltime, text = "Inter Arrival time(µs)")
res.pack(pady=10)

Value_Entry = Entry(res, font=("Helvetica",10))
Value_Entry.pack(pady=10,padx=10)

button_frame1 = Frame(InterArrivaltime)
button_frame1.pack(pady=10)

Result_Button = Button(button_frame1,text= 'Result',command = value)
Result_Button.grid(row=0,column=0,padx=10)
Result_Button.bind('<Return>', value)
root.mainloop()