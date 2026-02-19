import re
# either len of 6 or 7 (current trend)
student_id_length = "\d{6,7}"


# returns ID and Name tuple (ID, NAME)
def grab_name(extracted_text):
    expression = f'(\d{6})\s+(.*?)\s+0\s'
    # extracts femis id + names and put them in list [(ID, NAME)]
    names = re.findall(expression, extracted_text)
    return names


# literally all marks recorded with no relationship
def grab_marks(extracted_text):
    expression = '[A-Z]{2,5}\(\s*(\d+)\)'
    # extract marks

    marks = re.findall(expression, extracted_text)
    return marks

# returns a tuple with student id, name and their marks (ID, NAME, MARKS)
# good for displaying mark at each individual student
def all_student_mark(extracted_text):
    expression = f'\d+\s+({student_id_length})\s+(.+?)\s*0\s+(.*)'
    data = re.findall(expression, extracted_text)
    return data

# grabs every ID only
def grab_id(extracted_text):
    expression = f'\d+\s+({student_id_length})'
    data = re.findall(expression, extracted_text)
    return data

# returns data of specific student, given by student_id
def specific_student_mark(student_id, every_student_mark):
    i = 0
    for entry in every_student_mark:
        if student_id == every_student_mark[i][0]:
            return every_student_mark[i]
        else: 
            i+=1

# creates relationship between ID and raw marks
def id_mark_relationship(marks, student_id):
    # each student_id = 5 marks, we are slicing mark array to include 5 marks
    # each student is guaranteed 5 marks
    # [i:i+5] [0:5],[5:10],[10:15] *0 - 5 not including 5, 0 - idx4 = 5 marks
    i = 0
    final_arr = []
    for id in student_id:
        obj = {
            id:marks[i:i+5]
        }
        final_arr.append(obj)
        i+=5
    return final_arr
    # you can cast the .values() of dict to int() when using it :)


