import psycopg2

def test_query_all():

    # You will need to change the Port and the Password to use this code
    
    conn = psycopg2.connect(
        host="localhost",
        port=9999,
        database="mlepinski",
        user="mlepinski",
        password="MyDatabasePassword")

    cur = conn.cursor()

    sql = "SELECT name, abb FROM states"
    
    cur.execute( sql )

    # fetchall() returns a list containing all rows that matches your query
    row_list = cur.fetchall()

    # It is often useful to loop through all rows in a query result
    for row in row_list:
        print( row[1] )
    
    # Note: We could access individual items in the row
    # That is, row[0] would be the name column in the previous example
    #   ... and row[1] would be the abb column

    # Here I am leaving out the conn.commit() because we aren't changing
    #    either the database or the data in the database
    
    return None
