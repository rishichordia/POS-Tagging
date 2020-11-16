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
	'''Usage: python Predict.py input output [hmm/naive]'''

	if len(argv) != 4: 
		print("Need 4 args")
		exit()

	if argv[-1] == "hmm": PredictTag = HMM()
	if argv[-1] == "naive": PredictTag = Naive()

	ifile = argv[1]
	ofile = argv[2]
	with open(ifile,'r') as ifile:
		istring = ifile.read()
	output = open(ofile,'w')
	s=""
	predi_tag_set=[]
	for word in istring.split():
		s=s+" "+word.split('_')[0]
		if(word.split('_')[0] in ['.','!','?']):
			predi_tag_set=PredictTag.predict(s)
			output.write(' '.join(str(s) for s in predi_tag_set))
			output.write(' ')
			s=""
			predi_tag_set=[]
	output.close()
if __name__ == '__main__':
	main()
