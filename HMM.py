import pickle
from math import log
from collections import defaultdict
from Stat import load_obj,save_obj

class HMM:

	def __init__(self):
		self.pair_stats = defaultdict(lambda :0,load_obj("res/pair.pkl"))
		self.triple_stats = defaultdict(lambda :0,load_obj("res/triple.pkl"))
		self.stat = load_obj("res/stats.pkl")
		self.tag_stats = defaultdict(lambda :0, self.stat[2])
		self.word_stats = defaultdict(lambda :0, self.stat[1])
		self.wt_stats = defaultdict(lambda :0, self.stat[0])
		self.tag_set = set(self.tag_stats)
		self.NEG_INF = -10000000
		self.smoothness = 1  #Can modify this

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


	def tran_prob_ln(self,tag_tuple):
		pass
		
	def emis_prob_ln(self,tag,word):
		pass

	def tag_prob_ln(self,tag):
		pass

	def predict(self,sentence):
		pass
 
 
#def main():
#	Demo = HMM()
#	print(Demo.predict(input()))
#	
#if __name__ == "__main__":
#	main()
