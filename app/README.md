## App Structure

1. At `/` path two major files are there `__init__.py` to initialize the Flask app and `routes.py` mostly defines the routers pass on the conditional data to the plotter function.

2. In `/static` folder on style files is there one script to get the data from UI to the backend and check conditions as if the start date is later than the end date, another is to make website dynamics if there is a change in any condition request the backend to change the plot.

3. `/utils` path has two Python scripts `plotter.py` calls the "gen_plot" function from `returnplot.py` [Functionilty is detailed in PEP documentation]. 