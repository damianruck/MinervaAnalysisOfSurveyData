# MinervaAnalysisOfSurveyData

None of the data is included in the repo, this will need to be sent seperately

Thr following are the important notebooks for repeating the analysis

## 1. create_df_for_regressions.ipynb

This takes the raw survey data and creates the variables to be used in the regression. It saves the data
to three csv files for each of Ukraine, Belarus and Georgia as follows:

```
'{c}_regression.csv'.format(c=country)
```
## 2. regression.R

This takes the regression variiables (saved as csvs in the last step). and produces the regression results.

It automatically saves the various results into a new structured directory. Encoded as follows:

```
direct <- paste('regression_results/',country,'/', dp,'/',cf,
                '/',mq[1],'/',as.character(v), '/' , sep='')
...

write.csv(df_m,paste(direct,'marginal_effects_capitol_ord.csv',sep=''), row.names = FALSE)
save(glm.fit, file = paste(direct,"regression_capitol_ord.rda",sep=''))
```

## 3. Display_marginal_effects_multiple_regressions.ipynb

Takes the regression results produced in step 3, and grpahically represents the marginal effects. It saves the images to file.

## 4. descriptive_plots.ipynb

Takes the regresion variables from the outout of step 1 and creates descriptive plots of the variables. Saves them to file.



