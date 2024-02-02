from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
from flask import _request_ctx_stack as _ctx_stack


app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'tenancy_borys'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL(app)



app.static_folder = 'static'

@app.route("/")
def index():
   
    return render_template('index.html')


@app.route("/booking", methods=['POST'])
def book():
    terminal_origen_id = request.form['terminal_origen_id']
    terminal_destino_id = request.form['terminal_destino_id']

    conn = mysql.connect()
    cursor = conn.cursor()

    # Modifica la consulta para seleccionar las programaciones de horarios según la terminal de origen y destino
    query = f"SELECT * FROM transporte_programaciones WHERE terminal_origen_id = '{terminal_origen_id}' AND terminal_destino_id = '{terminal_destino_id}';"
    cursor.execute(query)

    programaciones = cursor.fetchall()
    conn.commit()
    return render_template('booking.html', programaciones=programaciones)


@app.route("/reclamos")
def reclamos():
    return render_template('reclamos.html')

@app.route("/nosotros")
def nosotros():
    return render_template('about.html')

@app.route("/servicios")
def servicios():
    return render_template('service.html')
@app.route("/contactanos")
def contactanos():
    return render_template('contact.html')
@app.route("/facturacion")
def facturacion():
    return render_template('facturacion.html')
if __name__ == "__main__":
    app.run(debug=True)
