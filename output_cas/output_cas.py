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
import psutil 
import decimal
import datetime
import platform
import linecache
import fileinput
import xml.dom.minidom
import xml.etree.cElementTree
from  distutils import util
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

#cpu usage
def cpu_usage():
    while True:                   
        cpu = psutil.cpu_percent(interval=0.1)   
        return float(cpu)

#xml
def xml_getdata(dir,tagname):
    file = xml.dom.minidom.parse(dir)
    tagtext=file.getElementsByTagName(tagname)
    tagtext1=tagtext[0]
    return tagtext1.firstChild.data.strip('\n')
def xml_changedata(dir,tagname,tagtext):
    updateTree = xml.etree.cElementTree.parse(dir) 
    root = updateTree.getroot()
    tag=root.find(tagname)
    tag.text = tagtext
    updateTree.write(dir)

#last line
def get_last_line(filedir):
    file=open(filedir, 'rb')
    off = -50                     #offset
    while True:
        file.seek(off, 2)            #seek(off, 2)represents the file pointer: 50 characters (-50) forward from the end of the file (2)
        lines = file.readlines()     #Read all lines in the file pointer range
        if len(lines)>=2:         #Determine whether there are at least two lines at the end, so as to ensure that the last line is complete
            last_line = lines[-1] #Take the last line
            break
        #If the readlines obtained when off is 50, there is only one line of content, then there is no guarantee that the last line is complete
        #So the off doubles and reruns until the readlines is more than one line
        off *= 2
    file.close()
    return last_line.split()

#replace specific line
def replacement(file, previousw, nextw):
   for line in fileinput.input(file, inplace=1):
       line = line.replace(previousw, nextw)
       sys.stdout.write(line)

#count the total lines
def count_lines(file):
    count = -1
    for count, line in enumerate(open(file, 'rb')):
        pass
        count += 1
    return count

#if last_phead <±5 than the previous one
def compare_last10_phead(file):
    count = count_lines(file)
    i=10
    j=0    
    while(i>0):
        text1=linecache.getline(file,count-i).split()
        text2=linecache.getline(file,count-i+1).split()
        p1=float(text1[1])
        p2=float(text2[1])
        dp=p2-p1
        if(dp<5.0 and dp>-5.0):
            j+=1
        i-=1
    if(j==10):
        return True
    else:
        return False

#Determine whether the calculation is complete
def wait_caculation():
    while(True):
        cpu_percent=cpu_usage()
        if(cpu_percent < 90.0 and cpu_percent != 0.0):
            break
        else:
            time.sleep(120)

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
print('                         Automatic CFD Simulation Framework                         ')
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

#xml settings
setfile=sys.path[0]+'//settings.xml'
#get flag
flag=bool(util.strtobool(xml_getdata(setfile,'is_seted')))
if(flag):
    print()
    print('                             Initial setup is completed.                            ')
    print()
    print('====================================================================================')
while(not flag):
    print()
    print('Please define the workbench path:')
    workbench_dir=input()
    print('Please define the material database path:')
    material_database_dir0=input()
    print()
    print('Initial setup is completed.')
    print()
    print('====================================================================================')
    material_database_dir='(cx-gui-do cx-set-text-entry "Open Database*TextEntry1(Database Name)" "'+ material_database_dir0.replace('\\','/') +'/blood.scm")'
    xml_changedata(setfile,'workbench_dir',workbench_dir)
    xml_changedata(setfile,'material_database_dir',material_database_dir)
    xml_changedata(setfile,'is_seted','True')
    #get flag
    flag=bool(util.strtobool(xml_getdata(setfile,'is_seted')))

#get two dir 
WorkbenchDir = str(xml_getdata(setfile,'workbench_dir'))
MaterialDir = str(xml_getdata(setfile,'material_database_dir'))

# Fluent setting
NumberOfProcessors=int(cpu_count())-2
NumberOfGPGPUs='1'

# Work setting
# Use relative paths instead
SCDMscriptname='SCDM_Script.py' 
Meshscriptname='MESH_Script.py'
Fluentscriptname='FLUENT_output_cas.scm'  

#change fluentscript
var1 = "material database dir"
replacement(Fluentscriptname, var1, MaterialDir)

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
print('                                  Initializing....                                  ')
print()
print('====================================================================================')

if not os.path.exists(workpath+"\\cas&dat"):
    os.mkdir(workpath+"\\cas&dat")
# loop
i=0
while(i<int(n)):
    try:
        d=decimal.Decimal(d0)+decimal.Decimal(step)*decimal.Decimal(i)
        name=str(i+1)+"_"+str(d)+"mm"
        wbpjname=name+".wbpj "
        if not os.path.exists(workpath+"\\"+name):
            os.mkdir(workpath+"\\"+name)
        
        # Create an instance of the wb unit and specify the ansys wb version
        coWbUnit = CoWbUnitProcess(WorkbenchDir, version=194, interactive=True) 
        coWbUnit.initialize()
        time.sleep(60)
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
        SCDMscript.close()
        print('['+datetime.datetime.now().strftime('%F %T')+']\0'+name+'\0SCDM Completed.')

        # Meshing
        coWbUnit.execWbCommand('MeshComponent1 = system1.GetComponent(Name="Mesh")')
        coWbUnit.execWbCommand('MeshComponent1.Refresh()')
        coWbUnit.execWbCommand('Mesh1 = system1.GetContainer(ComponentName="Mesh")')
        coWbUnit.execWbCommand('Mesh1.Edit()')
        Meshscript=open(Meshscriptname,"r",encoding='utf-8')
        #Sizing of throat <=0.13125mm (0.075d)
        if(d<=1.75):
            Meshcmd='mesh1 = Model.Mesh'+'\n'+'mesh1.NumberOfCPUsForParallelPartMeshing='+str(NumberOfProcessors)+'\n'+'d='+str(d)+'\n'+str(Meshscript.read())
        else:
            Meshcmd='mesh1 = Model.Mesh'+'\n'+'mesh1.NumberOfCPUsForParallelPartMeshing='+str(NumberOfProcessors)+'\n'+'d=1.75'+'\n'+str(Meshscript.read())
        coWbUnit.execWbCommand('Meshcmd="""'+Meshcmd+'"""')
        coWbUnit.execWbCommand('Mesh1.SendCommand(Language="Python",Command=Meshcmd)')
        coWbUnit.execWbCommand('Mesh1.Exit()')
        coWbUnit.execWbCommand('MeshComponent1.Update(AllDependencies=True)')
        Meshscript.close()
        print('['+datetime.datetime.now().strftime('%F %T')+']\0'+name+'\0Meshing Completed.')
        
        try:
            coWbUnit.saveProject(workpath+"\\"+name+"\\"+wbpjname)
            os.mkdir(workpath+"\\"+name+"\\"+name+"_files"+"\\dp0\\FFF\\Fluent")
            # Fluent

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
            Fluentscript.close()

            #exit fluent
            coWbUnit.execWbCommand('setup1.Exit()')
            print('['+datetime.datetime.now().strftime('%F %T')+']\0'+name+'\0Fluent Completed.')

        except Exception as e1:
            print()
            print(e1)
            print('['+datetime.datetime.now().strftime('%F %T')+'] Fluent exception!')
            print()

        finally:
            #Save
            coWbUnit.saveProject(workpath+"\\"+name+"\\"+wbpjname)
            coWbUnit.finalize()
            print('['+datetime.datetime.now().strftime('%F %T')+']\0'+name+'\0Save Completed.')
            print()

            #copy cas&dat to a new folder
            source = workpath+"\\"+name+"\\"+name+"_files"+"\\dp0\\FFF\\Fluent\\FFF-1.cas.gz"
            target = workpath+"\\cas&dat"
            shutil.copy(source, target)
            source2 = workpath+"\\"+name+"\\"+name+"_files"+"\\dp0\\FFF\\Fluent\\FFF-1-00000.dat.gz"
            shutil.copy(source2, target)

            renamesource=workpath+"\\cas&dat\\FFF-1.cas.gz"
            renametarget=workpath+"\\cas&dat\\"+name+".cas.gz"
            if os.path.exists(renamesource):
                os.rename(renamesource,renametarget)
            renamesource2=workpath+"\\cas&dat\\FFF-1-00000.dat.gz"
            renametarget2=workpath+"\\cas&dat\\"+name+".dat.gz"
            if os.path.exists(renamesource2):
                os.rename(renamesource2,renametarget2)
            
            t1=time.time()
            deltat=int(t1)-int(t0) 
            ET=datetime.timedelta(seconds=deltat)
            ETA=datetime.timedelta(seconds=deltat*(int(n)-int(i)-1))
            percentage=round(((i+1)/int(n))*100,2)
            print('\0'+str(percentage)+' % ( '+str(i+1)+' of '+n+' ) [ Elapsed Time: '+str(ET)+' ] [ ETA: '+str(ETA)+' ]')
            i+=1
    except Exception as e2:
        print()
        print(e2)
        print('['+datetime.datetime.now().strftime('%F %T')+'] Program exception!')
        print()


print()
print('====================================================================================')
print()
print('['+datetime.datetime.now().strftime('%F %T')+'] Work is completed.')
print()
print('====================================================================================')

#exit
replacement(Fluentscriptname, MaterialDir, var1) #change the script to origin
print()
print('Press any key to continue...')
input()
print("The program will terminate in ten seconds.")
time.sleep(10)
sys.exit()

