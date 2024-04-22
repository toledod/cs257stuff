# We use the psycopg2 library to help us connec to the Postgres SQL database
# This library is already installed on stearns.mathcs.carleton.edu
import psycopg2

# This function tests to make sure that you can connect to the database
def test_connection():

    # You will need to change the Port and the Password to use this code
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="toledod",
        user="toledod",
        password="mask777glass")

    if conn is not None:
        print( "Connection Worked!" )
    else:
        print( "Problem with Connection" )

    return None


# This function sends an SQL query to the database
def test_query_one():

    # You will need to change the Port and the Password to use this code
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="toledod",
        user="toledod",
        password="mask777glass")

    cur = conn.cursor()

    conn2 = psycopg2.connect(
	host="localhost",
        port=5432,
        database="mlepinski",
        user="toledod",
        password="mask777glass"

)
    cur2 = conn2.cursor()



    sql = """DROP TABLE IF EXISTS usstatepop;
	CREATE TABLE usstatepop (
  	code text,
  	state text,
  	pop INT
	);
	"""

    sql2 = """DROP TABLE IF EXISTS uscitiestop1k;
	CREATE TABLE uscitiestop1k (
  	city text,
  	state text,
  	pop int,
  	lat real,
  	ion real
	);
	"""    
    cur.execute( sql )
    cur2.execute( sql2 )
  
test_connection()
test_query_one()
