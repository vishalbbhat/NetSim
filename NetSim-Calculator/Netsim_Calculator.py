import os
import math
import tkinter as tk
from tkinter import *
from tkinter import ttk

flag_Rxpower = 0
flag_Genrate = 0
count_grate = 0
count_rxpower = 0


def frame_created_GR():
    ################################## CREATING NOTEBOOKS ################################################################
    global my_notebook
    my_notebook = ttk.Notebook(window)
    my_notebook.pack(padx=50, pady=50)
    global Generation_rate
    global InterArrivaltime
    global HTTP
    global VIDEO_FRAME

    Generation_rate = Frame(my_notebook, width=700, height=600)
    Generation_rate.pack(fill="both", expand=1)
    my_notebook.add(Generation_rate, text="Generation Rate")


    HTTP = Frame(my_notebook, width=500, height=750)
    VIDEO_FRAME = Frame(my_notebook, width=500, height=750)


    HTTP.pack(fill="both", expand=1)
    VIDEO_FRAME.pack(fill="both", expand=1)


    my_notebook.add(HTTP, text="HTTP")
    my_notebook.add(VIDEO_FRAME, text="VIDEO")



    ############################# GENERATION RATE BOOK #########################################################
    Receive_Power_Calc_Home = Label(Generation_rate, text='Generation Rate', font="Arial 12 bold")
    Receive_Power_Calc_Home.pack(pady=10)
    Receive_Power_Calc_Home.place(x=250, y=20)
    variable1 = Label(Generation_rate, text="Size of the Packet(in Bytes)", bd=3)
    variable1.pack(pady=10)
    variable1.place(x=30,y=60)
    # Entry box
    global var_entry
    var_entry = Entry(Generation_rate, width=15, bd=3, font=('Arial 10'))
    var_entry.insert(0, 1460)
    var_entry.pack(pady=10, padx=10)
    var_entry.place(x=220,y=58)

    # IAT
    variable2 = Label(Generation_rate, text="IAT (\u03BCs)", bd=3)
    variable2.pack(pady=10)
    variable2.place(x=30,y=120)
    global var2_entry
    var2_entry = Entry(Generation_rate, width=15, bd=3, font=('Arial 10'))
    var2_entry.pack(pady=10, padx=10)
    var2_entry.place(x=220,y=118)

    # result
    res = Label(Generation_rate, text="Generation Rate(Mbps)", bd=3)
    res.pack(pady=10)
    res.place(x=30,y=180)
    global result_Entry
    result_Entry = Entry(Generation_rate, width=15, bd=3, font=('Arial 10'))
    result_Entry.pack(pady=10, padx=10)
    result_Entry.place(x=220,y=178)

    # #BUTTONS
    Gen_rate_button = ttk.Button(Generation_rate, text="Generation Rate", command=GEN)
    Gen_rate_button.pack(ipadx=10, pady=10)
    Gen_rate_button.place(x=280, y=298)
    #
    IAT_button = ttk.Button(Generation_rate, text="IAT", command=IAT)
    IAT_button.pack(ipadx=10, pady=10)
    IAT_button.place(x=280, y=338)

    ############################## HTTP BOOK ####################################################################
    Receive_Power_Calc_Home = Label(HTTP, text='HTTP APP', font="Arial 12 bold")
    Receive_Power_Calc_Home.pack(pady=10)
    Receive_Power_Calc_Home.place(x=250, y=20)

    Page_size = Label(HTTP, text="Page Size(in Bytes)",bd=3)
    Page_size.pack(pady=10)
    Page_size.place(x=30,y=60)

    # Entry box
    global Page_size_Entry
    Page_size_Entry = Entry(HTTP, width=15, bd=3, font=('Arial 10'))
    Page_size_Entry.pack(pady=10, padx=10)
    Page_size_Entry.place(x=220,y=58)

    # INTER ARRIVAL TIME
    HTTP_IAT = Label(HTTP, text="InterArrivaltime (\u03BCs)", bd=3)
    HTTP_IAT.pack(pady=10)
    HTTP_IAT.place(x=30,y=120)
    global IAT_Value_Entry
    IAT_Value_Entry = Entry(HTTP, width=15, bd=3, font=('Arial 10'))
    IAT_Value_Entry.pack(pady=10, padx=10)
    IAT_Value_Entry.place(x=220,y=118)

    # PAGE COUNT
    Page_count = Label(HTTP, text="Page Count")
    Page_count.pack(pady=10)
    Page_count.place(x=30,y=180)
    global Page_count_Entry
    Page_count_Entry = Entry(HTTP, width=15, bd=3, font=('Arial 10'))
    Page_count_Entry.pack(pady=10, padx=10)
    Page_count_Entry.place(x=220,y=178)

    # GENERATION RATE
    HTTP_Gen = Label(HTTP, text="Generation Rate (Mbps)")
    HTTP_Gen.pack(pady=10)
    HTTP_Gen.place(x=30,y=240)
    global HTTP_Gen_Entry
    HTTP_Gen_Entry = Entry(HTTP, width=15, bd=3, font=('Arial 10'))
    HTTP_Gen_Entry.pack(pady=10, padx=10)
    HTTP_Gen_Entry.place(x=220,y=238)

    # #BUTTONS
    Gen_rate_button = ttk.Button(HTTP, text="Generation Rate", command=Gen_HTTP)
    Gen_rate_button.pack(ipadx=10, pady=10)
    Gen_rate_button.place(x=280, y=298)
    #
    IAT_button = ttk.Button(HTTP, text="IAT", command=IAT_HTTP)
    IAT_button.pack(ipadx=10, pady=10)
    IAT_button.place(x=280, y=338)

    # ################################ VIDEO BOOK ###################################################################
    Receive_Power_Calc_Home = Label(VIDEO_FRAME, text='VIDEO APP', font="Arial 12 bold")
    Receive_Power_Calc_Home.pack(pady=10)
    Receive_Power_Calc_Home.place(x=250, y=20)
    # FPS
    fps = Label(VIDEO_FRAME, text="Frames per Second")
    fps.pack(pady=10)
    fps.place(x=30,y=60)
    global fps_Entry
    fps_Entry = Entry(VIDEO_FRAME, width=15, bd=3, font=('Arial 10'))
    fps_Entry.pack(pady=10, padx=10)
    fps_Entry.place(x=220,y=58)

    # PPF
    ppf = Label(VIDEO_FRAME, text="Pixel per Frame")
    ppf.pack(pady=10)
    ppf.place(x=30,y=120)
    global ppf_Entry
    ppf_Entry = Entry(VIDEO_FRAME, width=15, bd=3, font=('Arial 10'))
    ppf_Entry.pack(pady=10, padx=10)
    ppf_Entry.place(x=220,y=118)

    # BPP
    bpp = Label(VIDEO_FRAME, text="Bits per Pixel(mean)")
    bpp.pack(pady=10)
    bpp.place(x=30,y=180)
    global bpp_Entry
    bpp_Entry = Entry(VIDEO_FRAME, width=15, bd=3, font=('Arial 10'))
    bpp_Entry.pack(pady=10, padx=10)
    bpp_Entry.place(x=220,y=178)

    # GENERATION RATE
    video_Gen = Label(VIDEO_FRAME, text="Generation Rate (Mbps)")
    video_Gen.pack(pady=10)
    video_Gen.place(x=30,y=240)
    global video_Gen_Entry
    video_Gen_Entry = Entry(VIDEO_FRAME, width=15, bd=3, font=('Arial 10'))
    video_Gen_Entry.pack(pady=10, padx=10)
    video_Gen_Entry.place(x=220,y=238)

    # #BUTTONS
    Gen_rate_button = ttk.Button(VIDEO_FRAME, text="Generation Rate", command=VIDEO_Gen)
    Gen_rate_button.pack(ipadx=10, pady=10)
    Gen_rate_button.place(x=280, y=298)

def frame_created_RP():
    global my_notebook2
    my_notebook2 = ttk.Notebook(window)
    my_notebook2.pack(padx=50, pady=50)
    #Frame1
    Frame1 = Frame(my_notebook2, width = 700, height = 500)
    Frame1.pack(fill="both",expand=1)
    my_notebook2.add(Frame1, text = "Log Distance")
    # Frame2
    Frame2 = Frame(my_notebook2, width=700, height=500)
    Frame2.pack(fill="both", expand=1)
    my_notebook2.add(Frame2, text="Hata Urban")
    # Frame3
    Frame3 = Frame(my_notebook2, width=700, height=500)
    Frame3.pack(fill="both", expand=1)
    my_notebook2.add(Frame3, text="Hata Suburban")
    # Frame4
    Frame4 = Frame(my_notebook2, width=700, height=500)
    Frame4.pack(fill="both", expand=1)
    my_notebook2.add(Frame4, text="Cost Hata urban & suburban")
    # Frame5
    Frame5 = Frame(my_notebook2, width=700, height=500)
    Frame5.pack(fill="both", expand=1)
    my_notebook2.add(Frame5, text="Indoor Office & Factory")
    # Frame6
    Frame6 = Frame(my_notebook2, width=700, height=500)
    Frame6.pack(fill="both", expand=1)
    my_notebook2.add(Frame6, text="Indoor Home")
    Frame7 = Frame(my_notebook2, width=700, height=500)
    Frame7.pack(fill="both", expand=1)
    my_notebook2.add(Frame7, text="Two Ray")

    #########################################################################################################
    Receive_Power_Calc = Label(Frame1, text='LOG DISTANCE', font="Arial 12 bold")
    Receive_Power_Calc.pack(pady=10)
    Receive_Power_Calc.place(x=260, y=20)
    # #Transmitter Power
    global Transmitter_Power_mW_Entry
    Transmitter_Power_mW = Label(Frame1, text='Transmitter Power (mW)')
    Transmitter_Power_mW.pack(pady=10)
    Transmitter_Power_mW.place(x=30, y=60)
    Transmitter_Power_mW_Entry = Entry(Frame1, width=15, bd=3, font=('Arial 10'))
    Transmitter_Power_mW_Entry.pack(pady=10, padx=10)
    Transmitter_Power_mW_Entry.place(x=220, y=58)
    #
    # #Gain at Transmitter
    global Tx_Antenna_Gain_Entry
    Tx_Antenna_Gain = Label(Frame1, text='AntennaGain at Transmitter (dBm)')
    Tx_Antenna_Gain.pack(pady=10)
    Tx_Antenna_Gain.place(x=30, y=120)
    Tx_Antenna_Gain_Entry = Entry(Frame1, width=15, bd=3, font=('Arial 10'))
    Tx_Antenna_Gain_Entry.pack(pady=10, padx=10)
    Tx_Antenna_Gain_Entry.place(x=220, y=118)
    #
    # #Gain at Receiver
    global Rx_Antenna_Gain_Entry
    Rx_Antenna_Gain = Label(Frame1, text='AntennaGain at Receiver (dBm)')
    Rx_Antenna_Gain.pack(pady=10)
    Rx_Antenna_Gain.place(x=30, y=180)
    Rx_Antenna_Gain_Entry = Entry(Frame1, width=15, bd=3, font=('Arial 10'))
    Rx_Antenna_Gain_Entry.pack(pady=10, padx=10)
    Rx_Antenna_Gain_Entry.place(x=220, y=178)
    #
    # #Frequency (GHz)
    global Frequency_Entry
    Frequency = Label(Frame1, text='Frequency (GHz)')
    Frequency.pack(pady=10)
    Frequency.place(x=30, y=240)
    Frequency_Entry = Entry(Frame1, width=15, bd=3, font=('Arial 10'))
    Frequency_Entry.pack(pady=10, padx=10)
    Frequency_Entry.place(x=220, y=238)
    #
    # #d0
    global d0_Entry
    d0 = Label(Frame1, text='Reference Distance (d0)')
    d0.pack(pady=10)
    d0.place(x=340, y=60)
    d0_Entry = Entry(Frame1, width=15, bd=3, font=('Arial 10'))
    d0_Entry.pack(pady=10, padx=10)
    d0_Entry.place(x=520, y=58)
    #
    # #Pathloss_Exponent
    global Pathloss_Exponent_Entry
    Pathloss_Exponent = Label(Frame1, text='Pathloss Exponent (\u03B7)')
    Pathloss_Exponent.pack(pady=10)
    Pathloss_Exponent.place(x=340, y=120)
    Pathloss_Exponent_Entry = Entry(Frame1, width=15, bd=3, font=('Arial 10'))
    Pathloss_Exponent_Entry.pack(pady=10, padx=10)
    Pathloss_Exponent_Entry.place(x=520, y=118)
    #
    # #Distance
    global Distance_Entry
    Distance = Label(Frame1, text='Distance (m)')
    Distance.pack(pady=10)
    Distance.place(x=340, y=180)
    Distance_Entry = Entry(Frame1, width=15, bd=3, font=('Arial 10'))
    Distance_Entry.pack(pady=10, padx=10)
    Distance_Entry.place(x=520, y=178)
    #
    # #Received_Power
    global Received_Power_Entry
    Received_Power = Label(Frame1, text='Received Power (dBm)')
    Received_Power.pack(pady=10)
    Received_Power.place(x=340, y=240)
    Received_Power_Entry = Entry(Frame1, width=15, bd=3, font=('Arial 10'))
    Received_Power_Entry.pack(pady=10, padx=10)
    Received_Power_Entry.place(x=520, y=238)
    #
    # #BUTTONS
    Calc_Rx_Power = ttk.Button(Frame1, text="Rxpower", command=Rxpower)
    Calc_Rx_Power.pack(ipadx=10, pady=10)
    Calc_Rx_Power.place(x=280, y=298)
    #
    Calc_Distance = ttk.Button(Frame1, text="Distance", command=Dist)
    Calc_Distance.pack(ipadx=10, pady=10)
    Calc_Distance.place(x=280, y=338)

    # ******************************************** Frame2 Hata Urban ***************************************************************************************************

    # #TITLE
    Receive_Power_Calc_Hata = Label(Frame2, text='HATA URBAN', font="Arial 12 bold")
    Receive_Power_Calc_Hata.pack(pady=10)
    Receive_Power_Calc_Hata.place(x=250, y=20)
    # #Transmitter Power
    Transmitter_Power_mW_Hata = Label(Frame2, text='Transmitter Power (mW)')
    Transmitter_Power_mW_Hata.pack(pady=10)
    Transmitter_Power_mW_Hata.place(x=30, y=60)
    global Transmitter_Power_mW_Hata_Entry
    Transmitter_Power_mW_Hata_Entry = Entry(Frame2, width=15, bd=3, font=('Arial 10'))
    Transmitter_Power_mW_Hata_Entry.pack(pady=10, padx=10)
    Transmitter_Power_mW_Hata_Entry.place(x=220, y=58)
    #
    # #Height at Transmitter
    Tx_Antenna_Height_Hata = Label(Frame2, text='Antenna Height at Transmitter(m)')
    Tx_Antenna_Height_Hata.pack(pady=10)
    Tx_Antenna_Height_Hata.place(x=30, y=120)
    global Tx_Antenna_Height_Hata_Entry
    Tx_Antenna_Height_Hata_Entry = Entry(Frame2, width=15, bd=3, font=('Arial 10'))
    Tx_Antenna_Height_Hata_Entry.pack(pady=10, padx=10)
    Tx_Antenna_Height_Hata_Entry.place(x=220, y=118)
    #
    # #Distance
    Distance_Hata = Label(Frame2, text='Distance (m)')
    Distance_Hata.pack(pady=10)
    Distance_Hata.place(x=30, y=180)
    global Distance_Hata_Entry
    Distance_Hata_Entry = Entry(Frame2, width=15, bd=3, font=('Arial 10'))
    Distance_Hata_Entry.pack(pady=10, padx=10)
    Distance_Hata_Entry.place(x=220, y=178)

    # #Height at Receiver
    Rx_Antenna_Height_Hata = Label(Frame2, text='Antenna Height at Receiver(m)')
    Rx_Antenna_Height_Hata.pack(pady=10)
    Rx_Antenna_Height_Hata.place(x=340, y=60)
    global Rx_Antenna_Height_Hata_Entry
    Rx_Antenna_Height_Hata_Entry = Entry(Frame2, width=15, bd=3, font=('Arial 10'))
    Rx_Antenna_Height_Hata_Entry.pack(pady=10, padx=10)
    Rx_Antenna_Height_Hata_Entry.place(x=520, y=58)
    #
    # #Frequency (GHz)
    Frequency_Hata = Label(Frame2, text='Frequency (GHz)')
    Frequency_Hata.pack(pady=10)
    Frequency_Hata.place(x=340, y=120)
    global Frequency_Hata_Entry
    Frequency_Hata_Entry = Entry(Frame2, width=15, bd=3, font=('Arial 10'))
    Frequency_Hata_Entry.pack(pady=10, padx=10)
    Frequency_Hata_Entry.place(x=520, y=118)

    # #Received_Power
    Received_Power_Hata = Label(Frame2, text='Received Power (mW)')
    Received_Power_Hata.pack(pady=10)
    Received_Power_Hata.place(x=340, y=180)
    global Received_Power_Hata_Entry
    Received_Power_Hata_Entry = Entry(Frame2, width=15, bd=3, font=('Arial 10'))
    Received_Power_Hata_Entry.pack(pady=10, padx=10)
    Received_Power_Hata_Entry.place(x=520, y=178)
    #
    # #BUTTONS
    Calc_Rx_Power_Hata = ttk.Button(Frame2, text="Rxpower", command=Rxpower_Hata)
    Calc_Rx_Power_Hata.pack(ipadx=10, pady=10)
    Calc_Rx_Power_Hata.place(x=280, y=298)
    #
    Calc_Distance_Hata = ttk.Button(Frame2, text="Distance", command=Dist_Hata)
    Calc_Distance_Hata.pack(ipadx=10, pady=10)
    Calc_Distance_Hata.place(x=280, y=338)
    # ******************************************** Frame3 Hata Suburban ***************************************************************************************************

    # #TITLE
    Receive_Power_Calc_Sub = Label(Frame3, text='HATA SUBURBAN', font="Arial 12 bold")
    Receive_Power_Calc_Sub.pack(pady=10)
    Receive_Power_Calc_Sub.place(x=250, y=20)
    # #Transmitter Power
    Transmitter_Power_mW_Sub = Label(Frame3, text='Transmitter Power (mW)')
    Transmitter_Power_mW_Sub.pack(pady=10)
    Transmitter_Power_mW_Sub.place(x=30, y=60)
    global Transmitter_Power_mW_Sub_Entry
    Transmitter_Power_mW_Sub_Entry = Entry(Frame3, width=15, bd=3, font=('Arial 10'))
    Transmitter_Power_mW_Sub_Entry.pack(pady=10, padx=10)
    Transmitter_Power_mW_Sub_Entry.place(x=220, y=58)
    #
    # #Height at Transmitter
    Tx_Antenna_Height_Sub = Label(Frame3, text='Antenna Height at Transmitter(m)')
    Tx_Antenna_Height_Sub.pack(pady=10)
    Tx_Antenna_Height_Sub.place(x=30, y=120)
    global Tx_Antenna_Height_Sub_Entry
    Tx_Antenna_Height_Sub_Entry = Entry(Frame3, width=15, bd=3, font=('Arial 10'))
    Tx_Antenna_Height_Sub_Entry.pack(pady=10, padx=10)
    Tx_Antenna_Height_Sub_Entry.place(x=220, y=118)
    #
    # #Distance
    Distance_Sub = Label(Frame3, text='Distance (m) ')
    Distance_Sub.pack(pady=10)
    Distance_Sub.place(x=30, y=180)
    global Distance_Sub_Entry
    Distance_Sub_Entry = Entry(Frame3, width=15, bd=3, font=('Arial 10'))
    Distance_Sub_Entry.pack(pady=10, padx=10)
    Distance_Sub_Entry.place(x=220, y=178)

    # #Height at Receiver
    Rx_Antenna_Height_Sub = Label(Frame3, text='Antenna Height at Receiver(m)')
    Rx_Antenna_Height_Sub.pack(pady=10)
    Rx_Antenna_Height_Sub.place(x=340, y=60)
    global Rx_Antenna_Height_Sub_Entry
    Rx_Antenna_Height_Sub_Entry = Entry(Frame3, width=15, bd=3, font=('Arial 10'))
    Rx_Antenna_Height_Sub_Entry.pack(pady=10, padx=10)
    Rx_Antenna_Height_Sub_Entry.place(x=520, y=58)
    #
    # #Frequency (GHz)
    Frequency_Sub = Label(Frame3, text='Frequency (GHz)')
    Frequency_Sub.pack(pady=10)
    Frequency_Sub.place(x=340, y=120)
    global Frequency_Sub_Entry
    Frequency_Sub_Entry = Entry(Frame3, width=15, bd=3, font=('Arial 10'))
    Frequency_Sub_Entry.pack(pady=10, padx=10)
    Frequency_Sub_Entry.place(x=520, y=118)

    # #Received_Power
    Received_Power_Sub = Label(Frame3, text='Received Power (dBm)')
    Received_Power_Sub.pack(pady=10)
    Received_Power_Sub.place(x=340, y=180)
    global Received_Power_Sub_Entry
    Received_Power_Sub_Entry = Entry(Frame3, width=15, bd=3, font=('Arial 10'))
    Received_Power_Sub_Entry.pack(pady=10, padx=10)
    Received_Power_Sub_Entry.place(x=520, y=178)
    #
    # #BUTTONS
    Calc_Rx_Power_Sub = ttk.Button(Frame3, text="Rxpower", command=Rxpower_Sub)
    Calc_Rx_Power_Sub.pack(ipadx=10, pady=10)
    Calc_Rx_Power_Sub.place(x=280, y=298)
    #
    Calc_Distance_Sub = ttk.Button(Frame3, text="Distance", command=Dist_Sub)
    Calc_Distance_Sub.pack(ipadx=10, pady=10)
    Calc_Distance_Sub.place(x=280, y=338)

    # ******************************************** Frame4 Cost Urban & Suburban ***************************************************************************************************

    # #TITLE
    Receive_Power_Calc_Cost = Label(Frame4, text='COST HATA URBAN & SUBURBAN', font="Arial 12 bold")
    Receive_Power_Calc_Cost.pack(pady=10)
    Receive_Power_Calc_Cost.place(x=250, y=20)
    # #Transmitter Power
    Transmitter_Power_mW_Cost = Label(Frame4, text='Transmitter Power (mW)')
    Transmitter_Power_mW_Cost.pack(pady=10)
    Transmitter_Power_mW_Cost.place(x=30, y=60)
    global Transmitter_Power_mW_Cost_Entry
    Transmitter_Power_mW_Cost_Entry = Entry(Frame4, width=15, bd=3, font=('Arial 10'))
    Transmitter_Power_mW_Cost_Entry.pack(pady=10, padx=10)
    Transmitter_Power_mW_Cost_Entry.place(x=220, y=58)
    #
    # #Height at Transmitter
    Tx_Antenna_Height_Cost = Label(Frame4, text='Antenna Height at Transmitter(m)')
    Tx_Antenna_Height_Cost.pack(pady=10)
    Tx_Antenna_Height_Cost.place(x=30, y=120)
    global Tx_Antenna_Height_Cost_Entry
    Tx_Antenna_Height_Cost_Entry = Entry(Frame4, width=15, bd=3, font=('Arial 10'))
    Tx_Antenna_Height_Cost_Entry.pack(pady=10, padx=10)
    Tx_Antenna_Height_Cost_Entry.place(x=220, y=118)
    #
    # #Distance
    Distance_Cost = Label(Frame4, text='Distance (m)')
    Distance_Cost.pack(pady=10)
    Distance_Cost.place(x=30, y=180)
    global Distance_Cost_Entry
    Distance_Cost_Entry = Entry(Frame4, width=15, bd=3, font=('Arial 10'))
    Distance_Cost_Entry.pack(pady=10, padx=10)
    Distance_Cost_Entry.place(x=220, y=178)

    # #Height at Receiver
    Rx_Antenna_Height_Cost = Label(Frame4, text='Antenna Height at Receiver(m)')
    Rx_Antenna_Height_Cost.pack(pady=10)
    Rx_Antenna_Height_Cost.place(x=340, y=60)
    global Rx_Antenna_Height_Cost_Entry
    Rx_Antenna_Height_Cost_Entry = Entry(Frame4, width=15, bd=3, font=('Arial 10'))
    Rx_Antenna_Height_Cost_Entry.pack(pady=10, padx=10)
    Rx_Antenna_Height_Cost_Entry.place(x=520, y=58)
    #
    # #Frequency (GHz)
    Frequency_Cost = Label(Frame4, text='Frequency (GHz)')
    Frequency_Cost.pack(pady=10)
    Frequency_Cost.place(x=340, y=120)
    global Frequency_Cost_Entry
    Frequency_Cost_Entry = Entry(Frame4, width=15, bd=3, font=('Arial 10'))
    Frequency_Cost_Entry.pack(pady=10, padx=10)
    Frequency_Cost_Entry.place(x=520, y=118)

    # #Received_Power
    Received_Power_Cost = Label(Frame4, text='Received Power (dBm)')
    Received_Power_Cost.pack(pady=10)
    Received_Power_Cost.place(x=340, y=180)
    global Received_Power_Cost_Entry
    Received_Power_Cost_Entry = Entry(Frame4, width=15, bd=3, font=('Arial 10'))
    Received_Power_Cost_Entry.pack(pady=10, padx=10)
    Received_Power_Cost_Entry.place(x=520, y=178)
    #
    ## CM
    cm = ttk.Label(Frame4, text="CM")
    cm.pack(pady=10)
    cm.place(x=340, y=240)
    n = tk.StringVar()
    global Value
    Value = ttk.Combobox(Frame4, width=15, textvariable=n)

    Value['values'] = ('3', '0')
    Value.pack()
    Value.place(x=520, y=238)

    # #BUTTONS
    Calc_Rx_Power_Cost = ttk.Button(Frame4, text="Rxpower", command=Rxpower_Cost)
    Calc_Rx_Power_Cost.pack(ipadx=10, pady=10)
    Calc_Rx_Power_Cost.place(x=280, y=298)
    #
    Calc_Distance_Cost = ttk.Button(Frame4, text="Distance", command=Dist_Cost)
    Calc_Distance_Cost.pack(ipadx=10, pady=10)
    Calc_Distance_Cost.place(x=280, y=338)
    # ******************************************** Frame5 Indoor Office & Factory ***************************************************************************************************

    # #TITLE
    Receive_Power_Indoor_Calc = Label(Frame5, text='INDOOR OFFICE & INDOOR FACTORY', font="Arial 12 bold")
    Receive_Power_Indoor_Calc.pack(pady=10)
    Receive_Power_Indoor_Calc.place(x=250, y=20)
    # #Transmitter Power
    global Transmitter_Power_Indoor_mW_Entry
    Transmitter_Power_Indoor_mW = Label(Frame5, text='Transmitter Power (mW)')
    Transmitter_Power_Indoor_mW.pack(pady=10)
    Transmitter_Power_Indoor_mW.place(x=30, y=60)
    Transmitter_Power_Indoor_mW_Entry = Entry(Frame5, width=15, bd=3, font=('Arial 10'))
    Transmitter_Power_Indoor_mW_Entry.pack(pady=10, padx=10)
    Transmitter_Power_Indoor_mW_Entry.place(x=220, y=58)
    #
    # #Gain at Transmitter
    global Tx_Antenna_Gain_Indoor_Entry
    Tx_Antenna_Gain_Indoor = Label(Frame5, text='AntennaGain at Transmitter (dBm)')
    Tx_Antenna_Gain_Indoor.pack(pady=10)
    Tx_Antenna_Gain_Indoor.place(x=30, y=120)
    Tx_Antenna_Gain_Indoor_Entry = Entry(Frame5, width=15, bd=3, font=('Arial 10'))
    Tx_Antenna_Gain_Indoor_Entry.pack(pady=10, padx=10)
    Tx_Antenna_Gain_Indoor_Entry.place(x=220, y=118)
    #
    # #Gain at Receiver
    global Rx_Antenna_Gain_Indoor_Entry
    Rx_Antenna_Gain_Indoor = Label(Frame5, text='AntennaGain at Receiver (dBm)')
    Rx_Antenna_Gain_Indoor.pack(pady=10)
    Rx_Antenna_Gain_Indoor.place(x=30, y=180)
    Rx_Antenna_Gain_Indoor_Entry = Entry(Frame5, width=15, bd=3, font=('Arial 10'))
    Rx_Antenna_Gain_Indoor_Entry.pack(pady=10, padx=10)
    Rx_Antenna_Gain_Indoor_Entry.place(x=220, y=178)
    #
    # #Frequency (GHz)
    global Frequency_Indoor_Entry
    Frequency_Indoor = Label(Frame5, text='Frequency (GHz)')
    Frequency_Indoor.pack(pady=10)
    Frequency_Indoor.place(x=30, y=240)
    Frequency_Indoor_Entry = Entry(Frame5, width=15, bd=3, font=('Arial 10'))
    Frequency_Indoor_Entry.pack(pady=10, padx=10)
    Frequency_Indoor_Entry.place(x=220, y=238)
    #
    # #d0
    global d0_Indoor_Entry
    d0_Indoor = Label(Frame5, text='Reference Distance (d0)')
    d0_Indoor.pack(pady=10)
    d0_Indoor.place(x=340, y=60)
    d0_Indoor_Entry = Entry(Frame5, width=15, bd=3, font=('Arial 10'))
    d0_Indoor_Entry.pack(pady=10, padx=10)
    d0_Indoor_Entry.place(x=520, y=58)
    #
    # #Pathloss_Exponent
    global Pathloss_Exponent_Indoor_Entry
    Pathloss_Exponent_Indoor = Label(Frame5, text='Pathloss Exponent (\u03B7)')
    Pathloss_Exponent_Indoor.pack(pady=10)
    Pathloss_Exponent_Indoor.place(x=340, y=120)
    n = tk.StringVar()
    Pathloss_Exponent_Indoor_Entry = ttk.Combobox(Frame5, width=15, textvariable=n)
    Pathloss_Exponent_Indoor_Entry['values'] = ('2.6', '2.1')
    Pathloss_Exponent_Indoor_Entry.pack(pady=10, padx=10)
    Pathloss_Exponent_Indoor_Entry.place(x=520, y=118)
    #
    # #Distance
    global Distance_Indoor_Entry
    Distance_Indoor = Label(Frame5, text='Distance (m)')
    Distance_Indoor.pack(pady=10)
    Distance_Indoor.place(x=340, y=180)
    Distance_Indoor_Entry = Entry(Frame5, width=15, bd=3, font=('Arial 10'))
    Distance_Indoor_Entry.pack(pady=10, padx=10)
    Distance_Indoor_Entry.place(x=520, y=178)
    #
    # #Received_Power
    global Received_Power_Indoor_Entry
    Received_Power_Indoor = Label(Frame5, text='Received Power (dBm)')
    Received_Power_Indoor.pack(pady=10)
    Received_Power_Indoor.place(x=340, y=240)
    Received_Power_Indoor_Entry = Entry(Frame5, width=15, bd=3, font=('Arial 10'))
    Received_Power_Indoor_Entry.pack(pady=10, padx=10)
    Received_Power_Indoor_Entry.place(x=520, y=238)
    #
    # #BUTTONS
    Calc_Rx_Power_Indoor = ttk.Button(Frame5, text="Rxpower", command=Rxpower_Indoor)
    Calc_Rx_Power_Indoor.pack(ipadx=10, pady=10)
    Calc_Rx_Power_Indoor.place(x=280, y=298)
    #
    Calc_Distance_Indoor = ttk.Button(Frame5, text="Distance", command=Dist_Indoor)
    Calc_Distance_Indoor.pack(ipadx=10, pady=10)
    Calc_Distance_Indoor.place(x=280, y=338)

    # ******************************************************Frame6 Indoor Home *******************************************************************************************
    # #TITLE
    Receive_Power_Calc_Home = Label(Frame6, text='INDOOR HOME', font="Arial 12 bold")
    Receive_Power_Calc_Home.pack(pady=10)
    Receive_Power_Calc_Home.place(x=250, y=20)
    # #Transmitter Power
    global Transmitter_Power_mW_Home_Entry
    Transmitter_Power_Home_mW = Label(Frame6, text='Transmitter Power (mW)')
    Transmitter_Power_Home_mW.pack(pady=10)
    Transmitter_Power_Home_mW.place(x=30, y=60)
    Transmitter_Power_mW_Home_Entry = Entry(Frame6, width=15, bd=3, font=('Arial 10'))
    Transmitter_Power_mW_Home_Entry.pack(pady=10, padx=10)
    Transmitter_Power_mW_Home_Entry.place(x=220, y=58)
    #
    # #Gain at Transmitter
    global Tx_Antenna_Gain_Home_Entry
    Tx_Antenna_Gain_Home = Label(Frame6, text='AntennaGain at Transmitter (dBm)')
    Tx_Antenna_Gain_Home.pack(pady=10)
    Tx_Antenna_Gain_Home.place(x=30, y=120)
    Tx_Antenna_Gain_Home_Entry = Entry(Frame6, width=15, bd=3, font=('Arial 10'))
    Tx_Antenna_Gain_Home_Entry.pack(pady=10, padx=10)
    Tx_Antenna_Gain_Home_Entry.place(x=220, y=118)
    #
    # #Gain at Receiver
    global Rx_Antenna_Gain_Home_Entry
    Rx_Antenna_Gain_Home = Label(Frame6, text='AntennaGain at Receiver (dBm)')
    Rx_Antenna_Gain_Home.pack(pady=10)
    Rx_Antenna_Gain_Home.place(x=30, y=180)
    Rx_Antenna_Gain_Home_Entry = Entry(Frame6, width=15, bd=3, font=('Arial 10'))
    Rx_Antenna_Gain_Home_Entry.pack(pady=10, padx=10)
    Rx_Antenna_Gain_Home_Entry.place(x=220, y=178)
    #
    # #Frequency (GHz)
    global Frequency_Home_Entry
    Frequency_Home = Label(Frame6, text='Frequency (GHz)')
    Frequency_Home.pack(pady=10)
    Frequency_Home.place(x=30, y=240)
    Frequency_Home_Entry = Entry(Frame6, width=15, bd=3, font=('Arial 10'))
    Frequency_Home_Entry.pack(pady=10, padx=10)
    Frequency_Home_Entry.place(x=220, y=238)
    #
    # #d0
    global d0_Home_Entry
    d0_Home = Label(Frame6, text='Reference Distance (d0)')
    d0_Home.pack(pady=10)
    d0_Home.place(x=340, y=60)
    d0_Home_Entry = Entry(Frame6, width=15, bd=3, font=('Arial 10'))
    d0_Home_Entry.pack(pady=10, padx=10)
    d0_Home_Entry.place(x=520, y=58)
    #
    # #Pathloss_Exponent
    global Pathloss_Exponent_Home_Entry
    Pathloss_Exponent_Home = Label(Frame6, text='Pathloss Exponent (\u03B7)')
    Pathloss_Exponent_Home.pack(pady=10)
    Pathloss_Exponent_Home.place(x=340, y=120)
    Pathloss_Exponent_Home_Entry = Entry(Frame6, width=15, bd=3, font=('Arial 10'))
    Pathloss_Exponent_Home_Entry.pack(pady=10, padx=10)
    Pathloss_Exponent_Home_Entry.place(x=520, y=118)
    Pathloss_Exponent_Home_Entry.configure(state='normal')
    Pathloss_Exponent_Home_Entry.insert('end', '3')
    Pathloss_Exponent_Home_Entry.configure(state='disabled')
    #
    # #Distance
    global Distance_Home_Entry
    Distance_Home = Label(Frame6, text='Distance (m)')
    Distance_Home.pack(pady=10)
    Distance_Home.place(x=340, y=180)
    Distance_Home_Entry = Entry(Frame6, width=15, bd=3, font=('Arial 10'))
    Distance_Home_Entry.pack(pady=10, padx=10)
    Distance_Home_Entry.place(x=520, y=178)
    #
    # #Received_Power
    global Received_Power_Home_Entry
    Received_Power_Home = Label(Frame6, text='Received Power (dBm)')
    Received_Power_Home.pack(pady=10)
    Received_Power_Home.place(x=340, y=240)
    Received_Power_Home_Entry = Entry(Frame6, width=15, bd=3, font=('Arial 10'))
    Received_Power_Home_Entry.pack(pady=10, padx=10)
    Received_Power_Home_Entry.place(x=520, y=238)
    #
    # #BUTTONS
    Calc_Rx_Power_Home = ttk.Button(Frame6, text="Rxpower", command=Rxpower_Home)
    Calc_Rx_Power_Home.pack(ipadx=10, pady=10)
    Calc_Rx_Power_Home.place(x=280, y=298)
    #
    Calc_Distance_Home = ttk.Button(Frame6, text="Distance", command=Dist_Home)
    Calc_Distance_Home.pack(ipadx=10, pady=10)
    Calc_Distance_Home.place(x=280, y=338)
    # ******************************************************Frame7 Two Ray *******************************************************************************************
    # #TITLE
    Receive_Power_Calc_Home = Label(Frame7, text='TWO RAY', font="Arial 12 bold")
    Receive_Power_Calc_Home.pack(pady=10)
    Receive_Power_Calc_Home.place(x=250, y=20)
    # #Transmitter Power
    global Transmitter_Power_mW_Ray_Entry
    Transmitter_Power_Ray_mW = Label(Frame7, text='Transmitter Power (mW)')
    Transmitter_Power_Ray_mW.pack(pady=10)
    Transmitter_Power_Ray_mW.place(x=30, y=60)
    Transmitter_Power_mW_Ray_Entry = Entry(Frame7, width=15, bd=3, font=('Arial 10'))
    Transmitter_Power_mW_Ray_Entry.pack(pady=10, padx=10)
    Transmitter_Power_mW_Ray_Entry.place(x=220, y=58)
    #
    # #Gain at Transmitter
    global Tx_Antenna_Gain_Ray_Entry
    Tx_Antenna_Gain_Ray = Label(Frame7, text='AntennaGain at Transmitter (dBm)')
    Tx_Antenna_Gain_Ray.pack(pady=10)
    Tx_Antenna_Gain_Ray.place(x=30, y=120)
    Tx_Antenna_Gain_Ray_Entry = Entry(Frame7, width=15, bd=3, font=('Arial 10'))
    Tx_Antenna_Gain_Ray_Entry.pack(pady=10, padx=10)
    Tx_Antenna_Gain_Ray_Entry.place(x=220, y=118)
    #
    # #Gain at Receiver
    global Rx_Antenna_Gain_Ray_Entry
    Rx_Antenna_Gain_Ray = Label(Frame7, text='AntennaGain at Receiver (dBm)')
    Rx_Antenna_Gain_Ray.pack(pady=10)
    Rx_Antenna_Gain_Ray.place(x=30, y=180)
    Rx_Antenna_Gain_Ray_Entry = Entry(Frame7, width=15, bd=3, font=('Arial 10'))
    Rx_Antenna_Gain_Ray_Entry.pack(pady=10, padx=10)
    Rx_Antenna_Gain_Ray_Entry.place(x=220, y=178)
    #
    # Antenna Height Tx
    global Tx_Antenna_Height_Ray_Entry
    Tx_Antenna_Height_Ray = Label(Frame7, text='Tx_Antenna_Height (m)')
    Tx_Antenna_Height_Ray.pack(pady=10)
    Tx_Antenna_Height_Ray.place(x=30, y=240)
    Tx_Antenna_Height_Ray_Entry = Entry(Frame7, width=15, bd=3, font=('Arial 10'))
    Tx_Antenna_Height_Ray_Entry.pack(pady=10, padx=10)
    Tx_Antenna_Height_Ray_Entry.place(x=220, y=238)
    # #Rx_Antenna_Height
    global Rx_Antenna_Height_Ray_Entry
    Rx_Antenna_Height_Ray = Label(Frame7, text='Rx_Antenna_Height (m)')
    Rx_Antenna_Height_Ray.pack(pady=10)
    Rx_Antenna_Height_Ray.place(x=340, y=60)
    Rx_Antenna_Height_Ray_Entry = Entry(Frame7, width=15, bd=3, font=('Arial 10'))
    Rx_Antenna_Height_Ray_Entry.pack(pady=10, padx=10)
    Rx_Antenna_Height_Ray_Entry.place(x=520, y=58)
    # #Distance
    global Distance_Ray_Entry
    Distance_Ray = Label(Frame7, text='Distance (m)')
    Distance_Ray.pack(pady=10)
    Distance_Ray.place(x=340, y=120)
    Distance_Ray_Entry = Entry(Frame7, width=15, bd=3, font=('Arial 10'))
    Distance_Ray_Entry.pack(pady=10, padx=10)
    Distance_Ray_Entry.place(x=520, y=118)
    #
    # #Received_Power
    global Received_Power_Ray_Entry
    Received_Power_Ray = Label(Frame7, text='Received Power (dBm)')
    Received_Power_Ray.pack(pady=10)
    Received_Power_Ray.place(x=340, y=180)
    Received_Power_Ray_Entry = Entry(Frame7, width=15, bd=3, font=('Arial 10'))
    Received_Power_Ray_Entry.pack(pady=10, padx=10)
    Received_Power_Ray_Entry.place(x=520, y=178)
    #
    # #BUTTONS
    Calc_Rx_Power_Ray = ttk.Button(Frame7, text="Rxpower", command=Rxpower_Ray)
    Calc_Rx_Power_Ray.pack(ipadx=10, pady=10)
    Calc_Rx_Power_Ray.place(x=280, y=298)
    #
    Calc_Distance_Ray = ttk.Button(Frame7, text="Distance", command=Dist_Ray)
    Calc_Distance_Ray.pack(ipadx=10, pady=10)
    Calc_Distance_Ray.place(x=280, y=338)
    window.mainloop()

def selection_changed(event):
    selection = combo.get()
    global flag_Rxpower
    global flag_Genrate
    global count_grate
    global count_rxpower
    if selection == "Generation_Rate":
        count_rxpower = 0
        count_grate+=1
        if count_grate==1:
            flag_Genrate = 1
            if flag_Rxpower == 1:
                my_notebook2.destroy()
            frame_created_GR()

    if selection == "Received_Power":
        count_grate = 0
        count_rxpower+=1
        if count_rxpower==1:
            flag_Rxpower = 1
            if flag_Genrate == 1:
                my_notebook.destroy()
            frame_created_RP()

#************************************************ Frame 1 Generation Rate *********************************
def GEN():
    result_Entry.delete(0, 'end')
    ps = float(var_entry.get())
    iat = float(var2_entry.get())
    result = (ps * 8) / iat
    result_Entry.insert(END, str(result))

def IAT():
    var2_entry.delete(0, 'end')
    ps = float(var_entry.get())
    gen = float(result_Entry.get())
    result = (ps * 8) / gen
    var2_entry.insert(END, str(result))
# ****************************************** Frame 2 HTTP **********************************************************
def Gen_HTTP():
    HTTP_Gen_Entry.delete(0, 'end')
    page_S = float(Page_size_Entry.get())
    page_C = float(Page_count_Entry.get())
    inter_AT = float(IAT_Value_Entry.get())
    result = (page_S * 8 * page_C) / inter_AT
    HTTP_Gen_Entry.insert(END, str(result))
def IAT_HTTP():
    IAT_Value_Entry.delete(0,'end')
    psize_IAT = float(Page_size_Entry.get())
    pcount_IAT = float(Page_count_Entry.get())
    genrate_IAT = float(HTTP_Gen_Entry.get())
    result = (psize_IAT * 8 * pcount_IAT) / genrate_IAT
    IAT_Value_Entry.insert(END,str(result))

# ************************************ Frame 3 VIDEO ***************************************************************
def VIDEO_Gen():
    video_Gen_Entry.delete(0, 'end')
    FPS = int(fps_Entry.get())
    PPF = int(ppf_Entry.get())
    BPP = float(bpp_Entry.get())
    result = (FPS * PPF * BPP)
    result /= 1000000
    video_Gen_Entry.insert(END, str(result))

#********************************************************** Received Power ********************************************
def Rxpower():
    Received_Power_Entry.delete(0, 'end')
    tp = float(Transmitter_Power_mW_Entry.get())
    agP = int(Tx_Antenna_Gain_Entry.get())
    agR = int(Rx_Antenna_Gain_Entry.get())
    freq = float(Frequency_Entry.get())
    d = float(d0_Entry.get())
    pe = float(Pathloss_Exponent_Entry.get())
    distR = float(Distance_Entry.get())
    Tp_in_dB = 10 * math.log10(tp)
    Lambda = (3 * (10 ** 8)) / (freq * (10 ** 9))
    temp = Lambda / (4 * math.pi * d)
    PL = 20 * math.log10(temp)
    logdist = d / distR
    Pathloss_Eta = 10 * pe * math.log10(logdist)
    Receive_power_Result = round((Tp_in_dB + agP + agR + PL + Pathloss_Eta), 4)
    Received_Power_Entry.insert(END, str(Receive_power_Result))
def Dist():
    Distance_Entry.delete(0, 'end')
    tp = float(Transmitter_Power_mW_Entry.get())
    rp = float(Received_Power_Entry.get())
    agP = int(Tx_Antenna_Gain_Entry.get())
    agR = int(Rx_Antenna_Gain_Entry.get())
    freq = float(Frequency_Entry.get())
    d = float(d0_Entry.get())
    pe = float(Pathloss_Exponent_Entry.get())
    Tp_in_dB = 10 * math.log10(tp)
    Lambda = (3 * (10 ** 8)) / (freq * (10 ** 9))
    temp = Lambda / (4 * math.pi * d)
    PL = 20 * math.log10(temp)
    variable_1=(rp-Tp_in_dB-agP-agR-PL)/(10*pe)
    variable_2=10**variable_1
    distance_req=round((d/variable_2),2)
    Distance_Entry.insert(END, str(distance_req))
#***************************************** FRAME2 Definition ********************************************************
def Rxpower_Hata():
    Received_Power_Hata_Entry.delete(0,'end')
    tp_Hata = float(Transmitter_Power_mW_Hata_Entry.get())
    aH_Tx_Hata = float(Tx_Antenna_Height_Hata_Entry.get())
    aH_Rx_Hata = float(Rx_Antenna_Height_Hata_Entry.get())
    freq_Hata = float(Frequency_Hata_Entry.get())
    distance_Hata = float(Distance_Hata_Entry.get())
    temp = 3.2 * ((math.log10(11.74 * aH_Rx_Hata))**2) - 4.97
    print(temp)
    TPower_Hata_dB = 10 * math.log10(tp_Hata)
    log_Txheight = math.log10(aH_Tx_Hata)
    log_dist = math.log10(distance_Hata)
    log_freq = math.log10(freq_Hata)
    LdB = 69.55 + (26.16 * log_freq) - (13.82 * log_Txheight) - temp + (44.9 - 6.55 * log_Txheight) * log_dist
    result_Hata = TPower_Hata_dB - LdB
    Received_Power_Hata_Entry.insert(END, str(result_Hata))

def Dist_Hata():
    Distance_Hata_Entry.delete(0, 'end')
    tp_Hata_dist = float(Transmitter_Power_mW_Hata_Entry.get())
    aH_Tx_Hata_dist = float(Tx_Antenna_Height_Hata_Entry.get())
    aH_Rx_Hata_dist = float(Rx_Antenna_Height_Hata_Entry.get())
    freq_Hata_dist = float(Frequency_Hata_Entry.get())
    receive_power_Hata = float(Received_Power_Hata_Entry.get())
    temp1 = 3.2 * ((math.log10(11.74 * aH_Rx_Hata_dist))**2) - 4.97
    Tpower_Hata = 10 * math.log10(tp_Hata_dist)
    log_Freq = math.log10(freq_Hata_dist)
    log_tx_height = math.log10(aH_Tx_Hata_dist)
    result = Tpower_Hata - (receive_power_Hata) - 69.55 - (26.16 * log_Freq) + (13.82 * log_tx_height) + temp1
    Result2 = result/(44.9-6.55*log_tx_height)
    Distance1 = 10 ** Result2
    Distance_Hata_Entry.insert(END, str(Distance1))

# #***************************************** FRAME3 Definition ********************************************************
def Rxpower_Sub():
    Received_Power_Sub_Entry.delete(0, 'end')
    tp_Sub = float(Transmitter_Power_mW_Sub_Entry.get())
    aH_Tx_Sub = float(Tx_Antenna_Height_Sub_Entry.get())
    aH_Rx_Sub = float(Rx_Antenna_Height_Sub_Entry.get())
    freq_Sub = float(Frequency_Sub_Entry.get())
    distance_Sub = float(Distance_Sub_Entry.get())
    if freq_Sub < (300 * 10 ** (-3)):
        temp = 8.9 * ((math.log10(1.54 * aH_Rx_Sub)) ** 2) - 1.1
    else:
        temp = 3.2 * ((math.log10(11.74 * aH_Rx_Sub)) ** 2) - 4.97
    TPower_Sub_dB = 10 * math.log10(tp_Sub)
    log_Txheight = math.log10(aH_Tx_Sub)
    log_dist = math.log10(distance_Sub)
    log_freq = math.log10(freq_Sub)
    LdB_Urban = 69.55 + (26.16 * log_freq) - (13.82 * log_Txheight) - temp + (44.9 - 6.55 * log_Txheight) * log_dist
    LdB = LdB_Urban - 2 * ((log_freq / 28) ** 2) - 5.4
    result_Sub = TPower_Sub_dB - LdB
    Received_Power_Sub_Entry.insert(END, str(result_Sub))
def Dist_Sub():
    Distance_Sub_Entry.delete(0, 'end')
    tp_Sub_dist = float(Transmitter_Power_mW_Sub_Entry.get())
    aH_Tx_Sub_dist = float(Tx_Antenna_Height_Sub_Entry.get())
    aH_Rx_Sub_dist = float(Rx_Antenna_Height_Sub_Entry.get())
    freq_Sub_dist = float(Frequency_Sub_Entry.get())
    Receive_Sub_dist = float(Received_Power_Sub_Entry.get())
    if freq_Sub_dist < (300 * 10 ** (-3)):
        temp = 8.9 * ((math.log10(1.54 * aH_Rx_Sub_dist)) ** 2) - 1.1
    else:
        temp = 3.2 * ((math.log10(11.74 * aH_Rx_Sub_dist)) ** 2) - 4.97
    TPower_Sub_dist_dB = 10 * math.log10(tp_Sub_dist)
    log_Txheight_dist = math.log10(aH_Tx_Sub_dist)
    log_freq_dist = math.log10(freq_Sub_dist)
    Log_Factor_Sub = 2 * ((log_freq_dist / 28) ** 2)
    result = TPower_Sub_dist_dB - (Receive_Sub_dist) - 69.55 - (26.16 * log_freq_dist) + (13.82 * log_Txheight_dist) + temp + Log_Factor_Sub + 5.4
    Result2 = result / (44.9 - 6.55 * log_Txheight_dist)
    Distance1 = 10 ** Result2
    Distance_Sub_Entry.insert(END, str(Distance1))


#***************************************** FRAME4 Definition ********************************************************
def Rxpower_Cost():
    Received_Power_Cost_Entry.delete(0, 'end')
    tp_Cost = float(Transmitter_Power_mW_Cost_Entry.get())
    aH_Tx_Cost = float(Tx_Antenna_Height_Cost_Entry.get())
    aH_Rx_Cost= float(Rx_Antenna_Height_Cost_Entry.get())
    freq_Cost = float(Frequency_Cost_Entry.get())
    distance_Cost = float(Distance_Cost_Entry.get())
    CM_Cost = int(Value.get())
    print(CM_Cost)
    if freq_Cost < (300 * 10 ** (-3)):
        temp = 8.9 * ((math.log10(1.54 * aH_Rx_Cost)) ** 2) - 1.1
    else:
        temp = 3.2 * ((math.log10(11.74 * aH_Rx_Cost)) ** 2) - 4.97
    TPower_Cost_dB = 10 * math.log10(tp_Cost)
    log_Txheight_Cost = math.log10(aH_Tx_Cost)
    log_dist_Cost = math.log10(distance_Cost)
    log_freq_Cost = math.log10(freq_Cost)
    LdB = 46.3 + (33.9 * log_freq_Cost) - (13.82 * log_Txheight_Cost) - temp + CM_Cost+ (44.9 - 6.55 * log_Txheight_Cost) * log_dist_Cost
    result_Cost = round((TPower_Cost_dB - LdB),3)
    Received_Power_Cost_Entry.insert(END, str(result_Cost))

def Dist_Cost():
    Distance_Cost_Entry.delete(0, 'end')
    tp_Cost_dist = float(Transmitter_Power_mW_Cost_Entry.get())
    aH_Tx_Cost_dist = float(Tx_Antenna_Height_Cost_Entry.get())
    aH_Rx_Cost_dist = float(Rx_Antenna_Height_Cost_Entry.get())
    freq_Cost_dist = float(Frequency_Cost_Entry.get())
    Receive_Cost_dist = float(Received_Power_Cost_Entry.get())
    CM_Cost_dist = int(Value.get())
    print(CM_Cost_dist)
    if freq_Cost_dist < (300 * 10 ** (-3)):
        temp = 8.9 * ((math.log10(1.54 * aH_Rx_Cost_dist)) ** 2) - 1.1
    else:
        temp = 3.2 * ((math.log10(11.74 * aH_Rx_Cost_dist)) ** 2) - 4.97
    TPower_Cost_dist_dB = 10 * math.log10(tp_Cost_dist)
    log_Txheight_dist = math.log10(aH_Tx_Cost_dist)
    log_freq_dist = math.log10(freq_Cost_dist)
    Log_Factor_Cost = 2 * ((log_freq_dist / 28) ** 2)
    result = TPower_Cost_dist_dB - (Receive_Cost_dist) - 46.3 - (33.9 * log_freq_dist) + (
                13.82 * log_Txheight_dist) + temp + Log_Factor_Cost - CM_Cost_dist
    Result2 = result / (44.9 - 6.55 * log_Txheight_dist)
    Distance1 = round((10 ** Result2),2)
    Distance_Cost_Entry.insert(END, str(Distance1))
# ***************************************** FRAME5 Definition ********************************************************
def Rxpower_Indoor():
    Received_Power_Indoor_Entry.delete(0, 'end')
    tp = float(Transmitter_Power_Indoor_mW_Entry.get())
    agP = int(Tx_Antenna_Gain_Indoor_Entry.get())
    agR = int(Rx_Antenna_Gain_Indoor_Entry.get())
    freq = float(Frequency_Indoor_Entry.get())
    d = float(d0_Indoor_Entry.get())
    pe = float(Pathloss_Exponent_Indoor_Entry.get())
    distR = float(Distance_Indoor_Entry.get())
    Tp_in_dB = 10 * math.log10(tp)
    Lambda = (3 * (10 ** 8)) / (freq * (10 ** 9))
    temp = Lambda / (4 * math.pi * d)
    PL = 20 * math.log10(temp)
    logdist = d / distR
    Pathloss_Eta = 10 * pe * math.log10(logdist)
    Receive_power_Result = round((Tp_in_dB + agP + agR + PL + Pathloss_Eta), 4)
    Received_Power_Indoor_Entry.insert(END, str(Receive_power_Result))

def Dist_Indoor():
    Distance_Indoor_Entry.delete(0, 'end')
    tp = float(Transmitter_Power_Indoor_mW_Entry.get())
    rp = float(Received_Power_Indoor_Entry.get())
    agP = int(Tx_Antenna_Gain_Indoor_Entry.get())
    agR = int(Rx_Antenna_Gain_Indoor_Entry.get())
    freq = float(Frequency_Indoor_Entry.get())
    d = float(d0_Indoor_Entry.get())
    pe = float(Pathloss_Exponent_Indoor_Entry.get())
    Tp_in_dB = 10 * math.log10(tp)
    Lambda = (3 * (10 ** 8)) / (freq * (10 ** 9))
    temp = Lambda / (4 * math.pi * d)
    PL = 20 * math.log10(temp)
    variable_1 = (rp - Tp_in_dB - agP - agR - PL) / (10 * pe)
    variable_2 = 10 ** variable_1
    distance_req = round((d / variable_2), 2)

    Distance_Indoor_Entry.insert(END, str(distance_req))

# ***************************************** FRAME6 Definition ********************************************************
def Rxpower_Home():
    Received_Power_Home_Entry.delete(0, 'end')
    tp = float(Transmitter_Power_mW_Home_Entry.get())
    agP = int(Tx_Antenna_Gain_Home_Entry.get())
    agR = int(Rx_Antenna_Gain_Home_Entry.get())
    freq = float(Frequency_Home_Entry.get())
    d = float(d0_Home_Entry.get())
    pe = float(Pathloss_Exponent_Home_Entry.get())
    distR = float(Distance_Home_Entry.get())
    Tp_in_dB = 10 * math.log10(tp)
    Lambda = (3 * (10 ** 8)) / (freq * (10 ** 9))
    temp = Lambda / (4 * math.pi * d)
    PL = 20 * math.log10(temp)
    logdist = d / distR
    Pathloss_Eta = 10 * pe * math.log10(logdist)
    Receive_power_Result = round((Tp_in_dB + agP + agR + PL + Pathloss_Eta), 4)
    Received_Power_Home_Entry.insert(END, str(Receive_power_Result))

def Dist_Home():
    Distance_Home_Entry.delete(0, 'end')
    tp = float(Transmitter_Power_mW_Home_Entry.get())
    rp = float(Received_Power_Home_Entry.get())
    agP = int(Tx_Antenna_Gain_Home_Entry.get())
    agR = int(Rx_Antenna_Gain_Home_Entry.get())
    freq = float(Frequency_Home_Entry.get())
    d = float(d0_Home_Entry.get())
    pe = float(Pathloss_Exponent_Home_Entry.get())
    Tp_in_dB = 10 * math.log10(tp)
    Lambda = (3 * (10 ** 8)) / (freq * (10 ** 9))
    temp = Lambda / (4 * math.pi * d)
    PL = 20 * math.log10(temp)

    variable_1 = (rp - Tp_in_dB - agP - agR - PL) / (10 * pe)
    variable_2 = 10 ** variable_1
    distance_req = round((d / variable_2), 2)

    Distance_Home_Entry.insert(END, str(distance_req))

# ###################################### Frame 7 Definition ##############################################
def Rxpower_Ray():
    Received_Power_Ray_Entry.delete(0, 'end')
    TxPower_Ray = float(Transmitter_Power_mW_Ray_Entry.get())
    Txantenna_Gain_Ray = float(Tx_Antenna_Gain_Ray_Entry.get())
    Rxantenna_Gain_Ray = float(Rx_Antenna_Gain_Ray_Entry.get())
    Rx_Height_Ray = float(Rx_Antenna_Height_Ray_Entry.get())
    Tx_Height_Ray = float(Tx_Antenna_Height_Ray_Entry.get())
    distance_Ray = float(Distance_Ray_Entry.get())
    Tx_in_dB_Ray = 10 * math.log10(TxPower_Ray)
    Gain_Product = Txantenna_Gain_Ray * Rxantenna_Gain_Ray
    Log_Gain_Product = 10 * math.log10(Gain_Product * (Rx_Height_Ray**2) * (Tx_Height_Ray**2))
    Log_Distance = 40 * math.log10(distance_Ray)
    Received_Power_Ray = Tx_in_dB_Ray + Rxantenna_Gain_Ray + Txantenna_Gain_Ray - Log_Distance + Log_Gain_Product
    Received_Power_Ray_Entry.insert(END, str(Received_Power_Ray))

def Dist_Ray():
    Distance_Ray_Entry.delete(0, 'end')
    TxPower_Ray_dist = float(Transmitter_Power_mW_Ray_Entry.get())
    Txantenna_Gain_Ray_dist = float(Tx_Antenna_Gain_Ray_Entry.get())
    Rxantenna_Gain_Ray_dist = float(Rx_Antenna_Gain_Ray_Entry.get())
    Rx_Height_Ray_dist = float(Rx_Antenna_Height_Ray_Entry.get())
    Tx_Height_Ray_dist = float(Tx_Antenna_Height_Ray_Entry.get())
    Rx_Power_Ray_dist = float(Received_Power_Ray_Entry.get())
    Tx_in_dB_Ray_dist = 10 * math.log10(TxPower_Ray_dist)
    Gain_Product_dist = Txantenna_Gain_Ray_dist * Rxantenna_Gain_Ray_dist
    Log_Gain_Product_dist = 10 * math.log10(Gain_Product_dist * (Rx_Height_Ray_dist**2) * (Tx_Height_Ray_dist**2))
    Result_dist = (Tx_in_dB_Ray_dist - Rx_Power_Ray_dist + Rxantenna_Gain_Ray_dist + Tx_Height_Ray_dist + Log_Gain_Product_dist)/40
    print(Result_dist)
    Distance_Ray_dist = round((10 ** Result_dist),4)
    Distance_Ray_Entry.insert(END, str(Distance_Ray_dist))
window = Tk()
window.geometry("1100x600")
window.title("Calculus - Rx & GR")
# Style of the UI
style = ttk.Style()
style.theme_use("clam")
# #TITLE
Receive_Power_Indoor_Calc = Label(window, text='Calculator - Rx & Gen.Rate', font="Arial 12 bold")
Receive_Power_Indoor_Calc.pack(padx=5,pady=5)
Receive_Power_Indoor_Calc.place(x=500,y=0)
Named_value = Label(window, text='select the calculator')
Named_value.pack(padx=5,pady=5)
Named_value.place(x=5, y=20)
combo = ttk.Combobox(values=["Generation_Rate","Received_Power"])
combo.bind("<<ComboboxSelected>>", selection_changed)
combo.place(x=5, y=40)
window.mainloop()