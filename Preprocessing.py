# Author: Erica da Cunha Ferreira
# Contact: erica.ferreira@poli.ufrj.br
# Data source: https://github.com/RodrigoMenegat/o-que-15-mil-tweets-revelam-sobre-seu-candidato

import re
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from spacy.lang.pt.stop_words import STOP_WORDS

nltk.download('stopwords')

PATH_list =        ["alvarodias_.csv",
                    "cirogomes.csv",
                    "geraldoalckmin.csv",
                    "Haddad_Fernando.csv",
                    "jairbolsonaro.csv",
                    "joaoamoedonovo.csv",
                    "lulapelobrasil.csv",
                    "MichelTemer.csv",
                    "meirelles.csv",
                    "silva_marina.csv"]

candidate_list =   ['AlvaroDias',
                    'CiroGomes',
                    'GeraldoAlckmin',
                    'FernandoHaddad',
                    'JairBolsonaro',
                    'JoaoAmoedo',
                    'Lula',
                    'MichelTemer',
                    'Meirelles',
                    'MarinaSilva']

candidate_info = dict(zip(candidate_list, PATH_list))

dfs = {}

def importing(dfs,candidate_info): 
    '''
    Takes dict candidate_info and import data using the path(value) and name
    of the candidate(keys).
    '''
    
    print('\nImporting Data...')
    
    for key, value in candidate_info.items():
        dfs[key] = pd.read_csv('./Raw Data/' + value)
    
def preprocessing(dfs,candidate_list):
    
    tt = TweetTokenizer()
    
    Stop_Words_Spacy = list(STOP_WORDS)
    Stop_Words_NLTK  = list(stopwords.words('portuguese'))
    
    All_Stop_Words = list(set(Stop_Words_NLTK + Stop_Words_Spacy))
    
    print('Preprocessing the Data...')
    
    for key in dfs:
        
        # Tokenizing - takes a phrase and isolate each word
        dfs[key]['token_list'] = dfs[key].apply(lambda x: tt.tokenize(x.text), axis = 1)
        
        # Dropping unnecessary labels
        dfs[key].drop(labels = ['id', 'datetime','text'], axis = 1, inplace = True)
        
        # Lowering words
        dfs[key]['token_list'] = [[word.lower() for word in lists] for lists in dfs[key].token_list]
        
        # Removing Stop Words - connectives, prepositions...
        dfs[key]['token_list'] = [[word for word in lists if word not in All_Stop_Words]for lists in dfs[key].token_list]
        
        # Separating Hashtags
        dfs[key]['Hashtag'] = [[word[1:] for word in lists if re.match('#', word) is not None] for lists in dfs[key].token_list]
        
        # Separating Twitter Mentions
        dfs[key]['Mentions'] = [[word[1:] for word in lists if re.match('@', word) is not None] for lists in dfs[key].token_list]
        
        # Removing Links, Hashtags and Mentions
        pattern_twitter = '((https)|@|#)'
        dfs[key]['token_list'] = [[word for word in lists if re.match(pattern_twitter, word) is None ] for lists in dfs[key].token_list]
        
        # Removing all symbols
        pattern_words_numbers = '[0-9a-zA-Z]+'
        dfs[key]['token_list'] = [[word for word in lists if re.match(pattern_words_numbers, word) is not None] for lists in dfs[key].token_list]

def saving_changes(dfs):
    print('Saving Changes...')
    for key in dfs:
        dfs[key].to_csv('.\Preprocessed Data\Clean_' + key + '.csv')


##############################################################################
############################ CALLING FUNCTIONS ###############################
##############################################################################

importing(dfs, candidate_info)
preprocessing(dfs,candidate_list)
saving_changes(dfs)

print('\nCode Executed Sucessfully')




    