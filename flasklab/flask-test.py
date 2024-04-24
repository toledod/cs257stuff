import flask

app = flask.Flask(__name__)

#
@app.route('/hello')
def my_function():
    return "Hello World!"

@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2;
    return the_string

@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:Orange">' + word1 + '</h1>'

@app.route('/add/<num1>/<num2>')
def my_add(num1, num2):
    addResult = int(num1) + int(num2)
    result = str(addResult)
    string = "the result is " + result;
    return string
    
@app.route('/pop/<abb>')
def popGet(abb):
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="toledod",
        user="toledod",
        password="mask777glass")
    
    cur = conn.cursor()

    sql = "SELECT * FROM usstatepop WHERE code = %s;"

    
    cur.execute( sql, [abb] )
    row = cur.fetchone()
    string = "The population of " + row[1] + "is : " + row[2];
    
    return string

if __name__ == '__main__':
    my_port = 5129
    app.run(host='0.0.0.0', port = my_port) 

