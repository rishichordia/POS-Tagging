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
		stats=({},{}) #Words tuple and tags tuple
 	count_dict=load_obj(argv[1])



if __name__ == '__main__':
    main()
