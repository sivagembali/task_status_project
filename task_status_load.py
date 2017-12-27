#! C:\ProgramData\Anaconda3\python
import cgi
import datetime
print ("Content-Type: text/html\r\n")
print("<!DOCTYPE html>")
print("<html><body>")
arguments = cgi.FieldStorage()
for i in arguments.keys():
    if(i == 'task'):
        task_name = arguments[i].value
    if(i == 'name'):
        student_name = arguments[i].value
    if(i == 'status'):
        status = arguments[i].value
file_access=open('python.csv','a+')
#function for loading data into CSV file
#file_access.write("username,taskname,task_status,created date,modified date"+" \n")
def load_data(file_access,task_name,student_name,status):
    dat = datetime.datetime.now()
    file_access.write(student_name+","+task_name+","+status+","+str(dat)+",13-12-2017"+" \n")
    file_access.close()
load_data(file_access,task_name,student_name,status)
print("</body></html>")