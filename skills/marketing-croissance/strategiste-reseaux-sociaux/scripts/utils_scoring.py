#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Utilitaires de scoring pour Hacienda Marketing Pack
Fonctions communes de calcul de scores et évaluations
"""

from typing import Dict, List, Tuple, Optional
import statistics


def calculer_score_composite(
    scores: Dict[str, float],
    poids: Optional[Dict[str, float]] = None
) -> Tuple[float, Dict[str, float]]:
    """
    Calcule un score composite à partir de scores individuels et de poids.
    
    Args:
        scores: Dictionnaire {critère: score}
        poids: Dictionnaire {critère: poids} (optionnel, par défaut égal)
    
    Returns:
        Tuple (score_final, scores_pondérés)
    
    Exemple:
        >>> scores = {"qualite": 8, "prix": 6, "innovation": 9}
        >>> poids = {"qualite": 0.5, "prix": 0.2, "innovation": 0.3}
        >>> calculer_score_composite(scores, poids)
        (7.9, {...})
    """
    if not scores:
        return 0.0, {}
    
    # Poids égaux par défaut
    if poids is None:
        poids = {k: 1.0/len(scores) for k in scores.keys()}
    
    # Normalisation des poids
    total_poids = sum(poids.values())
    poids_normalises = {k: v/total_poids for k, v in poids.items()}
    
    # Calcul des scores pondérés
    scores_ponderes = {
        k: scores[k] * poids_normalises.get(k, 0)
        for k in scores.keys()
    }
    
    score_final = sum(scores_ponderes.values())
    
    return round(score_final, 2), scores_ponderes


def evaluer_niveau(score: float, seuils: Optional[Dict[str, float]] = None) -> str:
    """
    Évalue le niveau d'un score selon des seuils.
    
    Args:
        score: Score numérique (généralement 0-10)
        seuils: Dictionnaire optionnel de seuils personnalisés
    
    Returns:
        Niveau: "Excellent", "Bon", "Moyen", "Faible", "Critique"
    
    Exemple:
        >>> evaluer_niveau(8.5)
        'Excellent'
    """
    if seuils is None:
        seuils = {
            "Excellent": 8.0,
            "Bon": 6.0,
            "Moyen": 4.0,
            "Faible": 2.0,
            "Critique": 0.0
        }
    
    for niveau, seuil in sorted(seuils.items(), key=lambda x: x[1], reverse=True):
        if score >= seuil:
            return niveau
    
    return "Critique"


def normaliser_scores(scores: List[float], min_val: float = 0, max_val: float = 10) -> List[float]:
    """
    Normalise une liste de scores dans une plage donnée.
    
    Args:
        scores: Liste de scores à normaliser
        min_val: Valeur minimale de la plage cible
        max_val: Valeur maximale de la plage cible
    
    Returns:
        Liste de scores normalisés
    """
    if not scores:
        return []
    
    score_min = min(scores)
    score_max = max(scores)
    
    if score_max == score_min:
        return [min_val + (max_val - min_val) / 2] * len(scores)
    
    return [
        min_val + (s - score_min) * (max_val - min_val) / (score_max - score_min)
        for s in scores
    ]


def calculer_statistiques(scores: List[float]) -> Dict[str, float]:
    """
    Calcule des statistiques descriptives sur une liste de scores.
    
    Args:
        scores: Liste de scores numériques
    
    Returns:
        Dictionnaire avec moyenne, médiane, écart-type, min, max
    """
    if not scores:
        return {
            "moyenne": 0.0,
            "mediane": 0.0,
            "ecart_type": 0.0,
            "minimum": 0.0,
            "maximum": 0.0
        }
    
    return {
        "moyenne": round(statistics.mean(scores), 2),
        "mediane": round(statistics.median(scores), 2),
        "ecart_type": round(statistics.stdev(scores), 2) if len(scores) > 1 else 0.0,
        "minimum": round(min(scores), 2),
        "maximum": round(max(scores), 2)
    }


def calculer_score_rice(reach: int, impact: float, confidence: float, effort: float) -> float:
    """
    Calcule le score RICE (Reach × Impact × Confidence / Effort).
    
    Args:
        reach: Portée (nombre de personnes impactées)
        impact: Impact (1-3: minimal à massif)
        confidence: Confiance (0-100%)
        effort: Effort (en jours/personnes)
    
    Returns:
        Score RICE
    """
    if effort == 0:
        return 0.0
    
    return round((reach * impact * (confidence / 100)) / effort, 2)


def calculer_score_ice(impact: float, confidence: float, ease: float) -> float:
    """
    Calcule le score ICE (Impact × Confidence × Ease).
    
    Args:
        impact: Impact (1-10)
        confidence: Confiance (1-10)
        ease: Facilité (1-10)
    
    Returns:
        Score ICE
    """
    return round(impact * confidence * ease, 2)


if __name__ == "__main__":
    # Exemples d'utilisation
    print("=== Test utils_scoring.py ===\n")
    
    # Test 1: Score composite
    scores = {"qualite": 8, "prix": 6, "innovation": 9}
    poids = {"qualite": 0.5, "prix": 0.2, "innovation": 0.3}
    score_final, _ = calculer_score_composite(scores, poids)
    print(f"Score composite: {score_final}/10 - {evaluer_niveau(score_final)}")
    
    # Test 2: RICE
    rice = calculer_score_rice(reach=1000, impact=2.5, confidence=80, effort=10)
    print(f"\nScore RICE: {rice}")
    
    # Test 3: Statistiques
    scores_list = [7.5, 8.2, 6.8, 9.1, 7.9]
    stats = calculer_statistiques(scores_list)
    print(f"\nStatistiques: Moyenne={stats['moyenne']}, Médiane={stats['mediane']}")
