#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Utilitaires de visualisation ASCII pour Hacienda Marketing Pack
Génération de graphiques et tableaux pour terminal
"""

from typing import Dict, List, Tuple, Optional
import math


def creer_barre_progression(valeur: float, max_val: float = 10, largeur: int = 20) -> str:
    """
    Crée une barre de progression ASCII.
    
    Args:
        valeur: Valeur actuelle
        max_val: Valeur maximale
        largeur: Largeur de la barre en caractères
    
    Returns:
        Barre de progression formatée
    
    Exemple:
        >>> creer_barre_progression(7.5, 10, 20)
        '███████████████░░░░░ 7.5/10'
    """
    if max_val == 0:
        return "░" * largeur + " 0/0"
    
    proportion = min(valeur / max_val, 1.0)
    rempli = int(proportion * largeur)
    vide = largeur - rempli
    
    barre = "█" * rempli + "░" * vide
    return f"{barre} {valeur}/{max_val}"


def creer_graphique_barres(
    donnees: Dict[str, float],
    largeur_max: int = 50,
    titre: Optional[str] = None
) -> str:
    """
    Crée un graphique en barres horizontales ASCII.
    
    Args:
        donnees: Dictionnaire {label: valeur}
        largeur_max: Largeur maximale des barres
        titre: Titre optionnel du graphique
    
    Returns:
        Graphique formaté en chaîne de caractères
    """
    if not donnees:
        return "Aucune donnée"
    
    max_valeur = max(donnees.values())
    max_label = max(len(str(k)) for k in donnees.keys())
    
    lignes = []
    if titre:
        lignes.append(f"\n{titre}")
        lignes.append("=" * (largeur_max + max_label + 10))
    
    for label, valeur in donnees.items():
        proportion = valeur / max_valeur if max_valeur > 0 else 0
        barre_len = int(proportion * largeur_max)
        barre = "█" * barre_len
        
        label_pad = label.ljust(max_label)
        lignes.append(f"{label_pad} │ {barre} {valeur:.1f}")
    
    return "\n".join(lignes)


def creer_tableau(
    donnees: List[Dict[str, any]],
    colonnes: List[str],
    titre: Optional[str] = None
) -> str:
    """
    Crée un tableau ASCII formaté.
    
    Args:
        donnees: Liste de dictionnaires avec les données
        colonnes: Liste des noms de colonnes à afficher
        titre: Titre optionnel du tableau
    
    Returns:
        Tableau formaté en chaîne de caractères
    """
    if not donnees or not colonnes:
        return "Aucune donnée"
    
    # Calculer les largeurs de colonnes
    largeurs = {}
    for col in colonnes:
        largeurs[col] = max(
            len(str(col)),
            max(len(str(row.get(col, ""))) for row in donnees)
        )
    
    lignes = []
    
    # Titre
    if titre:
        largeur_totale = sum(largeurs.values()) + (len(colonnes) - 1) * 3 + 4
        lignes.append("\n" + titre)
        lignes.append("═" * largeur_totale)
    
    # En-tête
    entete = " │ ".join(str(col).ljust(largeurs[col]) for col in colonnes)
    lignes.append("│ " + entete + " │")
    
    # Séparateur
    separateur = "─".join("─" * largeurs[col] for col in colonnes)
    lignes.append("├─" + separateur + "─┤")
    
    # Lignes de données
    for row in donnees:
        ligne = " │ ".join(
            str(row.get(col, "")).ljust(largeurs[col])
            for col in colonnes
        )
        lignes.append("│ " + ligne + " │")
    
    # Ligne de fin
    lignes.append("└─" + separateur + "─┘")
    
    return "\n".join(lignes)


def creer_matrice_2x2(
    quadrants: Dict[str, List[str]],
    titre: Optional[str] = None,
    axe_x: str = "X",
    axe_y: str = "Y"
) -> str:
    """
    Crée une matrice 2x2 ASCII.
    
    Args:
        quadrants: Dict avec clés "haut_gauche", "haut_droite", "bas_gauche", "bas_droite"
        titre: Titre optionnel
        axe_x: Label de l'axe horizontal
        axe_y: Label de l'axe vertical
    
    Returns:
        Matrice formatée
    """
    largeur = 35
    hauteur = 8
    
    lignes = []
    
    if titre:
        lignes.append(f"\n{titre}")
        lignes.append("═" * (largeur * 2 + 3))
    
    lignes.append(f"\n{axe_y} ↑")
    lignes.append("  │")
    
    # Quadrants supérieurs
    haut_g = quadrants.get("haut_gauche", [])
    haut_d = quadrants.get("haut_droite", [])
    
    for i in range(hauteur):
        g_text = haut_g[i][:largeur-2] if i < len(haut_g) else ""
        d_text = haut_d[i][:largeur-2] if i < len(haut_d) else ""
        lignes.append(f"  │ {g_text.ljust(largeur-2)} │ {d_text.ljust(largeur-2)} │")
    
    # Ligne centrale
    lignes.append("  " + "─" * (largeur * 2 + 3) + f"→ {axe_x}")
    lignes.append("  │")
    
    # Quadrants inférieurs
    bas_g = quadrants.get("bas_gauche", [])
    bas_d = quadrants.get("bas_droite", [])
    
    for i in range(hauteur):
        g_text = bas_g[i][:largeur-2] if i < len(bas_g) else ""
        d_text = bas_d[i][:largeur-2] if i < len(bas_d) else ""
        lignes.append(f"  │ {g_text.ljust(largeur-2)} │ {d_text.ljust(largeur-2)} │")
    
    return "\n".join(lignes)


def creer_jauge_circulaire(valeur: float, max_val: float = 10, label: str = "") -> str:
    """
    Crée une jauge circulaire ASCII simplifiée.
    
    Args:
        valeur: Valeur actuelle
        max_val: Valeur maximale
        label: Label descriptif
    
    Returns:
        Jauge formatée
    """
    proportion = min(valeur / max_val, 1.0) if max_val > 0 else 0
    pourcentage = int(proportion * 100)
    
    # Segments de jauge: vide, quart, demi, trois-quarts, plein
    if pourcentage >= 90:
        symbole = "●"
    elif pourcentage >= 60:
        symbole = "◕"
    elif pourcentage >= 30:
        symbole = "◑"
    elif pourcentage > 0:
        symbole = "◔"
    else:
        symbole = "○"
    
    return f"{symbole} {label}: {valeur}/{max_val} ({pourcentage}%)"


def creer_boite_info(titre: str, contenu: List[str], largeur: int = 70) -> str:
    """
    Crée une boîte d'information encadrée.
    
    Args:
        titre: Titre de la boîte
        contenu: Liste de lignes de contenu
        largeur: Largeur de la boîte
    
    Returns:
        Boîte formatée
    """
    lignes = []
    
    # En-tête
    lignes.append("╔" + "═" * (largeur - 2) + "╗")
    titre_centre = titre.center(largeur - 2)
    lignes.append(f"║{titre_centre}║")
    lignes.append("╠" + "═" * (largeur - 2) + "╣")
    
    # Contenu
    for ligne in contenu:
        # Découper les lignes trop longues
        if len(ligne) > largeur - 4:
            mots = ligne.split()
            ligne_courante = ""
            for mot in mots:
                if len(ligne_courante) + len(mot) + 1 <= largeur - 4:
                    ligne_courante += mot + " "
                else:
                    lignes.append(f"║ {ligne_courante.ljust(largeur - 4)} ║")
                    ligne_courante = mot + " "
            if ligne_courante:
                lignes.append(f"║ {ligne_courante.ljust(largeur - 4)} ║")
        else:
            lignes.append(f"║ {ligne.ljust(largeur - 4)} ║")
    
    # Pied
    lignes.append("╚" + "═" * (largeur - 2) + "╝")
    
    return "\n".join(lignes)


if __name__ == "__main__":
    # Exemples d'utilisation
    print("=== Test utils_visualisation.py ===\n")
    
    # Test 1: Barre de progression
    print(creer_barre_progression(7.5, 10, 30))
    
    # Test 2: Graphique en barres
    donnees = {"Feature A": 8.5, "Feature B": 6.2, "Feature C": 9.1}
    print(creer_graphique_barres(donnees, titre="Scores des fonctionnalités"))
    
    # Test 3: Jauge circulaire
    print("\n" + creer_jauge_circulaire(8.5, 10, "Satisfaction"))
    
    # Test 4: Boîte info
    print("\n" + creer_boite_info(
        "Information importante",
        ["Ceci est un test", "De la boîte d'information", "Avec plusieurs lignes"]
    ))
