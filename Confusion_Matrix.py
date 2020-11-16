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
	confusion_matrix=[[0] * N for _ in range(N)]

 
	input_list = [ i.strip('.pre.txt') for i in glob.glob("Test-corpus/*/*.pre.txt")]

	for ifile in input_list:
		given = ifile+'.pre.txt'
		pred = ifile+'.'+argv[-1]+'.tags'

		with open(given,'r') as ifile:
			givenstr = ifile.read()
		with open(pred,'r') as ifile:
			predstr = ifile.read()

		actual_tag_set=[wt.split('_')[1] for wt in givenstr.split()]
		predi_tag_set=predstr.split()

	

		for i,tag in enumerate(predi_tag_set):
			#breakpoint()
			if("-" in actual_tag_set[i]):
				tags=actual_tag_set[i].split('-')
				confusion_matrix[pos.index(tags[0])][pos.index(tag)]+=0.5
				confusion_matrix[pos.index(tags[1])][pos.index(tag)]+=0.5
			else:
				confusion_matrix[pos.index(actual_tag_set[i])][pos.index(tag)]+=1

	save_obj(confusion_matrix,"res/"+argv[-1]+".conf.pkl")
if __name__ == '__main__':
	main()
