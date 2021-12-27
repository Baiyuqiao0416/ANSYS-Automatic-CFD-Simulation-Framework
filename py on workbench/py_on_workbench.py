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
print('                    Automated Resistance Valve Simulation System                    ')
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
WorkbenchDir=r'D:\Program Files\ANSYS Inc\v194'  #change the workbench dir
in_content="N"
while(in_content!="Y"):
    workpath = input("Please define the work path:")   
    d0 = input("Please define the initial d 'd0':")
    step = input("Please define the delta d 'step':")
    n = input("Please define the number of caculation 'n':")
    print()
    print("Please make sure the following content is correct, press 'Y' if it is correct")
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
Fluentscriptname='FLUENT_Script.jou'
Additerationscriptname='Add_Iteration_Script.jou'

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
    print('['+datetime.datetime.now().strftime('%F %T')+']\0'+name+'\0Workbench Initialized')
    t0=time.time()

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
    #Sizing of throat <=0.175mm
    if(d<=1.75):
        Meshcmd='mesh1 = Model.Mesh'+'\n'+'mesh1.NumberOfCPUsForParallelPartMeshing='+str(NumberOfProcessors)+'\n'+'d='+str(d)+'\n'+str(Meshscript.read())
    else:
        Meshcmd='mesh1 = Model.Mesh'+'\n'+'mesh1.NumberOfCPUsForParallelPartMeshing='+str(NumberOfProcessors)+'\n'+'d=1.75'+'\n'+str(Meshscript.read())
    coWbUnit.execWbCommand('Meshcmd="""'+Meshcmd+'"""')
    coWbUnit.execWbCommand('Mesh1.SendCommand(Language="Python",Command=Meshcmd)')
    coWbUnit.execWbCommand('Mesh1.Exit()')
    coWbUnit.execWbCommand('MeshComponent1.Update(AllDependencies=True)')
    print('['+datetime.datetime.now().strftime('%F %T')+']\0'+name+'\0Meshing Complete')
    
    # Fluent
    source = "output_residual.jou"
    target = workpath+"\\"+name+"\\"+name+"_files"+"\\dp0\\FFF\\Fluent"
    shutil.copy(source, target)

    coWbUnit.execWbCommand('setupComponent1 = system1.GetComponent(Name="Setup")')
    coWbUnit.execWbCommand('setupComponent1.Refresh()')
    coWbUnit.execWbCommand('setup1 = system1.GetContainer(ComponentName="Setup")')
    coWbUnit.execWbCommand('fluentLauncherSettings1 = setup1.GetFluentLauncherSettings()')
    coWbUnit.execWbCommand('fluentLauncherSettings1.SetEntityProperties(Properties=Set(Precision="Double", EnvPath={}, RunParallel=True, NumberOfProcessors='+str(NumberOfProcessors)+', NumberOfGPGPUs=1))')
    coWbUnit.execWbCommand('setup1.Edit()')
    Fluentscript=open(Fluentscriptname,"r",encoding='utf-8')
    Fluentcmd=Fluentscript.read()
    coWbUnit.execWbCommand('Fluentcmd="""'+Fluentcmd+'"""')
    coWbUnit.execWbCommand('setup1.SendCommand(Language="Journal",Command=Fluentcmd)')

    #if residual > 1e-05 , excute another journal to increase the iteration (up to 10000 iterations)
    
    fname = workpath+"\\"+name+"\\"+name+"_files"+"\\dp0\\FFF\\Fluent\\residuals.dat"
    iteration=6000
    while(iteration<10000):
        with open(fname, 'rb') as f:  #打开文件
            off = -50      #设置偏移量
            while True:
                f.seek(off, 2) #seek(off, 2)表示文件指针：从文件末尾(2)开始向前50个字符(-50)
                lines = f.readlines() #读取文件指针范围内所有行
                if len(lines)>=2: #判断是否最后至少有两行，这样保证了最后一行是完整的
                    last_line = lines[-1] #取最后一行
                    break
                #如果off为50时得到的readlines只有一行内容，那么不能保证最后一行是完整的
                #所以off翻倍重新运行，直到readlines不止一行
                off *= 2
            a=last_line.split()
            print()
            print('iterations= '+str(iteration))
            print('continuity= {:.2e}'.format(float(a[0])))
            print('x-velocity= {:.2e}'.format(float(a[1])))
            print('y-velocity= {:.2e}'.format(float(a[2])))
            print('z-velocity= {:.2e}'.format(float(a[3])))
            print('         k= {:.2e}'.format(float(a[4])))	
            print('     omega= {:.2e}'.format(float(a[5])))
            print()
            if(float(a[0])>0.00001 or float(a[1])>0.00001 or float(a[2])>0.00001 or float(a[3])>0.00001 or float(a[4])>0.00001 or float(a[5])>0.00001):
                print('Not converged, add 2000 iterations')
                Additerationscript=open(Additerationscriptname,"r",encoding='utf-8')
                Additerationcmd=Additerationscript.read()
                coWbUnit.execWbCommand('Fluentcmd="""'+Additerationcmd+'"""')
                coWbUnit.execWbCommand('setup1.SendCommand(Language="Journal",Command=Fluentcmd)')
                iteration+=2000
            else:
                print('Converged')
                break

    coWbUnit.execWbCommand('setup1.Exit()')
    print('['+datetime.datetime.now().strftime('%F %T')+']\0'+name+'\0Fluent Complete')

    #Save
    coWbUnit.saveProject(workpath+"\\"+name+"\\"+wbpjname)
    coWbUnit.finalize()
    print('['+datetime.datetime.now().strftime('%F %T')+']\0'+name+'\0Save Complete')
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
print('['+datetime.datetime.now().strftime('%F %T')+'] Work is completed')

os.system("pause")
print("The program will exit in ten seconds.")
time.sleep(10)
sys.exit()

