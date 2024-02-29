import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/bus_stops')
def bus_stops():
  try:
    # open the connection to the database
    conn = sqlite3.connect('bus_stops_data.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from bus_stops")
    rows = cur.fetchall()
    conn.close()
    return render_template('bus_stops.html', rows=rows)
  except sqlite3.Error as e:
    return f"An error occurred: {e}"


@app.route('/details')
def details():
  try:
    # open the connection to the database
    conn = sqlite3.connect('bus_stops_data.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from details")
    rows = cur.fetchall()
    conn.close()
    return render_template('details.html', rows=rows)
  except sqlite3.Error as e:
    return f"An error occurred: {e}"

if __name__ == '__main__':
  app.run()