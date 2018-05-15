#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 16:10:02 2018

@author: rashinigam
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# Step 1: Understand the problem: About dataset, Data Summary

stats = pd.read_csv('Bikesharing.csv')
print stats.head(3)
stats.describe()
stats.info()
stats.shape #No. of records in dataset
stats.dtypes #datatypes of columns or variables

#Substep: Feature Engineering the columns "season","Month" and "weather" should be of "categorical" data type.
stats.Month = stats.Month.astype('category')
stats["season"] = stats.season.map({1: "Spring", 2 : "Summer", 3 : "Fall", 4 :"Winter" })
stats["weather"] = stats.weather.map({1: " Clear + Few clouds + Partly cloudy + Partly cloudy",\
                                        2 : " Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist ", \
                                        3 : " Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds", \
                                        4 :" Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog " }) 
categoryVariableList = ["season","weather","Month"]
for var in categoryVariableList:
    stats[var] = stats[var].astype("category")
stats.Month.cat.categories
stats.season.cat.categories
stats.weather.cat.categories


# Step 2: Univariable study i.e focus on Devpendent variable i.e. Count in this case

#Step3: Multivariate study: Relationship with other indepedednt variables

#Step 4: Basic cleaning handle missing data, outliers, categorical variables
# Sub step: Missing value analysis for the rows that have missing or null data
null_data = stats[stats.isnull().any(axis=1)]
print null_data

# Skewness in Distribution : Not able to understand

"""Outlier Analysis through Box Plot - Need to clarify. At first look, "count" variable contains lot of outlier data points which skews the distribution towards right (as there are more data points beyond Outer Quartile Limit).But in addition to that, following inferences can also been made from the simple boxplots given below.

Spring season has got relatively lower count.The dip in median value in boxplot gives evidence for it.
Most of the outlier points are mainly contributed from "Working Day" than "Non Working Day". It is quiet visible from from figure 4."""
import seaborn as sn
fig, axes = plt.subplots(nrows=2,ncols=2)
fig.set_size_inches(12, 10)
sn.boxplot(data=stats,y="count",orient="v",ax=axes[0][0])
sn.boxplot(data=stats,y="count",x="season",orient="v",ax=axes[0][1])
sn.boxplot(data=stats,y="count",x="Month",orient="v",ax=axes[1][0])
sn.boxplot(data=stats,y="count",x="workingday",orient="v",ax=axes[1][1])
axes[0][0].set(ylabel='Count',title="Box Plot On Count")
axes[0][1].set(xlabel='Season', ylabel='Count',title="Box Plot On Count Across Season")
axes[1][0].set(xlabel='Hour Of The Day', ylabel='Count',title="Box Plot On Count Across Months Of The Year")
axes[1][1].set(xlabel='Working Day', ylabel='Count',title="Box Plot On Count Across Working Day")

#Substep: Removing outliers in the Count column - Not clear
#dailyDataWithoutOutliers = dailyData[np.abs(dailyData["count"]-#dailyData["count"].mean())<=(3*dailyData["count"].std())] 
#print ("Shape Of The Before Ouliers: ",dailyData.shape)
#print ("Shape Of The After Ouliers: ",dailyDataWithoutOutliers.shape)

#Step5: Test assumptions
#Summarizing data across years
#Distribution:
fig=plt.figure()
ax = fig.add_subplot(1,1,1)
ax.hist(stats["season"])
plt.title('BIke Rental Count')
plt.xlabel("season")
plt.ylabel("count")
plt.show()
visl = sns.distplot(stats["count"])
visl = sns.distplot(stats["count"], bins = 30)
#CHART 1: Boxplots
vis2 = sns.boxplot(data=stats, x="Year", y = "count")

#CHART 2: Jointplot

j= sns.jointplot(data=stats, x= 'Year', y = 'count')

#Chart 3 Histograms

sns.set_style("white")
m1 = sns.distplot(stats.count, bins = 15)
sns.set_style("dark")
#m2 = sns.distplot(movies.CriticRating, bins = 15)
sns.set_style("darkgrid")

#CHART4: KDE Plot Kernel Density Estimate from Seaborn Library

vis1 = sns.lmplot(data = stats, x='Year', y= 'count',\
                  fit_reg = False, hue = 'count', \
                  size=5, aspect =1)
k1 = sns.kdeplot(stats.count, shade = True, shade_lowest = False, cmap = 'Reds')

#CHART 5: Violin Plots
z = sns.violinplot(data=stats, x='Year', y= 'count')

z1 = sns.violinplot(data=stats, x='season', y= 'count')

#Chart 6: Function plots
#season = [1,2,3,4]
plt.plot(stats.count, c = 'Blue', ls = '--', marker = 's', ms = 7)
plt.xticks(list(range(0,4)), season)
plt.show()

