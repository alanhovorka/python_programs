#Program that cross references times for final exams at Ball State with an official CSV and tells the user if there are any errors between the two. 
#Similar to part 1 because it uses the same find_exam_time function. 
import csv

def find_exam_time(time, period, credit_hours, days):
    final_time = ""
    if time == "8:00":
        if period == "AM":
            if credit_hours == "2":
                if days == "TR":
                    final_time = "Wednesday, December 14, 7:30 - 9:30 am"
                elif days == "MWF" or days == "MW" or days == "WF":
                    final_time = "Thursday, December 15, 7:30 - 9:30 am"
            elif credit_hours == "3":
                if days == "TR":
                    final_time = "Wednesday, December 14, 7:30 - 9:30 am"
                elif days == "MWF":
                    final_time = "Thursday, December 15, 7:30 - 9:30 am"
            elif credit_hours == "4":
                final_time = "Wednesday, December 14, 7:30 - 9:30 am"
            elif credit_hours == "5":
                    final_time = "Thursday, December 15, 7:30 - 9:30 am"
        elif period == "PM":
            if days == "TR":
                final_time = "Tuesday, December 13, 7:00 - 9:00 pm"
            elif days == "MW":
                final_time = "Wednesday, December 14, 7:00 - 9:00 pm"
    elif time == "9:00":
        if period == "AM":
            if credit_hours == "2":
                final_time = "Friday, December 16, 7:30 - 9:30 am"
            elif credit_hours == "3":
                if days == "MWF":
                    final_time = "Friday, December 16, 7:30 - 9:30 am"
            elif credit_hours == "4":
                final_time = "Friday, December 16, 7:30 - 9:30 am"
    elif time == "9:30":
        if period == "AM":
            if credit_hours == "2":
                final_time = "Friday, December 16, 9:45 - 11:45 am"
            elif credit_hours == "3":
                if days == "MWF":
                    final_time = "Friday, December 16, 9:45 - 11:45 am"
                elif days == "TR":
                    final_time = "Friday, December 16, 9:45 - 11:45 am"
            elif credit_hours == "4":
                final_time = "Friday, December 16, 9:45 - 11:45 am"
    elif time == "10:00":
        if period == "AM":
            if credit_hours == "2":
                    final_time = "Wednesday, December 14, 9:45 - 11:45 am"
            elif credit_hours == "3":
                if days == "MWF":
                    final_time = "Wednesday, December 14, 9:45 - 11:45 am"
            elif credit_hours == "4":
                final_time = "Wednesday, December 14, 9:45 - 11:45 am"
            elif credit_hours == "5":
                if days == "TR":
                    final_time = "Wednesday, December 14, 9:45 - 11:45 am"
                elif days == "MW":
                    final_time = "Wednesday, December 14, 9:45 - 11:45 am"
                elif days == "WF":
                    final_time = "Wednesday, December 14, 9:45 - 11:45 am"
                elif days == "MWF":
                    final_time = "Wednesday, December 14, 9:45 - 11:45 am"
    elif time == "11:00":
        if period == "AM":
            if credit_hours == "2":
                if days == "TR":
                    final_time = "Tuesday, December 13, 9:45 - 11:45 am"
                elif days == "MWF" or days == "MW" or days == "WF":
                    final_time = "Thursday, December 15, 9:45 - 11:45 am"
            elif credit_hours == "3":
                if days == "TR":
                    final_time = "Tuesday, December 13, 9:45 - 11:45 am"
                elif days == "MWF":
                    final_time = "Thursday, December 15, 9:45 - 11:45 am"
            elif credit_hours == "4":
                if days == "TR":
                    final_time = "Tuesday, December 13, 9:45 - 11:45 am"
                elif days == "MWF":
                    final_time = "Thursday, December 15, 9:45 - 11:45 am"
            elif credit_hours == "5":
                    final_time = "Thursday, December 15, 9:45 - 11:45 am"
    elif time == "12:00":
        if period == "PM":
            if credit_hours == "2":
                final_time = "Wednesday, December 14, 12:00 - 2:00 pm"
            elif credit_hours == "3":
                if days == "MWF":
                    final_time = "Wednesday, December 14, 12:00 - 2:00 pm"
            elif credit_hours == "4":
                final_time = "Wednesday, December 14, 12:00 - 2:00 pm"
            elif credit_hours == "5":
                final_time = "Wednesday, December 14, 12:00 - 2:00 pm"
    elif time == "12:30":
        if period == "PM":
            if credit_hours == "2":
                final_time = "Tuesday, December 13, 12:00 - 2:00 pm"
            elif credit_hours == "3":
                if days == "MWF":
                    final_time = "Tuesday, December 13, 12:00 - 2:00 pm"
                elif days == "TR":
                    final_time = "Tuesday, December 13, 12:00 - 2:00 pm"
            elif credit_hours == "4":
                final_time = "Tuesday, December 13, 12:00 - 2:00 pm"
            elif credit_hours == "5":
                final_time = "Tuesday, December 13, 12:00 - 2:00 pm"
    elif time == "1:00":
        if period == "PM":
            if credit_hours == "2":
                if days == "TR":
                    final_time = "Tuesday, December 13, 12:00 - 2:00 pm"
                elif days == "MWF" or days == "MW" or days == "WF":
                    final_time = "Friday, December 16, 12:00 - 2:00 pm"
            elif credit_hours == "3":
                if days == "MWF":
                    final_time = "Friday, December 16, 12:00 - 2:00 pm"
            elif credit_hours == "4":
                final_time = "Friday, December 16, 12:00 - 2:00 pm"
    elif time == "2:00":
        if period == "PM":
            if credit_hours == "2":
                if days == "TR":
                    final_time = "Thursday, December 15, 12:00 - 2:00 pm"
                elif days == "MWF" or days == "MW" or days == "WF":
                    final_time = "Thursday, December 15, 2:15 - 4:15 pm"
            elif credit_hours == "3":
                if days == "TR":
                    final_time = "Thursday, December 15, 12:00 - 2:00 pm"
                elif days == "MWF":
                    final_time = "Thursday, December 15, 2:15 - 4:15 pm"
            elif credit_hours == "4":
                final_time = "Thursday, December 15, 12:00 - 2:00 pm"
            elif credit_hours == "5":
                final_time = "Thursday, December 15, 2:15 - 4:15 pm"                
    elif time == "3:00":
        if period == "PM":
            if credit_hours == "2":
                final_time = "Wednesday, December 14, 2:15 - 4:15 pm"
            elif credit_hours == "3":
                if days == "MWF":
                    final_time = "Wednesday, December 14, 2:15 - 4:15 pm"
            elif credit_hours == "4":
                final_time = "Wednesday, December 14, 2:15 - 4:15 pm"
    elif time == "3:30":
        if period == "PM":
            if credit_hours == "2":
                if days == "TR":
                    final_time = "Tuesday, December 13, 2:15 - 4:15 pm"
            elif credit_hours == "3":
                if days == "TR":
                    final_time = "Tuesday, December 13, 2:15 - 4:15 pm"
            elif credit_hours == "4":
                final_time = "Tuesday, December 13, 2:15 - 4:15 pm"
    elif time == "4:00":
        if period == "PM":
            if credit_hours == "2":
                final_time = "Friday, December 16, 2:15 - 4:15 pm"
            elif credit_hours == "3":
                if days == "MWF":
                    final_time = "Friday, December 16, 2:15 - 4:15 pm"
            elif credit_hours == "4":
                final_time = "Friday, December 16, 2:15 - 4:15 pm"
    elif time == "5:00":
        if period == "PM":
            if credit_hours == "2":
                if days == "TR":
                    final_time = "Tuesday, December 13, 4:30 - 6:30 pm"
                elif days == "MWF" or days == "MW" or days == "WF":
                    final_time = "Wednesday, December 14, 4:30 - 6:30 pm"
            elif credit_hours == "3":
                if days == "TR":
                    final_time = "Tuesday, December 13, 4:30 - 6:30 pm"
                elif days == "MWF":
                    final_time = "Wednesday, December 14, 4:30 - 6:30 pm"
            elif credit_hours == "4":
                final_time = "Tuesday, December 13, 4:30 - 6:30 pm"
            elif credit_hours == "5":
                final_time = "Wednesday, December 14, 4:30 - 6:30 pm"
    elif time == "6:30":
        if period == "PM":
            if credit_hours == "1":
                if days == "M" or days == "MW":
                    final_time = "Monday, December 12, 6:30 - 7:25 pm"
            elif credit_hours == "2":
                if days == "M" or days == "MW":
                    final_time = "Monday, December 12, 6:30 - 8:20 pm"
            elif credit_hours == "3":
                if days == "M" or days == "MW":
                    final_time = "Monday, December 12, 6:30 - 9:30 pm"
            elif credit_hours == "4":
                if days == "M" or days == "MW":
                    final_time = "Monday, December 12, 6:30 - 10:15 pm"
            if days == "T" or days == "TR":
                final_time = "Tuesday, December 13, 7:00 - 9:00 pm"
            elif days == "W":
                final_time = "Wednesday, December 14, 7:00 - 9:00 pm"
            elif days == "R":
                final_time = "Thursday, December 15, 7:00 - 9:00 pm"
    if final_time:
        return final_time
    else:
        return "The course was not found. Please check the course details."

#Prints everything in the CSV file
courses = []
print("{0:10}{1:30}{2:60}{3:90}".format("#","Correct Date","Your Date", "Test"))
print("=" * 12)        
with open("final_exam_schedule.csv") as file:
    reader = csv.reader(file,delimiter = ",")
    next(reader)
    for row in reader:
        courses.append(row)     

for row in courses:
    final=find_exam_time(row[1], row[2], row[3], row[4])
    if final == row[5]:
        test = "Pass"
    else:
        test="Fail"

    print("{0:10}{1:50}{1:50}{3:50}".format(row[0], row[5], final, test))

"""
course_name = []
course_time = []
course_period = []
course_credit_hours = []
course_days = []
course_math_com = []


run = True
while run:
    name = input("What is your course name and section number? or type q to quit/finalize your selection of courses: ")
    if name == "q":
        run = False
    else:
        #int(input("") not needed)
        course_name.append(name)
        time = input("What time is your course(example: 8:00, 9:30.) No AM or PM here. Leave blank if not appliceable: ")
        course_time.append(time)
        period = input("AM or PM. Leave blank if not applicable: ")
        course_period.append(period)
        credit_hours = input("Credit hours (Leave blank if not appliceable): ")
        course_credit_hours.append(credit_hours)
        days = input("Days (TR, MWF, etc. Leave blank if not appliceable): ")
        course_days.append(days)
        print()


print()
print("{0:30}{1:10}".format("Course","Final Exam Time"))
print("=" * 60)
for i in range(len(course_name)):
    final_time = find_exam_time(course_time[i], course_period[i], course_credit_hours[i], course_days[i])

    print("{0:10}{1:>10}".format(course_name[i], final_time))
"""
