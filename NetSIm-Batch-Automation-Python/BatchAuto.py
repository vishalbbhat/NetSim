import os
import shutil

APPPATH = "C:\\Users\\ALICE\\Documents\\NetSim\\Workspaces\\demo\\bin_x64" #Workspace Bin folder
Samples = "C:\\Users\\ALICE\\Documents\\NetSim\\Workspaces\\demo\\" #Location of all samples
NetSimTempCore = "C:\\Users\\ALICE\\AppData\\Local\\Temp\\NetSimTemp\\" #change it to your desired path
License = "5053@192.168.0.9" #if cloud based license give path for it

# for running the scenario
for root, dirs, files in os.walk(Samples):
    for file in files:
        if file.endswith(".netsim"):
            os.mkdir(NetSimTempCore)
            shutil.copy(root+"\\"+file, NetSimTempCore)
            path = "start /w /MIN "+APPPATH+"\\NetSimCore.exe"+" -apppath "+APPPATH+" -iopath "+NetSimTempCore+" -license "+License
            os.system(path)
            for a, b, c in os.walk(NetSimTempCore):
                for d in c:
                    shutil.copy(NetSimTempCore+"\\"+d, root+"\\")
        if os.path.exists(NetSimTempCore):
            shutil.rmtree(NetSimTempCore)
            