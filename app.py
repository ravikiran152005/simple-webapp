import os
from flask import Flask
from flask_mysqldb import MySQL      # For newer versions of flask-mysql 
# from flask.ext.mysql import MySQL   # For older versions of flask-mysql
app = Flask(__name__)

mysql = MySQL()

mysql_database_host = os.getenv("MYSQL_DATABASE_HOST", "localhost")

# MySQL configurations
app.config['MYSQL_USER'] = 'db_user'
app.config['MYSQL_PASSWORD'] = 'Passw0rd'
app.config['MYSQL_DB'] = 'employee_db'
app.config['MYSQL_HOST'] = mysql_database_host
mysql.init_app(app)

@app.route("/")
def main():
    print("Home route was called")
    return """
        <!DOCTYPE html>
        <html>
        <head><title>Welcome</title></head>
        <body style='font-family:sans-serif; text-align:center; margin-top:20%;'>
            <h1>Welcome RAVIKIRAN!</h1>
            <p>Your Flask app is running inside Docker.</p>
        </body>
        </html>
    """

@app.route('/howareyou')
def hello():
    return 'I am good, how about you?'

@app.route('/read from database')
def read():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM employees")
    result = [row[0] for row in cur.fetchall()]
    cur.close()
    return ",".join(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
