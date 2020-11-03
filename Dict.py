from sys import argv
import pickle
def main():
 	'''Usage: ./Dict.py input.txt output.pkl'''
 	ifile=open(argv[1],"r")
 	count_dict={}
 	line=ifile.read();
 	for comb in line.split():
 		element=comb.split("_")
 		word=element[0].lower()
 		tag=element[1]
 		if word in count_dict:
 			if tag in count_dict[word]:
 				count_dict[word][tag]+=1
 			else:
 				count_dict[word][tag]=1	
 		else:
 			count_dict[word]={}
 			count_dict[word][tag]=1

 	with open(argv[2], 'wb') as f:
 		pickle.dump(count_dict, f, pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    main()
