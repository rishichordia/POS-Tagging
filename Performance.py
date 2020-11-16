import pickle
import glob
from sys import argv
from os import path
from Viterbi import HMM
from Stat import load_obj,save_obj

stat = load_obj("res/stats.pkl")
N=len(stat[2])

def main():
	'''Usage: python3 Confusion_Matrix.py input.txt'''
	input_list=glob.glob("res/*.conf.pkl")
	
	for ifile in input_list:
		print("\nInput file:",ifile)
		confusion_matrix=load_obj(ifile)
		if len(confusion_matrix)==0:
			print("Empty Confusion Matrix")
			quit()
		
		Total=[0]*N
		TP=[0]*N
		FN=[0]*N
		FP=[0]*N
		Recall=[0]*N
		Precision=[0]*N
		F_score=[0]*N
		wfscore=0
		for i in range(N):
			for j in range(N):
				if i==j:
					TP[i]+=confusion_matrix[i][j]
				else:
					FN[i]+=confusion_matrix[i][j]
					FP[j]+=confusion_matrix[i][j]
				Total[i]+=confusion_matrix[i][j]	
		print("\nAccuracy is: ",end='')
		print(sum(TP)/sum(Total))
		print("Recall is: ",end='')
		for i in range(N):
			if TP[i]!=0:Recall[i]=TP[i]/(TP[i]+FN[i])
		print(sum(Recall)/N)
		print("Precision is: ",end='')
		for i in range(N):
			if TP[i]!=0:Precision[i]=TP[i]/(TP[i]+FP[i])
		print(sum(Precision)/N)
		for i in range(N):
			if TP[i]!=0: F_score[i]=(2*Recall[i]*Precision[i])/(Recall[i]+Precision[i])
		print("Avg  F-Score: ",end='')
		print(sum(F_score)/N)
		print("Weighted  F-Score: ",end='')
		for i in range(N):wfscore+=Total[i]*F_score[i]
		wfscore=wfscore/sum(Total)
		print(wfscore)


if __name__ == '__main__':
	main()
