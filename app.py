from flask import Flask, render_template, jsonify, request
from model.models import CategorieProduit, Produit, User, Commentaire, Commande
from extensions import db

app = Flask(__name__, template_folder='./templates', static_folder='./static')

user = 'root'
host = '127.0.0.1'
db_name = 'e_commerce'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}@{host}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app) # instead of db = SQLAlchemy(app), we initialize it at the module extensions

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/main")
def displayProduct():
    produits = Produit.query.all()
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
    
@app.route("/produit/info/<int:id>")
def infoProduit(id):
    produit = Produit.query.filter_by(id=id).first_or_404()
    commentaires = produit.commentaires
    return render_template("info-product.html", produit=produit, commentaires=commentaires)

if __name__ == "__main__":
    app.run(debug=True, port=5000)