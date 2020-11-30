import pickle
from itertools import product
from HMM import HMM
from math import log
from Stat import load_obj,save_obj

class Trigram(HMM):

	def __init__(self):
		super().__init__()
		self.smoothness = 0.1
	
	def tran_prob_ln(self,tag_tuple):
		assert (len(tag_tuple) == 3)
		numerator = self.triple_stats[tag_tuple] + self.smoothness
		denominator = self.pair_stats[tag_tuple[0:2]] + (len(self.tag_set) * self.smoothness)
		return log(numerator/denominator)
		
	def emis_prob_ln(self,tag,word):
		if word not in self.wt_stats: word = "UNK"
		return log((self.wt_stats[word][tag]/self.tag_stats[tag]))

	def tag_prob_ln(self,tag_tuple):
		assert (len(tag_tuple) == 2)
		tag_total = sum ((self.pair_stats[j] for j in self.pair_stats))
		if tag_tuple not in self.pair_stats : return self.NEG_INF
		return log(self.pair_stats[tag_tuple]/tag_total)

	def predict(self,sentence):
		word_list = [w.lower() for w in sentence.split()]

		viterbi_dp = []  #Index == String length, Element = dictionary?
		viterbi_bp = []  
		FULL_ITERABLE_SET = { (x,y) for x in self.tag_set for y in self.tag_set }
#The second tag is current, first tag is previous
		temp = dict.fromkeys(FULL_ITERABLE_SET,self.NEG_INF)
		w = word_list[0]
		if w not in self.wt_stats: w = "UNK"
		iterate = iter(p for p in FULL_ITERABLE_SET if p[1] in self.wt_stats[w]) #Iterate over only tags ending 
		for t in iterate:
			temp[t] = self.tag_prob_ln(t) + self.emis_prob_ln(t[1],w)
		viterbi_dp.append(temp)

		
		for i,w in enumerate(word_list):
			if i==0: continue
			if w not in self.wt_stats: w = "UNK"

			iterate = iter(p for p in FULL_ITERABLE_SET if p[1] in self.wt_stats[w]) #Iterate over only tags ending 
			temp = dict.fromkeys(FULL_ITERABLE_SET,self.NEG_INF)
			temp2 = {}
			
			for tt in iterate:
				ct = tt[1]
				pt = tt[0]
				
				func = lambda ppt:(viterbi_dp[i-1][(ppt,pt)] + self.tran_prob_ln((ppt,pt,ct)) + self.emis_prob_ln(ct,w))
				#breakpoint()
				most_prob_tag = max (self.tag_set, key = func)
				temp[tt] = func(most_prob_tag)
				temp2[tt] = most_prob_tag
			viterbi_dp.append(temp)
			viterbi_bp.append(temp2)

		pred_tag_list = []
		last_2_tags =	max (FULL_ITERABLE_SET, key = lambda t: viterbi_dp[-1][t])
		pred_tag_list.extend(last_2_tags)
		rev = viterbi_bp[::-1]
		for i in rev:
			bttag = i[last_2_tags]
			pred_tag_list.insert(0,bttag)
			last_2_tags = (bttag,last_2_tags[0])
		del pred_tag_list[0]
		return pred_tag_list
	#	print(viterbi_dp)
	#	print(viterbi_bp)
	#	print(pred_tag_list)
 
 
def main():
	Demo = Trigram()
	print(Demo.predict(input()))
	
if __name__ == "__main__":
	main()
