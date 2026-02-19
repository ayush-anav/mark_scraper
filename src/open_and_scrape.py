from pypdf import PdfReader
import re

def open_file(full_file_path):
    try:
        # initialize reader
        reader = PdfReader(full_file_path)
        page = 0
        # string accumulator
        extracted_text = ""
        # iterate for every page in file and accumulate in extracted_text
        for current_page in reader.pages:
            current_page = reader.pages[page]
            extracted_text += current_page.extract_text().strip()
            page += 1
                
        return extracted_text
    
    except Exception as e:
        print("--------detailed error--------")
        print(e)
        
    