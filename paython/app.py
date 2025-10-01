from flask import Flask, render_template, request, redirect
import pymysql.cursors

app = Flask(__name__)

db = pymysql.connect(
    host="MySQL-8.2",
    user="root",
    password="",
    database="php-mysql",
    cursorclass=pymysql.cursors.DictCursor
)

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    error = None
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    date = request.form['date']

    with db.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) as count FROM example_users WHERE email = %s", (email,))
        result = cursor.fetchone()
        if result['count'] > 0:
            error = "Пользователь с таким email уже зарегистрирован!"
            return render_template('index.html', error=error)
        else:
            sql = "INSERT INTO example_users (name, email, pass, date) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (name, email, password, date))
            db.commit()
            return render_template('index.html', success="Регистрация прошла успешно!")

if __name__ == '__main__':
    app.run(debug=True)
























































































3223