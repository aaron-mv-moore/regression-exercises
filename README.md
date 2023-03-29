# Zillow Data: Linear REgression

## Description
- This repository has been created to hold work related to linear regression using a Zillow dataset. It will go through the data science pipeline and attempt to create a model that accuratle predicts diferent outcomes related to properties in the dataset.

## Goals
- Predict the values of single unit properties using the obervations from 2017
  - Construct a ML linear regression model that accurately predicts values
  - Deliver a report that a non-data scientist can read through and understand 

## Initial Questions
1. Can we predict the values of single unit properties using the obervations from 2017?
2. What features are drivers for the values of single unit properties?

## Plan
- Acquire data from MySQL
- Prepare data
  - Remove unnecessary features
  - Identify and replace missing values
  - Alter innapropriate data types
- Explore the data to find drivers and answer intital questions
- Create a model to predict values
  - Use features identified in explore to build predictive models
  - Evaluate models on train and validate data
  - Select the best model based on TBD
  - Evaluate the best model on test data
- Conclude with recommendations and next steps

## Data Dictionary
| Feature | Definition | 
|:--------|:-----------|
| beds | The number of bedrooms |
| baths | The number of bathrooms |
| square_feet | The number of calculated finished square feet |
| tax_value | Total tax assessed value of the property |
| year_built | The year the property was built |
| tax_amount | Total assessed property tax |
| fips | Federal Information Processing System (FIPS) Codes for States and Counties FIPS codes are numbers which uniquely identify geographic areas. |

## Steps to Reproduce
1. Clone this repo
2. Insert credentials in the blank_eny.py file and save
3. Run notebook

## Takeaways
- TBD

## Recommendations
- TBD
