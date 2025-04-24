import streamlit as st
import pandas as pd
import logging
from io import BytesIO
import traceback

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
log_stream = BytesIO()

# Custom Stream Handler to capture logs
class StreamToSidebar(logging.StreamHandler):
    def emit(self, record):
        log_entry = self.format(record)
        if "log_messages" not in st.session_state:
            st.session_state.log_messages = []
        st.session_state.log_messages.append(log_entry)

log_handler = StreamToSidebar()
log_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
logger.addHandler(log_handler)

# Page config and styling
st.set_page_config(page_title="File Convertor & Cleaner", layout="wide")
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&display=swap');
        html, body, [class*="st-"] {
            font-family: 'Quicksand', sans-serif;
        }
        .stApp {
            background-color: #fef9f4;
        }
        div[data-testid="stFileUploader"] > div {
            background-color: #f8e5d1 !important;
            border: 2px dashed #c48d5e !important;
            padding: 10px;
            border-radius: 10px;
        }
        div[data-testid="stFileUploader"] * {
            color: #5c4634 !important;
        }
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
            color: #5c4634;
            font-weight: 600;
        }
        .stButton button {
            background-color: #d29c61 !important;
            color: white !important;
            font-size: 16px !important;
            border-radius: 8px !important;
        }
        .stAlert {
            background-color: #fff3e3 !important;
            border-left: 6px solid #c48d5e !important;
        }
        .stRadio > div {
            background-color: #fff5ec !important;
            border-radius: 8px;
            padding: 8px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar for logs
st.sidebar.header("📋 Logs")
if "log_messages" in st.session_state:
    st.sidebar.code("\n".join(st.session_state.log_messages[-20:]))  # last 20 logs

# Title & Description
st.title("📁File Convertor & Cleaner")
st.write("Easily upload and process your CSV or Excel files. Clean your data, select specific columns, visualize insights, and convert formats—all in one place effortlessly! 🚀")

# File Upload
files = st.file_uploader("Upload CSV or Excel Files", type=["csv", "xlsx"], accept_multiple_files=True)

if files:
    for file in files:
        try:
            ext = file.name.split(".")[-1]
            df = pd.read_csv(file) if ext == "csv" else pd.read_excel(file)
            logger.info(f"Loaded file: {file.name}")

            st.subheader(f"🔍 {file.name} - Preview")
            st.dataframe(df.head())

            if st.checkbox(f"Fill Missing Values - {file.name}"):
                numeric_cols = df.select_dtypes(include="number")
                df.fillna(numeric_cols.mean(), inplace=True)
                st.success("Missing values filled successfully!")
                logger.info(f"Filled missing values in {file.name}")
                st.dataframe(df.head())

            selected_columns = st.multiselect(f"Select Columns - {file.name}", df.columns, default=df.columns)
            df = df[selected_columns]
            st.dataframe(df.head())

            if st.checkbox(f"📊 Show Chart - {file.name}") and not df.select_dtypes(include="number").empty:
                st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])

            format_choice = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)

            if st.button(f"⬇️ Download {file.name} as {format_choice}"):
                output = BytesIO()
                try:
                    if format_choice == "CSV":
                        df.to_csv(output, index=False)
                        mime = "text/csv"
                        new_name = file.name.replace(ext, "csv")
                    else:
                        df.to_excel(output, index=False)
                        mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        new_name = file.name.replace(ext, "xlsx")
                    output.seek(0)
                    st.download_button("⬇️ Downlaod File", file_name=new_name, data=output, mime=mime)
                    logger.info(f"File {file.name} converted and ready for download as {format_choice}")
                except Exception as e:
                    logger.error(f"Download failed for {file.name}: {str(e)}")
                    st.error(f"Download failed: {str(e)}")
            st.success("Processing Completed! 🎉")

        except Exception as e:
            error_msg = f"Error processing file {file.name}: {str(e)}"
            st.error(error_msg)
            logger.error(error_msg)
            logger.debug(traceback.format_exc())
