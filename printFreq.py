import pickle
import numpy as np
import matplotlib.pyplot as plt 
from sys import argv
from operator import itemgetter

def main():
	with open("res/stats.pkl", 'rb') as f:
		stats=pickle.load(f)

	word_count=stats[1]
	tag_count=stats[2]
	Words=dict(sorted(word_count.items(), key = itemgetter(1), reverse = True)[:10])
	Tags=dict(sorted(tag_count.items(), key = itemgetter(1), reverse = True)[:10])
	fig = plt.figure(figsize = (10, 5))
	plt.bar(Words.keys(),Words.values(),color='blue',width=0.2)
	plt.xlabel("Word")
	plt.ylabel("Frequency of word")
	plt.title("Top 10 Words")

	fig2 = plt.figure(figsize = (10, 5))
	plt.bar(Tags.keys(),Tags.values(),color='blue',width=0.2)
	plt.xlabel("Tags")
	plt.ylabel("Frequency of tags")
	plt.title("Top 10 Tags")
	plt.show()
	print("Top 10 Words:")
	print(Words)
	print("Top 10 Tags:")
	print(Tags)

if __name__ == '__main__':
    main()