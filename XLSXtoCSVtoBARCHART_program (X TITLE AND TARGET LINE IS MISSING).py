# Import the necessary modules
import matplotlib.pyplot as plt
import pandas as pd
# Seaborn is a visualization library and is built on top of matplotlib
import seaborn as sns

sns.set()

# Convert xlsx file to csv
read_file = pd.read_excel(r'C:\\Users\\user\\Desktop\\MStestdata.xlsx')
read_file.to_csv(r'C:\\Users\\user\\Desktop\\MStestdata_converted.csv', index = None, header=True)
  
# Initialize the lists for X and Y
data = pd.read_csv('C:\\Users\\user\\Desktop\\MStestdata_converted.csv')

# plt.bar(x=data['Units'],
#         y=data['Activation Rate'])

df = pd.DataFrame(data)

# Drop first row by selecting all rows from first row onwards
# df.iloc[row_start:row_end , col_start, col_end]
# df = df.iloc[1: , :]

# [:, column]
X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])
  
# Plot the data using bar() method
plt.bar(X, Y, color='g')
# plt.bar(X2, Y, color='r')
plt.title("% Activation Rate by Unit (MSBI)")
plt.xlabel("Units")
plt.ylabel("Activation Rate")

# Rotate by 45 degrees to avoid overlapping labels
plt.xticks(rotation=45)
  
# Show the plot
plt.show()