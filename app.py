from flask import Flask, render_template
from model.models import CategorieProduit, Produit, User, Commentaire, Commande
from extensions import db

app = Flask(__name__, template_folder='./templates', static_folder='./css')

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

if __name__ == "__main__":
    app.run(debug=True, port=5000)