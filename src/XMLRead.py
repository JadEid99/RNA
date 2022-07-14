import xml.etree.ElementTree as ET

def parser(xmlfile):
    tree = ET.parse(xmlfile)

    elemList = []
    attList = []
    i = 0
    for elem in tree.iter():
        if i < 5:
            i = i + 1
            continue
        else:
            elemList.append(elem.tag)
            attList.append(elem.attrib)

    return elemList, attList

