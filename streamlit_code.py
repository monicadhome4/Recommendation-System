#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import Project_2_Group_06

#st.title('Recommendation System Based on Popularity:sunglasses:')

#st.header("Popular books for you")

#if st.button('Recommend books'):
 #   for i in range(0,30):
 #       import streamlit as st

# Using HTML to set the font size
 #       st.write("<p style='font-size: 20px;'> " + Project_2_Group_06.top_popular_books.iloc[i, 0] + "</p>", unsafe_allow_html=True)
#        st.image(Project_2_Group_06.top_popular_books.iloc[i,6])
#        st.write("Book Name :",Project_2_Group_06.top_popular_books.iloc[i,0])
 #       st.write("Average Rating:",Project_2_Group_06.top_popular_books.iloc[i,1])
 #       st.write("Number of Rating:",Project_2_Group_06.top_popular_books.iloc[i,2])
#        st.write("Author:",Project_2_Group_06.top_popular_books.iloc[i,3])
 #       st.write("Year of Publication:",Project_2_Group_06.top_popular_books.iloc[i,4])
 #       st.write("Publisher:",Project_2_Group_06.top_popular_books.iloc[i,5])
        
        


# In[11]:


# Initialize the Streamlit app and set page configuration
st.set_page_config(page_title='Recommendation System', layout='wide')

st.title('Recommendation System for similar users :sunglasses:')

st.header("Welcome to Library")
input = st.number_input('Enter UserID')
if st.button("Login"):
    if (input not in Project_2_Group_06.filtered_data["User-ID"]):
        
        for i in range(0,500):
            st.write("<p style='font-size: 20px;'> " + Project_2_Group_06.top_popular_books.iloc[i, 0] + "</p>", unsafe_allow_html=True)
            st.image(Project_2_Group_06.top_popular_books.iloc[i,6])
            st.write("Book Name :",Project_2_Group_06.top_popular_books.iloc[i,0])
            st.write("Average Rating:",Project_2_Group_06.top_popular_books.iloc[i,1])
            st.write("Number of Rating:",Project_2_Group_06.top_popular_books.iloc[i,2])
            st.write("Author:",Project_2_Group_06.top_popular_books.iloc[i,3])
            st.write("Year of Publication:",Project_2_Group_06.top_popular_books.iloc[i,4])
            st.write("Publisher:",Project_2_Group_06.top_popular_books.iloc[i,5])
        
    else:
        recommendation = Project_2_Group_06.Recommend(input)
        recommendation = recommendation[["Book-Title","Book-Rating","Book-Author","Year-Of-Publication","Publisher","Image-URL-M"]]
        length = len(recommendation)
        if (length != 0):
            for i in range(0,length):
                st.write("<p style='font-size: 20px;'> " + recommendation.iloc[i, 0] + "</p>", unsafe_allow_html=True)
                st.image(recommendation.iloc[i,5])
                st.write("Book Name :",recommendation.iloc[i,0])
                st.write("Book-Rating:",recommendation.iloc[i,1])
                st.write("Book-Author:",recommendation.iloc[i,2])
                st.write("Year-Of-Publication:",recommendation.iloc[i,3])
                st.write("Publisher:",recommendation.iloc[i,4])
            
        else:
            
            for i in range(0,10):
                st.write("<p style='font-size: 20px;'> " + Project_2_Group_06.top_popular_books.iloc[i, 0] + "</p>", unsafe_allow_html=True)
                st.image(Project_2_Group_06.top_popular_books.iloc[i,6])
                st.write("Book Name :",Project_2_Group_06.top_popular_books.iloc[i,0])
                st.write("Average Rating:",Project_2_Group_06.top_popular_books.iloc[i,1])
                st.write("Number of Rating:",Project_2_Group_06.top_popular_books.iloc[i,2])
                st.write("Author:",Project_2_Group_06.top_popular_books.iloc[i,3])
                st.write("Year of Publication:",Project_2_Group_06.top_popular_books.iloc[i,4])
                st.write("Publisher:",Project_2_Group_06.top_popular_books.iloc[i,5])
        

