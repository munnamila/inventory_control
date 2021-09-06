import streamlit as st
from PIL import Image
import requests
from io import BytesIO

import func
import test_page

def search_page():

    detail = 0

    st.write("<キーワード>")

    # 検索項目
    object_search = st.text_input('部品名')
    id_search = st.text_input('型番')
    shelf_search = st.text_input('棚')
    container_search = st.text_input('容器')
    tag_search = st.text_input('タグ')

    left_column, right_column = st.columns(2)
    st.write("<検索結果>")
    column_0, column_1, column_2, column_3, column_4, column_5, column_6, column_7= st.columns(8)

    # 表示項目
    column_0.write('画像')
    column_1.write('部品名')
    column_2.write('型番')
    column_3.write('棚')
    column_4.write('容器')
    column_5.write('個数')
    column_6.write('棚卸し')
    column_7.write('詳細')

    detail = column_7.button('詳細')

    if detail:
        print(1)
        test_page.test_page()

    # 検索ボタンの動作
    if right_column.button('検索'):

        try:

            if object_search != '':

                # csvからデータを探し
                data = func.search('object', str(object_search))

                # データを表示
                try:
                    yzmdata = requests.get(data[2])
                    tempIm = BytesIO(yzmdata.content)
                    img = Image.open(tempIm)
                    column_0.image(img)

                except:
                    pass

                column_1.write(data[0])
                column_2.write(data[1])
                column_3.write(data[7])
                column_4.write(data[8])
                column_5.write(data[6])


                # detail = column_7.button('詳細')

            elif id_search != '':

                # csvからデータを探し
                data = func.search('id', str(id_search))

                # データを表示
                try:
                    yzmdata = requests.get(data[2])
                    tempIm = BytesIO(yzmdata.content)
                    img = Image.open(tempIm)
                    column_0.image(img)

                except:
                    pass
                column_1.write(data[0])
                column_2.write(data[1])
                column_3.write(data[7])
                column_4.write(data[8])
                column_5.write(data[6])

                # detail = column_7.button('詳細')

            elif shelf_search != '':

                # csvからデータを探し
                data = func.search('shelf', str(shelf_search))

                print(data)

                # データを表示
                try:
                    yzmdata = requests.get(data[2])
                    tempIm = BytesIO(yzmdata.content)
                    img = Image.open(tempIm)
                    column_0.image(img)

                except:
                    pass

                column_1.write(data[0])
                column_2.write(data[1])
                column_3.write(data[7])
                column_4.write(data[8])
                column_5.write(data[6])

                # detail = column_7.button('詳細')

            elif container_search != '':

                # csvからデータを探し
                data = func.search('container', str(container_search))

                # データを表示  
                try:
                    yzmdata = requests.get(data[2])
                    tempIm = BytesIO(yzmdata.content)
                    img = Image.open(tempIm)
                    column_0.image(img)

                except:
                    pass

                column_1.write(data[0])
                column_2.write(data[1])
                column_3.write(data[7])
                column_4.write(data[8])
                column_5.write(data[6])

                # detail = column_7.button('詳細')

            elif container_search != '':

                # csvからデータを探し
                data = func.search('container', str(container_search))

                # データを表示
                try:
                    yzmdata = requests.get(data[2])
                    tempIm = BytesIO(yzmdata.content)
                    img = Image.open(tempIm)
                    column_0.image(img)

                except:
                    pass

                column_1.write(data[0])
                column_2.write(data[1])
                column_3.write(data[7])
                column_4.write(data[8])
                column_5.write(data[6])

                # detail = column_7.button('詳細')

            elif tag_search != '':

                # csvからデータを探し
                data = func.search('tag', str(tag_search))

                # データを表示
                try:
                    yzmdata = requests.get(data[2])
                    tempIm = BytesIO(yzmdata.content)
                    img = Image.open(tempIm)
                    column_0.image(img)

                except:
                    pass

                column_1.write(data[0])
                column_2.write(data[1])
                column_3.write(data[7])
                column_4.write(data[8])
                column_5.write(data[6])

                # detail = column_7.button('詳細')


            else:
                st.warning('正しい情報を記入してください')

        except:
            st.warning('正しい情報を記入してください')



    if left_column.button('クリア'):
        pass

