
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
from scipy import stats


# In[4]:


df=pd.read_csv("body_fat.csv")


# In[5]:


df['zscore_age'] = (df.Age - df.Age.mean())/df.Age.std(ddof=0)
df['zscore_%fat'] = (df.perFat - df.perFat.mean())/df.perFat.std(ddof=0)



# In[38]:


new_col=['zscore_age','zscore_%fat']
new_df=pd.DataFrame(df[new_col])


# In[39]:


new_df.corr(method='pearson', min_periods=1)


# In[47]:


xi=df['zscore_age']
y=df['zscore_%fat']


# In[57]:




slope, intercept, r_value, p_value, std_err = stats.linregress(xi,y)
line = slope*xi+intercept

trace = go.Scatter(
    x = df['zscore_age'],
    y = df['zscore_%fat'],
    mode="markers",
    name= 'Age vs Body Fat %'
)

trace2= go.Scatter(
    x= xi,
    y= line,
    mode="lines",
    name='Fit')

annotation = go.Annotation(
                  x=0,
                  y=2.5,
                  text='Pearson correlation coefficient  = 0.8176',
                  showarrow=False,
                  font=go.Font(size=16)
                  )

layout = go.Layout(
                title='Correlation between Age and %Body Fat',
                annotations=[annotation]
                )

data=[trace,trace2]
fig = go.Figure(data=data, layout=layout)

py.iplot(fig, filename='basic_line')


# In[43]:


new_df.cov(min_periods=None)

