# Interective Polarity Score Plot

This project is an additional part of the paper "Independent fact-checking organizations exhibit a departure from political neutrality" by Singh et al. (2024). 

[<img align="center" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PvkGku1cP-sph35SRBDyCwHEKLMZyBggCw&s" width="60" height="20"/>](https://arxiv.org/abs/2407.19498) [(Preprint)](https://arxiv.org/abs/2407.19498)         [<img align="center" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTFaHW69OfhzFN9xaGJf68IUddHqWSoE-dI5q_lOLElXvZ4jMKjXs0DAGTdzJS7Kid8vNU&usqp=CAU" width="90" height="35"/>](https://github.com/sahajps/FC-Bias)[(Data & Code)](https://github.com/sahajps/FC-Bias)

In the paper, `Figure 2` shows the extent of neutrality (−1 ≤ P S ≤ 1) for the top-k = 5 most frequent political entities per fact-checking organization. PolitiFact, Snopes, and Check Your Fact are in the USA. Alt News, OpIndia, and Boom are based in India. Polarity Score (PS) establishes “how” the coverage of the political entities in the fake news leads to a positive, negative, or neutral image of the entity, impacting the reader’s perception. A higher neutrality is observed if PS ≈ 0. Meanwhile, a score closer to -1 (1) highlights a more pessimistic/critical (positive/promoting) tone.

## Why This Project?

In the paper, the Propensity Score (PS) is shown only for the top 5 entities and is presented year-wise. However, a reader might be more interested in examining the neutrality of fact-checking media during specific events (e.g., the farmers' protest in India). Researchers often face space constraints in papers, limiting the ability to present various permutations and combinations of figures. Therefore, I came up with the idea to create a tool that allows our readers to explore more.

## Setup (For user)
1. Clone the repository.
 ```sh
   git clone https://github.com/sahajps/FC-PolarityScore
   cd FC-PolarityScore
 ```
   
2. Install dependencies:
 ```sh
   pip install -r requirements.txt
 ```
3. To run the flask-web application:
 ```sh
   python3 run.py
 ```
4. Follow your local host link or put the following link in your web browser.
 ```sh
   127.0.0.1:5000/
 ```
## Maintenance (For developer)
There are three subdir-level README files to detail the functionality of [app](https://github.com/sahajps/FC-PolarityScore/blob/main/app/README.md), [data](https://github.com/sahajps/FC-PolarityScore/blob/main/data/README.md), and [tests](https://github.com/sahajps/FC-PolarityScore/blob/main/tests/README.md).
The high-level repo looks like the following:

```plaintext
FC-PolarityScore/
├── app/
│   ├── __init__.py         # Application factory and configuration
│   ├── routes.py           # Define the routes/endpoints
│   ├── utils/              # Ploting and returning plot data
│   │   ├── plotter.py
│   │   └── returnplot.py
│   ├── templates/          # HTML templates
│   │   ├── index.html
│   │   └── about.html
│   └── static/             # Static files (CSS, JS, images)
│       ├── style.css
│       └── script.js
│
├── data/
│   ├── Topic Sentiment Data/
│   │   └── *.json
│   ├── Test Case(s)/
│   │   └── *.json
│   └── README.md            # Discription of .json data
│
├── tests/
 ├── test_routes.py          # Unit tests for routes
 ├── test_graph_data.py      # Tests for polarity score values
│   └── README.md            # Details about tests
│
├── .gitignore               # Git ignore file
├── config.py                # Secret key can be added if any !!
├── README.md                # Project overview
├── requirements.txt         # Python dependencies
└── run.py                   # Entry point to Flask app
```

## Cite
If you find the website or data useful (this or root github for paper), do cite!! This must ring a bell. 🔔
```sh
   @article{singh2024independent,
      title={Independent fact-checking organizations exhibit a departure from political neutrality},
      author={Singh, Sahajpreet and Masud, Sarah and Chakraborty, Tanmoy},
      journal={arXiv preprint arXiv:2407.19498},
      year={2024}
   }
```