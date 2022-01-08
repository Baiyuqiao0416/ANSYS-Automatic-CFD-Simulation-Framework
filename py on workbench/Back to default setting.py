import sys
import xml.etree.cElementTree

setfile=sys.path[0]+'//settings.xml'
def xml_changedata(dir,tagname,tagtext):
    updateTree = xml.etree.cElementTree.parse(dir) 
    root = updateTree.getroot()
    tag=root.find(tagname)
    tag.text = tagtext
    updateTree.write(dir)

xml_changedata(setfile,'workbench_dir','default_workbench_dir')
xml_changedata(setfile,'material_database_dir','defaule_material_database_dir')
xml_changedata(setfile,'is_seted','False')

Fluentscript=open('FLUENT_Script.scm','r+')
fs=Fluentscript.readlines()
fs[16]='material database dir\n'
Fluentscript=open('FLUENT_Script.scm','w+')
Fluentscript.writelines(fs)

print('Back to default setting is completed.')
print('Press any key to continue...')
input()
sys.exit()