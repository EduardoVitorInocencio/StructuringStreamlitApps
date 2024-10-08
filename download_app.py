import streamlit as st
import streamlit.components as stc

import base64
import time
timestr = time.strftime("%Y%m%d-%H%M%S")

import pandas as pd


# FUNCTIONS
def text_downloader(raw_text):
    b64 = base64.b64encode(raw_text.encode()).decode()  # Corrigido para usar encode em vez de decode
    new_filename = f"new_text_file_{timestr}_.txt"
    st.markdown("### Download file ###")
    href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">CLICK HERE!</a>'
    st.markdown(href, unsafe_allow_html=True)

def csv_downloader(data):
    csvfile = data.to_csv()
    b64 = base64.b64encode(csvfile.encode()).decode()  # Corrigido para usar encode em vez de decode
    new_filename = f"new_text_file_{timestr}_.csv"
    st.markdown("### Download file ###")
    href = f'<a href="data:file/csv;base64,{b64}" download="{new_filename}">CLICK HERE!</a>'
    st.markdown(href, unsafe_allow_html=True)

# CLASS
class FileDownloader(object):
    """docstring for FileDonwloader
    >>> download = FileDownloader(data, filename, file_ext).download()
    """

    def __init__(self, data, filename='myfile', file_ext='txt'):
        super(FileDownloader,self).__init__()
        self.data = data
        self.filename = filename
        self.file_ext = file_ext

    def download(self):
        b64 = base64.b64encode(self.data.encode()).decode()  # Corrigido para usar encode em vez de decode
        new_filename = f"{self.filename}_{timestr}_{self.file_ext}_.txt"
        st.markdown("### Download file ###")
        href = f'<a href="data:file/{self.file_ext};base64,{b64}" download="{new_filename}">CLICK HERE!</a>'
        st.markdown(href, unsafe_allow_html=True)

def main_download():

    menu = ["Txt","CSV"]
    choice = st.selectbox("Options",menu)

    if choice == "Txt":
        st.subheader("Txt")
        my_text = st.text_area("Your message")
        if st.button("Save"):
            st.write(my_text)
            # text_downloader(my_text)
            download = FileDownloader(my_text).download()
    
    elif choice =="CSV":
        df = pd.read_csv('data/diabetes.csv')
        # csv_downloader(df)
        download = FileDownloader(df.to_csv(),file_ext='csv').download()
        st.dataframe(df)