import numpy as np
import pandas as pd
import streamlit as st

import plotly.express as px
import plotly.graph_objects as go
import pylab as plt
import matplotlib as mpl
import seaborn as sns
mpl.rcParams['font.size'] = 14
mpl.rcParams['figure.dpi'] = 90.

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
    papers = pd.read_csv('data/papers_sfb_2019.csv', index_col=0)
    papers = papers.reset_index(drop=True)
    return authors, papers
    
authors, papers = load_data()

st.title(f"Overview SFB/Transregio 285")
st.markdown("---")
st.subheader('Involved Scientists')
# st.sidebar.subheader("Navigation")
# option = st.sidebar.radio('Go to', ('Scientists','Publications'))
    
# if option ==  'People':
cols1 = st.multiselect('', options=['affil_short','degree','name','h_index','documents','citations','pub_period'],
default = ['name','degree','affil_short'])
st.write(authors[cols1])
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
    
    