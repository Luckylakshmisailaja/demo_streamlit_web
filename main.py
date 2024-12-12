import streamlit as st
# import pandas as pd
# dataset = pd.read_csv("Salary_Data.csv")
# st.dataframe(dataset)

name = st.text_input("Enter your name :")
father_name = st.text_input("Enter your father name :")
address = st.text_area("Enter your Address here :")
class_data = st.selectbox('Enter your class :',(1,2,3,4,5,6,7,8,9,10))

button = st.button("Done")
if button:
    st.markdown(f"""
    Name: {name}
    Father Name : {father_name}
    Address : {address}
    Class : {class_data}
""")











# st.title("Welcome to MyWorld")
# st.header("Python")
# st.subheader("Java")
# st.markdown("I love streamlit")
# st.code("""for i in range(1,5,1):
#     print("Hello!!!")""")
