from typing import List
from sqlalchemy.orm import Mapped
from extensions import db

class CategorieProduit(db.Model):
    __tablename__ = 'categorie_produit'
    id = db.Column(db.Integer, primary_key=True)
    categorie = db.Column(db.String(50), nullable=False)
    
    def __repr__(self) -> str:
        return f"<CategorieProduit {self.categorie}>"

class Produit(db.Model):
    __tablename__ = 'produit'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prix = db.Column(db.Numeric(15, 2), nullable=False)
    id_categorie_produit = db.Column(db.Integer, db.ForeignKey('categorie_produit.id'), nullable=False)
    
    categorie: Mapped['CategorieProduit'] = db.relationship('CategorieProduit', backref='produits')
    commentaires: Mapped[List['Commentaire']] = db.relationship('Commentaire', backref='produit')
    commandes: Mapped[List['Commande']] = db.relationship('Commande', backref='produit')

    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "prix": float(self.prix),
            "id_categorie_produit": self.id_categorie_produit,
        }
    
    def __repr__(self) -> str:
        return f"<Produit {self.nom}, {self.prix}>"

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    mot_de_passe = db.Column(db.String(255), nullable=False)
    solde = db.Column(db.Numeric(15, 2), nullable=False)
    
    commentaires: Mapped[List['Commentaire']] = db.relationship('Commentaire', backref='user')
    commandes: Mapped[List['Commande']] = db.relationship('Commande', backref='user')

    def __repr__(self) -> str:
        return f"<User {self.nom}, Solde: {self.solde}>"

class Commentaire(db.Model):
    __tablename__ = 'commentaire'
    id = db.Column(db.Integer, primary_key=True)
    commentaire = db.Column(db.Text, nullable=False)
    id_produit = db.Column(db.Integer, db.ForeignKey('produit.id'), nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "commentaire": self.commentaire,
            "id_produit": self.id_produit,
            "id_user": self.id_user,
        }
    
    def __repr__(self) -> str:
        return f"<Commentaire {self.commentaire[:30]}...>"

class Commande(db.Model):
    __tablename__ = 'commande'
    id = db.Column(db.Integer, primary_key=True)
    id_produit = db.Column(db.Integer, db.ForeignKey('produit.id'), nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def has_bought(user_id, product_id) -> bool:
        return Commande.query.filter_by(id_user=user_id, id_produit=product_id).first() is not None

    def __repr__(self) -> str:
        return f"<Commande ProduitID: {self.id_produit}, UserID: {self.id_user}>"