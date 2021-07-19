import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

db=pd.read_excel('user_cvrg_20210719.xls', header=1)
sb.countplot(data=db, x = '유입채널(마감)' )

