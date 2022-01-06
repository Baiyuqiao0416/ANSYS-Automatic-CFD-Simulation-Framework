import os
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

print('Back to default setting is conpleted.')
os.system('pause')