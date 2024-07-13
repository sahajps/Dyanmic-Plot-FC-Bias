# Interective Polarity Score Plot

This project is an additional part of paper `Independent fact-checking organizations exhibit a departure from political neutrality` by `Singh et al.`. 

In the paper `Figure 2` shows extent of neutrality (−1 ≤ P S ≤ 1) for the top-k = 5 most frequent policial entities per fact- checking organization. PolitiFact, Snopes, and Check Your Fact are in the USA. Alt News, OpIndia, and Boom are based in India. Polarity Score (PS) establishes “how” the coverage of the political entities in the fake news leads to positive, negative, or neutral image for the entity, impacting the reader’s perception. A higher neutrality is observed if PS ≈ 0. Meanwhile, a score closer to -1 (1) highlights a more pessimistic/critical (positive/promoting) tone.

## Why This Project?

In the paper, the Propensity Score (PS) is shown only for the top 5 entities and is presented year-wise. However, a reader might be more interested in examining the neutrality of fact-checking media during specific events (e.g., the farmers' protest in India). Researchers often face space constraints in papers, limiting the ability to present various permutations and combinations of figures. Therefore, I came up with the idea to create a tool that allows our readers to explore more.

## Setup
1. Clone the repository.
   ```sh
   git clone https://github.com/sahajps/FC-PolarityScore
   
2. Install dependencies:
   ```sh
   pip install -r requirements.txt

3. To run the flask-web application:
   ```sh
   python3 run.py
   
4. Follow your local host link or put the following link in your web browser.
   ```sh
   127.0.0.1:5000/
   
## Mentainance (For developers)
1. `Data/Topic Sentiment Data/*.json` contains the following data:
    ```sh
    date_year: Year of article publication
    date_month: Month of article publication
    date_day: Day of month of article publication
    sentiments: is a dic with key as a polical entity and value as image portrayed (say positive or negative !!)
    
Note: Articles (Title and Text) columns are removed in this version of data to make the processing and access of data fast. You can access the data from root github of the paper.
    
2. `app/utils/returnplot.py`'s function returns the plot for PS with several inputs (filters on webpage).

## Cite
If you find the website or data useful (this or root github for paper), do cite!! This must ring a bell. 🔔
```sh
    Bibtex will be added soon.
