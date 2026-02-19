from process_file import get_file_arg
from menu import menu
def main():
    print("Hello from mark-scraper!")


if __name__ == "__main__":
    # We first call process_file that returns the result of call_and_scrape()
    extracted_text = get_file_arg()
    
    # This is where we call all the processing functions
    menu(extracted_text)