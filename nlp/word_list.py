# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 17:45:29 2023

@author: Boris
"""

import json

# emergency words
lst = ["work", "family", "study", "job", "finance", "relationship", 
       "health", "exam", "deadline", "expectation", "trauma", "grief",
       "parent", "isolation", "discrimination", "change", "conflict",
       "insecurity", "burnout", "overcommitment", "illness", "poverty",
       "abuse", "unemployment", "bullying"]


with open("word_list.json", "w") as f:
    json.dump(lst, f, ensure_ascii=False, indent=4)
