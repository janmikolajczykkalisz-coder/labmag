import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st

@st.cache_resource
def get_worksheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(
        dict(st.secrets["gcp_service_account"]), scope
    )
    client = gspread.authorize(creds)

    spreadsheet_key = st.secrets["spreadsheet_key"]
    sheet_name = st.secrets.get("sheet_name", "Sheet1")

    # zamiast client.open() używamy klucza
    return client.open_by_key(spreadsheet_key).worksheet(sheet_name)
ws = get_worksheet()

