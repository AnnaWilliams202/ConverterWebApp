from converter import convert_excel_to_csv
import streamlit as st

st.title('Excel to CSV converter')
st.write('Upload your Excel file to convert to CSV')

uploaded_file = st.file_uploader('Choose an excel file', type=['xlsx','xls'])
if uploaded_file is not None:
    csv_data = convert_excel_to_csv(uploaded_file)
    st.download_button(label="Download CSV",
                       data=csv_data,
                       file_name='converted.csv',
                       mime='text/csv')


# run in terminal: streamlit run webApp.py
