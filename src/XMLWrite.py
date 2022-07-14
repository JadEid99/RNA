import xml.etree.ElementTree as ET
from Operations import *

def XMLWrite(EditScript, A, B):
    data = ET.Element('ES')

    acc = ET.SubElement(data, 'ACC')
    ET.SubElement(acc, 'A').text = A[0]
    ET.SubElement(acc, 'B').text = B[0]

    OPs = ET.SubElement(data, 'Operations')

    for operation in EditScript:
        currentOP = 0
        if type(operation) is Insert:
            currentOP = ET.SubElement(OPs, 'I')
            currentOP.set('I', str(operation.indexA))
            currentOP.set('L', str(operation.letter))
        elif type(operation) is Delete:
            currentOP = ET.SubElement(OPs, 'D')
            currentOP.set('I', str(operation.indexA))
        elif type(operation) is Update:
            currentOP = ET.SubElement(OPs, 'U')
            currentOP.set('I', str(operation.indexA))
            currentOP.set('L', str(operation.letter))

    mydata = ET.tostring(data)
    myfile = open("EditScript.xml", "w", encoding="UTF-8")
    myfile.write(mydata.decode())

def EStoString(EditScript, A, B):
    data = ET.Element('ES')

    acc = ET.SubElement(data, 'ACC')
    ET.SubElement(acc, 'A').text = A[0]
    ET.SubElement(acc, 'B').text = B[0]

    OPs = ET.SubElement(data, 'Operations')

    for operation in EditScript:
        currentOP = 0
        if type(operation) is Insert:
            currentOP = ET.SubElement(OPs, 'I')
            currentOP.set('I', str(operation.indexA))
            currentOP.set('L', str(operation.letter))
        elif type(operation) is Delete:
            currentOP = ET.SubElement(OPs, 'D')
            currentOP.set('I', str(operation.indexA))
        elif type(operation) is Update:
            currentOP = ET.SubElement(OPs, 'U')
            currentOP.set('I', str(operation.indexA))
            currentOP.set('L', str(operation.letter))
        elif type(operation) is FakeUpdate:
            currentOP = ET.SubElement(OPs, 'F')
            currentOP.set('I', str(operation.indexA))
            currentOP.set('L', str(operation.letter))

    return ET.tostring(data).decode()
