import numpy as np 
import matplotlib.pyplot as plt 
from sys import argv
from operator import itemgetter

Dict={}
word_count={}
tag_count={}

def makeDict(input):
 	file=open(input,"r")
 	line=list(file)[0]
 	for comb in line.split():
 		element=comb.split("_")
 		word=element[0].lower()
 		tag=element[1]
 		if tag in ["PUL","PUN","PUQ","PUR"]:
 			continue

 		if word in Dict:
 			if tag in Dict[word]:
 				Dict[word][tag]+=1
 			else:
 				Dict[word][tag]=1
 			word_count[word]+=1	
 		else:
 			Dict[word]={}
 			Dict[word][tag]=1
 			word_count[word]=1
 		if tag in tag_count :
 			tag_count[tag]+=1
 		else:
 			tag_count[tag]=1

def printMax():
	Words=dict(sorted(word_count.items(), key = itemgetter(1), reverse = True)[:10])
	Tags=dict(sorted(tag_count.items(), key = itemgetter(1), reverse = True)[:10])
	fig = plt.figure(figsize = (10, 5))
	plt.bar(Words.keys(),Words.values(),color='blue',width=0.2)
	plt.xlabel("Word")
	plt.ylabel("Frequency of word")
	plt.title("Top 10 Words")

	fig2 = plt.figure(figsize = (10, 5))
	plt.bar(Tags.keys(),Tags.values(),color='blue',width=0.2)
	plt.xlabel("Tags")
	plt.ylabel("Frequency of tags")
	plt.title("Top 10 Tags")
	plt.show()


def main():
 '''Usage: ./Dict.py input.txt '''
 inputFile=argv[1]
 makeDict(inputFile)
 printMax()

if __name__ == '__main__':
    main()

