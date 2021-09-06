import streamlit as st

import func

def new_object_page():
    object_new = st.text_input('部品名')

    id_new = str(st.text_input('型番'))

    img_URL_new = st.text_input('画像URL')

    date_new = st.date_input('購入日')

    unit_new = st.text_input('単位')

    unit_number_new = st.number_input('単位数量', 0, step = 1)

    purchase_number_new = st.number_input('購入数', 0, step = 1)

    '在庫数 : '

    shelf_new = st.text_input('棚')

    container_new = st.text_input('容器')

    tag_new = st.text_input('タグ')

    subsidy_new = st.text_input('助成金')

    remark_new = st.text_area('備考')


    left_column, right_column = st.columns(2)

    # clear_new = left_column.button('クリア')

    if right_column.button('送信'):
        func.write_csv([object_new, 
                        id_new, 
                        img_URL_new, 
                        date_new, 
                        unit_new, 
                        unit_number_new, 
                        purchase_number_new, 
                        shelf_new, 
                        container_new, 
                        tag_new, 
                        subsidy_new, 
                        remark_new], 'data_log.csv')

        func.renew_database()

        st.success('successful')

    if left_column.button('クリア'):
        pass