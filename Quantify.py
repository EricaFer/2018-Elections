# Author: Erica da Cunha Ferreira
# Contact: erica.ferreira@poli.ufrj.br
# Data source: https://github.com/RodrigoMenegat/o-que-15-mil-tweets-revelam-sobre-seu-candidato


import re
import pandas as pd
from Preprocessing import candidate_list
from collections import Counter
from nltk import flatten

dfs = {}

##############################################################################
############################ CREATING FUNCTIONS  #############################
##############################################################################

def Importing(dfs):
    '''
    Imports the Preprocessed Data and saves it in a dictionary.
    '''
   
    print('\nImporting Clean Data...')
    prefix = './Preprocessed Data/Clean_'
    
    for candidate_name in candidate_list:
        dfs['Clean_' + candidate_name] = pd.read_csv(prefix + candidate_name + '.csv', index_col = 0)
    
def Preprocess_Hashtag_Mentions(dfs):
    
    '''
        - Puts all the Hashtags and Mentions of a candidate into a big list.
        - Counts how many times a Hashtag or Mention was used.
        - Divides the frequency value for the total quantities of unique Hashtags and Mentions.
        - Sorts these words in a decrescent order according to their relevance value.
    '''
    
    print('Creating Bag of Words...')
    
    regex_pattern = "[^àÀáÁéÉçôõãúÚíÍ, ^A-Za-z0-9]+"
    
    dfs_combined = ['Hashtag', 'Mentions'] 
    
    # Creates empty list
    Hashtag_List = []
    Mentions_List = []
        
    # Turns the Mentions and Hashtags Columns in a list
        
    for key in dfs:
        for df in dfs_combined:
            for row in dfs[key][df]:
                if row != '[]':
                    
                    # Counts occurence of words in each Tweet
                    dfs[key]['BOW'] = [Counter(row) for row in dfs[key].token_list]
                    
                    string_list = row.split(',')
                    
                    if len(string_list) == 1:
                       string_list = re.sub(regex_pattern, "", string_list[0])
                    
                    else:
                        string_list = [re.sub(regex_pattern, "", string) for string in string_list]
                    

        if df == 'Hashtag':
            Hashtag_List.append(string_list)
            
            
        elif df == 'Mentions':
            Mentions_List.append(string_list)
            
        # Creates flatten list
        Hashtag_List = flatten(Hashtag_List)
        Mentions_List = flatten(Mentions_List)
        
        # Counts the occurences of hashtags and mentions
        Hashtag_count = Counter(Hashtag_List)
        Mentions_count = Counter(Mentions_List)
        
        
        # Saving Hashtags and Mentions into a Series
        dfs[key]['Hashtag_order'] = [x for x in Hashtag_count]
        dfs[key]['Mention_order'] = [x for x in Mentions_count]
        
        # Saving the number of occurences
        dfs[key]['Hashtag_occurences'] = [Hashtag_count[x] for x in Hashtag_count]
        dfs[key]['Mention_occurences'] = [Mentions_count[x] for x in Mentions_count]

def saving_changes(dfs):
    print('Saving Changes...')
    for key in dfs:
        dfs[key].to_csv('.\Processed Data\Clean_' + key + '.csv')
        
##############################################################################
############################ CALLING FUNCTIONS ###############################
##############################################################################
        
Importing(dfs)
Preprocess_Hashtag_Mentions(dfs)

print('\nCode Executed Sucessfully')
        
        