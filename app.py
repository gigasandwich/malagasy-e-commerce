from flask import Flask, render_template, jsonify, request

app = Flask(__name__, template_folder='./templates', static_folder='./static')

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

@app.route("/ajoutPanier")
def ajoutPanier():
    produits = [
        {"id": 1, "nom": "Ordi", "prix": 899.99},
        {"id": 2, "nom": "Clavier", "prix": 129.99},
        {"id": 3, "nom": "TV", "prix": 249.99},
        {"id": 4, "nom": "Casque", "prix": 79.99},
        {"id": 5, "nom": "Souris", "prix": 59.99}
    ]
    product_id = request.args.get("id", type=int)  # Récupère l'ID passé en AJAX
    produit = next((p for p in produits if p["id"] == product_id), None)
    
    if produit:
        return jsonify(produit)
    else:
        return jsonify({"error": "Produit non trouvé"}), 404


if __name__ == "__main__":
    app.run(debug=True)

