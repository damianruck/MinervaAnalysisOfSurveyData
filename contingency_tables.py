import survey_utils
import pandas as pd
import itertools
from scipy.stats import chi2_contingency

class contingency_table_analysis:
    def __init__(self, survey):
        self.survey = survey
        
    def pairwise_chi2_from_contingency(self):

        df = self.df_contingency_table
        df += 0.000001 #deal with zeros in the contingency table

        responses = [i for i in df.columns]

        response_pairs = list(itertools.combinations(responses, 2))

        df_list = []
        for rp in response_pairs:

            rp = [i for i in rp]
            df_rp = df[rp]
            g, p, dof, expctd = chi2_contingency(df_rp)
            df_list.append(pd.Series(rp + [g, p]))

        df_chi = pd.concat(df_list,1).T
        df_chi.columns = ['r1', 'r2', 'chi_squared', 'p']
        df_chi = df_chi.sort_values('chi_squared',ascending = False)

        directory_latex = 'chi_squared/latex_tables/{s}/{c}/{n}/{m}/'.format(
            s=self.survey.survey_name, c=self.survey.country, n=self.q1, m=self.q2)
        survey_utils.create_directory(directory_latex)

        directory_csv = 'chi_squared/csv_tables/{s}/{c}/{n}/{m}/'.format(
            s=self.survey.survey_name, c=self.survey.country, n=self.q1, m=self.q2)
        survey_utils.create_directory(directory_csv) 

        print('-------------- contingency ----------------------------------------------------------------------')
        print(df_chi)
        survey_utils.save_txt(df_chi.to_latex(index=True), directory_latex+'chi_squared.tex')
        df_chi.to_csv(directory_csv+'chi_squared.csv')
        print() 

        return df_chi
        
    def save_contingeny_table(self, q1, q2):

        all_codes = survey_utils.load_json('question_decode/all_codes.json')
        df_r = self.survey.data

        df = (df_r.groupby([q1, q2]).sum()["Weight"]).unstack(level=1)
        
        self.df_contingency_table = df
        self.q1 = q1
        self.q2 = q2

        directory_latex = 'contingency/latex_tables/{s}/{c}/{n}/{m}/'.format(
            s=self.survey.survey_name, c=self.survey.country, n=q1, m=q2)
        survey_utils.create_directory(directory_latex)

        directory_csv = 'contingency/csv_tables/{s}/{c}/{n}/{m}/'.format(
            s=self.survey.survey_name, c=self.survey.country, n=q1, m=q2)
        survey_utils.create_directory(directory_csv) 

        print('-------------- contingency ----------------------------------------------------------------------')
        print(df)
        survey_utils.save_txt(df.to_latex(index=True), directory_latex+'contingency.tex')
        df.to_csv(directory_csv+'contingency.csv')
        print() 

    def save_contingeny_table_media(self, media_ques, ques_capitol):

        all_codes = survey_utils.load_json('question_decode/all_codes.json')
        df_r = self.survey.data

        if media_ques == 'sources':
            ii_media = [i for i in df_r.columns if i.startswith('q1_')]

        if media_ques == 'trust':
            ii_media = [i for i in df_r.columns if i.startswith('q2_')]

        df_list = []
        for q in ii_media:
            dd = df_r[df_r[q] == 'Mentioned'].groupby([ques_capitol]).sum()['Weight']
            dd.name = q
            df_list.append(dd)

        df = pd.concat(df_list,1)
        df.columns = [all_codes[c] for c in df.columns.values]
        
        self.df_contingency_table = df
        self.q1 = media_ques
        self.q2 = ques_capitol
        
        ##### save contingency tables to file

        directory_latex = 'contingency/latex_tables/{s}/{c}/{n}/{m}/'.format(
            s=self.survey.survey_name, c=self.survey.country, n=ques_capitol, m=media_ques)
        survey_utils.create_directory(directory_latex)

        directory_csv = 'contingency/csv_tables/{s}/{c}/{n}/{m}/'.format(
            s=self.survey.survey_name, c=self.survey.country, n=ques_capitol, m=media_ques)
        survey_utils.create_directory(directory_csv) 

        print('-------------- contingency ----------------------------------------------------------------------')
        print(df)
        survey_utils.save_txt(df.to_latex(index=True), directory_latex+'contingency.tex')
        df.to_csv(directory_csv+'contingency.csv')
        print() 
