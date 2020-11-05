import pickle
from math import log
from Stat import load_obj,save_obj

pair_stats = load_obj("res/pair.pkl")
stat = load_obj("res/stats.pkl")
tag_stats = stat[2]
word_stats = stat[1]
wt_stats = stat[0]
tag_set = set(tag_stats)	

NEG_INF = -10000000


def tran_prob_ln(prev_tag,next_tag):
	pair = (prev_tag,next_tag)
	if pair not in pair_stats: return NEG_INF
	return log(pair_stats[(prev_tag,next_tag)]/tag_stats[prev_tag])

def emis_prob_ln(tag,word):
	if word not in wt_stats: return 0 #If word not in dictionary, we return 1.. We ignore the word
#else: c = wt_stats[word]
#t_pair_cnt = sum ((len(word_stats[w]) for w in wt_stats))#TODO: Smooth this shit... Maybe this is most apt?
#fav_cnt = sum ((1 for w in word_stats[w] if tag in word_stats[w]))
	return log((wt_stats[word.lower()][tag]/tag_stats[tag])) 

def tag_prob_ln(tag):
	tag_total = sum ((tag_stats[j] for j in tag_stats))
	return log(tag_stats[tag]/tag_total)

def viterbi(sentence):
	word_list = [w.lower() for w in sentence.split()]
	viterbi_dp = []  #Index == String length, Element = dictionary?
	viterbi_bp = []  

	temp = dict.fromkeys(tag_set,NEG_INF)

	w = word_list[0]
	iterate = iter(wt_stats[w]) if w in wt_stats else iter(tag_set)
	for t in iterate:
		temp[t] = tag_prob_ln(t) + emis_prob_ln(t,w)
	viterbi_dp.append(temp)

	for i,w in enumerate(word_list):
		if i==0: continue

		temp = dict.fromkeys(tag_set,NEG_INF)
		temp2 = {}
		
		iterate = iter(wt_stats[w]) if w in wt_stats else iter(tag_set)
		for t in iterate:
			temp2[t] = max (tag_set,key = lambda pt:(viterbi_dp[i-1][pt] + tran_prob_ln(pt,t) + emis_prob_ln(t,w)))
			temp[t] = viterbi_dp[i-1][temp2[t]] + tran_prob_ln(temp2[t],t) + emis_prob_ln(t,w)

		viterbi_dp.append(temp)
		viterbi_bp.append(temp2)

	pred_tag_list = []
	temp_tag =  max (tag_set, key = lambda t: viterbi_dp[-1][t] + tran_prob_ln(t,'PUN'))
#TODO: Include fullstop in our analysis -- Maybe we have to create a new tag for fullstop
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
