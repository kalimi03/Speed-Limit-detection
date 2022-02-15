from lxml import etree
import numpy as numpy
import os


path = r'D:\trafficSignDetection\data\TraindatasetforSSD'
file_list = os.listdir(path)
for file_name in file_list:
    #file_name = '00123(1)B3.xml'
    if (file_name[-4:] == '.xml'):
        file_path = path + '\\' + file_name
        root = etree.parse(file_path)
        root = root.getroot()
        #root.append(etree.Element('?xml', version="1.0"))
        objects = root.findall('object')
        cntr = 0
        lenn = len(objects)
        for i in range(0, lenn):
            object = objects[cntr]
            name = object.find('name').text
            #print(name)
            if( (len(name[:-3]) >= 11) and (name[0:11] == 'Speed Limit') ):
                cntr += 1
            else:
                objects.remove(object)
                object.getparent().remove(object)
        if (len(objects) == 0):
            try:
                os.remove(path + '\\' + file_name)
            except:
                print('did not deleted xml: ' + file_name)
            try:
                os.remove(path + '\\' + file_name[:-4] + '.jpg')
            except:
                print('did not deleted jpg: ' + file_name)
            try:
                os.remove(path + '\\' + file_name[:-4] + '.png')
            except:
                print('did not deleted png: ' + file_name)
        else:
            f = open(file_path, 'w')
            f.write("<?xml version=" + "\"" + str(1.0) + "\"" + " ?>")
            f.close()

            f = open(file_path, 'ab')
            f.write(etree.tostring(root))
            f.close()