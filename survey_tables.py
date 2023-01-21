import pandas as pd
import survey_utils

def save_tables_for_count_and_proportions_of_a_question(survey, q, decode_name=True):

    df = survey.data
    if decode_name:
        name = survey.merged_decoder[q]
    else:
        name = q

    directory_latex = 'tables/latex_tables/{s}/{c}/{n}/'.format(s=survey.survey_name, c=survey.country, n=q)
    survey_utils.create_directory(directory_latex)
    
    directory_csv = 'tables/csv_tables/{s}/{c}/{n}/'.format(s=survey.survey_name, c=survey.country, n=q)
    survey_utils.create_directory(directory_csv)    
    
    print('Latex tables are saved to {d}'.format(d=directory_latex))
    print('')
    print('')    
    print('CSV tables are saved to {d}'.format(d=directory_csv))
    print('')
    print('') 

    df_count = df[q].value_counts()
    df_proportion = (df[q].value_counts()/df_count.sum()).round(2)

    df_count.name = name
    df_proportion.name = name

    # print and save the results to latex files
    print('----------------------------------------------------------------------------------------------------')
    print(name)

    print('-------------- counts ----------------------------------------------------------------------')
    print(df_count)
    survey_utils.save_txt(df_count.to_latex(index=True), directory_latex+'counts.tex')
    df_count.to_csv(directory_csv+'counts.csv')
    print() 

    print('-------------- proportions -----------------------------------------------------------------------')
    print(df_proportion)
    survey_utils.save_txt(df_proportion.to_latex(index=True), directory_latex+'proportions.tex')
    df_proportion.to_csv(directory_csv+'proportions.csv')

    #print('-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o')
    #print('-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o')
    print('')
    print('')
