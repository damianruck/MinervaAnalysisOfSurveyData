import pandas as pd

def standardize_metadata(df, survey, country):

    '''
    we need to standardizre the column headers and category names between all surveys.
    The standard is Belarus in the case of the Capitol riot survey.
    '''

    if survey == 'Capitol':
        if country == 'Ukraine':
            df.columns = [c.lower() for c in df.columns]
            df = df.rename(columns={'weight':'Weight'})
            
            cols = [c for c in df.columns if c.startswith('q1_')] + [c for c in df.columns if c.startswith('q2_')] 
            df_temp = df[cols].values
            df_temp[df_temp == 'Yes'] = 'Mentioned'
            df_temp[df_temp == 'No'] = 'Not Mentioned'
            df[cols] = df_temp

        if country == 'Georgia':
            df.columns = [c.lower() for c in df.columns]
            df = df.rename(columns={'weight1':'Weight'})

            cols = [c for c in df.columns if c.startswith('q1_')] + [c for c in df.columns if c.startswith('q2_')] 
            df_temp = df[cols].values
            df_temp[df_temp == 'Yes'] = 'Mentioned'
            df_temp[df_temp == 'No'] = 'Not Mentioned'
            df[cols] = df_temp
    return df