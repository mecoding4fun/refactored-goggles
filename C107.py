import pandas as pd
import plotly.express as px
import csv
import math
import plotly.graph_objects as go


df = pd.read_csv('Data3.csv')
# print(df.groupby('level')['attempt'].mean())
# print(p)
# f = go.Figure(go.Bar(x=p.groupby('level')['attempt'].mean(),
#     y=['Level 1','Level 2','Level 3','Level 4'],orientation='h'))
# f.show()
mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
f = px.scatter(mean, x="student_id", y="level", size="attempt",color="attempt")
f.show()
# print(df.groupby('student_id')['level'].mean())
