# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 23:32:56 2023

@author: Rohith Challam
"""

import streamlit as st
import pickle
import numpy as np

def recommend(book):
    index = np.where(pivot_table.index==book)[0][0]
    similar_books =sorted(list(enumerate(similarity[index])),key=lambda x:x[1],reverse=True)[1:11]
    
    data = []
    for i in similar_books:
        item = []
        temp_df = books[books['Book-Title'] == pivot_table.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        
        data.append(item)
    return data

st.header("Book Recommender System")
popular_books = pickle.load(open('popular_25.sav','rb'))
books = pickle.load(open('books.sav','rb'))
pivot_table= pickle.load(open('pivot_table.sav','rb'))
similarity = pickle.load(open('similarity.sav','rb'))

book_list = pivot_table.index.values
image_url = popular_books['Image-URL-M'].tolist()
book_title = popular_books['Book-Title'].tolist() 
book_author = popular_books['Book-Author'].tolist()
no_of_ratings = popular_books['no_of_ratings'].tolist()
avg_ratings = popular_books['avg_ratings'].tolist()

st.sidebar.title("Top 25 Books")
if st.sidebar.button("SHOW"):
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.image(image_url[0])
        st.text(book_author[0])
        st.text("Ratings:" + str(no_of_ratings[0]))
        st.text("Avg.Rating:" + str(round(avg_ratings[0],2)))
    with col2:
        st.image(image_url[1])
        st.text(book_author[1])
        st.text("Ratings:" + str(no_of_ratings[1]))
        st.text("Avg.Rating:" + str(round(avg_ratings[1],2)))
    with col3:
        st.image(image_url[2])
        st.text(book_author[2])
        st.text("Ratings:" + str(no_of_ratings[2]))
        st.text("Avg.Rating:" + str(round(avg_ratings[2],2)))
    with col4:
        st.image(image_url[3])
        st.text(book_author[3])
        st.text("Ratings:" + str(no_of_ratings[3]))
        st.text("Avg.Rating:" + str(round(avg_ratings[3],2)))
    with col5:
        st.image(image_url[4])
        st.text(book_author[4])
        st.text("Ratings:" + str(no_of_ratings[4]))
        st.text("Avg.Rating:" + str(round(avg_ratings[4],2)))
        
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.image(image_url[5])
        st.text(book_author[5])
        st.text("Ratings:" + str(no_of_ratings[5]))
        st.text("Avg.Rating:" + str(round(avg_ratings[5],2)))
    with col2:
        st.image(image_url[6])
        st.text(book_author[6])
        st.text("Ratings:" + str(no_of_ratings[6]))
        st.text("Avg.Rating:" + str(round(avg_ratings[6],2)))
    with col3:
        st.image(image_url[7])
        st.text(book_author[7])
        st.text("Ratings:" + str(no_of_ratings[7]))
        st.text("Avg.Rating:" + str(round(avg_ratings[7],2)))
    with col4:
        st.image(image_url[8])
        st.text(book_author[8])
        st.text("Ratings:" + str(no_of_ratings[8]))
        st.text("Avg.Rating:" + str(round(avg_ratings[8],2)))
    with col5:
        st.image(image_url[9])
        st.text(book_author[9])
        st.text("Ratings:" + str(no_of_ratings[9]))
        st.text("Avg.Rating:" + str(round(avg_ratings[9],2)))

    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.image(image_url[10])
        st.text(book_author[10])
        st.text("Ratings:" + str(no_of_ratings[10]))
        st.text("Avg.Rating:" + str(round(avg_ratings[10],2)))
    with col2:
        st.image(image_url[11])
        st.text(book_author[11])
        st.text("Ratings:" + str(no_of_ratings[11]))
        st.text("Avg.Rating:" + str(round(avg_ratings[11],2)))
    with col3:
        st.image(image_url[12])
        st.text(book_author[12])
        st.text("Ratings:" + str(no_of_ratings[12]))
        st.text("Avg.Rating:" + str(round(avg_ratings[12],2)))
    with col4:
        st.image(image_url[13])
        st.text(book_author[13])
        st.text("Ratings:" + str(no_of_ratings[13]))
        st.text("Avg.Rating:" + str(round(avg_ratings[13],2)))
    with col5:
        st.image(image_url[14])
        st.text(book_author[14])
        st.text("Ratings:" + str(no_of_ratings[14]))
        st.text("Avg.Rating:" + str(round(avg_ratings[14],2)))  
    
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.image(image_url[15])
        st.text(book_author[15])
        st.text("Ratings:" + str(no_of_ratings[15]))
        st.text("Avg.Rating:" + str(round(avg_ratings[15],2)))
    with col2:
        st.image(image_url[16])
        st.text(book_author[16])
        st.text("Ratings:" + str(no_of_ratings[16]))
        st.text("Avg.Rating:" + str(round(avg_ratings[16],2)))
    with col3:
        st.image(image_url[17])
        st.text(book_author[17])
        st.text("Ratings:" + str(no_of_ratings[17]))
        st.text("Avg.Rating:" + str(round(avg_ratings[17],2)))
    with col4:
        st.image(image_url[18])
        st.text(book_author[18])
        st.text("Ratings:" + str(no_of_ratings[18]))
        st.text("Avg.Rating:" + str(round(avg_ratings[18],2)))
    with col5:
        st.image(image_url[19])
        st.text(book_author[19])
        st.text("Ratings:" + str(no_of_ratings[19]))
        st.text("Avg.Rating:" + str(round(avg_ratings[19],2))) 
            
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.image(image_url[20])
        st.text(book_author[20])
        st.text("Ratings:" + str(no_of_ratings[20]))
        st.text("Avg.Rating:" + str(round(avg_ratings[20],2)))
    with col2:
        st.image(image_url[21])
        st.text(book_author[21])
        st.text("Ratings:" + str(no_of_ratings[21]))
        st.text("Avg.Rating:" + str(round(avg_ratings[21],2)))
    with col3:
        st.image(image_url[22])
        st.text(book_author[22])
        st.text("Ratings:" + str(no_of_ratings[22]))
        st.text("Avg.Rating:" + str(round(avg_ratings[22],2)))
    with col4:
        st.image(image_url[23])
        st.text(book_author[23])
        st.text("Ratings:" + str(no_of_ratings[23]))
        st.text("Avg.Rating:" + str(round(avg_ratings[23],2)))
    with col5:
        st.image(image_url[24])
        st.text(book_author[24])
        st.text("Ratings:" + str(no_of_ratings[24]))
        st.text("Avg.Rating:" + str(round(avg_ratings[24],2)))

st.sidebar.title("Recommend Books")
selected_book = st.sidebar.selectbox("Type or select a book from the dropdown",book_list)
if st.sidebar.button("Recommend Me"):
    book = recommend(selected_book)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(book[0][2])
        st.text(book[0][0])
        st.text(book[0][1])  
    with col2:
        st.image(book[1][2])
        st.text(book[1][0])
        st.text(book[1][1])
    with col3:
        st.image(book[2][2])
        st.text(book[2][0])
        st.text(book[2][1])
    with col4:
        st.image(book[3][2])
        st.text(book[3][0])
        st.text(book[3][1])
    with col5:
        st.image(book[4][2])
        st.text(book[4][0])
        st.text(book[4][1])
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(book[5][2])
        st.text(book[5][0])
        st.text(book[5][1])  
    with col2:
        st.image(book[6][2])
        st.text(book[6][0])
        st.text(book[6][1])
    with col3:
        st.image(book[7][2])
        st.text(book[7][0])
        st.text(book[7][1])
    with col4:
        st.image(book[8][2])
        st.text(book[8][0])
        st.text(book[8][1])
    with col5:
        st.image(book[9][2])
        st.text(book[9][0])
        st.text(book[9][1])
    
        
    
