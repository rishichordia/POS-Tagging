import pickle
import glob
from sys import argv
from os import path
from Viterbi import HMM
from Naive import Naive
from Stat import load_obj,save_obj

stat = load_obj("res/stats.pkl")
N=len(stat[2])

def main():
	'''Usage: python3 Confusion_Matrix.py [naive/hmm]'''

	if len(argv) != 2: 
		print("Need 2 args")
		exit()

	pos=list(stat[2].keys())
	N = len(pos)
	confusion_matrix=[[0] * N for _ in range(N)]

	if argv[-1] == "hmm": PredictTag = HMM()
	if argv[-1] == "naive": PredictTag = Naive()
 
	input_list = glob.glob("Test-corpus/*/*.pre.txt")

	for ifile in input_list:
		print(ifile)
		with open(ifile,'r') as ifile:
			istring = ifile.read()
		s=""
		actual_tag_set=[]
		predi_tag_set=[]
		for word in istring.split():
			s=s+" "+word.split('_')[0]
			actual_tag_set.append(word.split('_')[1])
			if(word.split('_')[0] in ['.','!','?']):
				predi_tag_set=PredictTag.predict(s)
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
	save_obj(confusion_matrix,"res/"+argv[-1]+".conf.pkl")
if __name__ == '__main__':
	main()
