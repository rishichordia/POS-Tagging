import pickle
import glob
from os import path
from sys import argv

def save_obj(obj, name ):
	with open(name, 'wb') as f:
		pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
	with open(name, 'rb') as f:
		return pickle.load(f)

def main():
	'''Usage: python Stat.py '''
	stats=({},{},{}) #Words tuple and tags tuple

	input_list=glob.glob("Train-corpus/*/*.dict.pkl")

	final_dict=stats[0]
	word_count=stats[1]
	tag_count=stats[2]


	for item in input_list:
		count_dict=load_obj(item)
		for word in count_dict:
			if word not in final_dict: final_dict[word] = {}
			if word not in word_count: word_count[word] = 0

			for tag in count_dict[word]:
				if tag not in final_dict[word]: final_dict[word][tag] = 0
				if tag not in tag_count: tag_count[tag] = 0

				final_dict[word][tag] += count_dict[word][tag]
				word_count[word] += count_dict[word][tag]
				tag_count[tag] += count_dict[word][tag]

	lfword_set = { w for w in word_count if word_count[w] == 1 }
	final_dict["UNK"] = {}  #Note clever usage of caps
	word_count["UNK"] = 0
	for lfword in lfword_set:
		assert len(final_dict[lfword]) == 1
		tag = list(final_dict[lfword])[0] 
		if tag not in final_dict["UNK"]: final_dict["UNK"][tag] = 0
		final_dict["UNK"][tag] += 1
		word_count["UNK"] += 1
		del final_dict[lfword]
		del word_count[lfword]


	save_obj(stats,"res/stats.pkl")

if __name__ == '__main__':
	main()
