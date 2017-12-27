#! C:\Anaconda3\python
print ("Content-Type: text/html\r\n")
print("<!DOCTYPE html>")
print("<html><body bgcolor='Silver'>")

file_access=open('python.csv','r')
file_data=file_access.read()
file_data_lines = file_data.split("\n")
task_details = { }
#storing the data in the form of dictionary 
for i in range(1,len(file_data_lines)-1):
    line_data = file_data_lines[i].split(',')
    if(line_data[1] not in task_details.keys()):
        task_details[line_data[1]] ={}
        if(line_data[2] == 'started'):
            task_details[line_data[1]]["status"] = [1,0]
            task_details[line_data[1]]["student_details"] = {"completed":[],"started":[line_data[0]]}
        else:
            task_details[line_data[1]]["status"] = [0,1]
            task_details[line_data[1]]["student_details"] = {"completed":[line_data[0]],"started":[]}
    else:
        if(line_data[2] == 'started'):
            task_details[line_data[1]]["status"][0] = task_details[line_data[1]]["status"][0] + 1
            task_details[line_data[1]]["student_details"]["started"].append(line_data[0])
        else:
            task_details[line_data[1]]["status"][1] = task_details[line_data[1]]["status"][1] + 1
            task_details[line_data[1]]["student_details"]["completed"].append(line_data[0])
#to display the content
for task_name in task_details.keys():
    print(task_name,"<br>")
    val = list(task_details[task_name].keys())
    print(val[0],':',task_details[task_name][val[0]],"<br>")
    print(val[1],':<br>')
    for key1 in task_details[task_name][val[1]]:
        print(key1,":<br><br>")
        for student_name in task_details[task_name][val[1]][key1]:
            print("<tr>")
            print(student_name,"<br>")
            print("</tr>")
        print("<br>")
file_access.close() 
print("</body></html>")