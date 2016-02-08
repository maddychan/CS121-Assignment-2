
from collections import defaultdict


#open the data.txt file - there needs to be a data.txt file in the same file folder as this module
file = open("data.txt")

#variables to keep track of
maxWords = 0                #to keep track of the highest number of words on a page 
maxURL = ""                 #to keep track of the url with the most words
urls = set()                #to keep track of unique urls
urlDict = defaultdict(set)  #to keep track of subdomains
currentURL = ""             #to keep track of which url the data refers to
wordDict = defaultdict(int) #to keep track of words and their ferquencies
stopWords = {"a","about","above","after","again","against","all","am","an","and","any","are","aren't","as","at",
             "be","because","been","before","being","below","between","both","but","by","can't","cannot","could",
             "couldn't","did","didn't","do","does","doesn't","doing","don't","down","during","each","few","for",
             "from","further","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","he's",
             "her","here","here's","hers","herself","him","himself","his","how","how's","i","i'd","i'll","i'm","i've",
             "if","in","into","is","isn't","it","it's","its","itself","let's","me","more","most","mustn't","my","myself",
             "no","nor","not","of","off","on","once","only","or","other","ought","our","ours","ourselves","out",
             "over","own","same","shan't","she","she'd","she'll","she's","should","shouldn't","so","some","such",
             "than","that","that's","the","their","theirs","them","themselves","then","here","there's","these",
             "they","they'd","they'll","they're","they've","this","those","through","to","too","under","until","up",
             "very","was","wasn't","we","we'd","we'll","we're","we've","were","weren't","what","what's","when","when's",
             "where","where's","which","while","who","who's","whom","why","why's","with","won't","would","wouldn't",
             "you","you'd","you'll","you're","you've","your","yours","yourself","yourselves","|","&","-","~","+","=",
             "*","<",">",".",";",'1','2','3','4','5','6','7','8','9','b','@',':'}

#going through the file, looking to see if it's a url or data on a page.
#urls, urlDict, maxURL, and wordDict are updated accordingly
for i in file:
    line = i.strip()
    if len(line) > 7 and line[0:7] == "http://":
        sub = line[7:].split(".")
        urlDict[sub[0]].add(line)
        urls.add(line)
        currentURL = line
    else:
        line = line.replace("\\n","").replace("\\r","").replace("\\t","").split()
        if len(line) > maxWords:
            maxWords = len(line)
            maxURL = currentURL
        for a in line:
            wordDict[a.lower()]+=1
            
        

#printing out number of URLS and the page with the max amount of words
print("Number of urls:",len(urls))
print("max words",maxWords,maxURL)


#writing Subdomain.txt
subdomain = open("Subdomain.txt",'w')
for a in sorted(urlDict.items(),key = lambda x:x[1],reverse = True):
    subdomain.write(a[0]+", "+str(len(a[0]))+"\n")
subdomain.close()

#writing CommonWords.txt
words = open("CommonWords.txt",'w')
count = 0
for a in sorted(wordDict.items(),key = lambda x:x[1],reverse = True):
    if a[0] not in stopWords and a[0][0] !="\\":
        words.write(a[0]+", "+str(a[1])+"\n")
        count +=1
        if count == 501:
            break
words.close()
    
      



