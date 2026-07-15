from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <h1>🚚 Plataforma GEODIS</h1>
    <h2>Primera versión funcionando</h2>
    <p>¡Felicidades! Flask está funcionando correctamente.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)