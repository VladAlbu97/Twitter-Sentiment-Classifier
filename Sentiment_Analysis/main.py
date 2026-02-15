
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
negative_words = []
positive_words = []
tweets=[]

#striping the punctuation
def strip_punctuation(word):
    for char in punctuation_chars:
        word = word.replace(char, "")
    return word               
            
    
    
#defing what we consider negative words             
def get_neg(words):
    negative_count=0
    wordss=strip_punctuation(words)

    for word in wordss.split():
        if word.lower() in negative_words:
            negative_count+=1
    return negative_count


#defing what we consider positive words  
def get_pos(words):
    positive_count=0
    wordss=strip_punctuation(words)

    for word in wordss.split():
        if word.lower() in positive_words:
            positive_count+=1
    return positive_count




with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

#function for creating the data 
def reulting_data(tweets):
    nr_tweets=int(tweets[1])
    reply=int(tweets[2])
    positive=get_pos(tweets[0])
    negative=get_neg(tweets[0])
    net=positive-negative
    
    return [nr_tweets,reply,positive,negative,net]

#reading from the pseudo tweets
with open ('project_twitter_data.csv','r') as file:
    chars=file.readlines()
    for char in chars[1:]:
        clean_line = char.strip()
                
        if clean_line :
            tweet = clean_line.split(",")
            
            tweets.append(reulting_data(tweet))



#writing the new CSV file
header ="Number of Retweets,Number of Replies,Positive Score,Negative Score,Net Score"            
with open   (" resulting_datas.csv","w") as file:
    file.write(header + "\n")
    for row in tweets:
        
        string_row = [str(item) for item in row]
        
       
        file.write(",".join(string_row) + "\n")
