from flask import Flask, render_template, request

app = Flask(__name__)

class Cinepolis:
    def calcular_descuento(self, cantidad_boletos, usa_tarjeta):
        precio_boletos = cantidad_boletos * 12  # Cada boleto cuesta $12

        if cantidad_boletos > 5:
            descuento = precio_boletos * 0.15
        elif 3 <= cantidad_boletos <= 5:
            descuento = precio_boletos * 0.10
        else:
            descuento = 0

        total = precio_boletos - descuento

        if usa_tarjeta:
            total = total * 0.90  

        return round(total, 2)


cinepolis = Cinepolis()  

@app.route("/Cinepolis")
def index():
    return render_template("cinepolis.html", resultado=None)


@app.route("/procesar", methods=["POST"])
def procesar():
    nombre = request.form.get("nombre")
    cantidad_compradores = int(request.form.get("compradores", 0))
    cantidad_boletos = int(request.form.get("boletos", 0))
    usa_tarjeta = request.form.get("tarjeta") == "si"

    if cantidad_boletos > (7 * cantidad_compradores):
        return render_template("cinepolis.html", resultado="No puedes comprar más de 7 boletos por persona.")

    total = cinepolis.calcular_descuento(cantidad_boletos, usa_tarjeta)

    return render_template("cinepolis.html", resultado=f"Total a pagar: ${total}")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
