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

Default of credit card clients data set consists of 24 attributes such as clients six-month pay records e.g.; whether month-to-month bill was paid on time or not, whether the pay amount was full or partial comparing to the bill amount and clients other attributes such as age, sex, marriage, education and credit card (CC) balance.  

## Project II

This project analyzed online shoppers’ behavioral analysis such as shoppers online time-spent at various stages of shopping, weekly and month time preferences for shopping and other numerical and categorical features to predict whether a customer will be ended up with shopping (revenue True) or not (revenue False).

## Project I Review and Results 

We found the ratio of the number of clients who paid bill on time varies from month to month (mostly increases). However this trend varies in terms of clients attributes such as education, marriage, etc. As for example, university and grad students show better trend comparing to HS students. Inferential statistical analysis shows that the 95% confidence interval of clients balance with respect to the mean is very close to two times the STD. We applied several Machine Learning algorithms to make predictions whether a customer will be a default or not default, and compared their performance using classification report and ROC score.

## Project II Review and Results 

We found the largest group in terms of visitor type who did shopping is returning visitor and theymainly shop more in preferred months such as Nov, May, Mar, Dec. However, the new visitors shop pretty much all the year round.  We also found the weekdays and weekend shopping from month to month month show similar trends. Shoppers who ended up in buying spent more time in viewing the product online. 95% confidence interval of product related duration with respect to the mean is close to 2 times the STD. We found the Ensemble Gradient Boosting Classifier as the best classifier with ROC score 0.78 and precision 0.93.

We applied high performing Machine Learning Model to predict whether a shopper would ended up with revenue positive or negative based on various attributes such as online time-spent, shopping time preferences and other attributes as well. Based on the above prediction online shoppers can be grouped into cluster so that the companies can offer coupons to certain group of customers to increase their revenue.

## Feature 5 




