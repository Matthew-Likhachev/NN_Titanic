import numpy as np
import pandas as pd

#matters:
# PassengerId
# Survived 0 = No, 1 = Yes
# Pclass - Ticket class 1 = 1st, 2 = 2nd, 3 = 3rd
# Sex
# Age
# SibSp - of siblings / spouses aboard the Titanic
# Parch - of parents / children aboard the Titanic
# Cabin - Cabin number
colunms = ['PassengerId','Pclass','Pclass','Sex','Age','SibSp', 'Parch','Cabin' ,'Survived']
titanic_data = pd.read_csv('train.csv', sep=',', usecols = colunms)
cond_fem = titanic_data["Sex"] =='female'
column_name = 'Sex'
cond_male = titanic_data["Sex"] =='male'

#titanic_data.loc[cond_fem, column_name,cond_male,column_name] = 0,1
print(titanic_data)