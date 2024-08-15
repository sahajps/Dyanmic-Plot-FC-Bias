import unittest
import os
import json
from app import create_app # type: ignore
from app.utils.returnplot import top_entities_sorted, polarity_score # Adjust the import as necessary
from datetime import datetime

class BasicTests(unittest.TestCase):
    def setUp(self):
        self.all_media = ['checkyourfact', 'politifact', 'snopes', 'altnews', 'boomlive', 'opindia']
        self.st_date = datetime(2018, 1, 1)
        self.en_date = datetime(2023, 12, 31)
        self.top_en_no = 5
        self.cache_file_path = "data/Test Case(s)/"

    def test_plot_data(self):
        """
        This function calculates polarity score for top 5 entities of each orgs (2018-2023: all times)
        At second stages it verify the cached results and print the success or failure
        """
        for f in self.all_media:
            top_senti_list = top_entities_sorted(f, self.st_date, self.en_date)
            PS = {}
            for k in list(top_senti_list)[:self.top_en_no]:
                PS[k] = round(polarity_score(top_senti_list[k]), 2)  # Cached results are round-off to two decimal places !!

            #Open Cache resuls to match
            with open(self.cache_file_path+f+'.json', 'r') as json_file:
                C_PS = json.load(json_file)

            if PS == C_PS:
                print("Test case passed for " + f + " :)")
            else:
                print("Test case failed for " + f + " :(")


if __name__ == '__main__':
    xx = 5
    unittest.main()
