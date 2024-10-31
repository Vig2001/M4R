n <- 100# change this
t_effect <- 2 # change this
n_sim <- 1000
pvals <- rep(0, times = n_sim)
treat_coef <- rep(0, times = n_sim)

nsaa_baseline <- rnorm(2*n,
                       mean = 17.3,
                       sd = 4.4)
treatment <- rep(c(0,1), each = n)

nsaa_final <- t_effect*treatment + 3.8*nsaa_baseline + rnorm(2*n,
                                                           sd = 5.6)
plot(nsaa_baseline, nsaa_final, col=1+treatment)
cor(nsaa_baseline, nsaa_final)

for(i in 1:n_sim){
  nsaa_baseline <- rnorm(2*n,
                         mean = 15,
                         sd = 4)
  treatment <- rep(c(0,1), each = n)
  
  nsaa_final <- t_effect*treatment - 0.8*nsaa_baseline + rnorm(2*n,
                                                        sd = 4)
  
  df <- data.frame(nsaa_baseline = nsaa_baseline,
                   nsaa_final = nsaa_final,
                   treatment = treatment)
  
  fit0 <- lm(nsaa_final ~ nsaa_baseline + treatment,
             data = df)
  fit0_sum <- summary(fit0)
  treat_coef[i] <- fit0_sum$coefficients[3,1]
  pvals[i] <- fit0_sum$coefficients[3,4]
  
}
