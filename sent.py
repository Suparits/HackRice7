from nltk.sentiment.vader import SentimentIntensityAnalyzer
import csv
import pandas


fileCo = 'Microsoft.csv'
colnames = ['user','text','retweets']
data = pandas.read_csv(fileCo,names=colnames)
list0 = data.text.tolist()

sent_analyzer = SentimentIntensityAnalyzer()

pos_count=0
neg_count=0
neu_count=0
total_count=len(list0)

for tweet in list0:
	ss = sent_analyzer.polarity_scores(tweet)
	if ss['compound'] > 0:
		pos_count += 1
	elif ss['compound'] < 0:
		neg_count += 1
	else:
		neu_count += 1
	
	for k in sorted(ss):
		k = compound,neg,neu,pos, ss[k] = some number
		print('{0}: {1}, '.format(k,ss[k]),end ='')
	print() #adds newline after scores print

print("Positive tweets: ",pos_count/total_count,"%")
print("Negative tweets: ",neg_count/total_count,"%")
print("Neutral tweets: ",neu_count/total_count,"%")
print("total tweets: ",total_count)
