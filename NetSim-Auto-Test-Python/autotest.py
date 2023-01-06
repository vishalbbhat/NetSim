# Importing required libraries
from tkinter import *
from tkinter import ttk, filedialog
import os
import shutil
import psutil
from PIL import Image, ImageTk
import threading


# initializing variables
APPPATH = ""
Samples = ""
License = ""
con_count = sim_count = 0
# Creating a folder IOPath for temp simulation execution
if not os.path.exists("IOPath"):
    os.makedirs("IOPath")
NetSimCorePath = os.getcwd() + "\IOPath"
for root, dirs, files in os.walk("IOPath"):
    for file in files:
        os.remove(os.path.join(root, file))

# GUI Setting
window = Tk()
window.title("NetSim Batch Automation")
# set window width and height
window.minsize(height=350, width=750)
window.maxsize(height=350, width=750)
photo = PhotoImage(file="NetSim-Favicon.png")
window.iconphoto(True, photo)

# Resize the image in the given (width, height)
path1 = "TETCOS-Logo.png"
image1 = Image.open(path1)
img1=image1.resize((90,50))
my_img1=ImageTk.PhotoImage(img1)
label1=Label(window, image=my_img1)
label1.pack()
label1.place(x=20,y=0)

#Progress bar
def progress():
    each_count = 100 / con_count
    if pb['value'] < 300:
        pb['value'] += each_count

# Count the number of simulations
def config_count():
    global con_count,Samples
    for root, dirs, files in os.walk(Samples):
        for file in files:
            if file.endswith(".netsim"):
                con_count += 1
    total_cases = Label(window, text="Total cases: " + str(con_count))
    total_cases.pack(ipadx=10, ipady=10)
    total_cases.place(x=20, y=250)




# Select Binaries folder
def select_ap_file():
    global APPPATH
    APPPATH = filedialog.askdirectory()
    net_sim_text_input.delete(0, END)
    net_sim_text_input.insert(0, APPPATH)
    return APPPATH

# Select Binaries folder
def standard_ver_path():
    global APPPATH
    APPPATH = "C:\\Program Files\\NetSim\\Standard_v13_3\\bin\\bin_x64"
    net_sim_text_input.delete(0, END)
    net_sim_text_input.insert(0, APPPATH)
    return APPPATH

# Select Binaries folder
def acad_ver_path():
    global APPPATH
    APPPATH = "C:\\Program Files\\NetSim\\Academic_v13_3\\bin\\bin_x64"
    net_sim_text_input.delete(0, END)
    net_sim_text_input.insert(0, APPPATH)
    return APPPATH


# Select samples folder path
def select_config_file():
    global Samples
    Samples = filedialog.askdirectory()
    config_count()
    config_file_text_input.delete(0, END)
    config_file_text_input.insert(0, Samples)
    return Samples


#Select license file
def select_lic_file():
    global License
    License = filedialog.askdirectory()
    lic_file_text_input.delete(0, END)
    lic_file_text_input.insert(0, License)
    return License

def refresh():
    global APPPATH, Samples, License, con_count, sim_count
    APPPATH = ""
    Samples = ""
    License = ""
    net_sim_text_input.delete(0, END)
    config_file_text_input.delete(0, END)
    lic_file_text_input.delete(0, END)
    con_count_text_input.delete(0, END)
    con_count = 0
    sim_count = 0
    pb['value'] = 0
# To update the progress bar

def open_results():
    #cmd = ('notepad ' + Samples + '/results.txt')
    #os.system(cmd)
    pass

# To run the simulation
def run_sim():
    count=0
    sim_count = con_count
    # for running the scenario
    License = lic_file_text_input.get()
    APPPATH = net_sim_text_input.get()
    Samples = config_file_text_input.get()
    #Removing previously created files
    if os.path.exists(os.getcwd()+"\\results.txt"):
        os.remove(os.getcwd()+"\\results.txt")
    if os.path.exists(os.getcwd()+"\\appMetrics.txt"):
        os.remove(os.getcwd()+"\\appMetrics.txt")
    if os.path.exists(os.getcwd()+"\\compare.txt"):
        os.remove(os.getcwd()+"\\compare.txt")
    pb['value'] = 0
    for root, dirs, files in os.walk(Samples):
        for file in files:
            rem_case = "Remaining Cases: " + str(sim_count) + " of " + str(con_count)
            con_count_text_input.config(state="normal")
            con_count_text_input.insert(0, rem_case)
            if file.endswith(".netsim"):
                shutil.copy(root+'\\'+file, NetSimCorePath)
                if os.path.isfile(root+'\\Metrics.xml'):
                    if os.path.isfile(NetSimCorePath+'\\Metrics.xml'):
                        os.remove(NetSimCorePath+'\\Metrics.xml')
                    #Run the simulation
                    cmd = ('start "AutoTest" /wait /d '+ '"'+ APPPATH+ '" NetSimcore.exe'+ ' -apppath "'+ APPPATH+ '" -iopath "'+ NetSimCorePath+ '" -license '+ '"'+ License+ '"')
                    os.system(cmd)
                    if os.path.isfile(NetSimCorePath+'\\Metrics.xml'):
                        #Compares the Metrics.xml files
                        cmd1 = "C:\\windows\\system32\\fc.exe" + ' "' + root + "\\" + 'Metrics.xml' + '" ' + '"' + NetSimCorePath + "\\" + 'Metrics.xml' + '"' + " > " + NetSimCorePath + "\\" + 'diff.txt'
                        stat = os.system(cmd1)
                        count+=1
                        #If the previous command gives an error
                        if stat > 0:
                            plotError = 0
                            errorCounter = 0
                            plotCounter = 0
                            with open(NetSimCorePath + "\\" + 'diff.txt', 'r') as fid:
                                lines = fid.readlines()
                                for line in lines:
                                    if line.__contains__("MENU Name"):
                                        plotCounter +=1
                                    elif(line.__contains__("PLOT data_file_name")):
                                            plotCounter +=1
                                            plotError +=1
                                    elif(line.__contains__("/MENU")):
                                                plotCounter +=1
                                    elif(line.startswith("*****")):
                                        if(plotCounter==3):
                                            if(plotError !=0):
                                                if(errorCounter==1):
                                                    status="plotdifference"
                                    elif(plotError==0):
                                        if(errorCounter !=0):
                                            status="difference"
                                        errorCounter +=1
                                if(status==''):
                                    plotCounter=0
                                if(status=="difference"):
                                    with open(os.getcwd()+'\\results.txt', 'a') as fid:
                                        fid.write(str(root)+" - Difference Found\n")
                                else:
                                    if (status == "plotdifference"):
                                        with open(os.getcwd() + '\\results.txt', 'a') as fid:
                                            fid.write(str(root)+" - Plot Difference\n")
                        else:
                            with open(os.getcwd()+ '\\results.txt', 'a') as fid:
                                fid.write(str(root)+" - Success\n")
                        #The differences of diff.txt is appended to compare.txt
                        with open(os.getcwd() +'\\compare.txt', "a") as file:
                            file.write("------------------------------------------------------------------------------------------------------------\n")
                            with open(NetSimCorePath +'\\diff.txt') as file1:
                                for line in file1:
                                    file.write(line)
                            file.write("------------------------------------------------------------------------------------------------------------\n")
                        #Writes the throughput of all the applications to a file
                        flag=False
                        application=0
                        with open(NetSimCorePath + "\\" + 'Metrics.xml', 'r') as f:
                            lines = f.readlines()
                            for line in lines:
                                if line.__contains__("TABLE name"):
                                    if line.__contains__("Application_Metrics"):
                                        flag=True
                                if flag==True:
                                    if line.__contains__("TR"):
                                        application+=1
                                        count=0
                                if application !=0:
                                    if line.__contains__("TC Value"):
                                        count=count+1
                                        token = line.split('="')
                                        token1 = token[1].split('"/')
                                        val = token1[0]
                                        if count == 2:
                                            with open(os.getcwd()+"\\appMetrics.txt", "a") as file:
                                                file.write(f"{root} - "+str(val)+"\n")
                                        if count == 9:
                                            with open(os.getcwd()+"\\appMetrics.txt", "a") as file:
                                                file.write(f"Throughput(Mbps) = "+str(val)+"\n")
                                        if count == 10:
                                            with open(os.getcwd()+"\\appMetrics.txt", "a") as file:
                                                file.write(f"Delay(microSec) = "+str(val)+"\n")
                                if line.__contains__("/TABLE"):
                                    flag = False
                                    application = 0
                                    count = 0
                            with open(os.getcwd()+ "\\appMetrics.txt", "a") as file:
                                file.write("------------------------------------------------------------------------------------------------------------\n")
                    else:
                        with open(os.getcwd() + '\\results.txt', 'a') as fid:
                            fid.write(str(root) + " - Crashed\n")

                else:
                    with open(os.getcwd() + '\\results.txt', 'a') as fid:
                        fid.write(str(root) + " - Missing Metrics.xml\n")
                    progress()
                for process in (process for process in psutil.process_iter() if process.name() == "Wireshark.exe"):
                    process.kill()
                sim_count-=1
            con_count_text_input.delete(0, END)
    con_count_text_input.insert(0, "Simulation Completed!")
    con_count_text_input.config(state="normal")
    #print(cmd1)


    return 0

class run_simthread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        run_sim()

run_simthread.daemon=True

def run_sim_t():
    run_simthread().start()

# GUI Settings

#Main Label
batch_automation_label = Label(window, text='NetSim Batch Automation', font="Arial 12 bold")
batch_automation_label.pack(ipadx=10, ipady=10)
batch_automation_label.place(x=350,y=10)

# Workspace Bin Folder Label
net_sim_bin_label = Label(window, text='NetSim Workspace Bin Folder:')
net_sim_bin_label.pack(ipadx=10, ipady=10)
net_sim_bin_label.place(x=20, y=60)

# Text box for Bin folder
net_sim_text_input = Entry(width=55,bd=3,font=('Arial 10'))
net_sim_text_input.place(x = 200, y = 60)



# Browse Button for Bin folder
select_button1 = ttk.Button(window, text="Browse", command=select_ap_file)
select_button1.pack(ipadx=5, pady=15)
select_button1.place(x=600, y=60)

# Browse Button for Standard Bin folder
select_button1 = ttk.Button(window, text="Standard v13.3", command=standard_ver_path)
select_button1.pack(ipadx=5, pady=15)
select_button1.place(x=200, y=90)

# Browse Button for Standard Bin folder
select_button1 = ttk.Button(window, text="Academic v13.3", command=acad_ver_path)
select_button1.pack(ipadx=5, pady=15)
select_button1.place(x=300, y=90)

# Configuration folder lable
config_file_label = Label(window, text='Configuration File Path: ')
config_file_label.pack(ipadx=10, ipady=10)
config_file_label.place(x=20, y=130)

# Text box for config file folder
config_file_text_input = Entry(width=55,bd=3,font=('Arial 10'))
config_file_text_input.place(x = 200, y = 130)

# Browse button for Config folder
select_button2 = ttk.Button(window, text="Browse", command=select_config_file)
select_button2.pack(ipadx=5, pady=15)
select_button2.place(x=600, y=130)

# License file or server label
lic_file_label = Label(window, text='License (Cloud or Server IP): ')
lic_file_label.pack(ipadx=10, ipady=10)
lic_file_label.place(x=20, y=190)

# License file text box
lic_file_text_input= Entry(width=55,bd=3,font=(' Arial 10'))
lic_file_text_input.place(x = 200, y = 190)
lic_file_text_input.insert(0,"5053@192.168.0.9")

# Browse button for License file
select_button3 = ttk.Button(window, text="Browse", command=select_lic_file)
select_button3.pack(ipadx=5, pady=15)
select_button3.place(x=600, y=190)

# Run Simulation Button
run_sim_button = ttk.Button(window, text="Run", command=run_sim_t)
run_sim_button.pack(ipadx=5, pady=15)
run_sim_button.place(x=200, y=250)

# Refresh window button
refresh_button = ttk.Button(window, text="Refresh", command=refresh)
refresh_button.pack(ipadx=5, pady=15)
refresh_button.place(x=400, y=250)

# Status Lable
status_label = Label(window, text='Status: ')
status_label.pack(ipadx=10, ipady=10)
status_label.place(x=20, y=280)

#Text Input
con_count_text_input = Entry(width=25, bd=3, font=('Arial 10'))
con_count_text_input.place(x=80, y=280)
con_count_text_input.delete(0,END)
con_count_text_input.insert(0,"")
con_count_text_input.config(state="disabled")




#prgress bar
pb = ttk.Progressbar(
    window,
    orient='horizontal',
    mode='determinate',
    length=750
)
pb.place(x=0, y=330)




#Open results button
open_results_button = ttk.Button(window, text="Open Results", command=open_results)
open_results_button.pack(ipadx=5, pady=15)
open_results_button.place(x=600, y=250)
window.mainloop()


# Delete IOPath folder created
if os.path.exists(NetSimCorePath):
     shutil.rmtree(NetSimCorePath)
