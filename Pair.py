from sys import argv
import glob
import pickle

def main():
	'''Usage: ./Pair.py'''
	input_list=glob.glob("Train-corpus/*/*.txt")
	pair_count_dict={}
	for istr in input_list:
		with open(istr) as f:
			line=f.read()
		words = line.split()
		tags = [word.split('_')[1] for word in words]
		for i in range(len(tags)-1): #TODO: Multiple tags?
			for pair in ((x,y) for x in tags[i].split('-') for y in tags[i+1].split('-')):
				if pair not in pair_count_dict:
					pair_count_dict[pair] = 0
				pair_count_dict[pair] += 1

	with open('res/pair.pkl', 'wb') as f:
		pickle.dump(pair_count_dict, f, pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    main()
