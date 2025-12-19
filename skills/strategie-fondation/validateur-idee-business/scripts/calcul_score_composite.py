#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calcul du score composite de validation d'idée business
Framework 10 Dimensions pour Hacienda Marketing Pack
"""

import sys
import os

# Ajouter le chemin vers les utilitaires partagés
script_dir = os.path.dirname(os.path.abspath(__file__))
shared_scripts = os.path.abspath(os.path.join(script_dir, '../../../../shared/scripts'))
sys.path.insert(0, shared_scripts)

from utils_scoring import calculer_score_composite, evaluer_niveau
from utils_visualisation import creer_barre_progression, creer_graphique_barres, creer_boite_info


def calculer_score_validation_10d(scores_dimensions: dict, poids: dict = None) -> dict:
    """
    Calcule le score de validation 10D complet.
    
    Args:
        scores_dimensions: Dict avec les scores des 10 dimensions (1-10)
        poids: Dict optionnel avec les pondérations personnalisées
    
    Returns:
        Dict avec score final, détails, et recommandations
    """
    
    # Validation des dimensions
    dimensions_requises = [
        'probleme', 'solution', 'marche', 'timing', 'competences',
        'differenciation', 'monetisation', 'validation', 'ressources', 'passion'
    ]
    
    for dim in dimensions_requises:
        if dim not in scores_dimensions:
            raise ValueError(f"Dimension manquante : {dim}")
        if not 1 <= scores_dimensions[dim] <= 10:
            raise ValueError(f"Score de {dim} doit être entre 1 et 10")
    
    # Poids par défaut (équilibrés)
    if poids is None:
        poids = {dim: 0.1 for dim in dimensions_requises}
    
    # Calcul du score composite
    score_final, scores_ponderes = calculer_score_composite(scores_dimensions, poids)
    
    # Évaluation du niveau
    niveau = evaluer_niveau(score_final)
    
    # Identification des forces et faiblesses
    forces = [
        (dim, score) for dim, score in scores_dimensions.items() if score >= 8
    ]
    forces.sort(key=lambda x: x[1], reverse=True)
    
    faiblesses = [
        (dim, score) for dim, score in scores_dimensions.items() if score < 6
    ]
    faiblesses.sort(key=lambda x: x[1])
    
    # Recommandations basées sur le score
    recommandations = generer_recommandations(score_final, niveau, faiblesses)
    
    # Construction du résultat
    resultat = {
        'score_final': score_final,
        'niveau': niveau,
        'scores_par_dimension': scores_dimensions,
        'scores_ponderes': scores_ponderes,
        'forces': forces,
        'faiblesses': faiblesses,
        'recommandations': recommandations
    }
    
    return resultat


def generer_recommandations(score: float, niveau: str, faiblesses: list) -> list:
    """
    Génère des recommandations basées sur le score et les faiblesses.
    """
    recommandations = []
    
    # Recommandations générales selon le score
    if score >= 8:
        recommandations.append({
            'type': 'GO',
            'message': 'Excellent potentiel ! Les fondations sont solides.',
            'action': 'Concentre-toi sur l\'exécution et le lancement rapide.'
        })
    elif score >= 6:
        recommandations.append({
            'type': 'GO_AVEC_CONDITIONS',
            'message': 'Bonne base, mais quelques aspects à renforcer.',
            'action': 'Travaille sur les faiblesses identifiées avant de scaler.'
        })
    elif score >= 4:
        recommandations.append({
            'type': 'ATTENTION',
            'message': 'Potentiel mitigé. Amélioration nécessaire.',
            'action': 'Focus sur les 2-3 dimensions les plus faibles. Considère un pivot.'
        })
    else:
        recommandations.append({
            'type': 'STOP_OU_PIVOT',
            'message': 'Trop de faiblesses fondamentales.',
            'action': 'Prends du recul. Pivot majeur ou nouvelle idée recommandés.'
        })
    
    # Recommandations spécifiques par faiblesse
    for dim, score in faiblesses[:3]:  # Top 3 faiblesses
        if dim == 'probleme' and score < 6:
            recommandations.append({
                'type': 'CRITIQUE',
                'dimension': 'Problème',
                'action': 'Fais 20+ entretiens clients pour valider que le problème est réel et important.'
            })
        elif dim == 'validation' and score < 6:
            recommandations.append({
                'type': 'URGENT',
                'dimension': 'Validation',
                'action': 'Parle à des clients potentiels. Essaie de vendre avant même de construire.'
            })
        elif dim == 'marche' and score < 6:
            recommandations.append({
                'type': 'IMPORTANT',
                'dimension': 'Marché',
                'action': 'Définis mieux ton marché cible et estime le TAM/SAM/SOM précisément.'
            })
        elif dim == 'differenciation' and score < 6:
            recommandations.append({
                'type': 'IMPORTANT',
                'dimension': 'Différenciation',
                'action': 'Identifie ton avantage unique. Pourquoi toi et pas un concurrent ?'
            })
        elif dim == 'monetisation' and score < 6:
            recommandations.append({
                'type': 'IMPORTANT',
                'dimension': 'Monétisation',
                'action': 'Clarifie ton modèle économique. Valide la volonté de payer.'
            })
    
    return recommandations


def afficher_rapport_visuel(resultat: dict, nom_projet: str = "Mon Projet"):
    """
    Affiche un rapport visuel du résultat de validation.
    """
    print("\n")
    print("═" * 70)
    print(f"   RÉSULTAT DE VALIDATION - {nom_projet.upper()}")
    print("═" * 70)
    print()
    
    # Score global
    barre = creer_barre_progression(resultat['score_final'], 10, 40)
    print(f"📊 SCORE GLOBAL : {barre}")
    print(f"   Niveau : {resultat['niveau']}")
    print()
    
    # Détail des dimensions
    print("📋 DÉTAIL DES DIMENSIONS")
    print("─" * 70)
    
    dimensions_labels = {
        'probleme': '1. PROBLÈME',
        'solution': '2. SOLUTION',
        'marche': '3. MARCHÉ',
        'timing': '4. TIMING',
        'competences': '5. COMPÉTENCES',
        'differenciation': '6. DIFFÉRENCIATION',
        'monetisation': '7. MONÉTISATION',
        'validation': '8. VALIDATION',
        'ressources': '9. RESSOURCES',
        'passion': '10. PASSION'
    }
    
    for dim_key, label in dimensions_labels.items():
        score = resultat['scores_par_dimension'][dim_key]
        barre = creer_barre_progression(score, 10, 30)
        print(f"{label.ljust(20)} {barre}")
    
    print()
    print("═" * 70)
    
    # Forces
    if resultat['forces']:
        print("\n✅ POINTS FORTS")
        print("─" * 70)
        for dim, score in resultat['forces'][:3]:
            label = dimensions_labels.get(dim, dim).split('. ')[1]
            print(f"  • {label} : {score}/10")
    
    # Faiblesses
    if resultat['faiblesses']:
        print("\n⚠️ POINTS À AMÉLIORER")
        print("─" * 70)
        for dim, score in resultat['faiblesses'][:3]:
            label = dimensions_labels.get(dim, dim).split('. ')[1]
            print(f"  • {label} : {score}/10")
    
    # Recommandations
    print("\n💡 RECOMMANDATIONS")
    print("─" * 70)
    for i, reco in enumerate(resultat['recommandations'], 1):
        print(f"\n{i}. [{reco['type']}]")
        if 'dimension' in reco:
            print(f"   Dimension : {reco['dimension']}")
        if 'message' in reco:
            print(f"   {reco['message']}")
        print(f"   Action : {reco['action']}")
    
    print("\n" + "═" * 70)
    print()


def exemple_utilisation():
    """
    Exemple d'utilisation du calculateur de score.
    """
    print("=== EXEMPLE : Validation d'une Idée de SaaS ===\n")
    
    # Scores exemple pour une idée de SaaS de productivité
    scores = {
        'probleme': 8.0,      # Problème bien identifié
        'solution': 7.5,      # Solution claire
        'marche': 9.0,        # Grand marché
        'timing': 7.0,        # Bon timing (remote work)
        'competences': 6.0,   # Équipe technique mais peu business
        'differenciation': 8.0, # Innovation claire
        'monetisation': 6.5,  # Modèle SaaS classique
        'validation': 4.0,    # Peu de validation client
        'ressources': 7.0,    # Ressources correctes
        'passion': 10.0       # Passion très forte
    }
    
    # Calcul
    resultat = calculer_score_validation_10d(scores)
    
    # Affichage
    afficher_rapport_visuel(resultat, "SaaS de Productivité")
    
    # Export des données pour chaînage
    print("\n📦 DONNÉES POUR CHAÎNAGE")
    print("─" * 70)
    print(f"Score final : {resultat['score_final']}/10")
    print(f"Niveau : {resultat['niveau']}")
    print(f"Dimensions fortes : {[dim for dim, _ in resultat['forces']]}")
    print(f"Dimensions faibles : {[dim for dim, _ in resultat['faiblesses']]}")


if __name__ == "__main__":
    # Si appelé directement, lancer l'exemple
    if len(sys.argv) == 1:
        exemple_utilisation()
    else:
        print("Usage : python3 calcul_score_composite.py")
        print("Lance un exemple de calcul de score de validation 10D")
