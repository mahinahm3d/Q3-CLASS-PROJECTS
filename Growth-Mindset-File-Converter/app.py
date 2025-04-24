import streamlit as st
import pandas as pd
from io import BytesIO
import logging
import uuid

# Setup logging (for container stdout logs)
logging.basicConfig(level=logging.INFO)

# Constants
MAX_ROWS = 1_000_000

# Streamlit config
st.set_page_config(page_title="File Converter", layout="wide")
st.title("📁 File Converter")
st.write("Upload CSV or Excel files below and convert formats.")


# --- Helper Functions ---
def load_file(file):
    """Load CSV or Excel file and return a DataFrame."""
    try:
        ext = file.name.split(".")[-1].lower()
        if ext == "csv":
            return pd.read_csv(file), ext
        elif ext == "xlsx":
            return pd.read_excel(file), ext
        else:
            raise ValueError("Unsupported file extension.")
    except Exception as e:
        raise ValueError(f"Error loading file: {e}")


def clean_dataframe(df, remove_duplicates=False, fill_missing=False):
    """Apply data cleaning operations."""
    if remove_duplicates:
        df = df.drop_duplicates()
    if fill_missing:
        df.fillna(df.select_dtypes(include=["number"]).mean(), inplace=True)
    return df


def download_file(df, ext, format_choice):
    """Prepare DataFrame for download as CSV or Excel."""
    output = BytesIO()
    if format_choice == "csv":
        df.to_csv(output, index=False)
        mime = "text/csv"
        new_ext = "csv"
    else:
        df.to_excel(output, index=False, engine="openpyxl")
        mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        new_ext = "xlsx"
    output.seek(0)
    return output, mime, new_ext


# --- Main UI Logic ---
files = st.file_uploader(
    "Upload CSV or Excel Files", type=["csv", "xlsx"], accept_multiple_files=True
)

if files:
    for file in files:
        st.divider()
        unique_key = str(uuid.uuid4())

        try:
            df, ext = load_file(file)
            logging.info(f"Loaded file: {file.name} with {len(df)} rows.")

            if len(df) > MAX_ROWS:
                st.warning(f"{file.name} is too large! Showing first {MAX_ROWS} rows only.")
                df = df.head(MAX_ROWS)

            st.subheader(f"📄 {file.name} - Preview")
            st.dataframe(df.head())

            remove_duplicates = st.checkbox(f"Remove Duplicates - {file.name}", key=f"dedup_{unique_key}")
            fill_missing = st.checkbox(f"Fill Missing Values - {file.name}", key=f"fillna_{unique_key}")
            df = clean_dataframe(df, remove_duplicates, fill_missing)

            st.success("Data cleaned.") if remove_duplicates or fill_missing else None
            st.dataframe(df.head())

            selected_columns = st.multiselect(
                f"Select Columns - {file.name}",
                options=list(df.columns),
                default=list(df.columns),
                key=f"cols_{unique_key}"
            )
            df = df[selected_columns]

            if st.checkbox(f"📊 Show Chart - {file.name}", key=f"chart_{unique_key}"):
                numeric_df = df.select_dtypes(include=["number"])
                if not numeric_df.empty:
                    st.bar_chart(numeric_df.iloc[:, :2])
                else:
                    st.warning("No numeric data to plot.")

            format_choice = st.radio(
                f"Convert {file.name} to:",
                ["csv", "Excel"],
                key=f"format_{unique_key}"
            )

            if st.button(f"Download {file.name} as {format_choice}", key=f"download_{unique_key}"):
                output, mime, new_ext = download_file(df, ext, format_choice)
                new_name = file.name.rsplit(".", 1)[0] + "." + new_ext
                st.download_button(
                    "📥 Download File",
                    file_name=new_name,
                    data=output.getvalue(),
                    mime=mime
                )
                st.success("✅ Processing Complete!")

        except Exception as e:
            logging.error(f"Error processing {file.name}: {e}")
            st.error(f"❌ Failed to process {file.name}: {e}")
