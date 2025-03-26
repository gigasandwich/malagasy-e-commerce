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
                    panier[data.id] = { nom: data.nom, prix: data.prix, quantite: 1 };
                } else {
                    // Si le produit est déjà dans le panier, on augmente la quantité
                    panier[data.id].quantite++;
                }

                mettreAJourPanier();
            },
            error: function() {
                alert("Erreur lors de l'ajout au panier !");
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
                <a href="">Acheter</a>
            </div>
        `;

        $("#panier-contenu").html(panierHTML);
    }
});
