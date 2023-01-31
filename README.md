# **Passport requests prediction**
This is the **Final Teamwork Capstone Project** which aimed to solve a real-world data science & AI problem, as part of the **Data Science For All (DS4A)** bootcamp program organized by Correlation One and the Colombian Ministry for the Information and Communication Technologies.

***Disclaimer:*** Given the sensible nature of the data used for this project, and following the Rules and Regulations implemented during the program, the raw and processed data, the adjusted *Prophet* model and the name of the institution, are not included in this repository.

## **Project description**
Several governmental institutions in Colombia had been facing issues regarding passport emission. This was due to the copious amount of requests that were temporarily suspended during the nationwide 2020 lockdown for COVID-19 and the increasing number of requests coming from nationalized immigrants. Therefore, the institutional capacity was exceeded, resulting in a myriad of unattended requests and the accumulation of petitions, complaints and claims (PCCs) from citizens with poor customer satisfaction. 

In order to solve this problem, two key deliverables were suggested: 

1. A forecast for the demand of passports under the new adverse conditions and a normal / more stable scenario, which would result in a more efficient planning and resource allocation for the institution

2. A recommendation system for users, to allow the opportune submission of requests, considering variables such as: the passport expiry date, the number of unclaimed passports, the required paperwork, etc.

All this with the purpose of stabilizing the number of requests submitted through time, which would improve service levels and eventually translate into a lower number of PCCs received.

## **Objectives**
- To provide the local government of Boyacá with analytical tools that can help them handle the growing demand for passports in the region and make data-driven decisions.
- To forecast the weekly demand of passports in the institution.
- To present the results obtained in an easily accessible dashboard for the entity's employees.

## **Project Deliverables**
- For the first part of the problem a prophet model was fitted and mainly used to forecast the weekly number of passport requests, this kind of model “implements a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects” (Prophet package, 2021).

- Due to data limitations, it was not possible to build a recommender system to provide the users with insights about their passports. Instead, a word cloud with the most common words used by the users who submitted claims or complaints was provided in the dashboard.