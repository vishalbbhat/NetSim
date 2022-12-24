from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title('Generation Rate Calculator')
root.geometry("500x500")
################################## CREATING NOTEBOOKS ################################################################
my_notebook = ttk.Notebook(root)
my_notebook.pack(padx=20, pady=20)
    
Generation_rate = Frame(my_notebook, width = 480, height = 480)
InterArrivaltime = Frame(my_notebook, width = 480, height = 480)
HTTP = Frame(my_notebook, width = 480, height = 480)
VIDEO_FRAME = Frame(my_notebook, width = 480, height = 480)


Generation_rate.pack(fill="both",expand =1)
InterArrivaltime.pack(fill="both",expand = 1)
HTTP.pack(fill="both",expand = 1)
VIDEO_FRAME.pack(padx=20, pady=20)


my_notebook.add(Generation_rate, text = "calculate generation rate")
my_notebook.add(InterArrivaltime, text = "calculate Inter Arrival Time")
my_notebook.add(HTTP, text = "HTTP")
my_notebook.add(VIDEO_FRAME,text= "VIDEO")

##################################### CALCULATION ####################################################################
# def returnPressed_GEN(event):
#     GEN()
# def returnPressed_IAT(event):
#     IAT()
# def returnPressed_HTTP(event):
#     HTTPs()
# def returnPressed_VIDEO(event):
#     VIDEO()

def GEN():
    result_Entry.delete(0, 'end')
    ps=float(var_entry.get())
    iat=float(var2_entry.get())
    result=(ps*8)/iat
    result_Entry.insert(END, str(result))

def IAT():
    Value_Entry.delete(0, 'end')
    ps = float(Packet_Entry.get())
    gen = float(Gen_Entry.get())
    result = (ps * 8) / gen
    Value_Entry.insert(END, str(result))

def HTTPs():
    HTTP_Gen_Entry.delete(0, 'end')
    page_S=float(Page_size_Entry.get())
    page_C=float(Page_count_Entry.get())
    inter_AT=float(IAT_Value_Entry.get())
    result=(page_S*8*page_C)/inter_AT
    HTTP_Gen_Entry.insert(END, str(result))

def VIDEO():
    video_Gen_Entry.delete(0,'end')
    FPS=int(fps_Entry.get())
    PPF=int(ppf_Entry.get())
    BPP=float(bpp_Entry.get())
    result=(FPS*PPF*BPP)
    result/=1000000
    video_Gen_Entry.insert(END, str(result))
############################# GENERATION RATE BOOK #########################################################
variable1 = LabelFrame(Generation_rate, text = "Size of the Packet(in Bytes)")
variable1.pack(pady=10)
#Entry box
var_entry = Entry(variable1, font=("Helvetica",10))
var_entry.insert(0, 1460)
var_entry.pack(pady=10,padx=10)


#IAT
variable2 = LabelFrame(Generation_rate, text = "IAT (microseconds)")
variable2.pack(pady=10)

var2_entry = Entry(variable2, font=("Helvetica",10))
var2_entry.pack(pady=10,padx=10)

#result
res = LabelFrame(Generation_rate, text = "Generation Rate(Mbps)")
res.pack(pady=10)

result_Entry = Entry(res, font=("Helvetica",10))
result_Entry.pack(pady=10,padx=10)

#Button Frame
button_frame = Frame(Generation_rate)
button_frame.pack(pady=10)

#Button Creation
Result_Button = Button(button_frame,text= 'Result',command = GEN)
Result_Button.grid(row=0,column=0,padx=10)
# Result_Button.bind('<Return>', returnPressed_GEN)
############################## IAT BOOK ####################################################################

Packet_size = LabelFrame(InterArrivaltime, text = "Size of the Packet(in Bytes)")
Packet_size.pack(pady=10)
#Entry box
Packet_Entry = Entry(Packet_size, font=("Helvetica",10))
Packet_Entry.insert(0, 1460)
Packet_Entry.pack(pady=10,padx=10)


#GENERATION RATE
Gen = LabelFrame(InterArrivaltime, text = "Generation Rate (Mbps)")
Gen.pack(pady=10)

Gen_Entry = Entry(Gen, font=("Helvetica",10))
Gen_Entry.pack(pady=10,padx=10)

#result
res = LabelFrame(InterArrivaltime, text = "InterArrivaltime (Micro seconds)")
res.pack(pady=10)

Value_Entry = Entry(res, font=("Helvetica",10))
Value_Entry.pack(pady=10,padx=10)

#Button Frame
button_frame1 = Frame(InterArrivaltime)
button_frame1.pack(pady=10)

#Button Creation
Result_Button = Button(button_frame1,text= 'result',command = IAT)
#Result_Button.bind('<Return>', ans)
Result_Button.grid(row=0,column=0,padx=10)
#InterArrivaltime.bind('<Return>', returnPressed_IAT)
############################## HTTP BOOK ####################################################################

Page_size = LabelFrame(HTTP, text = "Page Size(in Bytes)")
Page_size.pack(pady=10)
#Entry box
Page_size_Entry = Entry(Page_size, font=("Helvetica",10))
Page_size_Entry.pack(pady=10,padx=10)

#INTER ARRIVAL TIME
HTTP_IAT = LabelFrame(HTTP, text = "InterArrivaltime (Microseconds)")
HTTP_IAT.pack(pady=10)

IAT_Value_Entry = Entry(HTTP_IAT, font=("Helvetica",10))
IAT_Value_Entry.pack(pady=10,padx=10)

#PAGE COUNT
Page_count = LabelFrame(HTTP, text = "Page Count")
Page_count.pack(pady=10)

Page_count_Entry = Entry(Page_count, font=("Helvetica",10))
Page_count_Entry.pack(pady=10,padx=10)

#GENERATION RATE
HTTP_Gen = LabelFrame(HTTP, text = "Generation Rate (Mbps)")
HTTP_Gen.pack(pady=10)

HTTP_Gen_Entry = Entry(HTTP_Gen, font=("Helvetica",10))
HTTP_Gen_Entry.pack(pady=10,padx=10)

#Button Frame
button_frame2 = Frame(HTTP)
button_frame2.pack(pady=10)


#Button Creation
Result_Button = Button(button_frame2,text= 'result',command = HTTPs)
Result_Button.grid(row=0,column=0,padx=10)
#HTTP.bind('<Return>', returnPressed_HTTP)

# ################################ VIDEO BOOK ###################################################################
#FPS
fps = LabelFrame(VIDEO_FRAME, text = "Frames per Second")
fps.pack(pady=10)

fps_Entry = Entry(fps, font=("Helvetica",10))
fps_Entry.pack(pady=10,padx=10)

#PPF
ppf = LabelFrame(VIDEO_FRAME, text = "Pixel per Frame")
ppf.pack(pady=10)

ppf_Entry = Entry(ppf, font=("Helvetica",10))
ppf_Entry.pack(pady=10,padx=10)

#BPP
bpp = LabelFrame(VIDEO_FRAME, text = "Bits per Pixel(mean)")
bpp.pack(pady=10)

bpp_Entry = Entry(bpp, font=("Helvetica",10))
bpp_Entry.pack(pady=10,padx=10)

#GENERATION RATE
video_Gen = LabelFrame(VIDEO_FRAME, text = "Generation Rate (Mbps)")
video_Gen.pack(pady=10)

video_Gen_Entry = Entry(video_Gen, font=("Helvetica",10))
video_Gen_Entry.pack(pady=10,padx=10)


#Button Frame
button_frame3 = Frame(VIDEO_FRAME)
button_frame3.pack(pady=10)



#Button Creation
Result_Button = Button(button_frame3,text= 'result',command = VIDEO)
Result_Button.grid(row=0,column=0,padx=10)
#VIDEO_FRAME.bind('<Return>', returnPressed_VIDEO)
# root.bind('<Return>', returnPressed)

root.mainloop()