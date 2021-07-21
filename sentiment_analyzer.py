from textblob import TextBlob

y = input("type ypur sentence: ")
edu = TextBlob(y)
x = edu.sentiment.polarity


if x<0:
    print("Negetive")
elif x==0:
    print("Nutral")
elif x>0 and x<=1:
    print("positive")