from flask import Flask, render_template

app = Flask(__name__, template_folder='./templates', static_folder='./css')

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/main")
def displayProduct():
    produits = [
        {"id": 1, "nom": "Ordi", "prix": 899.99},
        {"id": 2, "nom": "Clavier", "prix": 129.99},
        {"id": 3, "nom": "TV", "prix": 249.99},
        {"id": 4, "nom": "Casque", "prix": 79.99},
        {"id": 5, "nom": "Souris", "prix": 59.99}
    ]

    return render_template("main.html", produits = produits)


if __name__ == "__main__":
    app.run(debug=True)

