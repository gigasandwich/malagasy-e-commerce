DROP DATABASE IF EXISTS e_commerce;
CREATE DATABASE e_commerce;
USE e_commerce;

CREATE TABLE categorie_produit (
    id INT PRIMARY KEY AUTO_INCREMENT,
    categorie VARCHAR(50)
);

CREATE TABLE produit (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100),
    prix DECIMAL(15,2),
    id_categorie_produit INT,
    FOREIGN KEY (id_categorie_produit) REFERENCES categorie_produit(id) ON DELETE CASCADE
);

CREATE TABLE user (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100),
    mot_de_passe VARCHAR(255),
    solde DECIMAL(15,2)
);

CREATE TABLE commentaire (
    id INT PRIMARY KEY AUTO_INCREMENT,
    commentaire TEXT,
    id_produit INT,
    id_user INT,
    FOREIGN KEY (id_produit) REFERENCES produit(id) ON DELETE CASCADE,
    FOREIGN KEY (id_user) REFERENCES user(id) ON DELETE CASCADE
);

CREATE TABLE commande (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_produit INT,
    id_user INT,
    FOREIGN KEY (id_produit) REFERENCES produit(id),
    FOREIGN KEY (id_user) REFERENCES user(id)
);