$(document).ready(function() {
    let panier = {}; // Stocke les produits ajoutés

    $(".ajout-panier").click(function(e) {
        e.preventDefault(); // Empêche le lien de recharger la page

        let productId = $(this).data("id"); // Récupère l'ID du produit
        $.ajax({
            url: "/ajoutPanier",
            type: "GET",
            data: { id: productId },  // Envoie l'ID du produit en paramètre
            dataType: "json",
            success: function(data) {
                if (!panier[data.id]) {
                    // Si le produit n'est pas encore dans le panier, on l'ajoute avec quantité 1
                    panier[data.id] = { nom: data.nom, prix: data.prix, quantite: 1, id: productId };
                } else {
                    // Si le produit est déjà dans le panier, on augmente la quantité
                    panier[data.id].quantite++;
                }

                mettreAJourPanier();
            },
            error: function(e) {
                alert("Erreur lors de l'ajout au panier !" + e);
                console.log(e);
            }
        });
    });

    function mettreAJourPanier() {
        let panierHTML = `
            <h3>Panier</h3>
        `;

        if (Object.keys(panier).length === 0) {
            panierHTML += `<p>Votre panier est vide.</p>`;
        } else {
            for (let id in panier) {
                let produit = panier[id];

                panierHTML += `
                    <div class="info-panier">
                        <div class="info1">
                            <div class="id" style = "display: none;"> 
                                ${produit.id}
                            </div>  
                            <div class="nom-produit">
                                ${produit.nom}
                            </div>
                            <div class="quantite-produit">
                                x${produit.quantite}
                            </div>
                        </div>
                        <div class="prix">
                            Prix: <br>
                            ${produit.prix * produit.quantite}$
                        </div>
                    </div>
                `;
            }
        }

        panierHTML += `
            <div class="button-panier">
                <a href="#">Acheter</a>
            </div>
        `;

        $("#panier-contenu").html(panierHTML);
    }

    $(".button-panier a").click(function(event) {
        event.preventDefault();
        let panierData = []     // variable de stckage des donnees dans le panier

        $(".info-panier").each(function(){
            let nomProduit = $(this).find(".nom-produit").text().trim();
            let quantite = parseInt$(this).find(".quantite-produit").text().replace("x", "");
            let prix = parseFloat$(this).find(".prix").text().replace("prix", "").replace("$", "");
            let id = parseInt$(this).find(".id").text().trim();

            panierData.push({
                id: id,
                nom: nomProduit,
                quantite: quantite,
                prix: prix
            });
        });
        console.log("Données envoyées :", panierData); // Vérifie dans la console

        $.ajax({
            url: "/acheter",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({panier: panierData}),     // convertir en JSON
            success:function(response) {
                alert(response.message);
            },
            error: function(error) {
                console.error("Erreur lors de l'achat", error);
            }
        });
    });
});
