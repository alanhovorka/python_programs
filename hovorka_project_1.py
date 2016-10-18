def find_exam_time(time, period, credit_hours, days, math_com):
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
                    final_time = "Thursday, December 15, 9:45 - 11:45 am"
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
            if days == "T" or days == "TR":
                final_time = "Tuesday, December 13, 7:00 - 9:00 pm"
            elif days == "W":
                final_time = "Wednesday, December 14, 7:00 - 9:00 pm"
            elif days == "R":
                final_time = "Thursday, December 15, 7:00 - 9:00 pm"
    if final_time:
        print("The course final exam is {}.".format(final_time))
    else:
        print("The course was not found. Please check the course details.")

print("Please enter your course details:")
math_com = input("Math 201 Common Final (Y/N): ") 
if math_com == "Y":
    print("The course final exam is Thursday, December 15, 4:30 - 6:30 pm")
else:
    time = input("Time (example: 8:00, 9:30. Leave blank if not appliceable): ")
    period = input("AM or PM (Leave blank if not appliceable): ")
    days = input("Days (TR, MWF, etc. Leave blank if not appliceable): ")
    credit_hours = input("Credit hours (Leave blank if not appliceable): ")

    find_exam_time(time, period, credit_hours, days, math_com)

