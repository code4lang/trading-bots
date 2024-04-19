<?php
// Récupération des données du formulaire
$nomPrenom = $_POST['nom_prenom'];
$age = intval($_POST['age']);
$quantiteCarreOr = intval($_POST['quantite_carre_or']);
$quantitePremiereCategorie = intval($_POST['quantite_premiere_categorie']);
$quantiteDeuxiemeCategorie = intval($_POST['quantite_deuxieme_categorie']);
$carteFidelite = $_POST['carte_fidelite'];

// Calcul du prix du billet à l'unité
// ...

// Calcul des sous-totaux
// ...

// Calcul du total à régler
// ...

// Affichage des informations
echo "Prix du billet à l'unité : €XX.XX<br>";
echo "Quantité sélectionnée (carré or) : $quantiteCarreOr<br>";
// ...

// Message de bienvenue en fonction de l'âge
if ($age >= 30) {
        echo "Bonjour, $nomPrenom !<br>";
} else {
        echo "Salut, $nomPrenom !<br>";
}

// Points cumulés avec la carte de fidélité
// ...

// Validation de la carte de fidélité
if (($carteFidelite == 'carte jeune - 26 ans' && $age > 26) || ($carteFidelite == 'carte senior +65' && $age < 65)) {
        echo "Vous n'avez pas le droit à cette carte de fidélité !";
}
?>

