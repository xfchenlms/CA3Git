import csv
import sqlite3

# open the connection to the database
conn = sqlite3.connect('bus_stops_data.db')
cur = conn.cursor()

# drop the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS bus_stops')
print("table dropped successfully");
# creat bus_stops table
conn.execute('CREATE TABLE bus_stops (No INTEGER PRIMARY KEY, NaptanCode INTEGER, CommonName TEXT)')
print("table created successfully");

# drop the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS details')
print("table dropped successfully");
# create typeXY table
conn.execute('CREATE TABLE details (NaptanCode INTEGER PRIMARY KEY, CommonName TEXT, Street TEXT, LocalityName TEXT, BusStopType TEXT, x INTEGER, y INTEGER)')
print("table created successfully");

# open the file to read it into the database
with open('CA3/Bus_Stops_1.csv', newline='') as f:
  reader = csv.reader(f, delimiter=",")
  next(reader) # skip the header line
  for row in reader:
    print(row)
    
    No = row[0]
    NaptanCode = row[1]
    CommonName = row[2]

    cur.execute('INSERT INTO bus_stops VALUES (?,?,?)', (No, NaptanCode, CommonName))
    conn.commit()
print("data parsed successfully");

# open the file to read it into the database
with open('CA3/Bus_Stops_2.csv', newline='') as f:
  reader = csv.reader(f, delimiter=",")
  next(reader) # skip the header line
  for row in reader:
    print(row)
    
    NaptanCode = row[0]
    CommonName = row[1]
    Street = row[2]
    LocalityName = row[3]
    BusStopType = row[4]
    x = row[5]
    y = row[6]

    cur.execute('INSERT INTO details VALUES (?,?,?,?,?,?,?)', (NaptanCode, CommonName, Street, LocalityName, BusStopType, x, y))
    conn.commit()
print("data parsed successfully");

conn.close()