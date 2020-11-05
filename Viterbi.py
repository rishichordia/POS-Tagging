import pickle
from math import log
from Stat import load_obj,save_obj

pair_stats = load_obj("res/pair.pkl")
stat = load_obj("res/stats.pkl")
tag_stats = stat[2]
word_stats = stat[1]
wt_stats = stat[0]

tag_set = set(tag_stats)	

def tran_prob_ln(prev_tag,next_tag):
	pair = (prev_tag,next_tag)
	if pair not in pair_stats: return 0
	return log(pair_stats[(prev_tag,next_tag)]/tag_stats[prev_tag])

def emis_prob_ln(tag,word):
	return log(wt_stats[word.lower()][tag]/tag_stats[tag]) #TODO: Smooth this shit, use logs

def tag_prob_ln(tag):
	tag_total = sum ((tag_stats[j] for j in tag_stats))
	return log(tag_stats[tag]/tag_total)

def viterbi(sentence):
	word_list = [w.lower() for w in sentence.split()]
#	word_list.insert(0,'*')
	viterbi_dp = []  #Index == String length, Element = dictionary?
	viterbi_bp = []  

	temp = dict.fromkeys(tag_set,-10000000)
	for t in wt_stats[word_list[0]]:
		temp[t] = tag_prob_ln(t) + emis_prob_ln(t,word_list[0])
	viterbi_dp.append(temp)

	for i,w in enumerate(word_list):
		if i==0: continue

		temp = dict.fromkeys(tag_set,-10000000)
		temp2 = {}
		
		if w not in wt_stats:
			for t in wt_stats[w]:
				temp2[t] = max (tag_set,key = lambda pt:(viterbi_dp[i-1][pt] + tran_prob_ln(pt,t) + emis_prob_ln(t,w)))
				temp[t] = viterbi_dp[i-1][temp2[t]] + tran_prob_ln(temp2[t],t) + emis_prob_ln(t,w)

		for t in wt_stats[w]:
			temp2[t] = max (tag_set,key = lambda pt:(viterbi_dp[i-1][pt] + tran_prob_ln(pt,t) + emis_prob_ln(t,w)))
			temp[t] = viterbi_dp[i-1][temp2[t]] + tran_prob_ln(temp2[t],t) + emis_prob_ln(t,w)
		viterbi_dp.append(temp)
		viterbi_bp.append(temp2)
	

	pred_tag_list = []
	temp_tag =  max (tag_set, key = lambda t: viterbi_dp[-1][t])
#TODO: Include fullstop in our analysis
	pred_tag_list.append(temp_tag)

	rev = viterbi_bp[::-1]
	for i in rev:
		temp_tag = i[temp_tag]
		pred_tag_list.insert(0,temp_tag)



#	print(viterbi_dp)
#	print(viterbi_bp)
	print(pred_tag_list)


	


	

def main():
	viterbi (input())

if __name__ == "__main__":
	main()
