import pandas as PD
import xml.etree.ElementTree as ET

DataBase = PD.read_csv("DATABASE.csv", header=None, skiprows=[0])

data = ET.Element('Database')

for i in range(len(DataBase.index)):
    Name = ET.SubElement(data, "S" + str(i))
    Name.set('N', str(DataBase.iloc[i, 0][8:]))
    Name.text = str(DataBase.iloc[i, 4])

mydata = ET.tostring(data)
myfile = open("Database.xml", "w", encoding="UTF-8")
myfile.write(mydata.decode())
