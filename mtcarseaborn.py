import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv
mt_cars = pd.read_csv("mtcars.csv")
mt_cars = mt_cars.rename(columns = {"Unnamed: 0" : "car_model"})
#sns.lineplot(data = mt_cars[["mpg","cyl","qsec"]])
sns.lineplot(data = mt_cars[["mpg","cyl","qsec"]],markers = True);
