import pandas as pd
from io import StringIO

data="""
col1    col2    col3
A1  finished    1234
A2  ongoing 1235
A3  NaN 1236
A4  finished    1237
A5  started 1238
A6  finished    1239
"""

data_tsv = StringIO(data)

df = pd.read_csv(data_tsv, sep="\t", skiprows=1)

tab_not_finished = df[df['col2'] != 'finished']
print(tab_not_finished)