# This module helps rss_scraper_freq_dist.py via providing a method for
# frequency distribution calculation based on nltk FreqDist method. It uses
# rss_scraper_tokenizedtext_class and its method to scrape the feed and
# instantiate tokenized text.

import nltk, re, pprint
from nltk.corpus import stopwords
from rss_scraper_tokenizedtext_class import *

class FreqDist:
    """A simple attempt to model a frequency distribution. """

    def freq_dist():
        punctuation = [".", ":", ",", ";", "!", "?", "\"", "'", "-", "(",
        ")", "[", "]", "{", "}", "’", "“", "”", "*", "%", "``", "—", "--", "...",
        "‘", "–", "''", "&", "'s", "@", "n't", "©", "...."]
        stop_words = set(stopwords.words('english'))
        freq_dist_list = []
        tokenized_text = RssTokenizedText.tokenize()
        for x in range(len(tokenized_text)):
            article = tokenized_text[x]
            for entry in article:
                if entry.lower() not in stop_words:
                    if entry not in punctuation:
                        freq_dist_list.append(entry)
                        freq_dist_list = freq_dist_list[:]
        return freq_dist_list