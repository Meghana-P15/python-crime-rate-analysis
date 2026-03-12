#Importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("ggplot")

#Loading dataset
data=pd.read_csv("CrimeRate.csv",sep=",",header=0)

#Converting to DataFrame
df=pd.DataFrame(data) 
print(df)

#Setting state names as index
df1=df.set_index("States")

#-----Line graph-----
df1.plot(kind='line',linewidth=3,linestyle='dashed',marker='o',markersize=8)

plt.title("Crime Rate")
plt.xlabel("Years")
plt.ylabel("States")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.show()

#-----Bar graph-----
df1.plot(kind='bar',color=['#1f77b4','#ff7f0e','#2ca02c','#d62728'])

plt.title("Crime Rate Comparison by Year")
plt.xlabel("States")
plt.ylabel("Crime Rate")
plt.legend(title="Year")
plt.show()
