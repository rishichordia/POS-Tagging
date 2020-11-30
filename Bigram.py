import pickle
from HMM import HMM
from math import log
from Stat import load_obj,save_obj

class Bigram(HMM):


	def tran_prob_ln(self,prev_tag,next_tag):
		pair = (prev_tag,next_tag)
		if pair not in self.pair_stats: self.pair_stats[pair] = 0  
		numerator = self.pair_stats[pair] + self.smoothness
		denominator = self.tag_stats[prev_tag] + (len(self.tag_set) * self.smoothness)
		return log(numerator/denominator)
		
	def emis_prob_ln(self,tag,word):
		word = word.lower().strip()
		if word not in self.wt_stats: word = "UNK"
		return log((self.wt_stats[word][tag]/self.tag_stats[tag]))

	def tag_prob_ln(self,tag):
		tag_total = sum ((self.tag_stats[j] for j in self.tag_stats))
		return log(self.tag_stats[tag]/tag_total)

	def predict(self,sentence):
		word_list = [w.lower() for w in sentence.split()]
		viterbi_dp = []  #Index == String length, Element = dictionary?
		viterbi_bp = []  
		temp = dict.fromkeys(self.tag_set,self.NEG_INF)
		w = word_list[0]
		iterate = iter(self.wt_stats[w]) if w in self.wt_stats else iter(self.wt_stats["UNK"])
		for t in iterate:
			temp[t] = self.tag_prob_ln(t) + self.emis_prob_ln(t,w)
		viterbi_dp.append(temp)
		for i,w in enumerate(word_list):
			if i==0: continue
			temp = dict.fromkeys(self.tag_set,self.NEG_INF)
			temp2 = {}
			
			iterate = iter(self.wt_stats[w]) if w in self.wt_stats else iter(self.wt_stats["UNK"])
			for t in iterate:
				temp2[t] = max (self.tag_set,key = lambda pt:(viterbi_dp[i-1][pt] + self.tran_prob_ln(pt,t) + self.emis_prob_ln(t,w)))
				temp[t] = viterbi_dp[i-1][temp2[t]] + self.tran_prob_ln(temp2[t],t) + self.emis_prob_ln(t,w)
			viterbi_dp.append(temp)
			viterbi_bp.append(temp2)
		pred_tag_list = []
		temp_tag =	max (self.tag_set, key = lambda t: viterbi_dp[-1][t])
		#TODO: Maybe we have to create a new tag for fullstop
		pred_tag_list.append(temp_tag)
		rev = viterbi_bp[::-1]
		for i in rev:
			temp_tag = i[temp_tag]
			pred_tag_list.insert(0,temp_tag)
		return pred_tag_list
	#	print(viterbi_dp)
	#	print(viterbi_bp)
	#	print(pred_tag_list)
 
 
def main():
	Demo = Bigram()
	print(Demo.predict(input()))
	
if __name__ == "__main__":
	main()
