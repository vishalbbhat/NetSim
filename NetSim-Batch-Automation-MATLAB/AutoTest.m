% Set the path of 64 bit NetSim Binaries to be used for simulation.
prompt = "Enter NetSim Binaries Path: "
NETSIM_PATH = input(prompt,'s')
%NETSIM_PATH = "C:\Users\Hi\Documents\NetSim\Workspaces\matlab_samples\bin_x64";
prompt = "Enter LICENSE ARG Path: "
LICENSE_ARG = input(prompt,'s')
%LICENSE_ARG = "5053@192.168.0.9"; %Floating license
%LICENSE_ARG = """C:\Program Files\NetSim\Standard_v13_2\bin"""; %Node Locked license

% Set NETSIM_AUTO environment variable to avoid keyboard interrupt at the end of each simulation
setenv('NETSIM_AUTO','1');

%To get the Current Folder
%currentFolder = pwd;
prompt = "Enter from folder Path: "
from_folder = input(prompt,'s');
%from_folder = 'C:\Users\Hi\Desktop\BatchAuto\Cgf'; % Folder to copy file from
prompt = "Enter to folder Path: "
to_folder = input(prompt,'s')
% to_folder = 'C:\Users\Hi\Desktop\BatchAuto\TEMP'; % Folder to copy file to
%mkdir(to_folder)
file_name = 'Configuration.netsim'; % Name of file to copy

%Result File
resultfile = fullfile(pwd,'results.txt');
comparefile = fullfile(pwd,'compare.txt');
appMetrics = fullfile(pwd,'appMetrics.txt');

if exist(resultfile)
    delete(resultfile)
end

if exist("appMetrics.txt")
    delete("appMetrics.txt")
end

if exist(comparefile)
    delete(comparefile)
end
% Get all files in from_folder
filelist = dir(fullfile(from_folder, '**\*.netsim'));

% Iterate through all file
%Loop through the list of files
for i = 1:length(filelist)
    if(~isfolder(to_folder))
        mkdir(to_folder)
    end
    zee = copyfile(filelist(i,1).folder,to_folder);
    delete(fullfile(getenv('Temp'),'NetSimCoreAuto','Metrics.xml'))
    if exist(fullfile(filelist(i,1).folder,'Metrics.xml'))
        %Run NetSim via CLI mode by passing the apppath iopath and license information to the NetSimCore.exe
        cmd="start ""NetSim_Batch_Automation"" /wait /d "...
            +""""...
            +NETSIM_PATH...
            + """ "...
            + "NetSimcore.exe -apppath """...
            +NETSIM_PATH...
            + """ -iopath """...
            +to_folder...
             +""" -license "...
            +LICENSE_ARG;
        system(cmd)
        %If the Metrics.xml doesn't exist after simulation then the simulation is crashed
        if exist(fullfile(getenv('Temp'),'NetSimCoreAuto','Metrics.xml'))
            temp1=fullfile(filelist(i,1).folder,'Metrics.xml');
            temp2=fullfile(getenv('Temp'),'NetSimCoreAuto','Metrics.xml');
            %Define the executable filename
            exeName = 'C:\Windows\System32\fc.exe';
            difftxt = ['> ' fullfile(getenv('Temp'),'NetSimCoreAuto','diff.txt')];
            %Define any command line arguments for the executable
            argument = [exeName ' ' temp1 ' ' temp2 ' ' difftxt];
            disp(argument)
            %Call the executable
            [status]=system(argument,'-echo');
            % Compares the Metrics.xml files
            %[status,cmdout] = system(['C:\windows\system32\FC.exe ',fullfile(filelist(i,1).folder,fullfile(getenv('Temp'),'NetSimCoreAuto','Metrics.xml'),' > ',fullfile(getenv('Temp'),'NetSimCoreAuto','diff.txt'))]);
            % If the previous command gives an errorlevel equal to or greater
            if status >= 1
                plotError = 0;
                errorCounter = 0;
                plotCounter = 0;
                fid = fopen(fullfile(getenv('Temp'),'NetSimCoreAuto','diff.txt'),'r');
                tline = fgets(fid);
                while ischar(tline)
                    token2 = split(tline,"<=>");
                    %disp(token2)
                    if contains(token2,"MENU Name")
                        plotCounter = plotCounter + 1;
                    elseif contains(token2,"PLOT data_file_name")
                        plotCounter = plotCounter + 1;
                        plotError = plotError + 1;
                    elseif contains(token2,"/MENU")
                        plotCounter = plotCounter + 1;
                    else
                        if(contains(token2,"*****"))
                            if plotCounter == 3
                                if plotError ~= 0
                                    if errorCounter == 1
                                        status = 'plotDifference';
                                    end
                                end
                            end
                        else
                            if plotError == 0
                                if errorCounter ~= 0
                                    status = 'difference';
                                end
                                errorCounter = errorCounter + 1;
                            end
                        end
                    end
                    tline = fgetl(fid);
                end
                fclose(fid);
                if(status==0)
                    plotCounter=0;
                end
                if strcmp(status, 'difference')
                    fid = fopen(resultfile,'a');
                    fprintf(fid,'%s - Difference Found\n',fullfile(filelist(i,1).folder));
                    fclose(fid);
                elseif strcmp(status, 'plotDifference')
                    fid = fopen(resultfile,'a');
                    fprintf(fid,'%s - Plot Difference\n',fullfile(filelist(i,1).folder));
                    fclose(fid);
                end
            else
                fid = fopen(resultfile,'a');
                fprintf(fid,'%s - Success\n',fullfile(filelist(i,1).folder));
                fclose(fid);
            end
            %Appending from diff.txt to Compare.txt
            file1 = fopen(fullfile(getenv('Temp'),'NetSimCoreAuto','diff.txt'),'r');
            while ~feof(file1)
                line = fgetl(file1);
                file2 = fopen(comparefile,'a');
                fprintf(file2, '%s\n', line);
                fclose(file2);
            end
            fclose(file1);
            fid = fopen(comparefile,'a');
            fprintf(fid,'\n------------------------------------------------------------------------------------------------------------ >> compare.txt\n');
            fclose(fid);
            %Difference Check and Writing in Comapre.txt Process Ended
            %----------------------------------------------------------
            %Writing appMetrics.txt Code Starts Here
            %REM - Writes the throughput of all the applications to a file
            flag = false;
            application = 0;
            file1 = fopen(fullfile(getenv('Temp'),'NetSimCoreAuto','Metrics.xml'),'r');
            while ~feof(file1)
                line = fgetl(file1);
                if contains(line, 'TABLE name') && contains(line, 'Application_Metrics')
                    flag = true;
                end
                if flag
                    if contains(line, 'TR')
                        application = application + 1;
                        count = 0;
                    end
                end
                if application ~= 0
                    if contains(line, 'TC Value')
                        token = split(line,'="');
                        token1 = split(token(2,1),'"/');
                        stringz = string(token1(1,1));
                        count = count + 1;
                        fid = fopen(appMetrics,'a');
                        if count == 2
                            fprintf(fid,'%s - %s\n',fullfile(filelist(i,1).folder), stringz);
                        elseif count == 9
                            fprintf(fid,'Throughput(Mbps) = %s\n', stringz);
                        elseif count == 10
                            fprintf(fid,'Delay(microSec) = %s\n', stringz);
                        end
                        fclose(fid);
                    end
                end
                if contains(line, '/TABLE')
                    flag = false;
                    application = 0;
                    count = 0;
                end
            end
            fid = fopen(appMetrics,'a');
            fprintf(fid,'\n------------------------------------------------------------------------------------------------------------ >> appMetrics.txt\n');
            fclose(fid);
            fclose(file1);
        else
            fid = fopen(resultfile,'a');
            fprintf(fid,'%s -Crashed\n',fullfile(filelist(i,1).folder));
            fclose(fid);
        end
        [errorlevel] = system('tasklist /fi "IMAGENAME EQ Wireshark.exe" | find ":" > nul');
        if (errorlevel>=1)
            system('Taskkill /F /IM Wireshark.exe');
        end
    else
        fid = fopen(resultfile,'a');
        fprintf(fid,'%s -Missing Metrics.xml\n',fullfile(filelist(i,1).folder));
        fclose(fid);
    end
end
% Delete all the files from NetSimCoreAuto
delete(fullfile(tempdir, 'NetSimCoreAuto', '*'));