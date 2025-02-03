import pandas as pd
import matplotlib as plot
import matplotlib.pyplot as plt
import matplotlib.animation as animation


df=pd.read_csv("C:/Users/sharm/Downloads/2025-01-29 Modern Bhatti june-month_ vegetables prices(Sheet1).csv")





plt.title("Vegetables Price" )
plt.xlabel("Dates")
plt.xticks(rotation = 90)
plt.ylabel("Price per kg(Rs)")
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.grid(True)


plt.show()
print(df)
    