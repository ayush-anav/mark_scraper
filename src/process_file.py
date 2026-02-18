import sys 
import os

def get_file_arg():
    try:
        if(len(sys.argv[1]) < 1):
            raise Exception("check to see if you have supplied the file")
        
        if(os.path.exists(f'{os.path.abspath(sys.argv[1])}.pdf')):
            print("file exists")
            # call open_file()
        else:
            raise Exception("file not found :(")
            
    except Exception as e:
        print("Check to see if you have passed the file name!")
        print("open run.sh to see what to do :)\n")
        print("--------detailed error--------")
        print(e)