import sys
import xml.etree.cElementTree

setfile=sys.path[0]+'//settings.xml'
updateTree = xml.etree.cElementTree.parse(setfile) 
root = updateTree.getroot()
isset=root.find('is_seted')
isset.text = 'False'
updateTree.write(setfile)