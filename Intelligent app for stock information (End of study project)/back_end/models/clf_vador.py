# coding=utf-8
# Autor : Daro HENG
# Email :  hendgaro1@gmail.com
# Date creation : 18/03/2021


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sys
from tqdm import tnrange, tqdm
import pandas as pd
import numpy as np

class Vader_Sentiment:
    def __init__(self):
        self.name_model = "Vader"
        self.analyzer = SentimentIntensityAnalyzer()

    def pred(self, text):
        """
            This function detects the sentiment of the text.
            Input :
                - text: text to process.
            Ouptut : 
                - dict : result sentiment polarity.
      
        """
        return self.analyzer.polarity_scores(text)

    def pred_df(self, df, bool_reddit=False):
        """
            This function detects the sentiment of the text in a csv file.
            Input :
                - df : dataframe to process.
            Ouptut : 
                - df : dataframe processed.
      
        """
        score_comp = []
        score_neu = []
        score_neg = []
        score_pos = []
        for i,s in enumerate(tqdm(df['text'])):
            res = self.pred(s)
            score_comp.append(res["compound"])
            score_neg.append(res['neg'])
            score_pos.append(res['pos'])
            score_neu.append(res['neu'])

        df["vaderCompound"] = score_comp
        df["vaderNeg"] = score_neg
        df["vaderPos"] = score_pos
        df["vaderNeu"] = score_neu

 
        if bool_reddit :
            df["vaderScoreP"] = df['vaderCompound']*df['score_reddit']
            df["vader_nb_pos"] = np.where(df["vaderCompound"] > 0, 1, 0)
            df["vader_nb_neu"] = np.where(df["vaderCompound"] == 0, 1, 0)
            df["vader_nb_neg"] = np.where(df["vaderCompound"] < 0, 1, 0)   

        else:
            df["vaderScoreP"] = df["vaderCompound"] * (df["likes"]+1)
            df["vader_nb_pos"] = np.where(df["vaderScoreP"] > 0, 1, 0)
            df["vader_nb_neu"] = np.where(df["vaderScoreP"] == 0, 1, 0)
            df["vader_nb_neg"] = np.where(df["vaderScoreP"] < 0, 1, 0)

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
            tmp[-1] = "vader_"+tmp[-1]
            new_path_file = "/".join(tmp)
        else:
            new_path_file = path_dir_output+"vader_"+tmp[-1]
        df.to_csv(new_path_file)
        print('... {} save : ok'.format(new_path_file))
        print('... end vader sentiment anlysis')

    
def main():
    args = sys.argv[1:]
    if len(args) >= 2 and args[0] == '-file':
        file = args[1]
        path_dir_output = ''
        if len(args) >= 4 and args[2] == '-path_out':
            path_dir_output = args[3]
        print('... process Vader Sentiment Analysis on file : ',file)
        vader = Vader_Sentiment()
        vader.pred_file(file, path_dir_output=path_dir_output)


if __name__ == "__main__": 
    main()