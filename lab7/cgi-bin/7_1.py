#!C:\Python311\python.exe

import cgi

# Встановлюємо HTTP-заголовки для відповіді
print("Content-type: text/html\n")

# Отримуємо дані від користувача з POST-запиту
form = cgi.FieldStorage()

# Отримуємо значення сторін трикутника з форми
side_a = float(form["side_a"].value)
side_b = float(form["side_b"].value)
side_c = float(form["side_c"].value)

# Обчислюємо площу трикутника за формулою Герона
s = (side_a + side_b + side_c) / 2
area = (s * (s - side_a) * (s - side_b) * (s - side_c)) ** 0.5

# Виводимо результат обчислення площі
print("<html>")
print("<head>")
print("<title>Результат обчислення</title>")
print("</head>")
print("<body>")
print("<h1>Площа трикутника</h1>")
print("<div>")
print(f"<p>Сторона A: {side_a}</p>")
print(f"<p>Сторона B: {side_b}</p>")
print(f"<p>Сторона C: {side_c}</p>")
print(f"<p>Площа трикутника: {area:.2f}</p>")
print("</div>")
print("</body>")
print("</html>")
