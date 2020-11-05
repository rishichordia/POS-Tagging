import pickle
from Stat import load_obj,save_obj

pair_stats = load_obj("res/pair.pkl")
stat = load_obj("res/stats.pkl")
tag_stats = stat[2]
word_stats = stat[1]
wt_stats = stat[0]

tag_set = set(tag_stats)	

def tran_prob(prev_tag,next_tag):
	pair = (prev_tag,next_tag)
	if pair not in pair_stats: return 0
	return pair_stats[(prev_tag,next_tag)]/tag_stats[prev_tag]

def emis_prob(tag,word):
	return wt_stats[word.lower()][tag]/tag_stats[tag] #TODO: Smooth this shit, use logs

def tag_prob(tag):
	tag_total = sum ((tag_stats[j] for j in tag_stats))
	return tag_stats[tag]/tag_total

def viterbi(sentence):
	word_list = [w.lower() for w in sentence.split()]
#	word_list.insert(0,'*')
	viterbi_dp = []  #Index == String length, Element = dictionary?
	for t in wt_stats[word_list[0]]:
		temp = dict.fromkeys(tag_set,0)
		temp[t] = tag_prob(t) * emis_prob(t,word_list[0])
		viterbi_dp.append(temp)

	for i,w in enumerate(word_list,1):
		temp = dict.fromkeys(tag_set,0)
		for t in wt_stats[w]:
			temp[t] = max ((viterbi_dp[i-1][pt] * tran_prob(pt,t) * emis_prob(t,w) for pt in tag_set))
		viterbi_dp.append(temp)


	print(viterbi_dp)

	


	

def main():
	viterbi ("Enter the dragon")

if __name__ == "__main__":
	main()
