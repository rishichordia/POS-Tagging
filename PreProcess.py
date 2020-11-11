import xml.etree.ElementTree as ET 
from sys import argv

def main():
	'''Usage: ./PreProcess.py input.xml output.txt '''
	source=argv[1]
	destination=argv[2]
	parser = ET.XMLParser(encoding = 'utf-8')
	tree = ET.parse(source,parser)

	root = tree.getroot()
	output = open(destination,"w")
	for element in root.iter('*') :
		if element.tag=='w' or element.tag=='c':
				text=element.text
				if text is None: continue
				text = text.strip().replace(' ','~')
				text+="_"
				text+=element.attrib['c5'].strip()
				text+=" "
				output.write(text)


if __name__ == '__main__':
	main()
