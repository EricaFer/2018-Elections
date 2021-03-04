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
    
    regex_pattern = "[^A-Za-z0-9]+"
    
    dfs_combined = ['Hashtag', 'Mentions'] 
    
    # Creates empty list
    Hashtag_List = []
    Mentions_List = []
        
    # Turns the Mentions and Hashtags Columns in a list
        
    for key in dfs:
        for df in dfs_combined:
            for row in dfs[key][df]:
                if row != '[]':
                    
                    string_list = row.split(',')
                    
                    if len(string_list) == 1:
                       string_list = re.sub(regex_pattern, "", string_list[0])
                    
                    else:
                        string_list = [re.sub(regex_pattern, "", string) for string in string_list]
            
            if df == 'Hashtag':
                Hashtag_List.extend(string_list)
                dfs[key][df] = Hashtag_List.value_counts().index
                dfs[key][df + '_valor'] = dfs[key][df]/len(Hashtag_List)
                
                
            elif df == 'Mentions':
                Mentions_List.extend(string_list)
                dfs[key][df] = Hashtag_List.value_counts().index
                dfs[key][df + '_valor'] = dfs[key][df]/len(Mentions_List)
                
            dfs[key].sort_values(by = str(df) + '_valor', inplace = True, ascending = False)
    
def Counting():

                     
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


##############################################################################
############################ CALLING FUNCTIONS ###############################
##############################################################################
    
        
Importing(dfs)
Preprocess_Hashtag_Mentions(dfs)  

print('\nCode Executed Sucessfully')
        
        