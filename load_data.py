import pandas as pd

def load_survey_data(direct, filename):
    
    df = pd.read_spss(direct+filename)

    print('number of participants: ', df.shape[0])
    print('number of entries: ', df.shape[1])
    
    return df