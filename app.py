import streamlit as st
import pandas as pd


st.title("Qalashetra's Product Management System")

df=pd.read_csv('database.csv')


options_form=st.form("options_form")

prod_id=options_form.text_input("Product ID")
prod_name=options_form.text_input("Product Name")
category=options_form.text_input("Category")
artist=options_form.text_input("Artist")
qty=options_form.selectbox("Quantity",('1','2','3','4','5','6','7'))
price=options_form.text_input("Price")
soldon=options_form.selectbox("Sold on",('2023-10-27','2023-10-28','2023-10-29'))
mode=options_form.selectbox("Payment Mode",('Online','Cash'))

add_data=options_form.form_submit_button()
if add_data:
    new_data={'Product ID':prod_id,'Product Name':prod_name,'Category':category,'Artist':artist,'Qty':qty,
              'Price':price,'Sold On':soldon,'Payment Mode':mode}
    df=df.append(new_data,ignore_index=True)
    df.to_csv('database.csv',index=False)

st.header('Recently Added')
st.write(df.tail(1))