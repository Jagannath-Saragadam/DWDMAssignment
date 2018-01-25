# DWDMAssignment

Using the data for age and body fat given below:

 age | 23 | 23 | 27 | 27 | 39 | 41 | 47 | 49 | 50
 --- | -- | -- | -- | -- | -- | -- | -- | -- | -- 
%fat | 9.5 | 26.5 | 7.8 | 17.8 | 31.4 | 25.9 | 27.4 | 27.2 | 31.2

 age | 52 | 54 | 54 | 56 | 57 | 58 | 58 | 60 | 61
 --- | -- | -- | -- | -- | -- | -- | -- | -- | -- 
%fat | 34.6 | 42.5 | 28.8 | 33.4 | 30.2 | 34.1 | 32.9 | 41.2 | 35.7

**Answer the following:**

1.Normalize the two attributes based on z-score normalization.

2.Calculate the correlation coefficient (Pearson’s product moment coefficient). Are these two attributes positively or negatively correlated? Compute their covariance.

<h2> Solutions </h2>

**1. Z-scored Normalised data**

```python

df['zscore_age'] = (df.Age - df.Age.mean())/df.Age.std(ddof=0)
df['zscore_%fat'] = (df.perFat - df.perFat.mean())/df.perFat.std(ddof=0)

```

Age |	perFat |	zscore_age |	zscore_%fat
--- | ------ | ----------- | ------------ 
23 |	9.5 |	-1.825011 |	-2.144104
23 |	26.5 |	-1.825011 |	-0.253883
27 |	7.8 |	-1.513635 |	-2.333126
27 |	17.8 |	-1.513635 |	-1.221231
39 |	31.4 |	-0.579506 |	0.290946
41 |	25.9 |	-0.423818 |	-0.320596
47 |	27.4 |	0.043247 |	-0.153812
49 |	27.2 |	0.198935 |	-0.176050
50 |	31.2 |	0.276779 |	0.268708
52 |	34.6 |	0.432467 |	0.646752
54 |	42.5 |	0.588155 |	1.525149
54 |	28.8 |	0.588155 |	0.001853
56 |	33.4 |	0.743843 |	0.513325
57 |	30.2 |	0.821687 |	0.157518
58 |	34.1 |	0.899531 |	0.591157
58 |	32.9 |	0.899531 |	0.457730
60 |	41.2 |	1.055220 |	1.380603
61 |	35.7 |	1.133064 |	0.769061

**2. Pearson Corealtion Factor**


![Pearson Coefficent](https://github.com/Jagannath-Saragadam/DWDMAssignment/blob/master/pearson.svg)

```python
new_df.corr(method='pearson', min_periods=1)
```

r= 0.817619


![Scatter PLot](https://github.com/Jagannath-Saragadam/DWDMAssignment/blob/master/basic_line.png)
