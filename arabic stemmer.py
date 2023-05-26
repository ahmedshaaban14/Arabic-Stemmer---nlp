#!/usr/bin/env python
# coding: utf-8

# In[14]:


from nltk import word_tokenize
from nltk.stem.isri import ISRIStemmer
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
nltk.download('stopwords')
import re 


# In[23]:


#prefix
p1=['ا','ل','ب','و','ف','س','ى','ت']
p2=['اى','ون','فى','فب','فت','لي','فن','وب','فا','ول','وو','اف','لا','ات','وى','وت','اا','ال','ست','سى','يس','يت','گت','ىى','تت']
p3=['مست','ولت','فلى','فلن','فلل','فهو','فهم','فال','ىست','تست','است','فهى','سيا','فلا','ءست','بمس','لىت']
p4=['اتست','اىست','فاست','ءاست','انهم','ءانى','والم','باست','گمست','والا']
p5=['فلىست','الاست','افاست']


#suffixes
s1=['ت','گ','ى','ه']
s2=['وا','ون','هن','ان','وك','اك','اه','ها','هم','كن','ات','ىن']
s3=['تنا','نها','تان','ناگ','ونه','ناه','هما','وعا','نهم','وهم','ونى','وعن','تها','تهم','نگم','هات','هان','تان','تهن','وگم','ونه','ونگ','انگ']
s4=['موهم','موهن','ناگم','نوهن','ونهم','ناهم','ونگم','توهم','اتها','اتهم','يانه','اءهم']
s5=['گموها','ناهما','ناگمو']


stop_words  = ['من',
 'في',
 'على',
 'و',
 'فى',
 'يا',
 'عن',
 'مع',
 'ان',
 'هو',
 'علي',
 'ما',
 'اللي',
 'كل',
 'بعد',
 'ده']
articles = ['بال','فال','وال','كال','ولل','ال','ل','ال', 'لي','ل',' ا',' فبال','لبال','وبال']


# In[24]:


def normalize(word):
    for x in range(3):
        word = re.sub("أ","ا", word)
        word = re.sub("ي", "ى", word)
        word = re.sub("ؤ", "ء", word)
        word = re.sub("ئ", "ء", word)
        word = re.sub("ة", "ه", word)
        word = re.sub("ك", "گ", word)
    return word

print("Normalization :" + "" + normalize("الحياة"))


# In[25]:


def remove_stopwords(words):
    without_stop= []
    for x in words:
        if x in stop_words :
            without_stop.append("")
        else:
            without_stop.append(x)
    return without_stop


# In[26]:


def Def_articles_removal(word):
    if word[0:1] in articles :
        word=word.replace(word[0:1],"")
        
    if word[0:2] in articles :
        word=word.replace(word[0:2],"")
    
    if word[0:3] in articles :
        word=word.replace(word[0:3],"")
        
    return word


# In[27]:


def prefix_removal(word):
    
    if len(word)>=4:
        if word[0:1] in p1:
            word=word.replace(word[0:1],"")            
    if len(word)>=5:
        if word[0:2] in p2:
             word=word.replace(word[0:2],"")
    if len(word)>=6:
        if word[0:3] in p3:
            word=word.replace(word[0:3],"")
    if len(word)>=7:
        if word[0:4] in p4:
            word=word.replace(word[0:4],"")
    if len(word)>=8:
        if word[0:5] in p5:
            word=word.replace(word[0:5],"")
    return word


# In[28]:


def suffix_removal(word):
    for x in range(len(word)):
        if len(word)>=4:
            if word[-1:] in s1 :
                word=word.replace(word[-1:],"")
                return word
                
        if len(word)>=5:
            if word[-2:] in s2 :
                word=word.replace(word[-2:],"")  
                return word
                
        if len(word)>=6:
            if word[-3:] in s3 :
                word=word.replace(word[-3:],"")
                return word
                
        if len(word)>=7:
            if word[-4:] in s4 :
                word=word.replace(word[-4:],"")
                return word 
                
        if len(word)>=8:
            if word[-5:] in s5 :
                word=word.replace(word[-5:],"")
                return word
                
    return word


# In[69]:


from nltk.stem import SnowballStemmer

# Create an instance of the Snowball stemmer for Arabic
stemmer = SnowballStemmer('arabic')


# In[73]:


def Arabic_stemmer(text):
    #words = text.split()
    root=[]
    for s in text :
        s1 = normalize(s)
        s2 = Def_articles_removal(s1)
        s3 = prefix_removal(s2)
        s4 = suffix_removal (s3)
        if s == 'الله':
            root.append(s)
        else:
           
            root.append(s4)
    return root


# In[74]:


Words =['يندمون','يلعبون','يلهو','الاولاد','عملهما','الوقت','الامل','الذهب','يذهبون','الدنيوية','العاملان','الله']
root = Arabic_stemmer(Words)

print("Word    Root \n")
for i in range(len(Words)):
    print(Words[i]+'\t '+root[i])


# In[ ]:




