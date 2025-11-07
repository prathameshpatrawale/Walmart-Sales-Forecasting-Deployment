# <center> Walmart Sales Forecasting using the Best ML algorithms

![alt test](https://github.com/RawatMeghna/Walmart-Sales-Forecasting-using-Best-ML-algorithms/blob/main/Others/Wallmart1.jpg)

The objective of this project is to develop a Walmart sales forecasting model using the best machine learning algorithms. The project involves understanding and cleaning up the dataset, building regression models to predict sales based on single and multiple features, evaluating model performance using metrics like RMSE, and performing data exploration, manipulation, feature selection, and predictive modeling. The project aims to provide insights into the dataset and conclude with reliable sales forecasts for Walmart.

## <center> Description:

One of the leading retail stores in the US, Walmart, would like to predict the sales and demand accurately. There are certain events and holidays which impact sales on each day. There are sales data available for 45 stores of Walmart. The business is facing a challenge due to unforeseen demands and runs out of stock some times, due to the inappropriate machine learning algorithm. An ideal ML algorithm will predict demand accurately and ingest factors like economic conditions including CPI, Unemployment Index, etc.

Walmart runs several promotional markdown events throughout the year. These markdowns precede prominent holidays, the four largest of all, which are the Super Bowl, Labour Day, Thanksgiving, and Christmas. The weeks including these holidays are weighted five times higher in the evaluation than non-holiday weeks. Part of the challenge presented by this competition is modeling the effects of markdowns on these holiday weeks in the absence of complete/ideal historical data. Historical sales data for 45 Walmart stores located in different regions are available.

### <center> Dataset Info:
This is the historical data that covers sales from 2010-02-05 to 2012-11-01, in the files 'stores' and 'features'. Within this file you will find the following fields :-

* Store - the store number
* Date - the week of sales
* Weekly_Sales -  sales for the given store
* IsHoliday - whether the week is a special holiday week 1 – Holiday week 0 – Non-holiday week
* Temperature - Temperature on the day of sale
* Fuel_Price - Cost of fuel in the region
* CPI – Prevailing consumer price index
* Unemployment - Prevailing unemployment rate

## <center> Strategic Planning

We aim to solve the problem statement by creating a plan of action, Here are some of the necessary steps:

1. Importing Libraries
2. Loading Dataset
3. Data Exploration
4. Data Preprocessing
5. Feature Selection/Extraction
6. Predictive Modelling
7. Project Outcomes & Conclusion
8. model dumping using pickle
9. creating a simple streamlit app to deploy the model

### <center> Project Outcomes & Conclusion
* Weekly_sales are impacted because of rate of Unemployment as when the rate of unemployment increases people only buy during holiday seasons, as there are only few outliers present for weekly_sales and which are on the day of Holiday. Speaking of which people only buy necessary products and try to save more.

* The Sales are very high during November and December and go down in January. So its better to employee more staff as casual employee in November and December and encourage permanent staff to take leaves during January.

* The predicted sales data can be used to analyse the sales pattern and accordingly adjust the staff in the store.

* As sales increases by a slight margin when temperature is less, hence it states people prefer to go for shopping in less temperatures unless it is a holiday week.

* The CPI is not normally distributed and line regression plot is showing how CPI is varying with Weekly_Sales on days of Holidays and non holiday weeks

* CPI, Fuel_Price are positively correlated with Weekly_Sales whereas, rate of Unemployment is fairly negatively correlated and we have seen drop in weekly_sales of Products due to increase of rate of unemployment.

* Top performing stores according to the historical data are Store number 20, 4, 14, 13, 2

* Worst performing stores according to the historical data are Store number 33, 5, 36, 38, 3. The difference between the highest and lowest performing stores 3608700.2 for Weekly_Sales.



* There are quarters in which stores major loss, due to high rate of unemployment, mostly during the spring sem altogether we can expect less weekly_sales as compared to spring semester.

* Mostly people try to buy expensive products during the holiday seasons likely to be christmas and Super bowl days where we have seen rise in weekly_sales of Product.

* Store 20 is overall doing fine in terms of Weekly_sales, as analysed it is the only store with max weekly_sales, whereas Store 35 has no particular pattern of Weekly_Sales due to high variance observed.

* Walmart should invest in marketing of expensive products during the spring sem, to get more customer base for such products, also should only open the supply chain for the prodcuts which are in demand during that season.

### <center> Here are some of the key outcomes of the project:
- The Dataset was quiet small with just 6435 samples & after preprocessing 7.5% of the datasamples were dropped. 
- Visualising the distribution of data & their relationships, helped us to get some insights on the feature-set.
- The features had high multicollinearity, hence in Feature Extraction step, we shortlisted the appropriate features with VIF Technique.
- Testing multiple algorithms with default hyperparamters gave us some understanding for various models performance on this specific dataset.
- It is safe to use multiple regression algorithm performed better than other algorithms, as their scores were quiet comparable & also they're more generalisable.



