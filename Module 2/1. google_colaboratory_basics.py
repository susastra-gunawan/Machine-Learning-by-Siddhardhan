# -*- coding: utf-8 -*-
"""Google Colaboratory - Basics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h_ke6fkVCA21whUwLPvAwDOx7AD1j-Dw

System Specifications
"""

#!cat /proc/cpuinfo

#!cat /proc/meminfo

"""Installing Libraries"""

#!pip install pandas

import pandas as pd

df = pd.read_csv('/content/BostonHousing.csv')

df.head()

print('Machine Learning')

#!ls