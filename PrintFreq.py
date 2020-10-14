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
	fig = plt.figure(figsize = (15, 10))
	plt.bar(Words.keys(),Words.values(),color='maroon',width=0.5)
	plt.xlabel("Word")
	plt.ylabel("Frequency of word")
	plt.title("Top 10 Most Frequent Words:")

	fig2 = plt.figure(figsize = (15, 10))
	plt.bar(Tags.keys(),Tags.values(),color='maroon',width=0.5)
	plt.xlabel("Tags")
	plt.ylabel("Frequency of tags")
	plt.title("Top 10 Most Frequent Tags")
	plt.show()


	print("Top 10 Most Frequent Words:")
	n=20
	print(50*"-")
	for word in Words:
		print("|"+(24-len(word))*" "+word+"|"+(23-len(str(Words[word])))*" "+str(Words[word])+"|")
	print(50*"-")
	print("\nTop 10 Most Frequent Tags: ")
	print(50*"-")
	for tag in Tags:
		print("|"+(24-len(tag))*" "+tag+"|"+(23-len(str(Tags[tag])))*" "+str(Tags[tag])+"|")
	print(50*"-")
if __name__ == '__main__':
    main()