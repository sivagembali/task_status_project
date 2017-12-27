#! C:\ProgramData\Anaconda3\python
import socket

print ("Content-Type: text/html\r\n")
print("<!DOCTYPE html>")
print("<html><body bgcolor='Silver'>")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #this for getting ip address
s.connect(("8.8.8.8", 80))
print("<form action='http://%s/python/task_dashboard.py' method='get'>"%s.getsockname()[0])
print("<input type='submit' value='ViewStatus' />")
s.close()
print("</body></html>")