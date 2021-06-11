import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

def main():
    html_temp1 = """<div>
                        <h4 >Exploratory data Analysis Automator</h4>
                    </div>
                    </br>"""
    st.markdown(html_temp1, unsafe_allow_html=True)

    menu = ["Home", "EDA", "About"]
    choice = st.sidebar.selectbox("Menu", menu, 2)
    # for hide menu
    hide_streamlit_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    </style>
                    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    st.sidebar.markdown(
        """ Developed by Komali Beeram    """)
    if choice == "Home":
        # color codes  ff1a75  6D7B8D
        html_temp2 = """<div>
                            <h4>This is the Exploratory data Analysis Automator  created using Streamlit framework and pandas-profiling library.</h4>
                        </div>
                        </br>"""
        st.markdown(html_temp2, unsafe_allow_html=True)

    elif choice == "EDA":
        html_temp3 = """
                        		<div>
                        		<h4 >Upload file Your file in csv formate and perform Exploratory Data Analysis</h4>
                        		<h5 >Make sure your columns have correct data types before uploading.</h5>
                        		</div>
                        		<br></br>"""

        st.markdown(html_temp3, unsafe_allow_html=True)
        st.subheader("Perform Exploratory data Analysis with Pandas Profiling Library")
        data_file= st.file_uploader("Upload a csv file", type=["csv"])
        if st.button("Analyze"):
            if data_file is not None:
                # Pandas Profiling Report
                @st.cache
                def load_csv():
                    csv = pd.read_csv(data_file)
                    return csv

                df = load_csv()
                pr = ProfileReport(df, explorative=True)
                st.header('*User Input DataFrame*')
                st.write(df)
                st.write('---')
                st.header('*Exploratory Data Analysis Report Using Pandas Profiling*')
                st_profile_report(pr)
            else:
                st.success("Upload file")
        else:
            pass
    elif choice == "About":
        html_temp4 = """
                       		<div>
                       		<h4>This Application is developed by Komali Beeram using Streamlit Framework.</h4>
                       		</div>
                       		<br></br>
                       		<br></br>"""

        st.markdown(html_temp4, unsafe_allow_html=True)
    else:
        pass


if __name__ == "__main__":
    main()