import streamlit as st
from cleaning_data import final_df


hshd_num_search = st.text_input("Enter HSHD_NUM to search for:")

if hshd_num_search:
    filtered_df = final_df[final_df['HSHD_NUM'].astype(str).str.contains(hshd_num_search)]
else:
    filtered_df = final_df

sort_by = st.selectbox("Sort by", options=["HSHD_NUM", "BASKET_NUM", "PURCHASE_", "PRODUCT_NUM", "DEPARTMENT", "COMMODITY"])

# Sorting the DataFrame based on the selected column
sorted_df = filtered_df.sort_values(by=sort_by)

# 3. Display the sorted DataFrame
st.write(f"Displaying data sorted by {sort_by}:")
st.dataframe(sorted_df)