import pickle
from sys import argv

def load_obj(name ):
	with open(name, 'rb') as f:
		return pickle.load(f)

def main():
	'''Usage: python Prob.py word tag #output to stdout'''

	stats = load_obj("res/stats.pkl")

	final_dict=stats[0]
	word_count=stats[1]
	tag_count=stats[2]
	
	target_word = argv[1].lower()
	target_tag = argv[2].upper()

	if target_word not in final_dict:
		exit()
	if target_tag not in final_dict[target_word]:
		exit()
	if target_tag not in tag_count:
		exit()


	prob = final_dict[target_word][target_tag] / tag_count[target_tag]

	print (prob)


if __name__ == '__main__':
	main()
