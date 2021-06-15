# coding=utf-8
# Autor : Daro HENG
# Email :  hendgaro1@gmail.com
# Date creation : 17/03/2021


from transformers import pipeline

import pandas as pd
from tqdm import tqdm

import os
import multiprocessing as mp
import time
import sys
import numpy as np

class Sentiment_DistilBert:
    def __init__(self):
        self.name_model = "DistilBert"
        self.clf = pipeline('sentiment-analysis')
        
    def pred(self, text):
        """
            Sentiment analysis on a text.
            Input:
                - text : str
            Output:
                - score of the prediction [-1,1]
        """
        res_raw = self.clf(text)
        if res_raw[0]['label'] == "NEGATIVE":
            return(res_raw[0]['score']*(-1))
        else:
            return(res_raw[0]['score'])
            
    def pred_df(self, df, bool_multip=False):
        """
            Sentiment analysis on a dataframe.
            Input:
                - df : pandas dataframe
                - bool_multip : True if we want to use multiprocessing of python
            Output:
                - df : pandas dataframe with a new column 'sent' (sentiment score)
        """
        print("... prediction on df")
        if bool_multip:
            with mp.Pool(8) as pool:
                df['senti'] = list(tqdm(pool.map(self.pred, df['text']),total=len(df)))
        else:
            tqdm.pandas()
            df["sent"]  = df["text"].progress_apply(self.pred)
        
        df["distilbert_nb_pos"] = np.where(df["distilb_score"] > 0.3, 1, 0)
        df["distilbert_nb_neu"] = np.where((df["distilb_score"]  >= -0.3)&(df["distilb_score"]  <=0.3) , 1, 0)
        df["distilbert_nb_neg"] = np.where(df["distilb_score"] < -0.3, 1, 0)
        return df
    
    def pred_file(self,  file):
        """
           Sentiment analysis on a csv file.
           Input:
               - path_dir : the path of the directory
               - file : the file name
        """
        if ".csv" in file:
            t0 = time.time()
            tmp = file.split('.')
            new_filename =  tmp[0]+'_sentiment.csv'
            print("... new file : "+new_filename)
            df = pd.read_csv(file, encoding='utf-8')
            df = self.pred_df(df)
            df.to_csv(new_filename)
            print('... {} save : ok'.format(new_path_file))
            t1 = time.time()
            total = t1-t0
            print(total)
        else:
            print("... It's not a csv file.")
            
                
                
def main():
    args = sys.argv[1:]
    if len(args) == 2 and args[0] == '-file':
        file = args[1]
        print('... process on file : ',file)
        cfl_sent = Sentiment_DistilBert()
        cfl_sent.pred_file(file )
   
    
if __name__ == "__main__": 

    main()
