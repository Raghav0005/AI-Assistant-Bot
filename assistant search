#import the libiraries
from newspaper import Article
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
warnings.filterwarnings('ignore')


#get the website by the keywords as inputs
import requests, sys, webbrowser, bs4


r = requests.get('https://google.com/search?q='+''.join(sys.argv[1:]))
r.raise_for_status()

soup= bs4.BeautifulSoup(r.text , "html.parser")
LinkElements = soup.select(' .r a')
LinkToOpen = min(5 , len(LinkElements))

for i in range(LinkToOpen):
    webbrowser.open('https://.google.com' + LinkElements[i].get('href'))
    
    
    #download punkt package
nltk.download ('punkt' , quiet=True)

#get the article
article = Article(r)
article.download()
article.parse()
article.nlp()
corpus = article.text

#tokenization
text = corpus
sentence_list = nltk.sent_tokenize(text) #a list of sentences

# print the list of sentences
print (sentence_list)

#greeting function
def greeting_response(text):
  text = text.lower()


  # bot response

  bot_greetings = ["Hi", "How are you", "Is anyone there?", "Hello", "Good day"]

  # user greetings 
  my_greetings=["Hi", "How are you", "Is anyone there?", "Hello", "Good day", "i hope u r fine"]

  for word in text.split():
      if word in my_greetings:
        return random.choice(bot_greetings)
        
        def index_sort(list_var):
  lenght= len(list_var)
  list_index = list(range(0,length))

  x= list_var
  for i in range(length):
    for j in range(length):
      if x[list_index[i]]> x[list_index[j]]:
        #swap
        temp= list_index[i]
        list_index[i]= list_index[j]
        list_index[j]= temp


  return list_index   
  
  #create the bot response
def bot_response(user_input):
  user_input = user_input.lower()
  sentence_list.append(user_input)
  bot_responce =''
  cm = CountVectorizer().fit_transform(sentence_list)
  similarity_scores = cosine_similarity(cm[-1], cm)
  similarity_scores_list = similarity_scores.flatten()
  index = index_sort(similarity_scores_list)
  index = index[1:]
  response_flag = 0 

  j= 0
  for i in range(len(index)):
    if similarity_scores_list[index[i]] > 0.0:
      bot_response = bot_response+ ' ' +sentence_list[index[i]]
      response_flag = 1

      j=j+1
    if j>2:
      break

  if response_flag == 0:
    bot_response = bot_response +' ' + "I apologise, i can't get u"

  sentence_list.remove(user_input)
  return bot_response  
  
  #start the chat 
print ('ill answer u')
exit_list = ['exit', 'see u later' , 'bye' , 'break' , 'quit']
while (True):
  user_input= input()
  if user_input.lower() in exit_list:
    print("chat with u later")
    break
  else:
    if greeting_response(user_input) !=None:
      print('doc bot: '+ greeting_response(user_input))
