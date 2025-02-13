from flask import Flask , render_template, request

app=Flask(__name__)

@app.route('/')
def index():
    titulo = "IDGS801"
    lista = ["Juan", "Pedro", "Maria", "Jose"]
    return render_template("index.html", titulo=titulo, lista=lista)

@app.route('/ejemplo1')
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route('/ejemplo2')
def ejemplo2():
    return render_template("ejemplo2.html")

@app.route('/HOLA')
def hola():
    return "<h1>Hola, Mundo!-- HOLA --</h1>"

@app.route("/user/<string:user>")
def user(user):
    return f"<h1>HOLA: {user}</h1>"

@app.route("/numero/<int:n1>")
def numero(n1):
    return f"<h1>Numero: {n1}</h1>"

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return f"<h1>HOLA: {username} - TU ID ES: {id}</h1>"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f"<h1>La suma es: {n1 + n2}</h1>"

@app.route("/default/")
@app.route("/default/<string:param>")
def func(param="Juan"):
    return f"<h1>Hola: {param}</h1>"

@app.route("/operas")
def operas():
    return '''
    <form action="/procesar" method="post">
        <label for="name">Nombre:</label>
        <input type="text" id="name" name="name" required>
        <br><br>

        <label for="email">Correo:</label>
        <input type="email" id="email" name="email" required>
        <br><br>

        <button type="submit">Enviar</button>
    </form>
    '''




@app.route("/procesar", methods=["POST"])
def procesar():
    return "<h1>Formulario enviado correctamente</h1>"




@app.route("/OperasBas")
def operas1():
    return render_template("OperasBas.html", resultado=None)


@app.route("/resultado", methods=["GET", "POST"])
def result():
    n1=request.form.get("n1")
    n2=request.form.get("n2")

    operacion = request.form.get("operacion")

    # Verificar si los números están vacíos
    if not n1 or not n2:
        resultado = "Por favor, ingrese ambos números"
    else:
        n1 = int(n1)
        n2 = int(n2)

        if operacion == "suma":
            resultado = "La suma de {} + {} es {}".format(n1, n2, n1 + n2)
        
        elif operacion == "resta":
            resultado = "La resta de {} - {} es {}".format(n1, n2, n1 - n2)

        elif operacion == "multiplicar":
            resultado = "La multiplicación de {} × {} es {}".format(n1, n2, n1 * n2)

        elif operacion == "dividir":
            if n2 != 0:
                resultado = "La división de {} ÷ {} es {}".format(n1, n2, n1 / n2)
            else:
                resultado = "Error: No se puede dividir entre cero"
        else:
            resultado = "Error: Seleccione una operación válida"

    return render_template("OperasBas.html", resultado=resultado)



if __name__ == "__main__":
    app.run(debug=True, port=5000)