#html ui 

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title(":green[Explorative Data Analysis]")
st.sidebar.header("Created by :blue[Khusbu Champaneria.]")
st.sidebar.subheader("By Under guidence :blue[Dr.Ronak Panchal]")

uploaded_file = st.file_uploader("Upload a file", type="csv")
#if file_uploader is not None:
    # Process the uploaded file
    #st.write("File uploaded successfully!")
    # Do something with the file, such as reading its contents
    #df = file_uploader.read(file)
    #st.write("File contents:", df)
#else:
 #   st.write("No file uploaded.")

# Check if a file has been uploaded
if uploaded_file is not None:
    # Read the uploaded CSV file
    df = pd.read_csv(uploaded_file)
   

if st.button('Get data'):
    # This display will go away with the user's next action.
    st.write(df)


if st.button('Get columns'):
    # This display will go away with the user's next action.
    st.write(df.columns)

if st.button('Total RowColumn'):
    # This display will go away with the user's next action.
    st.write(df.shape)
if st.button('Details'):
    # This display will go away with the user's next action.
    st.write(df.info())

if st.button('Description'):
    # This display will go away with the user's next action.
    st.write(df.describe())

#if st.button('Duplication'):
    # This display will go away with the user's next action.
 #   st.write(df.duplicated())
if st.button('Numericcolumdata'):
    # This display will go away with the user's next action.
    numeric_columns = df.select_dtypes(include='number').columns.tolist()
    st.write(numeric_columns)
    
if st.button('Correlation'):
    # This display will go away with the user's next action.
    correlation_matrix = df.corr()
    st.write(correlation_matrix)


if st.button('Graph'): 
        st.set_option('deprecation.showPyplotGlobalUse', False)       
        plt.hist(df, bins=20)
        st.pyplot()


#if st.button('onlyGraph'):
#    fig, ax = plt.subplots()
#    for column in df.columns:
#        ax.plot(df[column], label=column)
#    ax.set_xlabel('X-axis label')
#    ax.set_ylabel('Y-axis label')
#    ax.set_title('Data Visualization')
#    ax.legend()
#    st.pyplot(fig)

if st.button("GRAPH1"):
    st.write("line chart")
    st.line_chart(df)



