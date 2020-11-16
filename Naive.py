import pickle
from math import log
from Stat import load_obj,save_obj

class Naive:

	def __init__(self):
		self.pair_stats = load_obj("res/pair.pkl")
		self.stat = load_obj("res/stats.pkl")
		self.tag_stats = self.stat[2]
		self.word_stats = self.stat[1]
		self.wt_stats = self.stat[0]
		self.tag_set = set(self.tag_stats)

		lfword_set = { w for w in self.word_stats if self.word_stats[w] == 1 }
		self.wt_stats["UNK"] = {}  #Note clever usage of caps
		self.word_stats["UNK"] = 0

		for lfword in lfword_set:
			assert len(self.wt_stats[lfword]) == 1
			tag = list(self.wt_stats[lfword])[0] 
			if tag not in self.wt_stats["UNK"]: self.wt_stats["UNK"][tag] = 0
			self.wt_stats["UNK"][tag] += 1
			self.word_stats["UNK"] += 1
			del self.wt_stats[lfword]
			del self.word_stats[lfword]


	def predict(self,sentence):
		word_list = [w.lower() for w in sentence.split()]
		tag_list = []
		for w in word_list:
			if w not in self.wt_stats: w = "UNK"
			tag = max (self.wt_stats[w], key = lambda t : self.wt_stats[w][t] )
			tag_list.append(tag)
		return tag_list
 
 
def main():
	Demo = Naive()
	print(Demo.predict(input()))
	
if __name__ == "__main__":
	main()
