from flask import Flask, render_template, jsonify, request
from src.model.models import CategorieProduit, Produit, User, Commentaire, Commande
from src.training import sentiment
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
def displayProductGroupByCategorie():
    categories = CategorieProduit.query.all()
    produitsParCategorie = {
        categorie: categorie.produits for categorie in categories
    }
    return render_template("main.html", produitsParCategorie = produitsParCategorie)

@app.route("/ajoutPanier")
def ajoutPanier():
    product_id = request.args.get("id", type=int)  # Récupère l'ID passé en AJAX
    produit: Produit = Produit.query.filter_by(id=product_id).first()
    
    if produit:
        return jsonify(produit.to_dict())
    else:
        return jsonify({"error": "Produit non trouvé"}), 404
    
@app.route("/produit/info/<int:id_produit>")
def infoProduit(id_produit):
    produit = Produit.query.filter_by(id=id_produit).first_or_404()
    commentaires = produit.commentaires
    
    user: User = User.query.filter_by(id=1).first()
    has_bought = user.has_bought(id_produit)

    commentaires = sentiment.get_sentiments(commentaires)
    return render_template("info-product.html", produit=produit, commentaires=commentaires, has_bought=has_bought)

@app.route("/acheter", methods = ["POST"])
def acheter():
    data = request.get_json()
    panier = data.get("panier", [])
    idUser = 1

    if not panier:
        return jsonify({"message": "Le panier est vide"}), 400

    try:
        for produit in panier:
            nouvelle_commande = Commande(
                id_produit = produit['id'],
                id_user = idUser,
                quantite = produit['quantite']
            )
            db.session.add(nouvelle_commande)
        
        db.session.commit()
        return jsonify({"message": "Achat effectue avec succes"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)