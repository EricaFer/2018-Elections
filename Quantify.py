# Author: Erica da Cunha Ferreira
# Contact: erica.ferreira@poli.ufrj.br
# Data source: https://github.com/RodrigoMenegat/o-que-15-mil-tweets-revelam-sobre-seu-candidato


import re
import pandas as pd
from Preprocessing import candidate_list
from collections import Counter

dfs = {}

##############################################################################
############################ CREATING FUNCTIONS  #############################
##############################################################################

def importing(dfs):
    '''
    Imports the Preprocessed Data and saves it in a dictionary.
    '''
   
    print('\nImporting Clean Data...')
    prefix = './Preprocessed Data/Clean_'
    
    for candidate_name in candidate_list:
        dfs['Clean_' + candidate_name] = pd.read_csv(prefix + candidate_name + '.csv', index_col = 0)
    
def Frequency(dfs):
    
    '''
    Creates a Bag of Words (counts words frequency of each tweet, mention and Hashtag)
    '''
    
    print('Creating Bag of Words...')
        
    # Turns the Mentions and Hashtags Columns in a list
        
    for key in dfs:
        
    # Creates empty list
        Hashtag_List = []
        Mentions_List = []                       

        for row in dfs[key].Hashtag:
            if row != '[]':
                
                string_list = row.split(',')
                
                if len(string_list) == 1:
                   string_list = re.sub("[^A-Za-z0-9]+", "", string_list[0])
                
                else:
                    string_list = [re.sub("[^A-Za-z0-9]+", "", string) for string in string_list]
                
                    Hashtag_List.extend(string_list)
                    
        for row in dfs[key].Mentions:
            if row != '[]':
                
                string_list = row.split(',')
                
                if len(string_list) == 1:
                   string_list = re.sub("[^A-Za-z0-9]+", "", string_list[0])
                
                else:
                    string_list = [re.sub("[^A-Za-z0-9]+", "", string) for string in string_list]
                
                    Mentions_List.extend(string_list)
                   
        '''
        # Counts occurences of Hashtags and Mentions
        print('\nCounting Mentions and Hashtags occurences...')
        Counter_Hashtag = Counter(Hashtag_List)
        Counter_Mentions = Counter(Mentions_List)
        
        # Sorts the occurences in a decrescent order
        print('\nSorting Mentions and Hashtags occurences...')
        Counter_Hashtag = sorted(Hashtag_List[:][0], key = Hashtag_List[:][1], reverse = True)
        Counter_Mentions = sorted(Mentions_List[:][0], key = Mentions_List[:][1], reverse = True)
        
        # Counts occurence of words in each Tweet
        dfs[key]['BOW'] = [Counter(row) for row in dfs[key].token_list]
        
    return Counter_Hashtag, Counter_Mentions'''

    print(Hashtag_List)
    
    
    

##############################################################################
############################ CALLING FUNCTIONS ###############################
##############################################################################
    
        
importing(dfs)
Frequency(dfs)  

print('\nCode Executed Sucessfully')
        
        