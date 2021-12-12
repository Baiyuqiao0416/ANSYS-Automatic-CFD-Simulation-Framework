# -*- coding: utf-8 -*-
from PyWbUnit import CoWbUnitProcess

workpath="E:\OneDrive - stu.suda.edu.cn\Resistance Valve\test2"
# 创建wb单元实例，指定ansys wb版本
coWbUnit = CoWbUnitProcess(workDir=r'D:\Program Files\ANSYS Inc\v194', version=194, interactive=True)
coWbUnit.initialize()
coWbUnit.execWbCommand('SetScriptVersion(Version="19.4.159")')
coWbUnit.execWbCommand('system1 = GetTemplate(TemplateName="Fluid Flow").CreateSystem()')
coWbUnit.execWbCommand('geometry1 = system1.GetContainer(ComponentName="Geometry")')
coWbUnit.execWbCommand('geometry1.Edit(IsSpaceClaimGeometry=True)')

#SCDM
scdmscript=open("E:/OneDrive - stu.suda.edu.cn/Resistance Valve/test2/SCDM_Script.py","r",encoding='utf-8')
scdmcmd=scdmscript.read()
coWbUnit.execWbCommand('scdmcmd="""'+scdmcmd+'"""')
coWbUnit.execWbCommand('geometry1.SendCommand(Language="Python",Command=scdmcmd)')

# Save File###有问题 需要解决
#coWbUnit.execWbCommand('geometry1.SendCommand(DocumentSave.Execute("E:\OneDrive - stu.suda.edu.cn\Resistance Valve\test2\ID_16.scdoc", ExportOptions.Create()))')

coWbUnit.execWbCommand('geometry1.Exit()')
#coWbUnit.saveProject(workpath)
#mesh
coWbUnit.execWbCommand('meshComponent1 = system1.GetComponent(Name="Mesh")')
coWbUnit.execWbCommand('meshComponent1.Refresh()')
coWbUnit.execWbCommand('mesh1 = system1.GetContainer(ComponentName="Mesh")')
coWbUnit.execWbCommand('mesh1.Edit()')
