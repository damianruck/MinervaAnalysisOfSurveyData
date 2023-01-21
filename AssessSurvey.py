import load_data
import reformat_survey_metadata
import survey_utils

class LoadSurvey:
    def __init__(self, survey, country):
        if survey == 'Capitol':
            self.survey_name = survey
            self.country = country
            self.direct = "Wave 2 Spring 2021/Surveys/SPSS/"
             
            #load question decoder (these codes were dervided using the Belarus survey)
            directory = 'question_decode/'
            self.capitol_riots_questions = survey_utils.load_json(directory+'capitol_riots_questions.json')
            self.trust_media_consumption = survey_utils.load_json(directory+'media_trust.json')
            self.normal_media_consumption = survey_utils.load_json(directory+'media_consumption.json')
            self.dem_decode = survey_utils.load_json(directory+'demographics.json')
            
            self.merged_decoder = survey_utils.merge_dicts(
                        self.normal_media_consumption,
                        self.trust_media_consumption,
                        self.capitol_riots_questions,
                        self.dem_decode
                      )
         
        print('load data from {c}...'.format(c=country))
        
        self.filename = "Survey-SPSS-Spring-2021-{c}.sav".format(c=country)
        self.data = load_data.load_survey_data(self.direct, self.filename)
        self.data = reformat_survey_metadata.standardize_metadata(self.data, survey, country)
        
