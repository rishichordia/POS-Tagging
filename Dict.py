#! /usr/bin/python3
from sys import argv
def main():
 	'''Usage: ./Dict.py input.txt '''
 	input=argv[1]
 	file=open(input,"r")
 	dict={}
 	line=list(file)[0]
 	for comb in line.split():
 		element=comb.split("_")
 		word=element[0]
 		tag=element[1]
 		if word in dict:
 			if tag in dict[word]:
 				dict[word][tag]+=1
 			else:
 				dict[word][tag]=1	
 		else:
 			dict[word]={}
 			dict[word][tag]=1

 	print(dict)

if __name__ == '__main__':
    main()

