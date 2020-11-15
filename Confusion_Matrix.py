import pickle
import glob
from sys import argv
from os import path
from Viterbi import HMM
from Stat import load_obj,save_obj

stat = load_obj("res/stats.pkl")
N=len(stat[2])

def main():
	'''Usage: python3 Confusion_Matrix.py input.txt'''
	#input_list=glob.glob("Test-corpus/*/*.pre.txt")
	confusion_matrix=stat[3]
	if len(confusion_matrix)==0:
     confusion_matrix=[ [0] * N for _ in range(N)]
	pos=list(stat[2].keys())

	PredictTag=HMM()
 
	with open(argv[1],'r') as ifile:
		istring = ifile.read()

	s=""
	actual_tag_set=[]
	predi_tag_set=[]
	for word in istring.split():
		s=s+" "+word.split('_')[0]
		actual_tag_set.append(word.split('_')[1])
		if(word.split('_')[0] in ['.','!','?']):
			#print (s)
			predi_tag_set=PredictTag.viterbi(s)
			for i in range(len(predi_tag_set)):
				if("-" in actual_tag_set[i]):
					tags=actual_tag_set[i].split('-')
					if tags[0] == predi_tag_set[i]:
						confusion_matrix[pos.index(tags[0])][pos.index(predi_tag_set[i])]+=1
					elif tags[1] == predi_tag_set[i]:
						confusion_matrix[pos.index(tags[1])][pos.index(predi_tag_set[i])]+=1
					else:
						confusion_matrix[pos.index(tags[0])][pos.index(predi_tag_set[i])]+=1
						confusion_matrix[pos.index(tags[1])][pos.index(predi_tag_set[i])]+=1
				else:
					confusion_matrix[pos.index(actual_tag_set[i])][pos.index(predi_tag_set[i])]+=1
			s=""
			actual_tag_set=[]
			predi_tag_set=[]
	stat[3]=confusion_matrix
	save_obj(stats,"res/stats.pkl")
if __name__ == '__main__':
	main()
