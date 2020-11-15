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
	confusion_matrix=[ [0] * N for _ in range(N)]
	pos=list(stat[2].keys())

	PredictTag=HMM()
	#breakpoint()
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

	Total=[0]*N
	TP=[0]*N
	FN=[0]*N
	FP=[0]*N
	Recall=[0]*N
	Precision=[0]*N
	for i in range(N):
		for j in range(N):
			if i==j:
				TP[i]+=confusion_matrix[i][j]
			else:
				FN[i]+=confusion_matrix[i][j]
				FP[j]+=confusion_matrix[i][j]
			Total[i]+=confusion_matrix[i][j]	
	print("Accuracy is:")
	print(sum(TP)/sum(Total))
	print("Recall is:")
	for i in range(N):Recall[i]=TP[i]/(TP[i]+FN[i])
	print(sum(Recall)/N)
	print("Precision is:")
	for i in range(N):Precision[i]=TP[i]/(TP[i]+FP[i])
	print(sum(Precision)/N)

	print("\n F-Score:")
	print(2/(1/sum(Recall)+1/sum(Precision)))


if __name__ == '__main__':
	main()
