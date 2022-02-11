import os
import sys
import xml.etree.cElementTree
try:
    #setfile=sys.path[0]+'//settings.xml'
    setfile='settings.xml'
    def xml_changedata(dir,tagname,tagtext):
        updateTree = xml.etree.cElementTree.parse(dir) 
        root = updateTree.getroot()
        tag=root.find(tagname)
        tag.text = tagtext
        updateTree.write(dir)

    xml_changedata(setfile,'workbench_dir','default_workbench_dir')
    xml_changedata(setfile,'material_database_command','default_material_database_command')
    xml_changedata(setfile,'mass_flow_command','default_mass_flow_command')
    xml_changedata(setfile,'is_seted','False')

    Fluentscript=open('FLUENT_output_cas.scm','r+')
    fs=Fluentscript.readlines()
    fs[16]='material_database_command\n'
    fs[36]='mass_flow_command\n'
    Fluentscript=open('FLUENT_output_cas.scm','w+')
    Fluentscript.writelines(fs)
except Exception as e:
    print(e)
    os.system("pause")
finally:
    print('Back to default setting is completed.')
    print('Press any key to continue...')
    input()
    sys.exit()