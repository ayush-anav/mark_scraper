import sys 
import os
from open_and_scrape import open_file

def get_file_arg():
    try:
        if(len(sys.argv[1]) < 1):
            raise Exception("check to see if you have supplied the file")
        
        # relative path to file
        rel_path = f'file/{sys.argv[1]}'
        
        if(os.path.exists(f'{os.path.abspath(rel_path)}.pdf')):
            print("\n== FILE OPENED SUCCESSFULLY, STARTING PROCESSING NOW ===\n")
            full_file_path = f'{os.path.abspath(rel_path)}.pdf'
            return open_file(full_file_path)
        else:
            print("open run.sh to see what to do :)\n")
            raise Exception("file not found :(")
            
    except Exception as e:
        print("--------detailed error--------")
        print(e)