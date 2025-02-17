import mysql.connector
from flask import Flask,render_template

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root' ,
    password = '',
    database = 'JamalAwangLegacy'   
 
    )
if conn.is_connected():
    print('Connected to MySQL database')

cursor = conn.cursor()  

cursor.execute('SELECT * FROM person')
data = cursor.fetchall()

for row in data:
    print(row)      


cursor.close()
conn.close()


app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)