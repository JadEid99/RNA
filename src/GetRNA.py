from xml.dom import minidom
from xml.etree.ElementTree import ElementTree

mydoc = ElementTree(file='Database.xml')


def GetRNA(s1, s2):
    RNA = []

    e = mydoc.findall('/S' + str(s1))[0]

    RNA.append(["", 'piR-hsa-' + e.get('N'), e.text, len(e.text)])

    e = mydoc.findall('/S' + str(s2))[0]

    RNA.append(["", 'piR-hsa-' + e.get('N'), e.text, len(e.text)])

    return RNA
# Database = minidom.parse('Database.xml')

# accessions = Database.getElementsByTagName('Accession' + str(s1))
# sequences = Database.getElementsByTagName('Sequence')
# organism = Database.getElementsByTagName('Organism')
# length = Database.getElementsByTagName('Length')
#
# RNA.append([accessions[0].attributes['Accession'].value, organism[s1].childNodes[0].data, sequences[s1].childNodes[0].data, int(length[s1].childNodes[0].data)])
#
# accessions = Database.getElementsByTagName('Accession' + str(s2))
#
# RNA.append([accessions[0].attributes['Accession'].value, organism[s2].childNodes[0].data, sequences[s2].childNodes[0].data, int(length[s2].childNodes[0].data)])

# sequences = Database.getElementsByTagName('Sequence')
# Names = Database.getElementsByTagName('S' + str(s1))
# RNA.append(["", 'piR-hsa-' + Names[0].attributes['N'].value, sequences[s1].childNodes[0].data,
#             len(sequences[s1].childNodes[0].data)])
#
# Names = Database.getElementsByTagName('S' + str(s2))
# RNA.append(["", 'piR-hsa-' + Names[0].attributes['N'].value, sequences[s2].childNodes[0].data,
#             len(sequences[s2].childNodes[0].data)])
#
# return RNA
