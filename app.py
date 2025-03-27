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

    return render_template("info-product.html", produit=produit, commentaires=commentaires, has_bought=has_bought)

if __name__ == "__main__":
    app.run(debug=True, port=5000)