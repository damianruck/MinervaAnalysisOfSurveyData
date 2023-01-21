#install.packages("margins")
#install.packages('stargazer')
library("margins")
library('stargazer')

setwd("/Users/damianruck/Documents/UTK_stuff_survey/Public Opinion")
print(getwd())

#print(names(df))

dep <- c("capitol_weak_strong", "capitol_weak_noeffect", "capitol_strong_noeffect")
dep <- c("capitol_ordinal")#, "capitol_effect_noeffect")

#country_future <- c("country_future_russia_eu", "country_future_dontknow_eu", "country_future_russia_dontknow")
country_future <- c("country_future_ordinal")

media_ques <- list( c("trust_russian", "trust_digital"), c("source_russian", "source_digital") )

for (country in c('Ukraine', 'Belarus', 'Georgia')) {
    reg <- list()
    reg_cnt <- 1
  for (dp in dep) {
    for (mq in media_ques) {

    for (cf in country_future) {
        v <- 1
        print(cf)
        equations <- list(
          c(mq[1], mq[2]),
          c(mq[1], mq[2], cf),
          c(mq[1], mq[2], cf, 'age', 'education', 'rural', 'wealth', 'female')
        )
        for (variables in equations) {
          
          fn <- paste(country,'_regression.csv', sep='')
          df = read.csv(fn,header = TRUE)
          
          direct <- paste('regression_results/',country,'/', dp,'/',cf,
                          '/',mq[1],'/',as.character(v), '/' , sep='')
          
          print(direct)
          
          dir.create(file.path(direct), recursive = TRUE, showWarnings = FALSE)
          
          outcome <- dp
          f <- as.formula(paste(outcome, paste(variables, collapse = " + "), sep = " ~ "))   
          glm.fit <- glm(f, family=binomial(link='logit'), na.action = na.exclude, data = df)
          #print(summary(glm.fit))
          m <- margins(glm.fit)
          
          #print(summary(m))
          #png(filename=paste(direct,'marginal_plot.png',sep=''))
          #jpeg(file="saving_plot1.jpeg")
          #plot(m)
          #dev.off()
          # print(summary(glm.fit))
          
          reg[[reg_cnt]] <- glm.fit
          reg_cnt <- reg_cnt + 1
          
          df_m <- data.frame(summary(m))
          write.csv(df_m,paste(direct,'marginal_effects_capitol_ord.csv',sep=''), row.names = FALSE)
          save(glm.fit, file = paste(direct,"regression_capitol_ord.rda",sep=''))
          v <- v+1
          
        }
        
        
    }

    }
  }
  order = c(1,2,9,10,3,4,5,6,7,8,11)
  sg <- stargazer(reg, keep.stat="n", order=order) # float.env = "sidewaystable",
  cat(paste(sg, collapse = "\n"), "\n")
}

# 
