INSERT INTO user (nom, mot_de_passe, solde) VALUES
('Jean', '1234', 500000.00),
('Hary', '1234', 300000.00),
('Koto', '1234', 400000.00),
('Rojo', '1234', 500000.00),
('Tsinjo', '1234', 600000.00);

INSERT INTO categorie_produit (categorie) VALUES
('Sakafo'),
('Zavatra vita amin''ny tanana'),
('Boky');

-- Sakafo
INSERT INTO produit (nom, prix, id_categorie_produit) VALUES
('Vary Gasy', 8000.00, 1),
('Mofo Sakay', 500.00, 1),
('Lasary Romazava', 6500.00, 1),
('Sambos Malagasy', 1200.00, 1),
('Akoho sy Voanio', 15000.00, 1),
('Koba Ravina', 2000.00, 1),
('Ranon''ampango', 2500.00, 1),
('Masikita', 300.00, 1),
('Voanjobory sy Henakisoa', 10000.00, 1),
('Mokary', 1000.00, 1);

-- Zavabita @ tanana
INSERT INTO produit (nom, prix, id_categorie_produit) VALUES
('Lamba Landy', 45000.00, 2),
('Kitapo Rofia', 25000.00, 2),
('Satroka Antemoro', 18000.00, 2),
('Vilia Tanimanga', 15000.00, 2),
('Poketram-behivavy', 80000.00, 2),
('Kifafa', 35000.00, 2),
('Salaka mena', 12000.00, 2),
('Kapa fotsy', 30000.00, 2),
('Kilalaon-jaza', 55000.00, 2),
('Zipo', 28000.00, 2);

-- Boky
INSERT INTO produit (nom, prix, id_categorie_produit) VALUES
('Laureat Malagasy', 15000.00, 3),
('Vakivakim-piainana', 12000.00, 3),
('Ho avy ny maraina', 20000.00, 3),
('Mitaraina ny tany', 10000.00, 3),
('Adidy miafina', 25000.00, 3),
('Iza no anjarako', 18000.00, 3),
('Domohina', 8000.00, 3),
('Menarana', 15000.00, 3),
('Voninkazon-jaridaina', 22000.00, 3),
('Trano rava', 10000.00, 3);

-- Comments Sakafo 
INSERT INTO commentaire (commentaire, id_produit, id_user) VALUES
('Mahafinaritra be! Tena mamy ny Vary Gasy.', 1, 1),
('Tsara ny kalitao, fa mba hampitomboina ny habetsahana.', 1, 2),
('Ny vidiny dia mirary ary mahavoky tsara.', 1, 3),

('Tena mafana foana ny Mofo Sakay, tiako be!', 2, 4),
('Mety tsara amin’ny sakafo maraina, mahavoky!', 2, 5),
('Tsara ny tsiro, fa somary madinika loatra.', 2, 1),

('Ny Lasary Romazava dia tena matsiro be!', 3, 2),
('Mba ampiana sakafo kely fa somary kely loatra.', 3, 3),
('Tiako fa tena manome tsiro malagasy tena izy.', 3, 4),

('Mahafinaritra ny Sambos Malagasy, tena croquant!', 4, 5),
('Tsara ny fofona sy ny tsiro, fa mba tsy ho masiaka loatra.', 4, 1),
('Mety tsara amin’ny gouter, ho avy indray aho!', 4, 2),

('Tena matsiro ny Akoho sy Voanio, tena authentic!', 5, 3),
('Mety tsara amin’ny sakafo hariva, be dia be.', 5, 4),
('Sady mamy no manitra, tena nahafinaritra.', 5, 5),

('Mahafinaritra ny Koba Ravina, tena mamy!', 6, 1),
('Tsara amin’ny zava-pisotro mafana, mifanaraka tsara.', 6, 2),
('Nostalgique be! Nahatsiarovako ny fahazazana.', 6, 3),

('Ranon’ampango matsiro be! Toy ny fanaon’ny Neny.', 7, 4),
('Mafana tsara, mety amin’ny maraina.', 7, 5),
('Tena mety amin’ny sakafo malagasy, tsara be.', 7, 1),

('Masikita no tena tiako amin’ny barbecue!', 8, 2),
('Matsiro fa mba ampiana hena kely kokoa.', 8, 3),
('Mety tsara amin’ny lanonana sy fety.', 8, 4),

('Voanjobory sy Henakisoa tena matsiro sy malefaka!', 9, 5),
('Mba ampiana saosy kely ho an’ny tsiro lavorary.', 9, 1),
('Mahafinaritra! Tena Malagasy authentic.', 9, 2),

('Ny Mokary dia tena mamy sy malefaka!', 10, 3),
('Mety tsara amin’ny dite na kafe!', 10, 4),
('Mahafinaritra fa mba hampitomboina kely.', 10, 5);

-- Comments Vita tanana
INSERT INTO commentaire (commentaire, id_produit, id_user) VALUES
('Tena malefaka sy tsara kalitao ny Lamba Landy!', 11, 1),
('Ny loko dia tena manintona sy mampiavaka.', 11, 2),
('Sady mahafinaritra no maharitra ela.', 11, 3),

('Mety tsara amin’ny fitsangatsanganana ny Kitapo Rofia!', 12, 4),
('Sady tsara tarehy no maharitra, tiako be.', 12, 5),
('Mety tsara amin’ny fanomezana, tena tsara!', 12, 1),

('Satroka Antemoro tena maivana sy mahafinaritra.', 13, 2),
('Tsara amin’ny andro mafana, tena ilaina.', 13, 3),
('Ny endrika sy ny famoronana dia tena tsara.', 13, 4),

('Vilia Tanimanga tena tsara amin’ny endrika sy ny kalitao.', 14, 5),
('Mahafinaritra amin’ny sakafo Malagasy!', 14, 1),
('Tsy dia mavesatra loatra, mety amin’ny fampiasana isan’andro.', 14, 2),

('Poketram-behivavy tena classy sy elegant!', 15, 3),
('Ny fitaovana ampiasaina dia tena maharitra.', 15, 4),
('Tsara amin’ny fety sy lanonana, tiako be!', 15, 5),

('Kifafa mahavita manadio tsara sy mateza.', 16, 1),
('Mety amin’ny trano sy tokotany, mahafinaritra.', 16, 2),
('Tsy dia mora simba, kalitao tsara.', 16, 3),

('Salaka mena tena manome endrika Malagasy.', 17, 4),
('Tena mahafinaritra amin’ny fitafiana nentim-paharazana.', 17, 5),
('Sady tsotra no tsara, tena manome style!', 17, 1),

('Kapa fotsy tena mahazo aina sy maharitra.', 18, 2),
('Mety amin’ny akanjo rehetra, tsotra nefa classy.', 18, 3),
('Ny habe dia mety tsara, tena mahazo aina.', 18, 4),

('Kilalaon-jaza tena mahafinaritra sy azo antoka.', 19, 5),
('Natao ho an’ny ankizy, tsy misy loza mety hitranga.', 19, 1),
('Mahavita manome fahafinaretana amin’ny ankizy!', 19, 2),

('Zipo tsara tarehy sy mirindra amin’ny vatana.', 20, 3),
('Tena mahafinaritra amin’ny fety sy fotoana manokana.', 20, 4),
('Ny endrika sy ny fanjairana dia tena matotra.', 20, 5);

-- Comments Boky
INSERT INTO commentaire (commentaire, id_produit, id_user) VALUES
('Laureat Malagasy dia tena manampy amin’ny fiofanana!', 21, 1),
('Boky tsara ho an’ny mpianatra, feno fampianarana.', 21, 2),
('Tena ilaina amin’ny fianarana, tsipiriany tsara.', 21, 3),

('Vakivakim-piainana dia feno lesona sarobidy.', 22, 4),
('Ny tantara dia tena mandona sy misy dikany lalina.', 22, 5),
('Mahafinaritra, manome aingam-panahy.', 22, 1),

('Ho avy ny maraina dia manome fanantenana.', 23, 2),
('Tsara soratra sy manana tantara mahavariana.', 23, 3),
('Tena boky tsara ho an’ny tia tantara.', 23, 4),

('Mitaraina ny tany dia manaitra amin’ny olana ara-tontolo iainana.', 24, 5),
('Manan-danja ho an’ny fahatsiarovan-tena ara-tsosialy.', 24, 1),
('Tena tsara fa somary lava loatra.', 24, 2),

('Adidy miafina dia boky feno tantara mahaliana.', 25, 3),
('Ny hafatra ao anatiny dia tena lalina.', 25, 4),
('Sarobidy ho an’ny tia tantara manitikitika saina.', 25, 5),

('Iza no anjarako dia tantara feno fihetseham-po.', 26, 1),
('Mampianatra amin’ny fiainana andavanandro.', 26, 2),
('Mahafinaritra, tsy zakako nijanona tamin’ny famakiana.', 26, 3),

('Domohina dia boky misy tantara mampientanentana.', 27, 4),
('Tsara fa somary fohy loatra.', 27, 5),
('Manaitra ary mahery vaika ny fanehoana ny fiainana.', 27, 1),

('Menarana dia tantara misy mistery mahafinaritra.', 28, 2),
('Tsy nampoiziko ny fiafaran’ny tantara, tena tsara!', 28, 3),
('Misy lesona maro azo tsoahina amin’ny fiainana.', 28, 4),

('Voninkazon-jaridaina dia tantara feno fihetseham-po lalina.', 29, 5),
('Tiako ny fomba fanoratra, sady mamy no mahafinaritra.', 29, 1),
('Tantaram-pitiavana tsara sy mahasarika.', 29, 2),

('Trano rava dia misy lesona lehibe amin’ny fiainana.', 30, 3),
('Tantaran’ny fiainana izay tena mahakasika.', 30, 4),
('Fomba fanoratra mahaliana, tiako be!', 30, 5);