from open_and_scrape import open_file
from mark_processing import all_student_mark, grab_id, grab_marks, id_mark_relationship, grab_name, specific_student_mark, total_mark_student


def menu(extracted_text):
    display_hello()
    # list of all student ids (good for validation)
    all_students_id = grab_id(extracted_text)
    raw_marks = grab_marks(extracted_text)
    every_student_mark = all_student_mark(extracted_text)
    
    id_mark = id_mark_relationship(raw_marks, all_students_id)
    
    while True:
        user_choice = input("SELECT (a,b,c OR q)-> ")
        
        match(user_choice):
            case "a":
                                
                student_id = input("Enter ID: ")
                
                if(validate_student_id(student_id, all_students_id)):
                    print(f"\n======================================================\n")
                    print(f"{specific_student_mark(student_id, every_student_mark)}")
                    print(f"\nTOTAL MARK: {total_mark_student(student_id, id_mark)}")
                    print(f"\n======================================================\n")
                break
            
            case "b":
                break
            
            case "c":
                break
            
            case "q":
                break
            
            case _:
                print("\nInvalid choice, try again\n")
                
def validate_student_id(student_id, all_students_id):
    if student_id not in all_students_id:
        print("\nInvalid ID, try again\n")
        return False
    return True
    
    
def display_hello():
     print("""
╔══════════════════════════════════════════╗
║            MAIN MENU                     ║
╠══════════════════════════════════════════╣
║  a ➜ Display marks by FEMIS ID           ║
║  b ➜ Rank Highest → Lowest               ║
║  c ➜ Rank Lowest  → Highest              ║
║  q ➜ Quit                                ║
╚══════════════════════════════════════════╝
""")
    