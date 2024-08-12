import streamlit as st
import pandas as pd
from io import StringIO

st.title('Bank Statement Report Generator')

st.write("## Enter your bank transactions below:")

# User input for transactions
with st.form(key='transaction_form'):
    st.write("### Add a Transaction")
    date = st.date_input('Date')
    description = st.text_input('Description')
    amount = st.number_input('Amount', format="%.2f")
    balance = st.number_input('Balance', format="%.2f")

    submit_button = st.form_submit_button(label='Add Transaction')

    if submit_button:
        # Create a new DataFrame or load existing data
        if 'data' not in st.session_state:
            st.session_state.data = pd.DataFrame(columns=['Date', 'Description', 'Amount', 'Balance'])

        new_row = pd.DataFrame([[date, description, amount, balance]], columns=['Date', 'Description', 'Amount', 'Balance'])
        st.session_state.data = pd.concat([st.session_state.data, new_row], ignore_index=True)
        st.write("Transaction added!")

# Display the transactions
st.write("## Transactions")
if 'data' in st.session_state and not st.session_state.data.empty:
    st.write(st.session_state.data)

    # Option to download the report
    @st.cache
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')

    csv = convert_df(st.session_state.data)
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name='bank_statement_report.csv',
        mime='text/csv'
    )
else:
    st.write("No transactions to display.")
