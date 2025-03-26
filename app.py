from flask import Flask, render_template
from model.models import CategorieProduit, Produit, User, Commentaire, Commande
from extensions import db

app = Flask(__name__, template_folder='./templates', static_folder='./css')

user = 'root'
host = '127.0.0.1'
db_name = 'e_commerce'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}@{host}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app) # instead of db = SQLAlchemy(app)

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
    app.run(debug=True, port=5000)