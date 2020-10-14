import pickle
from os import path
from sys import argv

def save_obj(obj, name ):
	with open(name, 'wb') as f:
		pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
	with open(name, 'rb') as f:
		return pickle.load(f)

def main():
	'''Usage: ./Stat.py input.dict.pkl'''
	if path.exists("res/stats.pkl"):
		stats=load_obj("res/stats.pkl")
	else:
		stats=({},{},{}) #Words tuple and tags tuple
	final_dict=stats[0]
	word_count=stats[1]
	tag_count=stats[2]
	count_dict=load_obj(argv[1])
	for word in count_dict:
		for tag in count_dict[word]:
			if tag in tag_count:
				tag_count[tag]+=count_dict[word][tag]
			else:
				tag_count[tag]=count_dict[word][tag]
		if word in final_dict:
			for tag in count_dict[word]:
				if tag in final_dict[word]:
					final_dict[word][tag]+=count_dict[word][tag]
				else:
					final_dict[word][tag]=count_dict[word][tag]
				word_count[word]+=count_dict[word][tag]
		else:
			final_dict[word]=count_dict[word]
			word_count[word]=0
			for tag in count_dict[word]:
				word_count[word]+=count_dict[word][tag]

	save_obj(stats,"res/stats.pkl")

if __name__ == '__main__':
	main()
