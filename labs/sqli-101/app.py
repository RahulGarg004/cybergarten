from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# --- Database Setup ---
conn = sqlite3.connect(':memory:', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('CREATE TABLE users (username TEXT, password TEXT)')
cursor.execute("INSERT INTO users VALUES ('admin', 'p@ssword123')")
conn.commit()

# --- HTML Template ---
LOGIN_TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>Login Page</title></head>
<body>
    <h2>Please Login</h2>
    <form method="POST">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
    <p style="color:red;">{{ message }}</p>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # VULNERABLE QUERY!
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            message = f"Welcome, {result[0]}!"
        else:
            message = "Invalid credentials."

    return render_template_string(LOGIN_TEMPLATE, message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
