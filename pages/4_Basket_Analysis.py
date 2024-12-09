import streamlit as st
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from cleaning_data import encoded_df, final_df

# Streamlit UI
st.title("Association Rules for Retail Basket Analysis")

# Ensure data is properly formatted (encoded_df should be a one-hot encoded DataFrame)
if encoded_df.empty:
    st.error("Encoded data is empty. Please check your data preprocessing.")
else:
    # Generate frequent itemsets with apriori
    frequent_itemsets = apriori(encoded_df, min_support=0.001, use_colnames=True)

    # Display frequent itemsets
    if not frequent_itemsets.empty:
        st.subheader("Frequent Itemsets")
        st.dataframe(frequent_itemsets)
    else:
        st.warning("No frequent itemsets generated. Please try with a lower min_support.")

    # Generate association rules from frequent itemsets
    if not frequent_itemsets.empty:
        rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.1)
    else:
        rules = pd.DataFrame()

    # Displaying the association rules if they exist
    if not rules.empty:
        st.subheader("Association Rules")
        
        # Display the rules table
        st.dataframe(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head())
        
        # Provide a summary
        st.write(f"Number of rules generated: {len(rules)}")
        
        # Allow user to filter by support or confidence if desired
        min_support = st.slider("Minimum Support", 0.001, 0.1, 0.01, 0.001)
        min_confidence = st.slider("Minimum Confidence", 0.1, 1.0, 0.5, 0.01)
        
        # Filter rules based on user input
        filtered_rules = rules[(rules['support'] >= min_support) & (rules['confidence'] >= min_confidence)]
        
        # Display filtered rules
        st.subheader("Filtered Association Rules")
        st.dataframe(filtered_rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
    else:
        st.write("No association rules generated with the current thresholds.")
