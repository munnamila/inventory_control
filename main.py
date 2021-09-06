import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

import func
import search_page
import new_object_page
import database_page


# side_bar
st.sidebar.title('aba在庫管理システム')

pages = ['新規登録', '在庫検索', '登録歴史', 'データベース']

page = st.sidebar.radio('メニュー', options=pages)

st.title(page)



if page == "新規登録":

    # 新規登録ページ
    new_object_page.new_object_page()    

elif page == "在庫検索":

    # 在庫検索ページ
    search_page.search_page()

elif page == "登録歴史":
    pass

elif page == "データベース":
    database_page.database_page()


