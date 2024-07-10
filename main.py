'''
author: arunkumar-js25
'''
import xml.etree.cElementTree as ET

def rootIterator(root,countParam=1,intent="    "):
    result = root.tag
    for ite in root.findall("./*"):
        result = result +"\n" + intent*countParam + ite.tag
        ite2list = ite.findall("./*")
        for ite2 in ite2list:
            result = result + "\n" + intent*(countParam+1) + rootIterator(ite2,countParam+2)
    return result

def saveTxtOutput(result,output_filepath=r"D:\output.txt"):
    with open(output_filepath, "w") as text_file:
        text_file.write(result)

def ak_xml_parser(inputXML_filename):
    tree = ET.parse(inputXML_filename)
    return tree.getroot()


if __name__ == "__main__":
    root = ak_xml_parser(r"C:\Users\Arun Kumar\Downloads\XXXX.xml")
    result = rootIterator(root, countParam=1, intent="    ")