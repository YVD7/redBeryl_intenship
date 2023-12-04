"""$---> single reposertry principle


in single reposertry pattern each classs,method shoud perform only one reseon to change or update the code

for single reposertry principle we have to create differnt classes for each opretion so it should satisfy condition i.eonly one resaon to change or update



"""
# here we have created differnt class for single reposertty principle which have one reason to update the code
class school:
    def student(self,name):
        pass
    def staff(self,staff):
        pass

class Student_attendance:
    def attendance(self,student):
        if student=="p":
            print("present mark  succesfully")
        elif student==None:
            print("student is absent")

class staff_attendance:
    def attendance(self,staff):
        if staff=="p":
            print("attendance mark succesfully and credited salary of the day")
        elif staff==None:
            print("staff is absent ...todays salary is not credited to staff")

# Creating instances of classes
school = school()
student_attendance = Student_attendance()
staff_attendance = staff_attendance()

# Marking student attendance
student_attendance.attendance("p")  # Student present
student_attendance.attendance(None)  # Student absent

# Marking staff attendance
staff_attendance.attendance("p")  # Staff present
staff_attendance.attendance(None)  # Staff absent