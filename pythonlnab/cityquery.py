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

   sql = "SELECT * FROM uscitiestop1k WHERE city = 'Chicago';"
    
   cur.execute( sql )

   # fetchall() returns a list containing all rows that matches your query
   row_list = cur.fetchone()

   # It is often useful to loop through all rows in a query result
   if row_list == None:
      print("City does not exist")
      return None
   else:
       print("Lat:", row_list[3] )
       print("Long:", row_list[4] )
    
   # Note: We could access individual items in the row
   # That is, row[0] would be the name column in the previous example
   #   ... and row[1] would be the abb column

   # Here I am leaving out the conn.commit() because we aren't changing
   #    either the database or the data in the database
    
   return None



def bigPop():
   conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="toledod",
        user="toledod",
        password="mask777glass")
    
   cur = conn.cursor()

   sql = "SELECT * FROM uscitiestop1k ORDER BY pop DESC;"
   cur.execute( sql )
   row_list = cur.fetchone()
   print("Biggest Population:", row_list[0] )

def smallMN():
   conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="toledod",
        user="toledod",
        password="mask777glass")
    
   cur = conn.cursor()

   sql = "SELECT * FROM uscitiestop1k WHERE state = 'Minnesota' ORDER BY pop ASC;"
   cur.execute( sql )
   row_list = cur.fetchone()
   print("Smallest City in MN:", row_list[0] )




def dirCit():
   conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="toledod",
        user="toledod",
        password="mask777glass")
    
   cur = conn.cursor()

   sql = "SELECT * FROM uscitiestop1k ORDER BY lat ASC;"
   cur.execute( sql )
   row_list = cur.fetchone()
   print("Most South:", row_list[0] )
   
   sql = "SELECT * FROM uscitiestop1k ORDER BY lat DESC;"
   cur.execute( sql )
   row_list = cur.fetchone()
   print("Most North:", row_list[0] )

   sql = "SELECT * FROM uscitiestop1k ORDER BY ion ASC;"
   cur.execute( sql )
   row_list = cur.fetchone()
   print("Most West:", row_list[0] )
   
   sql = "SELECT * FROM uscitiestop1k ORDER BY ion DESC;"
   cur.execute( sql )
   row_list = cur.fetchone()
   print("Most East:", row_list[0] )

def userIn():
   conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="toledod",
        user="toledod",
        password="mask777glass")
    
   cur = conn.cursor()
   userInput = input("What state you want?")
   if len(userInput) == 2:
      sql = "SELECT * FROM usstatepop WHERE code = %s;"
      state_abb1 = userInput
      cur.execute( sql, [state_abb1]  )
      row = cur.fetchone()
      stateName = row[1]
      
      sql2 = "SELECT * FROM uscitiestop1k WHERE state = %s;"

      cur.execute( sql2, [stateName] )
      tabResult = cur.fetchall()
      
      total = 0
      for x in tabResult:
         total = total + int( x[2] );
      
      print(total)
   else:
      sql = "SELECT * FROM uscitiestop1k WHERE state = %s;"
      stateName = userInput
      cur.execute( sql, [stateName]  )
      tabResult = cur.fetchall()
      
      total = 0
      for x in tabResult:
         total = total + int( x[2] );
      
      print(total)


findNorthfield()
bigPop()
smallMN()
dirCit()
userIn()




