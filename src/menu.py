from open_and_scrape import open_file
from mark_processing import all_student_mark, grab_id, grab_marks, id_mark_relationship, grab_name, specific_student_mark, total_mark_student, id_total_relationship


def menu(extracted_text):
    display_hello()
    # list of all student ids (good for validation)
    all_students_id = grab_id(extracted_text)
    raw_marks = grab_marks(extracted_text)
    every_student_mark = all_student_mark(extracted_text)
    
    id_mark = id_mark_relationship(raw_marks, all_students_id)
    total_id_relo = id_total_relationship(all_students_id, id_mark)
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
                print(highest_to_lowest(total_id_relo, every_student_mark))
                break
            
            case "c":
                print(lowest_to_highest(total_id_relo, every_student_mark))
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
║                                          ║
║  NOTE: (options)                         ║
║  b and c will generate a file :)         ║
╚══════════════════════════════════════════╝
""")

def highest_to_lowest(id_total_relationship, every_student_mark):
    h_t_l = sorted(id_total_relationship, key = lambda x: x[1], reverse=True)
    data = write_to_file("highest_to_lowest", h_t_l, every_student_mark)
    return data

def lowest_to_highest(id_total_relationship, every_student_mark):
    l_t_l = sorted(id_total_relationship, key = lambda x: x[1])    
    data = write_to_file("lowest_to_highest", l_t_l, every_student_mark)
    return data

def write_to_file(filename, data, every_student_mark):
    file_data = "\n\n\tID\tSTUDENT DETAILS\t\tMARK\n\n"
    i = 1
    with open(f"{filename}.txt", "w") as f:
        for tup in data:
            id, mark = tup
            file_data += f"NO: {i} ||  {id}: {specific_student_mark(id, every_student_mark)[1]} = {mark}\n"
            i+=1
        f.write(file_data)
    return file_data