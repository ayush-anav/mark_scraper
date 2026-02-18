import sys 

def get_file_arg():
    try:
        sys.argv[1]
        
    except Exception as e:
        print("Check to see if you have passed the file name!")
        print("open run.sh to see what to do :)")