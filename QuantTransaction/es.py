#!/usr/bin/python
# -*- coding:utf-8 -*-

from __future__ import  print_function

import matplotlib.pyplot as plt
import pandas as pd


es =pd.io.parsers.read_csv('./CSV/600808.csv', index_col="date")
es['close'].plot()
plt.show()