from sys import argv
import glob
import pickle
from collections import defaultdict

def main():
	'''Usage: ./Triple.py'''
	input_list=glob.glob("Train-corpus/*/*.txt")
	triple_count_dict=defaultdict(lambda :0)
	for istr in input_list:
		with open(istr) as f:
			line=f.read()
		words = line.split()
		tags = [word.split('_')[1] for word in words]
		for i in range(len(tags)-2):
			for triple in ((x,y,z) for x in tags[i].split('-') for y in tags[i+1].split('-') for z in tags[i+2].split('-')):
				triple_count_dict[triple] += 1

	with open('res/triple.pkl', 'wb') as f:
		pickle.dump(dict(triple_count_dict), f, pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    main()
