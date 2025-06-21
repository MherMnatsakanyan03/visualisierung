import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataframe = pd.read_csv("co2_data.csv")
# example of the dataframe:
# ,Country,Identifier,Year,Emissions
# 266,Afghanistan,AFG,2017,178502925
# 800,Albania,ALB,2017,277278189

####################
# Task 1a          #
####################
fig, ax1 = plt.subplots()
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')
plt.ylim(0,500)

# Sort the datagrame by Emissions in descending order
dataframe = dataframe.sort_values(by='Emissions', ascending=False)
# get the top 20 countries
top_20_countries = dataframe.head(20)
top_20_countries['Emissions'] = top_20_countries['Emissions'] * 10**-9

ax1.bar(top_20_countries['Country'], top_20_countries['Emissions'], color='steelblue', label='Emissions in Gt CO2')

####################
# Task 1b          #
####################
ax2 = ax1.twinx()
plt.ylim(0,1)

# Calculate the cumulative percentage of total emissions for the top 20 countries
total_emissions = dataframe['Emissions'].sum() * 10**-9
cumulative_percentage = top_20_countries['Emissions'].cumsum() / total_emissions

# Plot the cumulative percentage line (Pareto line)
ax2.plot(top_20_countries['Country'], cumulative_percentage, color='red', marker='o', label='Cumulative Percentage')
ax2.set_ylabel('Cumulative Percentage')

# Show the result
plt.title('Total CO2 Emissions 1751-2017')
plt.tight_layout()
plt.show()