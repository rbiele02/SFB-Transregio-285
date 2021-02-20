import numpy as np
import pandas as pd
import streamlit as st
from SessionState import get

# import plotly.express as px
# import plotly.graph_objects as go
# import pylab as plt
# import matplotlib as mpl
# import seaborn as sns
# mpl.rcParams['font.size'] = 14
# mpl.rcParams['figure.dpi'] = 90.

import base64
# import io

st.set_page_config(page_title="SFB285", page_icon="🧊", layout="wide", initial_sidebar_state="expanded")
def get_table_download_link_csv(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" download="papers_sfb.csv">Download csv file</a>'
    return href


@st.cache
def load_data():
    authors = pd.read_csv('data/authors.csv', index_col=0)
    authors['h_index'] = authors['h_index'].fillna(0)
    authors['h_index'] = authors['h_index'].astype('Int64')
    papers = pd.read_csv('data/papers_sfb_2019.csv', index_col=0)
    papers = papers.reset_index(drop=True)
    return authors, papers

def main():
    authors, papers = load_data()
    st.title(f"Overview SFB/Transregio 285")
    st.markdown("---")
    st.subheader('Involved Scientists')
    # st.sidebar.subheader("Navigation")
    # option = st.sidebar.radio('Go to', ('Scientists','Publications'))
    
    # if option ==  'People':
    cols1 = st.multiselect('', options=['affil_short','degree','name','h_index','documents','citations','pub_period','areas','gender'],
    default = ['name','degree','affil_short','areas'])
    st.write(authors[cols1].astype('object'))
        # st.write(df[cols1].style.highlight_null(null_color='yellow'))

    st.markdown("---")
    st.subheader('Publication in 2019 from all scientists involved')   
    # if option == 'Publications':
    cols1 = st.multiselect('',  options = ['doi','title','subtype','subtypeDescription','fund_acr',
                                            'author_names','publicationName', 'aggregationType','citedby_count',
                                            'openaccess','coverDate'],
    default = ['title','aggregationType','citedby_count','doi','coverDate','author_names','fund_acr'])
    st.write(papers[cols1])
    st.markdown(get_table_download_link_csv(papers[cols1]), unsafe_allow_html=True)


# session_state = get(password='password')
# if session_state.password != 'Meschut':
#     user_placeholder = st.sidebar.empty()
#     pwd_placeholder = st.sidebar.empty()
#     user = user_placeholder.text_input('username')
#     pwd = pwd_placeholder.text_input("Password:", value="", type="password")
#     # user = st.sidebar.text_input('username')
#     session_state.password = pwd
#     session_state.user = user
#     if session_state.password == 'SFBTRR285' and session_state.user=='Meschut':
#         user_placeholder.empty()
#         pwd_placeholder.empty()
#         st.balloons()
#         main()
#     elif session_state.password != '':
#         st.error("the password you entered is incorrect")
# else:
#     main()

session_state = get(password='password')
if session_state.password != 'SFBTRR285':
    # user_placeholder = st.sidebar.empty()
    pwd_placeholder = st.sidebar.empty()
    # user = user_placeholder.text_input('username')
    pwd = pwd_placeholder.text_input("Password:", value="", type="password")
    # user = st.sidebar.text_input('username')
    session_state.password = pwd
    if session_state.password == 'SFBTRR285':
        # user_placeholder.empty()
        pwd_placeholder.empty()
        st.balloons()
        main()
    elif session_state.password != '':
        st.error("the password you entered is incorrect")
else:
    main()
    
    
