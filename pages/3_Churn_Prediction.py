import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from cleaning_data import correlation_matrix, customer_engagement


# Assuming customer_engagement and correlation_matrix are pre-defined DataFrames

# Correlation Heatmap
st.write("### Correlation Analysis Between Disengagement and Demographics")
# Displaying heatmap with 'viridis' colormap
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="Blues", ax=ax)
plt.title("Correlation Analysis Between Disengagement and Demographics")
st.pyplot(fig)



# Total Spend Trends by Disengagement Status
st.write("### Total Spend Trends by Disengagement Status")
# Group by year and disengagement status, and calculate the total spend
total_spend_trends = customer_engagement.groupby(['year', 'disengaged'])['total_spend'].sum().unstack()

# Customizing line colors for total spend trends
fig, ax = plt.subplots(figsize=(10, 6))
colors = ['#FF6347', '#4682B4']  # Example colors for two categories

# Plotting with custom colors
for i, disengaged_status in enumerate(total_spend_trends.columns):
    ax.plot(total_spend_trends.index, total_spend_trends[disengaged_status], label=f'Disengaged: {disengaged_status}', color=colors[i], lw=2)

# Customize the plot
ax.set_title("Total Spend Trends by Disengagement Status")
ax.set_xlabel("Year")
ax.set_ylabel("Total Spend")
ax.legend(title="Disengagement Status")
st.pyplot(fig)

# Purchase Frequency Trends by Disengagement Status
st.write("### Purchase Frequency Trends by Disengagement Status")
# Group by year and disengagement status, and calculate the total purchase frequency
purchase_frequency_trends = customer_engagement.groupby(['year', 'disengaged'])['frequency_of_purchase'].sum().unstack()

# Customizing line colors for purchase frequency trends
fig, ax = plt.subplots(figsize=(10, 6))
# Custom colors for the lines
for i, disengaged_status in enumerate(purchase_frequency_trends.columns):
    ax.plot(purchase_frequency_trends.index, purchase_frequency_trends[disengaged_status], label=f'Disengaged: {disengaged_status}', color=colors[i], lw=2)

# Customize the plot
ax.set_title("Purchase Frequency Trends by Disengagement Status")
ax.set_xlabel("Year")
ax.set_ylabel("Purchase Frequency")
ax.legend(title="Disengagement Status")
st.pyplot(fig)

