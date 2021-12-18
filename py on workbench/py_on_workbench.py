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
import decimal
import datetime
import platform
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

print('System Information')
print()
print('Platform:'+platform.platform())
print('System Version:'+platform.version())
print('System Architecture:'+str(platform.architecture()))
print('Computer Name:'+platform.node())
print('Processor:'+platform.processor())
print('Number of logical processors:'+str(cpu_count()))
print()
print('================================================================================')

# Input parameters
WorkbenchDir=r'D:\Program Files\ANSYS Inc\v194'  #change the workbench dir
in_content="N"
while(in_content!="Y"):
    workpath = input("Please define the work path:")   
    d0 = input("Please define the initial d 'd0':")
    step = input("Please define the delta d 'step':")
    n = input("Please define the number of caculation 'n':")
    print('')
    print("Please make sure the following content is correct, press 'Y' if it is correct")
    print('')
    print('workpath='+workpath)
    print('d0='+d0)
    print('step='+step)
    print('n='+n)
    print()
    in_content=input()
    
print()
print("Initializing...")
print()

# Fluent setting
NumberOfCPUs=int(cpu_count())-2
NumberOfGPGPUs='1'

# Work setting
# Use relative paths instead
SCDMscriptname='SCDM_Script.py' 
Meshscriptname='MESH_Script.py'
Fluentscriptname='FLUENT_Script.jou'

# loop
i=0
while(i<int(n)):
    d=decimal.Decimal(d0)+decimal.Decimal(step)*decimal.Decimal(i)
    name=str(i)+"_"+str(d)+"mm"
    wbpjname=name+".wbpj "
    os.mkdir(workpath+"\\"+name)
    
    # Create an instance of the wb unit and specify the ansys wb version
    coWbUnit = CoWbUnitProcess(WorkbenchDir, version=194, interactive=True) 
    coWbUnit.initialize()
    coWbUnit.execWbCommand('SetScriptVersion(Version="19.4.159")')
    coWbUnit.execWbCommand('system1 = GetTemplate(TemplateName="Fluid Flow").CreateSystem()')

    print('================================================================================')
    print()
    print('n='+str(i+1))
    print('['+datetime.datetime.now().strftime('%F %T')+']\0'+name+'\0Workbench initialized')

    # SCDM
    coWbUnit.execWbCommand('Geometry1 = system1.GetContainer(ComponentName="Geometry")')
    coWbUnit.execWbCommand('Geometry1.Edit(IsSpaceClaimGeometry=True)')
    SCDMscript=open(SCDMscriptname,"r",encoding='utf-8')
    SCDMcmd='d='+str(d)+'\n'+'NumberOfProcessors='+str(NumberOfProcessors)+'\n'+str(SCDMscript.read())
    coWbUnit.execWbCommand('SCDMcmd="""'+SCDMcmd+'"""')
    coWbUnit.execWbCommand('Geometry1.SendCommand(Language="Python",Command=SCDMcmd)')
    coWbUnit.execWbCommand('Geometry1.Exit()')
    print('['+datetime.datetime.now().strftime('%F %T')+']\0'+name+'\0SCDM Complete')

    # Meshing
    coWbUnit.execWbCommand('MeshComponent1 = system1.GetComponent(Name="Mesh")')
    coWbUnit.execWbCommand('MeshComponent1.Refresh()')
    coWbUnit.execWbCommand('Mesh1 = system1.GetContainer(ComponentName="Mesh")')
    coWbUnit.execWbCommand('Mesh1.Edit()')
    Meshscript=open(Meshscriptname,"r",encoding='utf-8')
    Meshcmd='d='+str(d)+'\n'+str(Meshscript.read())
    coWbUnit.execWbCommand('Meshcmd="""'+Meshcmd+'"""')
    coWbUnit.execWbCommand('Mesh1.SendCommand(Language="Python",Command=Meshcmd)')
    coWbUnit.execWbCommand('Mesh1.Exit()')
    coWbUnit.execWbCommand('MeshComponent1.Update(AllDependencies=True)')
    print('['+datetime.datetime.now().strftime('%F %T')+']\0'+name+'\0Meshing Complete')
    
    # Fluent
    coWbUnit.execWbCommand('setupComponent1 = system1.GetComponent(Name="Setup")')
    coWbUnit.execWbCommand('setupComponent1.Refresh()')
    coWbUnit.execWbCommand('setup1 = system1.GetContainer(ComponentName="Setup")')
    coWbUnit.execWbCommand('NumberOfProcessors='+str(NumberOfProcessors))
    coWbUnit.execWbCommand('fluentLauncherSettings1 = setup1.GetFluentLauncherSettings()')
    coWbUnit.execWbCommand('fluentLauncherSettings1.SetEntityProperties(Properties=Set(Precision="Double", EnvPath={}, RunParallel=True, NumberOfProcessors=NumberOfProcessors, NumberOfGPGPUs=1))')
    coWbUnit.execWbCommand('setup1.Edit()')
    Fluentscript=open(Fluentscriptname,"r",encoding='utf-8')
    Fluentcmd=Fluentscript.read()
    coWbUnit.execWbCommand('Fluentcmd="""'+Fluentcmd+'"""')
    coWbUnit.execWbCommand('setup1.SendCommand(Language="Journal",Command=Fluentcmd)')
    coWbUnit.execWbCommand('setup1.Exit()')
    print('['+datetime.datetime.now().strftime('%F %T')+']\0'+name+'\0Fluent Complete')

    #Save
    coWbUnit.saveProject(workpath+"\\"+name+"\\"+wbpjname)
    coWbUnit.finalize()
    print('['+datetime.datetime.now().strftime('%F %T')+']\0'+name+'\0Save Complete')
    print()
    i+=1

print('['+datetime.datetime.now().strftime('%F %T')+'] Work is completed')