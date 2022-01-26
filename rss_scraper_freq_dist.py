# This program creates frequency distribution list and most common 200
# frequency distributions excluding punctuation and stopwords based on
# nltk Freqqist method for all the entries combined from rss/atom feed
# by scraping the feed after the url for the feed is provided by the user.
# It uses rss_scraper_freqdist_class and its method to calculate frequency
# distribution which uses rss_scraper_tokenizedtext_class and its method to
# scrape the feed and instantiate tokenized text

import nltk, re, pprint
from rss_scraper_freqdist_class import *

frequency_distribution_list = FreqDist.freq_dist()
fdist_rss = nltk.FreqDist(frequency_distribution_list)
fdist_200 = fdist_rss.most_common(200)
result = print("Name of frequency distrubution list: 'fdist_rss' \
Name of most common 200 frequency distrubutions list: 'fdist_200'")

#https://www.globalhungerindex.org/case-studies/rss.xml