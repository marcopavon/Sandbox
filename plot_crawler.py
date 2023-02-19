# Import the necessary modules
from asyncore import read
from turtle import title
import matplotlib
import matplotlib.pyplot as plt
from numpy import NaN
import pandas as pd
import re
import datetime
import os, sys
from  builtins import any


#personal lib


"""
from test_regex import update_csv_output
update_csv_output()
"""

# reading line by line
with open('./Crawler/prime.csv', 'r') as f:
   
    # store in text variable
    text = f.read()
     
    # getting the pattern for [],(),{}
    # brackets and replace them to empty string
    # creating the regex pattern & use re.sub()
    pattern = re.sub(r"[\[\]\"\']", "", text)
 
 
# Appending the changes in new file
# It will create new file in the directory
# and write the changes in the file.
with open('./Sandbox/prime_output.csv', 'w') as my_file:
    my_file.write(pattern)


#Own libraries
from class_function import Csv
  
#print(f"This is the current directory, which you are in: {os.getcwd()}")
#print(f"Files in cwd: {os.listdir()}")
# Initialize the lists for X and Y
data = pd.read_csv("./Sandbox/prime_output.csv",  sep=',', index_col=False)
data_delay = pd.read_csv("./Crawler/delay.csv",  sep=',', index_col=False)
print(data)


df_delay = pd.DataFrame(data_delay)
print(df_delay[' Duration ELVIA'])
df_delay[' Duration ELVIA'] = df_delay[' Duration ELVIA'].replace("ELVIA not listed",NaN)
df_delay[' Duration ELVIA'] = pd.to_numeric(df_delay[' Duration ELVIA'])
df_delay['Date'] = pd.to_datetime(df_delay['Date'])
df_delay['Week'] = df_delay['Date'].dt.week
df_delay['Month'] = df_delay['Date'].dt.month
df_delay['Year'] = df_delay['Date'].dt.year

df = pd.DataFrame(data)
df['Ranking'] = df['Ranking'].replace(["No Ranking"],NaN)
df[' Prime'] = df[' Prime'].replace(["No Price"],NaN)
df[' Coverage'] = df[' Coverage'].replace(r'\W|\s','',regex=True)
df['Ranking'] = pd.to_numeric(df['Ranking'])
df[' Prime'] = pd.to_numeric(df[' Prime'])
df[' Date'] = pd.to_datetime(df[' Date'])
df['Week'] = df[' Date'].dt.week.astype("Int64")
df['Week day'] = df[' Date'].dt.weekday.astype("Int64")
df['Month day'] = df[' Date'].dt.day.astype("Int64")
df['Month'] = df[' Date'].dt.month.astype("Int64")
df[' Date with time'] = pd.to_datetime(df[' Date with time'])
df[' Postcode'] = df[' Postcode'].astype("Int64")
df[' Year of birth'] = df[' Year of birth'].astype("Int64")
print(df)
#print(df_delay)
#print(df.dtypes)



#Y = list(df.iloc[:,0])
#Y= df["Ranking"]
#print(Y.mean())
#Y = list(Y)
#print(Y)



#X = df[" Date"]
#print(X)

# Plot the data using bar() method
#plt.plot(X, Y, color='g')
data_mean = df_delay.groupby(["Week"])[" Duration ELVIA"].mean()
print(data_mean[:10])

#print(set(df[" Date"]))


fig, axes = plt.subplots(nrows=3, ncols=3)
plt.subplots_adjust(hspace = 0.51)

fig.suptitle('Crawler Analysis Comparis')

fig.set_size_inches(18.5, 10.5, forward=True)



df.groupby(["Week"]).agg(
    {
    "Ranking" : "mean",
    #" Prime" : "mean"
    }
).plot(kind = "bar", ax=axes[0,0])

df.groupby(["Week"]).agg(
    {
    #"Ranking" : "mean",
    " Prime" : "count"
    }
).plot(kind = "bar", ax=axes[0,1])

df.groupby([" Postcode", " Coverage"]).agg(
    {
    "Ranking" : "mean",
    #" Prime" : "mean"
    }
).unstack(' Coverage').plot(kind = "bar", ax=axes[1,0])

df.groupby(["Week", " Year of birth"]).agg(
    {
    "Ranking" : "mean",
    #" Prime" : "mean"
    }
).unstack(' Year of birth').plot(kind = "line", ax=axes[1,1], title="Rankig per Coverage")

df.groupby(["Month day"]).agg(
    {
    "Ranking" : "mean",
    #"Ranking" : "mean"
    }
).plot(kind = "line", legend= True, ax=axes[1,2], title="Month Day Ranking")

df_delay.groupby(["Week"]).agg(
    {
    " Duration ELVIA" : "mean",
    " Duration fastest insurer" : "mean"
    }
).plot(kind = "bar", ax=axes[0,2], title="Average Response Time")


df.groupby(["Week", " Coverage"]).agg(
    {
    "Ranking" : "mean",
    #"Ranking" : "mean"
    }
).unstack(' Coverage').plot(kind = "bar", legend= True, ax=axes[2,0], title="Weekly Ranking development for Coverage")

df.groupby(["Week day", " Coverage"]).agg(
    {
    "Ranking" : "mean",
    #"Ranking" : "mean"
    }
).unstack(' Coverage').plot(kind = "line", legend= True, ax=axes[2,1], title="Weekday Ranking for Coverage")


df.groupby(["Month", " Coverage"]).agg(
    {
    "Ranking" : "mean",
    #"Ranking" : "mean"
    }
).unstack(' Coverage').plot(kind = "line", legend= True,ax=axes[2,2], title="Monthly Rankig for Coverage")

plt.title("Average Ranking on Comparis")
plt.xlabel("Date")
plt.ylabel("Ø Ranking")


plot_date = datetime.datetime.now().strftime("%Y-%m-%d")
path = "/home/pi/Dokumente/Code/Crawler/plots/"

#print(os.listdir(path))


if (any(plot_date in filename for filename in os.listdir(path))):
    print("exist")
else:
    plt.savefig(f"{path}crawler_{plot_date}.pdf")
    print("file created")


send()

# Show the plot
#plt.show()

