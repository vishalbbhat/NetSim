import math
import tkinter as tk
from tkinter import *
from tkinter import ttk

#********************************************Definitions*****************************************************
#*************************************** FRAME1 Definitions **************************************************
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
# def Rxpower_Hata():
#     Received_Power_Hata_Entry.delete(0,'end')
#     tp_Hata = float(Transmitter_Power_mW_Hata_Entry.get())
#     aH_Tx_Hata = float(Tx_Antenna_Height_Hata_Entry.get())
#     aH_Rx_Hata = float(Rx_Antenna_Height_Hata_Entry.get())
#     freq_Hata = float(Frequency_Hata_Entry.get())
#     distance_Hata = float(Distance_Hata_Entry.get())
#     if freq_Hata < (300 * (10**(-3))):
#         temp = 8.29 * ((math.log10(1.54 * aH_Rx_Hata))**2) - 1.1
#     else:
#         temp = 3.2 * ((math.log10(11.74 * aH_Rx_Hata))**2) - 4.97
#     TPower_Hata_dB = 10 * math.log10(tp_Hata)
#     l50 = 69.55 + (26.26 * math.log10(freq_Hata)) - (13.82 * math.log10(aH_Tx_Hata)) - temp + (44.9 - 6.55 * math.log10(aH_Tx_Hata)) * math.log10(distance_Hata)
#     result_Hata =(TPower_Hata_dB - l50)
#     Received_Power_Hata_Entry.insert(END, str(result_Hata))
#
# def Dist_Hata():
#     Distance_Hata_Entry.delete(0, 'end')
#     tp_Hata_dist = float(Transmitter_Power_mW_Hata_Entry.get())
#     aH_Tx_Hata_dist = float(Tx_Antenna_Height_Hata_Entry.get())
#     aH_Rx_Hata_dist = float(Rx_Antenna_Height_Hata_Entry.get())
#     freq_Hata_dist = float(Frequency_Hata_Entry.get())
#     receive_power_Hata = float(Received_Power_Hata_Entry.get())
#
#     if freq_Hata_dist < (300 * (10**(-3))):
#         temp = 8.29 * ((math.log10(1.54 * aH_Rx_Hata_dist))**2) - 1.1
#     else:
#         temp = 3.2 * ((math.log10(11.74 * aH_Rx_Hata_dist))**2) - 4.97
#     # var_x = 26.16 * math.log10(freq_Hata_dist)
#     # var_y = 13.82 * math.log10(aH_Tx_Hata_dist)
#     # var_z = -44.9 + 6.55 * math.log10(aH_Tx_Hata_dist)
#     # result = receive_power_Hata - tp_Hata_dist + 69.55 + var_x - var_y - temp
#     # result2 = result / var_z
#     # Distance = 10 ** result2
#     Tpower_Hata = 10 * math.log10(tp_Hata_dist)
#     result = Tpower_Hata - receive_power_Hata - 69.55 - (26.16 * math.log10(freq_Hata_dist)) + (13.82 * math.log10(aH_Tx_Hata_dist)) + temp
#     Result2 = result / (44.9 - 6.55 * math.log10(aH_Tx_Hata_dist))
#     print(Result2)
#     Distance1 = 10 ** Result2
#     Distance_Hata_Entry.insert(END, str(Distance1))
# #***************************************** FRAME3 Definition ********************************************************
# def Rxpower_Sub():
#     exit
# def Dist_Sub():
#     exit
#
# #***************************************** FRAME4 Definition ********************************************************
# def Rxpower_Cost():
#     Received_Power_Cost_Entry.delete(0, 'end')
#     tp_Cost = float(Transmitter_Power_mW_Cost_Entry.get())
#     aH_Tx_Cost = float(Tx_Antenna_Height_Cost_Entry.get())
#     aH_Rx_Cost = float(Rx_Antenna_Height_Cost_Entry.get())
#     freq_Cost = float(Frequency_Cost_Entry.get())
#     distance_Cost = float(Distance_Cost_Entry.get())
#     Tpower_Cost_dB = 10 * math.log10(tp_Cost)
#     CM_Cost = int(Value.get())
#     l50 = 46.3 + (33.9 * math.log10(freq_Cost)) - (13.82 * math.log10(aH_Tx_Cost)) + (44.9 - (6.55*math.log10(aH_Tx_Cost))) * math.log10(distance_Cost) + CM_Cost
#     RPower_Cost = Tpower_Cost_dB - l50
#     Received_Power_Cost_Entry.insert(END, str(RPower_Cost))
#
#
# def Dist_Cost():
#     exit

#***************************************** FRAME5 Definition ********************************************************
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
    # distR = float(Distance_Entry.get())
    Tp_in_dB = 10 * math.log10(tp)
    Lambda = (3 * (10 ** 8)) / (freq * (10 ** 9))
    temp = Lambda / (4 * math.pi * d)
    PL = 20 * math.log10(temp)
    # logdist = d / distR
    # Pathloss_Eta = 10 * pe * math.log10(logdist)
    variable_1 = (rp - Tp_in_dB - agP - agR - PL) / (10 * pe)
    variable_2 = 10 ** variable_1
    distance_req = round((d / variable_2), 2)

    # Receive_power_Result = round((Tp_in_dB + agP + agR + PL + Pathloss_Eta), 4)
    Distance_Indoor_Entry.insert(END, str(distance_req))
#***************************************** FRAME6 Definition ********************************************************
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
    # distR = float(Distance_Entry.get())
    Tp_in_dB = 10 * math.log10(tp)
    Lambda = (3 * (10 ** 8)) / (freq * (10 ** 9))
    temp = Lambda / (4 * math.pi * d)
    PL = 20 * math.log10(temp)
    # logdist = d / distR
    # Pathloss_Eta = 10 * pe * math.log10(logdist)
    variable_1 = (rp - Tp_in_dB - agP - agR - PL) / (10 * pe)
    variable_2 = 10 ** variable_1
    distance_req = round((d / variable_2), 2)

    # Receive_power_Result = round((Tp_in_dB + agP + agR + PL + Pathloss_Eta), 4)
    Distance_Home_Entry.insert(END, str(distance_req))
# GUI Setting
window = Tk()
# window.title("Receive Power Calculator")
# set window width and height
window.geometry("1000x500")
#***********************************FRAMES****************************************
my_notebook = ttk.Notebook(window)
my_notebook.pack(padx=20, pady=20)
#Frame1
Frame1 = Frame(my_notebook, width = 700, height = 500)
Frame1.pack(fill="both",expand=1)
my_notebook.add(Frame1, text = "Log Distance")
# #Frame2
# Frame2 = Frame(my_notebook, width = 700, height = 500)
# Frame2.pack(fill="both",expand=1)
# my_notebook.add(Frame2, text = "Hata Urban")
# #Frame3
# Frame3 = Frame(my_notebook, width = 700, height = 500)
# Frame3.pack(fill="both",expand=1)
# my_notebook.add(Frame3, text = "Hata Suburban")
# #Frame4
# Frame4 = Frame(my_notebook, width = 700, height = 500)
# Frame4.pack(fill="both",expand=1)
# my_notebook.add(Frame4, text = "Cost Hata urban & suburban")
#Frame5
Frame5 = Frame(my_notebook, width = 700, height = 500)
Frame5.pack(fill="both",expand=1)
my_notebook.add(Frame5, text = "Indoor Office & Factory")
#Frame6
Frame6 = Frame(my_notebook, width = 700, height = 500)
Frame6.pack(fill="both",expand=1)
my_notebook.add(Frame6, text = "Indoor Home")

#******************************************************Frame1 LOG DISTANCE*******************************************************************************************
# #TITLE
Receive_Power_Calc = Label(Frame1, text='Receive Power Calculator', font="Arial 12 bold")
Receive_Power_Calc.pack(pady=10)
Receive_Power_Calc.place(x=250,y=20)
# #Transmitter Power
Transmitter_Power_mW = Label(Frame1, text='Transmitter Power (mW)')
Transmitter_Power_mW.pack(pady=10)
Transmitter_Power_mW.place(x=30, y=60)
Transmitter_Power_mW_Entry = Entry(Frame1,width=15,bd=3,font=('Arial 10'))
Transmitter_Power_mW_Entry.pack(pady=10,padx=10)
Transmitter_Power_mW_Entry.place(x = 200, y = 58)
#
# #Gain at Transmitter
Tx_Antenna_Gain = Label(Frame1, text='Antenna Gain at Transmitter')
Tx_Antenna_Gain.pack(pady=10)
Tx_Antenna_Gain.place(x=30, y=120)
Tx_Antenna_Gain_Entry = Entry(Frame1,width=15,bd=3,font=('Arial 10'))
Tx_Antenna_Gain_Entry.pack(pady=10,padx=10)
Tx_Antenna_Gain_Entry.place(x = 200, y = 118)
#
# #Gain at Receiver
Rx_Antenna_Gain = Label(Frame1, text='Antenna Gain at Receiver')
Rx_Antenna_Gain.pack(pady=10)
Rx_Antenna_Gain.place(x=30, y=180)
Rx_Antenna_Gain_Entry = Entry(Frame1,width=15,bd=3,font=('Arial 10'))
Rx_Antenna_Gain_Entry.pack(pady=10,padx=10)
Rx_Antenna_Gain_Entry.place(x = 200, y = 178)
#
# #Frequency (GHz)
Frequency = Label(Frame1, text='Frequency (GHz)')
Frequency.pack(pady=10)
Frequency.place(x=30, y=240)
Frequency_Entry = Entry(Frame1,width=15,bd=3,font=('Arial 10'))
Frequency_Entry.pack(pady=10,padx=10)
Frequency_Entry.place(x = 200, y = 238)
#
# #d0
d0 = Label(Frame1, text='Reference Distance (d0)')
d0.pack(pady=10)
d0.place(x=330, y=60)
d0_Entry = Entry(Frame1,width=15,bd=3,font=('Arial 10'))
d0_Entry.pack(pady=10,padx=10)
d0_Entry.place(x = 500, y = 58)
#
# #Pathloss_Exponent
Pathloss_Exponent = Label(Frame1, text='Pathloss Exponent (\u03B7)')
Pathloss_Exponent.pack(pady=10)
Pathloss_Exponent.place(x=330, y=120)
Pathloss_Exponent_Entry = Entry(Frame1,width=15,bd=3,font=('Arial 10'))
Pathloss_Exponent_Entry.pack(pady=10,padx=10)
Pathloss_Exponent_Entry.place(x = 500, y = 118)
#
# #Distance
Distance = Label(Frame1, text='Distance (in metres) ')
Distance.pack(pady=10)
Distance.place(x=330, y=180)
Distance_Entry = Entry(Frame1,width=15,bd=3,font=('Arial 10'))
Distance_Entry.pack(pady=10,padx=10)
Distance_Entry.place(x = 500, y = 178)
#
# #Received_Power
Received_Power = Label(Frame1, text='Received Power (mW)')
Received_Power.pack(pady=10)
Received_Power.place(x=330, y=240)
Received_Power_Entry = Entry(Frame1,width=15,bd=3,font=('Arial 10'))
Received_Power_Entry.pack(pady=10,padx=10)
Received_Power_Entry.place(x = 500, y = 238)
#
# #BUTTONS
Calc_Rx_Power = ttk.Button(Frame1, text="Rxpower", command=Rxpower)
Calc_Rx_Power.pack(ipadx=10, pady=10)
Calc_Rx_Power.place(x=280, y=298)
#
Calc_Distance = ttk.Button(Frame1, text="Distance", command=Dist)
Calc_Distance.pack(ipadx=10, pady=10)
Calc_Distance.place(x=280, y=338)
#******************************************** Frame2 Hata Urban ***************************************************************************************************

# # #TITLE
# Receive_Power_Calc_Hata = Label(Frame2, text='Receive Power Calculator', font="Arial 12 bold")
# Receive_Power_Calc_Hata.pack(pady=10)
# Receive_Power_Calc_Hata.place(x=250,y=20)
# # #Transmitter Power
# Transmitter_Power_mW_Hata = Label(Frame2, text='Transmitter Power (mW)')
# Transmitter_Power_mW_Hata.pack(pady=10)
# Transmitter_Power_mW_Hata.place(x=30, y=60)
# Transmitter_Power_mW_Hata_Entry = Entry(Frame2,width=15,bd=3,font=('Arial 10'))
# Transmitter_Power_mW_Hata_Entry.pack(pady=10,padx=10)
# Transmitter_Power_mW_Hata_Entry.place(x = 200, y = 58)
# #
# # #Height at Transmitter
# Tx_Antenna_Height_Hata = Label(Frame2, text='Antenna Height at Transmitter')
# Tx_Antenna_Height_Hata.pack(pady=10)
# Tx_Antenna_Height_Hata.place(x=30, y=120)
# Tx_Antenna_Height_Hata_Entry = Entry(Frame2,width=15,bd=3,font=('Arial 10'))
# Tx_Antenna_Height_Hata_Entry.pack(pady=10,padx=10)
# Tx_Antenna_Height_Hata_Entry.place(x = 200, y = 118)
# #
# # #Distance
# Distance_Hata = Label(Frame2, text='Distance (in metres) ')
# Distance_Hata.pack(pady=10)
# Distance_Hata.place(x=30, y=180)
# Distance_Hata_Entry = Entry(Frame2,width=15,bd=3,font=('Arial 10'))
# Distance_Hata_Entry.pack(pady=10,padx=10)
# Distance_Hata_Entry.place(x = 200, y = 178)
#
# # #Height at Receiver
# Rx_Antenna_Height_Hata = Label(Frame2, text='Antenna Height at Receiver')
# Rx_Antenna_Height_Hata.pack(pady=10)
# Rx_Antenna_Height_Hata.place(x=330, y=60)
# Rx_Antenna_Height_Hata_Entry = Entry(Frame2,width=15,bd=3,font=('Arial 10'))
# Rx_Antenna_Height_Hata_Entry.pack(pady=10,padx=10)
# Rx_Antenna_Height_Hata_Entry.place(x = 500, y = 58)
# #
# # #Frequency (GHz)
# Frequency_Hata = Label(Frame2, text='Frequency (GHz)')
# Frequency_Hata.pack(pady=10)
# Frequency_Hata.place(x=330, y=120)
# Frequency_Hata_Entry = Entry(Frame2,width=15,bd=3,font=('Arial 10'))
# Frequency_Hata_Entry.pack(pady=10,padx=10)
# Frequency_Hata_Entry.place(x = 500, y = 118)
#
# # #Received_Power
# Received_Power_Hata = Label(Frame2, text='Received Power (mW)')
# Received_Power_Hata.pack(pady=10)
# Received_Power_Hata.place(x=330, y=180)
# Received_Power_Hata_Entry = Entry(Frame2,width=15,bd=3,font=('Arial 10'))
# Received_Power_Hata_Entry.pack(pady=10,padx=10)
# Received_Power_Hata_Entry.place(x = 500, y = 178)
# #
# # #BUTTONS
# Calc_Rx_Power_Hata = ttk.Button(Frame2, text="Rxpower", command=Rxpower_Hata)
# Calc_Rx_Power_Hata.pack(ipadx=10, pady=10)
# Calc_Rx_Power_Hata.place(x=280, y=298)
# #
# Calc_Distance_Hata = ttk.Button(Frame2, text="Distance", command=Dist_Hata)
# Calc_Distance_Hata.pack(ipadx=10, pady=10)
# Calc_Distance_Hata.place(x=280, y=338)
#
# #******************************************** Frame3 Hata Suburban ***************************************************************************************************
#
#
# # #TITLE
# Receive_Power_Calc_Sub = Label(Frame3, text='Receive Power Calculator', font="Arial 12 bold")
# Receive_Power_Calc_Sub.pack(pady=10)
# Receive_Power_Calc_Sub.place(x=250,y=20)
# # #Transmitter Power
# Transmitter_Power_mW_Sub = Label(Frame3, text='Transmitter Power (mW)')
# Transmitter_Power_mW_Sub.pack(pady=10)
# Transmitter_Power_mW_Sub.place(x=30, y=60)
# Transmitter_Power_mW_Sub_Entry = Entry(Frame3,width=15,bd=3,font=('Arial 10'))
# Transmitter_Power_mW_Sub_Entry.pack(pady=10,padx=10)
# Transmitter_Power_mW_Sub_Entry.place(x = 200, y = 58)
# #
# # #Height at Transmitter
# Tx_Antenna_Height_Sub = Label(Frame3, text='Antenna Height at Transmitter')
# Tx_Antenna_Height_Sub.pack(pady=10)
# Tx_Antenna_Height_Sub.place(x=30, y=120)
# Tx_Antenna_Height_Sub_Entry = Entry(Frame3,width=15,bd=3,font=('Arial 10'))
# Tx_Antenna_Height_Sub_Entry.pack(pady=10,padx=10)
# Tx_Antenna_Height_Sub_Entry.place(x = 200, y = 118)
# #
# # #Distance
# Distance_Sub = Label(Frame3, text='Distance (in metres) ')
# Distance_Sub.pack(pady=10)
# Distance_Sub.place(x=30, y=180)
# Distance_Sub_Entry = Entry(Frame3,width=15,bd=3,font=('Arial 10'))
# Distance_Sub_Entry.pack(pady=10,padx=10)
# Distance_Sub_Entry.place(x = 200, y = 178)
#
# # #Height at Receiver
# Rx_Antenna_Height_Sub = Label(Frame3, text='Antenna Height at Receiver')
# Rx_Antenna_Height_Sub.pack(pady=10)
# Rx_Antenna_Height_Sub.place(x=330, y=60)
# Rx_Antenna_Height_Sub_Entry = Entry(Frame3,width=15,bd=3,font=('Arial 10'))
# Rx_Antenna_Height_Sub_Entry.pack(pady=10,padx=10)
# Rx_Antenna_Height_Sub_Entry.place(x = 500, y = 58)
# #
# # #Frequency (GHz)
# Frequency_Sub = Label(Frame3, text='Frequency (GHz)')
# Frequency_Sub.pack(pady=10)
# Frequency_Sub.place(x=330, y=120)
# Frequency_Sub_Entry = Entry(Frame3,width=15,bd=3,font=('Arial 10'))
# Frequency_Sub_Entry.pack(pady=10,padx=10)
# Frequency_Sub_Entry.place(x = 500, y = 118)
#
# # #Received_Power
# Received_Power_Sub = Label(Frame3, text='Received Power (mW)')
# Received_Power_Sub.pack(pady=10)
# Received_Power_Sub.place(x=330, y=180)
# Received_Power_Sub_Entry = Entry(Frame3,width=15,bd=3,font=('Arial 10'))
# Received_Power_Sub_Entry.pack(pady=10,padx=10)
# Received_Power_Sub_Entry.place(x = 500, y = 178)
# #
# # #BUTTONS
# Calc_Rx_Power_Sub = ttk.Button(Frame3, text="Rxpower", command=Rxpower_Sub)
# Calc_Rx_Power_Sub.pack(ipadx=10, pady=10)
# Calc_Rx_Power_Sub.place(x=280, y=298)
# #
# Calc_Distance_Sub = ttk.Button(Frame3, text="Distance", command=Dist_Sub)
# Calc_Distance_Sub.pack(ipadx=10, pady=10)
# Calc_Distance_Sub.place(x=280, y=338)
#
# #******************************************** Frame4 Cost Urban & Suburban ***************************************************************************************************
#
# # #TITLE
# Receive_Power_Calc_Cost = Label(Frame4, text='Receive Power Calculator', font="Arial 12 bold")
# Receive_Power_Calc_Cost.pack(pady=10)
# Receive_Power_Calc_Cost.place(x=250,y=20)
# # #Transmitter Power
# Transmitter_Power_mW_Cost = Label(Frame4, text='Transmitter Power (mW)')
# Transmitter_Power_mW_Cost.pack(pady=10)
# Transmitter_Power_mW_Cost.place(x=30, y=60)
# Transmitter_Power_mW_Cost_Entry = Entry(Frame4,width=15,bd=3,font=('Arial 10'))
# Transmitter_Power_mW_Cost_Entry.pack(pady=10,padx=10)
# Transmitter_Power_mW_Cost_Entry.place(x = 200, y = 58)
# #
# # #Height at Transmitter
# Tx_Antenna_Height_Cost = Label(Frame4, text='Antenna Height at Transmitter')
# Tx_Antenna_Height_Cost.pack(pady=10)
# Tx_Antenna_Height_Cost.place(x=30, y=120)
# Tx_Antenna_Height_Cost_Entry = Entry(Frame4,width=15,bd=3,font=('Arial 10'))
# Tx_Antenna_Height_Cost_Entry.pack(pady=10,padx=10)
# Tx_Antenna_Height_Cost_Entry.place(x = 200, y = 118)
# #
# # #Distance
# Distance_Cost = Label(Frame4, text='Distance (in metres) ')
# Distance_Cost.pack(pady=10)
# Distance_Cost.place(x=30, y=180)
# Distance_Cost_Entry = Entry(Frame4,width=15,bd=3,font=('Arial 10'))
# Distance_Cost_Entry.pack(pady=10,padx=10)
# Distance_Cost_Entry.place(x = 200, y = 178)
#
# # #Height at Receiver
# Rx_Antenna_Height_Cost = Label(Frame4, text='Antenna Height at Receiver')
# Rx_Antenna_Height_Cost.pack(pady=10)
# Rx_Antenna_Height_Cost.place(x=330, y=60)
# Rx_Antenna_Height_Cost_Entry = Entry(Frame4,width=15,bd=3,font=('Arial 10'))
# Rx_Antenna_Height_Cost_Entry.pack(pady=10,padx=10)
# Rx_Antenna_Height_Cost_Entry.place(x = 500, y = 58)
# #
# # #Frequency (GHz)
# Frequency_Cost = Label(Frame4, text='Frequency (GHz)')
# Frequency_Cost.pack(pady=10)
# Frequency_Cost.place(x=330, y=120)
# Frequency_Cost_Entry = Entry(Frame4,width=15,bd=3,font=('Arial 10'))
# Frequency_Cost_Entry.pack(pady=10,padx=10)
# Frequency_Cost_Entry.place(x = 500, y = 118)
#
# # #Received_Power
# Received_Power_Cost = Label(Frame4, text='Received Power (mW)')
# Received_Power_Cost.pack(pady=10)
# Received_Power_Cost.place(x=330, y=180)
# Received_Power_Cost_Entry = Entry(Frame4,width=15,bd=3,font=('Arial 10'))
# Received_Power_Cost_Entry.pack(pady=10,padx=10)
# Received_Power_Cost_Entry.place(x = 500, y = 178)
# #
# ## CM
# cm = ttk.Label(Frame4, text = "CM",font = ("Times New Roman", 10))
# cm.pack(pady=10)
# cm.place(x=330, y=240)
# n = tk.StringVar()
# Value = ttk.Combobox(Frame4, width = 15, textvariable = n)
#
# Value['values'] = ('3','0')
# Value.pack()
# Value.place(x= 500, y= 238)
#
# # #BUTTONS
# Calc_Rx_Power_Cost = ttk.Button(Frame4, text="Rxpower", command=Rxpower_Cost)
# Calc_Rx_Power_Cost.pack(ipadx=10, pady=10)
# Calc_Rx_Power_Cost.place(x=280, y=298)
# #
# Calc_Distance_Cost = ttk.Button(Frame4, text="Distance", command=Dist_Cost)
# Calc_Distance_Cost.pack(ipadx=10, pady=10)
# Calc_Distance_Cost.place(x=280, y=338)

#******************************************** Frame5 Indoor Office & Factory ***************************************************************************************************

# #TITLE
Receive_Power_Indoor_Calc = Label(Frame5, text='Receive Power Calculator', font="Arial 12 bold")
Receive_Power_Indoor_Calc.pack(pady=10)
Receive_Power_Indoor_Calc.place(x=250,y=20)
# #Transmitter Power
Transmitter_Power_Indoor_mW = Label(Frame5, text='Transmitter Power (mW)')
Transmitter_Power_Indoor_mW.pack(pady=10)
Transmitter_Power_Indoor_mW.place(x=30, y=60)
Transmitter_Power_Indoor_mW_Entry = Entry(Frame5,width=15,bd=3,font=('Arial 10'))
Transmitter_Power_Indoor_mW_Entry.pack(pady=10,padx=10)
Transmitter_Power_Indoor_mW_Entry.place(x = 200, y = 58)
#
# #Gain at Transmitter
Tx_Antenna_Gain_Indoor = Label(Frame5, text='Antenna Gain at Transmitter')
Tx_Antenna_Gain_Indoor.pack(pady=10)
Tx_Antenna_Gain_Indoor.place(x=30, y=120)
Tx_Antenna_Gain_Indoor_Entry = Entry(Frame5,width=15,bd=3,font=('Arial 10'))
Tx_Antenna_Gain_Indoor_Entry.pack(pady=10,padx=10)
Tx_Antenna_Gain_Indoor_Entry.place(x = 200, y = 118)
#
# #Gain at Receiver
Rx_Antenna_Gain_Indoor = Label(Frame5, text='Antenna Gain at Receiver')
Rx_Antenna_Gain_Indoor.pack(pady=10)
Rx_Antenna_Gain_Indoor.place(x=30, y=180)
Rx_Antenna_Gain_Indoor_Entry = Entry(Frame5,width=15,bd=3,font=('Arial 10'))
Rx_Antenna_Gain_Indoor_Entry.pack(pady=10,padx=10)
Rx_Antenna_Gain_Indoor_Entry.place(x = 200, y = 178)
#
# #Frequency (GHz)
Frequency_Indoor = Label(Frame5, text='Frequency (GHz)')
Frequency_Indoor.pack(pady=10)
Frequency_Indoor.place(x=30, y=240)
Frequency_Indoor_Entry = Entry(Frame5,width=15,bd=3,font=('Arial 10'))
Frequency_Indoor_Entry.pack(pady=10,padx=10)
Frequency_Indoor_Entry.place(x = 200, y = 238)
#
# #d0
d0_Indoor = Label(Frame5, text='Reference Distance (d0)')
d0_Indoor.pack(pady=10)
d0_Indoor.place(x=330, y=60)
d0_Indoor_Entry = Entry(Frame5,width=15,bd=3,font=('Arial 10'))
d0_Indoor_Entry.pack(pady=10,padx=10)
d0_Indoor_Entry.place(x = 500, y = 58)
#
# #Pathloss_Exponent
Pathloss_Exponent_Indoor = Label(Frame5, text='Pathloss Exponent (\u03B7)')
Pathloss_Exponent_Indoor.pack(pady=10)
Pathloss_Exponent_Indoor.place(x=330, y=120)
n = tk.StringVar()
Pathloss_Exponent_Indoor_Entry = ttk.Combobox(Frame5, width =15, textvariable= n)
Pathloss_Exponent_Indoor_Entry['values'] = ('2.6', '2.1')
Pathloss_Exponent_Indoor_Entry.pack(pady=10,padx=10)
Pathloss_Exponent_Indoor_Entry.place(x = 500, y = 118)
#
# #Distance
Distance_Indoor = Label(Frame5, text='Distance (in metres) ')
Distance_Indoor.pack(pady=10)
Distance_Indoor.place(x=330, y=180)
Distance_Indoor_Entry = Entry(Frame5,width=15,bd=3,font=('Arial 10'))
Distance_Indoor_Entry.pack(pady=10,padx=10)
Distance_Indoor_Entry.place(x = 500, y = 178)
#
# #Received_Power
Received_Power_Indoor = Label(Frame5, text='Received Power (mW)')
Received_Power_Indoor.pack(pady=10)
Received_Power_Indoor.place(x=330, y=240)
Received_Power_Indoor_Entry = Entry(Frame5,width=15,bd=3,font=('Arial 10'))
Received_Power_Indoor_Entry.pack(pady=10,padx=10)
Received_Power_Indoor_Entry.place(x = 500, y = 238)
#
# #BUTTONS
Calc_Rx_Power_Indoor = ttk.Button(Frame5, text="Rxpower", command=Rxpower_Indoor)
Calc_Rx_Power_Indoor.pack(ipadx=10, pady=10)
Calc_Rx_Power_Indoor.place(x=280, y=298)
#
Calc_Distance_Indoor = ttk.Button(Frame5, text="Distance", command=Dist_Indoor)
Calc_Distance_Indoor.pack(ipadx=10, pady=10)
Calc_Distance_Indoor.place(x=280, y=338)

#******************************************************Frame6 Indoor Home *******************************************************************************************
# #TITLE
Receive_Power_Calc_Home = Label(Frame6, text='Receive Power Calculator', font="Arial 12 bold")
Receive_Power_Calc_Home.pack(pady=10)
Receive_Power_Calc_Home.place(x=250,y=20)
# #Transmitter Power
Transmitter_Power_Home_mW = Label(Frame6, text='Transmitter Power (mW)')
Transmitter_Power_Home_mW.pack(pady=10)
Transmitter_Power_Home_mW.place(x=30, y=60)
Transmitter_Power_mW_Home_Entry = Entry(Frame6,width=15,bd=3,font=('Arial 10'))
Transmitter_Power_mW_Home_Entry.pack(pady=10,padx=10)
Transmitter_Power_mW_Home_Entry.place(x = 200, y = 58)
#
# #Gain at Transmitter
Tx_Antenna_Gain_Home = Label(Frame6, text='Antenna Gain at Transmitter')
Tx_Antenna_Gain_Home.pack(pady=10)
Tx_Antenna_Gain_Home.place(x=30, y=120)
Tx_Antenna_Gain_Home_Entry = Entry(Frame6,width=15,bd=3,font=('Arial 10'))
Tx_Antenna_Gain_Home_Entry.pack(pady=10,padx=10)
Tx_Antenna_Gain_Home_Entry.place(x = 200, y = 118)
#
# #Gain at Receiver
Rx_Antenna_Gain_Home = Label(Frame6, text='Antenna Gain at Receiver')
Rx_Antenna_Gain_Home.pack(pady=10)
Rx_Antenna_Gain_Home.place(x=30, y=180)
Rx_Antenna_Gain_Home_Entry = Entry(Frame6,width=15,bd=3,font=('Arial 10'))
Rx_Antenna_Gain_Home_Entry.pack(pady=10,padx=10)
Rx_Antenna_Gain_Home_Entry.place(x = 200, y = 178)
#
# #Frequency (GHz)
Frequency_Home = Label(Frame6, text='Frequency (GHz)')
Frequency_Home.pack(pady=10)
Frequency_Home.place(x=30, y=240)
Frequency_Home_Entry = Entry(Frame6,width=15,bd=3,font=('Arial 10'))
Frequency_Home_Entry.pack(pady=10,padx=10)
Frequency_Home_Entry.place(x = 200, y = 238)
#
# #d0
d0_Home = Label(Frame6, text='Reference Distance (d0)')
d0_Home.pack(pady=10)
d0_Home.place(x=330, y=60)
d0_Home_Entry = Entry(Frame6,width=15,bd=3,font=('Arial 10'))
d0_Home_Entry.pack(pady=10,padx=10)
d0_Home_Entry.place(x = 500, y = 58)
#
# #Pathloss_Exponent
Pathloss_Exponent_Home = Label(Frame6, text='Pathloss Exponent (\u03B7)')
Pathloss_Exponent_Home.pack(pady=10)
Pathloss_Exponent_Home.place(x=330, y=120)
Pathloss_Exponent_Home_Entry = Entry(Frame6,width=15,bd=3,font=('Arial 10'))
Pathloss_Exponent_Home_Entry.pack(pady=10,padx=10)
Pathloss_Exponent_Home_Entry.place(x = 500, y = 118)
Pathloss_Exponent_Home_Entry.configure(state='normal')
Pathloss_Exponent_Home_Entry.insert('end', '3')
Pathloss_Exponent_Home_Entry.configure(state='disabled')
#
# #Distance
Distance_Home = Label(Frame6, text='Distance (in metres) ')
Distance_Home.pack(pady=10)
Distance_Home.place(x=330, y=180)
Distance_Home_Entry = Entry(Frame6,width=15,bd=3,font=('Arial 10'))
Distance_Home_Entry.pack(pady=10,padx=10)
Distance_Home_Entry.place(x = 500, y = 178)
#
# #Received_Power
Received_Power_Home = Label(Frame6, text='Received Power (mW)')
Received_Power_Home.pack(pady=10)
Received_Power_Home.place(x=330, y=240)
Received_Power_Home_Entry = Entry(Frame6,width=15,bd=3,font=('Arial 10'))
Received_Power_Home_Entry.pack(pady=10,padx=10)
Received_Power_Home_Entry.place(x = 500, y = 238)
#
# #BUTTONS
Calc_Rx_Power_Home = ttk.Button(Frame6, text="Rxpower", command=Rxpower_Home)
Calc_Rx_Power_Home.pack(ipadx=10, pady=10)
Calc_Rx_Power_Home.place(x=280, y=298)
#
Calc_Distance_Home = ttk.Button(Frame6, text="Distance", command=Dist_Home)
Calc_Distance_Home.pack(ipadx=10, pady=10)
Calc_Distance_Home.place(x=280, y=338)
window.mainloop()