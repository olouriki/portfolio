# coding=utf-8
# Autor : Daro HENG
# Email :  hendgaro1@gmail.com
# Date creation : 19/03/2021


from textblob import TextBlob
import sys
from tqdm import tnrange, tqdm
import pandas as pd
import numpy as np

class Sentiment_TextBlob:
    def __init__(self):
        self.name = "TextBlob"

    def pred(self, text):
        """
            This function detects the sentiment of the text.
            Input :
                - text: text to process.
            Ouptut : 
                - int : sentiment polarity.
      
        """
        analysis = TextBlob(text)
        if analysis.sentiment.polarity > 0:
            return 1
        elif analysis.sentiment.polarity == 0:
            return 0
        else:
            return -1

    def pred_df(self, df):
        """
            This function detects the sentiment of the text in a csv file.
            Input :
                - df : dataframe to process.
            Ouptut : 
                - df : dataframe processed.
      
        """
        df['textBlob_score'] = df['text'].apply(self.pred)
        df["textBlob_pos"] = np.where(df["textBlob_score"] > 0, 1, 0)
        df["textBlob_neu"] = np.where(df["textBlob_score"] == 0, 1, 0)
        df["textBlob_neg"] = np.where(df["textBlob_score"] < 0, 1, 0)
        return df

    def pred_file(self, path_file, path_dir_output=''):
        """
            This function detects the sentiment of the text in a csv file.
            Input :
                - path_file : file path.
                - path_dir_output : path to the directory to save.
      
        """
        df = pd.read_csv(path_file, encoding='utf-8')
        df = self.pred_df(df)
        
        tmp = path_file.split('/')
        if path_dir_output=='':
            tmp[-1] = "txtblob"+tmp[-1]
            new_path_file = "/".join(tmp)
        else:
            new_path_file = path_dir_output+"txtblob_"+tmp[-1]
        df.to_csv(new_path_file)
        print('... {} save : ok'.format(new_path_file))
        print('... end txtblob sentiment anlysis')


def main():
    args = sys.argv[1:]
    if len(args) >= 2 and args[0] == '-file':
        file = args[1]
        path_dir_output = ''
        if len(args) >= 4 and args[2] == '-path_out':
            path_dir_output = args[3]
        print('... process txtblob Sentiment Analysis on file : ',file)
        txtBlob_model = Sentiment_TextBlob()
        txtBlob_model.pred_file(file, path_dir_output=path_dir_output)


if __name__ == "__main__": 
    main()