import os
import sys
import xml.etree.cElementTree
try:
    setfile='settings.xml'
    def xml_changedata(dir,tagname,tagtext):
        updateTree = xml.etree.cElementTree.parse(dir) 
        root = updateTree.getroot()
        tag=root.find(tagname)
        tag.text = tagtext
        updateTree.write(dir)
    xml_changedata(setfile,'workbench_dir','default_workbench_dir')
    xml_changedata(setfile,'material_database_dir','default_material_database_dir')
    xml_changedata(setfile,'host','default_host')
    xml_changedata(setfile,'user','default_uesr')
    xml_changedata(setfile,'password','default_password')
    xml_changedata(setfile,'is_seted','False')
    Fluentscript=open('FLUENT_output_cas.scm','r+')
    fs=Fluentscript.readlines()
    fs[16]='material database dir\n'
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