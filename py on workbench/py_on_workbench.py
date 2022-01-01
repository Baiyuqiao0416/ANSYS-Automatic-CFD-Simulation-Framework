# -*- coding: utf-8 -*-
# Based on ANSYS 2019R2
# Python 3.7 x64

#  ----------------------------------------------------------------------------------
# |                                                                                  |
# |  Copyright © 2021 by Yuqiao Bai & Xiangyu Zhao of AOT Lab in Soochow University  |
# |                                                                                  |
#  ----------------------------------------------------------------------------------

import os 
import sys
import time
import shutil
import decimal
import datetime
import platform
import linecache
import fileinput
from PyWbUnit import CoWbUnitProcess
from multiprocessing import cpu_count

#Log
class Logger(object):

    def __init__(self, stream=sys.stdout):
        output_dir = "log"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        log_name = '{}.log'.format(time.strftime('%Y-%m-%d-%H-%M'))
        filename = os.path.join(output_dir, log_name)

        self.terminal = stream
        self.log = open(filename, 'a+')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

sys.stdout = Logger(sys.stdout)  # write console to log
sys.stderr = Logger(sys.stderr)  # write err to log 

print()
print('====================================================================================')
print()
print('                             ,@@@@\.       ,/@@@@@@@@`. @@@@@@@@@@@@@@@@@@@@@.      ')
print('                            =@@@@@@@.    ,@@@`.   .\@@@^,@@@@@@@@@@@@@@@@@@@`       ')
print('                           ,@@@@@@@@\   =@@`  .` @@`,@@@^      =@@@@@@.             ')
print('                          .@@@@@@@=@@^  @@^  /@@. ,@^=@@@.     =@@@@@@.             ')
print('                          /@@@@@@. \@@` @@^  @@`  ,@^=@@@.     =@@@@@@.             ')
print('                         =@@@@@@`  .@@@.=@@`   ,\/@/,@@@^      =@@@@@@.             ')
print('    .*******]@@@@\`*.   ,@@@@@@^    ,@@\.,@@\`. ..,@@@@^       =@@@@@@.             ')
print('   [[[[[[[[`.  .*[[\@..@@@@@@^      =@@^  ,\@@@@@@@@^]]*.     =@@@@@@.              ')
print('                    .@\/@@@@@/        \@@` .]]]/@@@@[[**[@@]****\@@@/*********..    ')
print('                      \@@@@@`         .@@@/@`**.          .,[[[[[[`[[[[[[[[[[[[.    ')
print('                                       ,@@/                                         ')
print('                                        ,[                                          ')
print()
print('====================================================================================') 
print()
print('                 SOOCHOW UNIVERSITY ARTIFICIAL ORGAN TECHNOLOGY LAB                 ')                                                                                
print()
print('                        Automatic Fluid Simulation Framework                        ')
print()
print('                               Based On ANSYS 2019 R2                               ')
print()
print('====================================================================================')
print()
print('System Information')
print()
print('Platform:'+platform.platform())
print('System Version:'+platform.version())
print('System Architecture:'+str(platform.architecture()))
print('Computer Name:'+platform.node())
print('Processor:'+platform.processor())
print('Number of logical processors:'+str(cpu_count()))
print()
print('====================================================================================')

# Input parameters

in_content="N"
while(in_content!="Y"):
    print("Please define the work path:")
    workpath = input()   
    print("Please define the initial d 'd0':")
    d0 = input()
    print("Please define the delta d 'step':")
    step = input()
    print("Please define the number of caculation 'n':")
    n = input()
    print()
    print("Please make sure the following content is correct, press 'Y' if it is correct.")
    print()
    print('workpath='+workpath)
    print('d0='+d0)
    print('step='+step)
    print('n='+n)
    print()
    in_content=input()
    
print('====================================================================================')
print()
print("Initializing...")
print()
print('====================================================================================')

# Fluent setting
NumberOfProcessors=int(cpu_count())-2
NumberOfGPGPUs='1'

# Work setting
# Use relative paths instead
SCDMscriptname='SCDM_Script.py' 
Meshscriptname='MESH_Script.py'
Fluentscriptname='FLUENT_Script.jou'   #line 17 (cx-gui-do cx-set-text-entry "Open Database*TextEntry1(Database Name)" "G:/zxy/py on workbench/blood.scm") Change the datebase path
Additerationscriptname='Add_Iteration_Script.jou'
setfile='settings.set'
WorkbenchDir = linecache.getline(setfile, 1).strip('\n')
MaterialDir = linecache.getline(setfile, 2).strip('\n')
def replacement(file, previousw, nextw):
   for line in fileinput.input(file, inplace=1):
       line = line.replace(previousw, nextw)
       sys.stdout.write(line)
var1 = "material database dir"
replacement(Fluentscriptname, var1, MaterialDir)

# loop
i=0
while(i<int(n)):
    d=decimal.Decimal(d0)+decimal.Decimal(step)*decimal.Decimal(i)
    name=str(i+1)+"_"+str(d)+"mm"
    wbpjname=name+".wbpj "
    os.mkdir(workpath+"\\"+name)
    
    # Create an instance of the wb unit and specify the ansys wb version
    coWbUnit = CoWbUnitProcess(WorkbenchDir, version=194, interactive=True) 
    coWbUnit.initialize()
    coWbUnit.execWbCommand('SetScriptVersion(Version="19.4.159")')
    coWbUnit.execWbCommand('system1 = GetTemplate(TemplateName="Fluid Flow").CreateSystem()')

    print()
    print('====================================================================================')
    print()
    print('n='+str(i+1))
    print('['+datetime.datetime.now().strftime('%F %T')+']\0'+name+'\0Workbench Initialized.')
    t0=time.time()

    # SCDM
    coWbUnit.execWbCommand('Geometry1 = system1.GetContainer(ComponentName="Geometry")')
    coWbUnit.execWbCommand('Geometry1.Edit(IsSpaceClaimGeometry=True)')
    SCDMscript=open(SCDMscriptname,"r",encoding='utf-8')
    SCDMcmd='d='+str(d)+'\n'+'NumberOfProcessors='+str(NumberOfProcessors)+'\n'+str(SCDMscript.read())
    coWbUnit.execWbCommand('SCDMcmd="""'+SCDMcmd+'"""')
    coWbUnit.execWbCommand('Geometry1.SendCommand(Language="Python",Command=SCDMcmd)')
    coWbUnit.execWbCommand('Geometry1.Exit()')
    print('['+datetime.datetime.now().strftime('%F %T')+']\0'+name+'\0SCDM Completed.')

    # Meshing
    coWbUnit.execWbCommand('MeshComponent1 = system1.GetComponent(Name="Mesh")')
    coWbUnit.execWbCommand('MeshComponent1.Refresh()')
    coWbUnit.execWbCommand('Mesh1 = system1.GetContainer(ComponentName="Mesh")')
    coWbUnit.execWbCommand('Mesh1.Edit()')
    Meshscript=open(Meshscriptname,"r",encoding='utf-8')
    #Sizing of throat <=0.175mm
    if(d<=1.75):
        Meshcmd='mesh1 = Model.Mesh'+'\n'+'mesh1.NumberOfCPUsForParallelPartMeshing='+str(NumberOfProcessors)+'\n'+'d='+str(d)+'\n'+str(Meshscript.read())
    else:
        Meshcmd='mesh1 = Model.Mesh'+'\n'+'mesh1.NumberOfCPUsForParallelPartMeshing='+str(NumberOfProcessors)+'\n'+'d=1.75'+'\n'+str(Meshscript.read())
    coWbUnit.execWbCommand('Meshcmd="""'+Meshcmd+'"""')
    coWbUnit.execWbCommand('Mesh1.SendCommand(Language="Python",Command=Meshcmd)')
    coWbUnit.execWbCommand('Mesh1.Exit()')
    coWbUnit.execWbCommand('MeshComponent1.Update(AllDependencies=True)')
    print('['+datetime.datetime.now().strftime('%F %T')+']\0'+name+'\0Meshing Completed.')
    
    coWbUnit.saveProject(workpath+"\\"+name+"\\"+wbpjname)
    os.mkdir(workpath+"\\"+name+"\\"+name+"_files"+"\\dp0\\FFF\\Fluent")
    # Fluent
    source = "output_residual.jou"
    target = workpath+"\\"+name+"\\"+name+"_files"+"\\dp0\\FFF\\Fluent"
    shutil.copy(source, target)
    source2 = "residuals.dat"
    shutil.copy(source2, target)

    coWbUnit.execWbCommand('setupComponent1 = system1.GetComponent(Name="Setup")')
    coWbUnit.execWbCommand('setupComponent1.Refresh()')
    coWbUnit.execWbCommand('setup1 = system1.GetContainer(ComponentName="Setup")')
    coWbUnit.execWbCommand('fluentLauncherSettings1 = setup1.GetFluentLauncherSettings()')
    coWbUnit.execWbCommand('fluentLauncherSettings1.SetEntityProperties(Properties=Set(Precision="Double", EnvPath={}, RunParallel=True, NumberOfProcessors='+str(NumberOfProcessors)+', NumberOfGPGPUs=1))')
    coWbUnit.execWbCommand('setup1.Edit()')
    Fluentscript=open(Fluentscriptname,"r",encoding='utf-8')
    Fluentline=Fluentscript.readline()
    while Fluentline:
        Fluentline=Fluentline.strip('\n')
        coWbUnit.execWbCommand('setup1.SendCommand("""'+Fluentline+'""")')
        Fluentline=Fluentscript.readline()
    #time.sleep(120)
    #if residual > 1e-05 , excute another journal to increase the iteration (up to 10000 iterations)
    
    fname_residuals = workpath+"\\"+name+"\\"+name+"_files"+"\\dp0\\FFF\\Fluent\\residuals.dat"
    fname_p_head = workpath+"\\"+name+"\\"+name+"_files"+"\\dp0\\FFF\\Fluent\\p-head-rfile.out"
    fname_d_mfr = workpath+"\\"+name+"\\"+name+"_files"+"\\dp0\\FFF\\Fluent\\diff-mfr-rfile.out"

    #lines of residuals.dat
    count = -1
    countnext=0
    while(1):
        count = -1
        for count, line in enumerate(open(fname_residuals, 'rb')):
            pass
        count += 1       
        if(countnext==count+1):
            print('['+datetime.datetime.now().strftime('%F %T')+']\0'+str(count-1)+' iterations completed.')
            break
        countnext=count+1
        time.sleep(30)       #Iteration time per step

    iteration=count
    i=0
    with open(fname_residuals, 'rb') as fr:      #open file
            with open(fname_p_head, 'rb') as fp:
                    with open(fname_d_mfr, 'rb') as fm:
                        while(True):
                            #residuals
                            off = -50                     #offset
                            while True:
                                fr.seek(off, 2)            #seek(off, 2)represents the file pointer: 50 characters (-50) forward from the end of the file (2)
                                lines = fr.readlines()     #Read all lines in the file pointer range
                                if len(lines)>=2:         #Determine whether there are at least two lines at the end, so as to ensure that the last line is complete
                                    last_line1 = lines[-1] #Take the last line
                                    break
                                #If the readlines obtained when off is 50, there is only one line of content, then there is no guarantee that the last line is complete
                                #So the off doubles and reruns until the readlines is more than one line
                                off *= 2
                            #d_mfr
                            off = -50                    
                            while True:
                                fm.seek(off, 2)            
                                lines = fm.readlines()     
                                if len(lines)>=2:         
                                    last_line2 = lines[-1] 
                                    break                            
                                off *= 2
                            #p_head
                            off = -50                    
                            while True:
                                fp.seek(off, 2)            
                                lines = fp.readlines()     
                                if len(lines)>=2:         
                                    last_line3 = lines[-1] 
                                    break                            
                                off *= 2
                            a=last_line1.split()
                            b=last_line2.split()
                            c=last_line3.split()
                            print()
                            print('iterations= '+str(iteration))
                            print('continuity= {:.4e}'.format(float(a[0])))
                            print('x-velocity= {:.4e}'.format(float(a[1])))
                            print('y-velocity= {:.4e}'.format(float(a[2])))
                            print('z-velocity= {:.4e}'.format(float(a[3])))
                            print('         k= {:.4e}'.format(float(a[4])))	
                            print('     omega= {:.4e}'.format(float(a[5])))
                            print(' delta mfl= {:.4e}'.format(float(b[1])))  #delta mass flow
                            print('    p-head= {:.4e} Pa'.format(float(c[1])))
                            print('          = {:.4e} mmHg'.format(float(c[1])*0.0075))
                            print()
                            if(i==4):
                                break
                            if(((float(b[1])-1)>1e-05 and float(a[0])>1e-05) or ((float(b[1])-1)>1e-05 and float(a[0])<=1e-05) or float(a[1])>1e-05 or float(a[2])>1e-05 or float(a[3])>1e-05 or float(a[4])>1e-05 or float(a[5])>1e-05):
                                print('Not converged, add 2000 iterations.')
                                Additerationscript=open(Additerationscriptname,"r",encoding='utf-8')
                                Additerationcmd=Additerationscript.readline()
                                while Additerationcmd:
                                    Additerationcmd=Additerationcmd.strip('\n')
                                    coWbUnit.execWbCommand('setup1.SendCommand(Command="""'+Additerationcmd+'""")')
                                    Additerationcmd=Additerationscript.readline()
                                Additerationscript.close()
                                i+=2
                                count = -1
                                while(1):
                                    count = -1
                                    for count, line in enumerate(open(fname_residuals, 'rb')):
                                        pass
                                    count += 1
                                    if(countnext==count+1):
                                        print('['+datetime.datetime.now().strftime('%F %T')+']\0'+str(count-i)+' iterations completed.')
                                        break
                                    countnext=count+1
                                    time.sleep(30)          #Iteration time per step
                                iteration+=(count-i)
                            else:
                                print('Converged.')
                                break

    with open(fname_residuals, 'rb') as fr:   
         off = -50                     
         while True:
             fr.seek(off, 2)            
             lines = fr.readlines()     
             if len(lines)>=2:         
                 last_line1 = lines[-1] 
                 break                
             off *= 2
         a=last_line1.split()
    with open(fname_d_mfr, 'rb') as fm:   
         off = -50                     
         while True:
             fm.seek(off, 2)            
             lines = fm.readlines()     
             if len(lines)>=2:         
                 last_line2 = lines[-1] 
                 break                
             off *= 2
         b=last_line2.split()
    if(((float(b[1])-1)>1e-05 and float(a[0])>1e-05) or ((float(b[1])-1)>1e-05 and float(a[0])<=1e-05) or float(a[1])>1e-05 or float(a[2])>1e-05 or float(a[3])>1e-05 or float(a[4])>1e-05 or float(a[5])>1e-05):
        print('['+datetime.datetime.now().strftime('%F %T')+']\0'+'---Not converged---')
        shutil.move(workpath+"\\"+name,workpath+"\\"+name+"Not converged")

    coWbUnit.execWbCommand('setup1.Exit()')
    print('['+datetime.datetime.now().strftime('%F %T')+']\0'+name+'\0Fluent Completed.')

    #Save
    coWbUnit.saveProject(workpath+"\\"+name+"\\"+wbpjname)
    coWbUnit.finalize()
    print('['+datetime.datetime.now().strftime('%F %T')+']\0'+name+'\0Save Completed.')
    print()    
    t1=time.time()
    deltat=int(t1)-int(t0) 
    ET=datetime.timedelta(seconds=deltat)
    ETA=datetime.timedelta(seconds=deltat*(int(n)-int(i)-1))
    print(str(((i+1)/int(n))*100)+'% ('+str(i+1)+'of'+n+') [Elapsed Time:'+str(ET)+'] [ETA: '+str(ETA)+']')
    i+=1

print()
print('====================================================================================')
print()
print('['+datetime.datetime.now().strftime('%F %T')+'] Work is completed.')

#exit
replacement(Fluentscriptname, MaterialDir, var1) #change the script to origin
os.system("pause")
print("The program will exit in ten seconds.")
time.sleep(10)
sys.exit()

