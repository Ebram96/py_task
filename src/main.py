import json

from db_interface import Database

from attendance import Attendance


attendance_system = Attendance(Database("attendance.db"))

print("***********Trying get_attendance('EMP01', '2020-04-01')*************")
print(json.dumps(
    attendance_system.get_attendance('EMP01', '2020-04-02'), indent=4
))
print("*********************************Done*******************************\n")

print("********************Trying get_history('EMP01')*********************")
print(json.dumps(attendance_system.get_history('EMP01'), indent=4))
print("*********************************Done*******************************\n")
