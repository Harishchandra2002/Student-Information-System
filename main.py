from flask import *
import mysql.connector
app= Flask(__name__)


@app.route('/firstorsec')
def firstorsec():
    return render_template('firstorsec.html')

@app.route('/')
def home():
    return render_template('mainpage.html')

@app.route('/mainpage')
def home1():
    return render_template('mainpage.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signin')
def signin():
    return render_template('firstorsec.html')

@app.route('/source')
def source():
    return render_template('source')

@app.route('/option')
def option():
    return render_template('firstorsec.html')


@app.route('/cards')
def display_cards():
    # Step 1: Establish a database connection
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Harish@123',
        database='1st_project'
    )
    cursor = conn.cursor()

    # Step 2: Execute a query
    query = "SELECT * FROM student_data"
    cursor.execute(query)

    # Step 3: Fetch the data
    data = cursor.fetchall()

    # Step 4: Generate a list of dictionaries
    cards = []
    for row in data:
        card = {
            'dec1': row[0],
            'dec2': row[1],
            'dec3': row[2],
            'dec4': row[3]
        }
        cards.append(card)

    # Step 5: Render the template and pass the data to it
    return render_template('cards.html', cards=cards)



if __name__=='__main__':
    app.run(debug=True)