## Contents
1. [Project Overview](README.md#project-overview)
2. [Project I](README.md#comments-on-feature-1)
3. [Project II](README.md#comments-on-feature-2)
4. [Project I Review and Results](README.md#comments-on-feature-3)
5. [Project II Review and Results](README.md#comments-on-feature-4)
6. [Feature 6](README.md#comments-on-feature-5)

## Project Overview

The following sets of data stored on UCI Machine Learning Repository System  
  o Default of credit card clients and  
  o Online Shoppers Purchasing Intention 

## Project I

Interesting trends were identified such as, client group with the highest credit limit does show the best trend (dccc-pay-trend-creditable-clients.png) however there is time fluctuations, may be due to risk-factors involved in investments.


## Project II

This project analyzed online shoppers’ behavioral analysis such as shoppers online time-spent at various stages of shopping, weekly and month time preferences for shopping and other numerical and categorical features to predict whether a customer will be ended up with shopping (revenue True) or not (revenue False).

## Project I Review and Results 

We found the ratio of the number of clients who paid bill on time varies from month to month (mostly increases). However this trend varies in terms of clients attributes. Clients' balance with respect to the mean is distributed within two STD can be claimed with 95% confidence. We applied several Machine Learning algorithms to make predictions whether a customer will be a default or not, and compared their performance using classification report and ROC score.

We also found other interesting trends. As for example, client group with the highest credit limit does show the best trend in terms of paying full bill on time, however there exists time fluctions may be due to risk factor involved in credit investment.


## Project II Review and Results 

We found the largest group in terms of visitor type who did shopping is returning visitor and they mainly shop more in preferred months such as Nov, May, Mar, Dec. However, the new visitors shop pretty much all the year round.  We also found the weekdays and weekend shopping from month to month month show similar trends. Shoppers who ended up in buying visit the shopping site more frequently and spent more time in viewing the product as well (pearson-correlation(ranked)-UCI-online-shoppers-int_.png). 95% confidence interval of product related duration with respect to the mean is close to 2 times the STD. We found the Ensemble Gradient Boosting Classifier as the best classifier with ROC score 0.78 and precision 0.93.

We applied high performing Machine Learning Model to predict whether a shopper would ended up with revenue positive or negative based on various attributes such as online time-spent, shopping time preferences and other attributes as well. Based on the above prediction online shoppers can be grouped into cluster so that the companies can offer coupons to certain group of customers to increase their revenue.

We found the average value for a web page that a user visited before completing an e-commerce transaction has highest correlation. All attributes were ranked (pearson-correlation(ranked)-UCI-online-shoppers-int_.png). 


## Feature 5 




