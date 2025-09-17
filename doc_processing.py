import pandas as pd
import pdfplumber
import re

def read_excel(file_path):
    """
    Reads all sheets from Excel and returns combined text.
    """
    try:
        xls = pd.ExcelFile(file_path)
        text = ""
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            text += df.to_string(index=False) + "\n"
        return text
    except Exception as e:
        return f"Error reading Excel: {e}"

def read_pdf(file_path):
    """
    Reads PDF and extracts text page by page.
    """
    text = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text
    except Exception as e:
        return f"Error reading PDF: {e}"

def clean_text(text):
    """
    Optional: clean text by removing unnecessary spaces, tabs, or special chars
    """
    text = re.sub(r"\s+", " ", text)
    return text.strip()
