# -*- coding: utf-8 -*-
# Based on ANSYS 2019R2
# Python 3.7 x64

#  ----------------------------------------------------------------------------------
# |                                                                                  |
# |  Copyright © 2021 by Yuqiao Bai & Xiangyu Zhao of AOT Lab in Soochow University  |
# |                                                                                  |
#  ----------------------------------------------------------------------------------

import datetime
import decimal
import fileinput
import linecache
import os
import platform
import shutil
import sys
import time
import xml.dom.minidom
import xml.etree.cElementTree
from distutils import util
from multiprocessing import cpu_count

import psutil  # Third package
from PyWbUnit import CoWbUnitProcess  # Third package

# Fluent setting
NumberOfProcessors=int(cpu_count())-2
NumberOfGPGPUs='1'

# Work setting
# Use relative paths instead
SCDMscriptname='SCDM_Script.py' 
Meshscriptname='MESH_Script.py'
Fluentscriptname='FLUENT_output_cas.scm'  

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

#replace specific line
def replacement(file, previousw, nextw):
   for line in fileinput.input(file, inplace=1):
       line = line.replace(previousw, nextw)
       sys.stdout.write(line)

#Create jou
def jou_create(path,msg):
    full_path = path + '\\journal.jou'  
    file = open(full_path, 'w')
    file.write(msg)
    file.close()
    
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
    #print('Please define the material database path:')
    material_database_dir0=sys.path[0]
    print()
    print('Initial setup is completed.')
    print()
    print('====================================================================================')
    material_database_command='(cx-gui-do cx-set-text-entry "Open Database*TextEntry1(Database Name)" "'+ material_database_dir0.replace('\\','/') +'/blood.scm")' 
    xml_changedata(setfile,'workbench_dir',workbench_dir)
    xml_changedata(setfile,'material_database_command',material_database_command)
    xml_changedata(setfile,'is_seted','True')
    #get flag
    flag=bool(util.strtobool(xml_getdata(setfile,'is_seted')))

# Input parameters
in_content="N"
while(in_content!="Y"):
    print("Please define the work path:")
    workpath = input()
    print('Please set the volume flow (LPM):')
    volume_flow=input()   
    print("Please define the initial d 'd0' (mm):")
    d0 = input()
    print("Please define the delta d 'step' (mm):")
    step = input()
    print("Please define the number of caculation 'n':")
    n = input()
    print()
    print("Please make sure the following content is correct, press 'Y' if it is correct.")
    print()
    print('workpath='+workpath)
    print('volume_flow='+volume_flow+' LPM')
    print('d0='+d0+' mm')
    print('step='+step+' mm')
    print('n='+n)
    print()
    in_content=input()
    
print('====================================================================================')
print()
print('                                  Initializing....                                  ')
print()
print('====================================================================================')


mass_flow_command="(cx-gui-do cx-set-expression-entry \"Mass-Flow Inlet*Frame3*Frame1(Momentum)*Table1*Table8*ExpressionEntry1(Mass Flow Rate)\" \'(\""+str(round(float(float(volume_flow)/60*1.055),5))+"\" . 0))"
xml_changedata(setfile,'mass_flow_command',mass_flow_command)
#get command 
WorkbenchDir = str(xml_getdata(setfile,'workbench_dir'))
MaterialCommand = str(xml_getdata(setfile,'material_database_command'))
MassFlowCommand = str(xml_getdata(setfile,'mass_flow_command'))

#change fluentscript
var1 = "material_database_command"
replacement(Fluentscriptname, var1, MaterialCommand)
var2 = "mass_flow_command"
replacement(Fluentscriptname, var2, MassFlowCommand)

if not os.path.exists(workpath+"\\cas_dat"):
    os.mkdir(workpath+"\\cas_dat")
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
        if(d<=1.25 and d>0.75):
            Meshcmd='mesh1 = Model.Mesh'+'\n'+'mesh1.NumberOfCPUsForParallelPartMeshing='+str(NumberOfProcessors)+'\n'+'d='+str(d)+'\n'+str(Meshscript.read())
        elif(d<=0.75):
            Meshcmd='mesh1 = Model.Mesh'+'\n'+'mesh1.NumberOfCPUsForParallelPartMeshing='+str(NumberOfProcessors)+'\n'+'d=0.75'+'\n'+str(Meshscript.read())    
        else:
            Meshcmd='mesh1 = Model.Mesh'+'\n'+'mesh1.NumberOfCPUsForParallelPartMeshing='+str(NumberOfProcessors)+'\n'+'d=1.25'+'\n'+str(Meshscript.read())
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

            #copy cas_dat to a new folder
            if not os.path.exists(workpath+"\\cas_dat\\"+name):
                os.mkdir(workpath+"\\cas_dat\\"+name)
            source = workpath+"\\"+name+"\\"+name+"_files"+"\\dp0\\FFF\\Fluent\\FFF-1.cas.gz"
            target = workpath+"\\cas_dat\\"+name
            shutil.copy(source, target)
            source2 = workpath+"\\"+name+"\\"+name+"_files"+"\\dp0\\FFF\\Fluent\\FFF-1-00000.dat.gz"
            shutil.copy(source2, target)
            source3 = "sub.slurm"
            shutil.copy(source3, target)
            source4 = "journal.jou"
            shutil.copy(source4, target)

            renamesource=workpath+"\\cas_dat\\"+name+"\\FFF-1.cas.gz"
            renametarget=workpath+"\\cas_dat\\"+name+"\\"+name+".cas.gz"
            if os.path.exists(renamesource):
                os.rename(renamesource,renametarget)
            renamesource2=workpath+"\\cas_dat\\"+name+"\\FFF-1-00000.dat.gz"
            renametarget2=workpath+"\\cas_dat\\"+name+"\\"+name+".dat.gz"
            if os.path.exists(renamesource2):
                os.rename(renamesource2,renametarget2)
            renamesource3=workpath+"\\cas_dat\\"+name+"\\sub.slurm"
            renametarget3=workpath+"\\cas_dat\\"+name+"\\zxy_"+name+".slurm"
            if os.path.exists(renamesource3):
                os.rename(renamesource3,renametarget3)
            
            #Create jou file
            full_path = workpath+"\\cas_dat\\"+name+"\\journal.jou"
            file = open(full_path, 'w')
            file.write("\n")
            file.write("/file/read-case/"+name+".cas.gz\n")
            file.write("/file/read-data/"+name+".dat.gz\n")
            file.write("/file/auto-save/case-frequency if-case-is-modified\n")
            file.write("/file/auto-save/data-frequency/700\n")
            file.write("/solve/set/transient-controls/duration-specification-method 1\n")
            file.write("/parallel/timer/reset\n")
            file.write("/solve/dual-time-iterate\n")
            file.write("2800\n")
            file.write("25\n")
            file.write("yes\n")
            file.write("yes\n")
            file.write("yes\n")
            file.write("yes\n")
            file.write("yes\n")
            file.write("yes\n")
            file.write("yes\n")
            file.write("yes\n")
            file.write("yes\n")
            file.write("yes\n")
            file.write("/parallel/timer/usage\n")
            file.write("/file/write-data\n")
            file.write(name+"_2800_final.dat.gz\n")
            file.write("/file/write-case\n")
            file.write(name+"_2800_final.cas.gz\n")
            file.write("/exit\n")
            file.write("yes")
            file.close()

            t1=time.time()
            deltat=int(t1)-int(t0) 
            ET=datetime.timedelta(seconds=deltat)
            ETA=datetime.timedelta(seconds=deltat*(int(n)-int(i)-1))
            percentage=round(((i+1)/int(n))*100,2)
            print('\0'+str(percentage)+' % ( '+str(i+1)+' of '+n+' ) [ Elapsed Time: '+str(ET)+' ] [ ETA: '+str(ETA)+' ]')
            
    except Exception as e2:
        print()
        print(e2)
        print('['+datetime.datetime.now().strftime('%F %T')+'] Program exception!')
        print()
    i+=1


print()
print('====================================================================================')
print()
print('['+datetime.datetime.now().strftime('%F %T')+'] Work is completed.')
print()
print('====================================================================================')

#exit
replacement(Fluentscriptname, MaterialCommand, var1) #change the script to origin
replacement(Fluentscriptname, MassFlowCommand, var2) #change the script to origin
print()
print('Press any key to continue...')
input()
print("The program will terminate in ten seconds.")
time.sleep(10)
sys.exit()

