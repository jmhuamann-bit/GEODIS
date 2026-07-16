from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <h1>🚚 Plataforma GEODIS</h1>
    <h2>Primera versión funcionando</h2>
    <p>¡Felicidades! La aplicación está publicada en Internet.</p>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)