#!C:\Users\91876\Anaconda3\python.exe

import gmaps
#Import modules for CGI handling

import cgi, cgitb
cgitb.enable()


gmaps.configure(api_key='AIzaSyBZKKIlgHqpu3EG8uNB7QFgyNZBDELANu8')

fig = gmaps.figure()
print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title>Wecolme</title>')
print('</head>')
print('<body>')
print('<center><h2>')
print(fig)
print('</h2></center>')
print('</body>')
print('</html>')