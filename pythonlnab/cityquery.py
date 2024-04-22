import psycopg2

def findNorthfield():

   # You will need to change the Port and the Password to use this code
    
   conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="toledod",
        user="toledod",
        password="mask777glass")
    
   cur = conn.cursor()

   sql = "SELECT * FROM uscitiestop1k WHERE city = 'Northfield';"
    
   cur.execute( sql )

   # fetchall() returns a list containing all rows that matches your query
   row_list = cur.fetchone()

   # It is often useful to loop through all rows in a query result
   if row_list == None:
      print("City does not exist")
      return None
   
   for row in row_list:
       print( row[3] )
       print( row[4] )
    
   # Note: We could access individual items in the row
   # That is, row[0] would be the name column in the previous example
   #   ... and row[1] would be the abb column

   # Here I am leaving out the conn.commit() because we aren't changing
   #    either the database or the data in the database
    
   return None

findNorthfield()
