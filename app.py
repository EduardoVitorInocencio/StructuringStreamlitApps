# CORE PACKAGES
import streamlit as st

# IMPORT OUR MINI APPS
from eda_app import run_eda_app
from ml_app import run_ml_app
from download_app import main_download

# UTILS
import logging

# CREATE A LOGGER / TERMINAL
LOGS_FORMAT = "%(levelname)s %(asctime)s.%(msecs)03d-%(message)s" # Formato obtido no console por meio do comando logging.DEBUG
logging.basicConfig(level=logging.DEBUG,format=LOGS_FORMAT) #Configuração báscia para determinar a forma de interação e formato
logger = logging.getLogger(__name__)

# SAVE LOGGER MESSAGES TO FILE
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(levelname)s %(asctime)s.%(msecs)03d-%(message)s")

# LOG FILE
file_handler = logging.FileHandler('activity.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def main():
    st.title("Main App")
    st.text("Track all activities/visited page")

    menu = ['Home','EDA','ML','Download','About']
    choice = st.sidebar.selectbox("Menu",menu)

    if choice =="Home":
        st.subheader("Home")
        logger.info("Home Section")

    elif choice == "EDA":
        run_eda_app()
        logger.info("EDA Section")

    elif choice == "ML":
        run_ml_app()
        logger.info("ML Section")
    
    elif choice == "Download":
        main_download()
    else:
        st.subheader("About")
        logger.info("About Section")

if __name__ == '__main__':
    main()