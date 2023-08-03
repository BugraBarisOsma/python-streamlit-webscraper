import streamlit as st
import requests
from bs4 import BeautifulSoup

st.markdown("<h1 style='text-align: center'>Web Scraper</h1>", unsafe_allow_html=True)


with st.form("Search"):
    keyword = st.text_input("Enter keyword")

    search = st.form_submit_button("Search")
    placeholder=st.empty()
    if search:
        
        page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
        soup = BeautifulSoup(page.content, 'lxml')  # get all the html of the page
        rows = soup.find_all("div", class_="ripi6")
        col1, col2 = placeholder.columns(2)
        for row in rows:
            figures = row.find_all("figure")
            for i in range(2):
                t_img = figures[i].find("img", class_="tB6UZ a5VGX")
                if t_img is not None:
                    my_list = t_img["srcset"].split("?")
                    if i == 0:
                        col1.image(my_list[0])
                    else: 
                        col2.image(my_list[0])

