## Data Description

#### 1. Topic Sentiment Data
`data/Topic Sentiment Data/*.json` contains the following data:
```sh
date_year: Year of article publication
date_month: Month of article publication
date_day: Day of month of article publication
sentiments: A dic with key as a political entity and value as image portrayed (say positive or negative !!)
```

Note: Articles (Title and Text) columns are removed in this version of data to make the processing and access of data fast. You can access the data from the root GitHub of the paper.

#### 2. Test Case(s)
`data/Test Case(s)/*.json` contains the data for the base test case of plot-data. For the base test case the conditions over-different fields are as follows:
```
date-range: From Jan 1st, 2018 To Dec 31st, 2023
top-entities: 5
order: Frequency-based
```