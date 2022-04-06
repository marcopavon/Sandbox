# Import the necessary modules
import matplotlib.pyplot as plt
from numpy import NaN
import pandas as pd
import os

#Own libraries
from class_function import Csv
  
#print(f"This is the current directory, which you are in: {os.getcwd()}")
#print(f"Files in cwd: {os.listdir()}")
# Initialize the lists for X and Y
data = pd.read_csv("../Sandbox/prime.csv",  sep=',', index_col=False)
#print(data)

df = pd.DataFrame(data)
#print(df)
df['Ranking'] = df['Ranking'].replace(["No Ranking"],NaN)
df[' Prime'] = df[' Prime'].replace(["No Price"],NaN)
df['Ranking'] = pd.to_numeric(df['Ranking'])
df[' Prime'] = pd.to_numeric(df[' Prime'])
#df[' Date'] = pd.to_datetime(df[' Date'])
df[' Date with time'] = pd.to_datetime(df[' Date with time'])
df[' Postcode'] = df[' Postcode'].astype("Int64")
df[' Year of birth'] = df[' Year of birth'].astype("Int64")
print(df)
print(df.dtypes)



#Y = list(df.iloc[:,0])
#Y= df["Ranking"]
#print(Y.mean())
#Y = list(Y)
#print(Y)



#X = df[" Date"]
#print(X)

# Plot the data using bar() method
#plt.plot(X, Y, color='g')
data_mean = df.groupby([" Date"])["Ranking"].mean()
print(data_mean[:10])

print(set(df[" Date"]))


fig, axes = plt.subplots(nrows=2, ncols=2)
plt.subplots_adjust(hspace = 0.51)


df.groupby([" Date"]).agg(
    {
    "Ranking" : "mean",
    #" Prime" : "mean"
    }
).plot(kind = "bar", ax=axes[0,0])

df.groupby([" Date"]).agg(
    {
    #"Ranking" : "mean",
    " Prime" : "mean"
    }
).plot(kind = "bar", ax=axes[0,1])

df.groupby([" Postcode"]).agg(
    {
    "Ranking" : "mean",
    #" Prime" : "mean"
    }
).plot(kind = "bar", ax=axes[1,0])

df.groupby([" Coverage"]).agg(
    {
    "Ranking" : "mean",
    #" Prime" : "mean"
    }
).plot(kind = "bar", ax=axes[1,1])


plt.title("Avergae Ranking on Comparis")
plt.xlabel("Date")
plt.ylabel("Ø Ranking")


# Show the plot
plt.show()

