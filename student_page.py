#! C:\Anaconda3\python
print ("Content-Type: text/html\r\n")
print("<!DOCTYPE html>")
print("<html><body bgcolor='Silver'>")
print("<form action='task_status_load.py' method='get'>")
print("<input type='text' name='name' value='Raja' />")
print("<input type='text' name='task' value='Task1'/>")    
print("<input type='hidden' name='status' value='started' />")
print("<input type='submit' value='Start' />")
print("</form>")
print("<form action='task_status_load.py' method='get'>")
print("<input type='text' name='name' value='Raja' />")
print("<input type='text' name='task' value='Task1'/>")
print("<input type='hidden' name='status' value='completed' />")    
print("<input type='submit' value='Completed' />")    
print("</form>")
print("</body></html>")
