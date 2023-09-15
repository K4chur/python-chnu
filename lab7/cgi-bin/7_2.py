#!C:\Python311\python.exe

import cgi

# Встановлюємо HTTP-заголовки для відповіді
print("Content-type: text/html\n")

# Отримуємо дані від користувача з POST-запиту
form = cgi.FieldStorage()

num_x = float(form["num_x"].value)
num_y = float(form["num_y"].value)

if num_x < 0 and num_y < 0:
    num_x = abs(num_x)
    num_y = abs(num_y)
elif (num_x < 0 <= num_y) or (num_x >= 0 > num_y):
    num_x += 0.5
    num_y += 0.5

print("<html>")
print("<head>")
print("<title>Результат обчислення</title>")
print("</head>")
print("<body>")
print("<h1>Some data</h1>")
print("<div>")
print(f"<p>X: {num_x}</p>")
print(f"<p>Y: {num_y}</p>")
print("</div>")
print("</body>")
print("</html>")
