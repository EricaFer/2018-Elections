# Author: Erica da Cunha Ferreira
# Contact: erica.ferreira@poli.ufrj.br
# Data source: https://github.com/RodrigoMenegat/o-que-15-mil-tweets-revelam-sobre-seu-candidato

import pandas as pd
import Preprocessing as pre

#from polyglot.text import Text
from collections import Counter
#from gensim.models.tfidfmodel import TfidfModel

dfs = {}

def importing(dfs):
    '''
    Imports the Preprocessed Data and saves it in a dictionary.
    '''
   
    print('\nImporting Clean Data...')
    prefix = './Preprocessed Data/Clean_'
    
    for candidate_name in pre.candidate_list:
        dfs[candidate_name] = pd.read_csv(prefix + candidate_name + '.csv')
    
def Frequency(dfs):
    
    '''
    Creates a Bag of Words (counts words frequency of each tweet, mention and Hashtag)
    '''
    
    print('Creating Bag of Words...')
        
    for key in dfs:
        
        # Creates empty list
        Hashtag_List = []
        Mentions_List = []
        
        # Turns the Mentions and Hashtags Columns in a list
        Hashtag_List = [[Hashtag_List.append(word) for word in row] if len(row) != 0 for row in dfs[key].Hashtag]
        Mentions_List = [[Mentions_List.append(word) for word in row] if len(row) != 0 for row in dfs[key].Mentions]
        
        # Counts occurences of Hashtags and Mentions
        Counter_Hashtag = Counter(Hashtag_List)
        Counter_Mentions = Counter(Mentions_List)
        
        # Sorts the occurences in a decrescent order
        Counter_Hashtag = sorted(Hashtag_List[:][0], key = Hashtag_List[:][1], reverse = True)
        Counter_Mentions = sorted(Mentions_List[:][0], key = Mentions_List[:][1], reverse = True)
        
        # Counts occurence of words in each Tweet
        dfs[key]['BOW'] = [Counter(row) for row in dfs[key].token_list]
    
def Tfidf(dfs):
    '''
    Calculates the relevance of each word of each tweet.
    '''
    
    print('Calculting TFIDF...')
    
    # Instantiating Model
    tfidf = TfidfModel()
    
    for key in dfs:
    
        dfs[key]['Tfidf'] = [tfidf(row) for row in dfs[key].BOW]
        dfs[key].drop(labels = 'BOW', axis =  1, inplace = True)
        
def Total_Relevance(dfs):
    '''
    
    ''' 
        
    total_relevance = []
    
    print('Calculating Total Relevance...')

        
importing(dfs)
Frequency(dfs)       
        
        