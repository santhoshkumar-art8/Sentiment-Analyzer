sentence=input("Enter the Text:")
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid=SentimentIntensityAnalyzer()

score=sid.polarity_scores(sentence)

value=score.values()

values_list=list(value)
print("")
print("")

if(values_list[0]>0):
    print("It is a negative word")
elif(values_list[1]>0):
    print("It is neutral words")
elif(values_list[1]>0 and values_list[2]>0):
    print("It is common word")
elif(values_word[2]>0):
    print("It is positive words")