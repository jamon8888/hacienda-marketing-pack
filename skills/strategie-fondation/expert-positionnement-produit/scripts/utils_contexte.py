#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Utilitaires de gestion de contexte pour Hacienda Marketing Pack
Lecture/écriture des outputs de skills pour le chaînage
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Any
from pathlib import Path


class GestionnaireContexte:
    """Gestionnaire de contexte pour le chaînage de skills."""
    
    def __init__(self, repertoire_base: str = ".hacienda"):
        """
        Initialise le gestionnaire de contexte.
        
        Args:
            repertoire_base: Nom du répertoire pour stocker les outputs
        """
        self.repertoire_base = repertoire_base
        self.chemin_complet = None
    
    def initialiser(self, chemin_projet: str) -> str:
        """
        Initialise le répertoire de contexte dans le projet.
        
        Args:
            chemin_projet: Chemin du projet utilisateur
        
        Returns:
            Chemin complet du répertoire .hacienda
        """
        self.chemin_complet = os.path.join(chemin_projet, self.repertoire_base)
        os.makedirs(self.chemin_complet, exist_ok=True)
        
        # Créer sous-dossiers par catégorie
        for categorie in [
            "strategie-fondation",
            "strategie-marche-produit",
            "marketing-croissance",
            "retention-metriques",
            "levee-fonds-operations"
        ]:
            os.makedirs(os.path.join(self.chemin_complet, categorie), exist_ok=True)
        
        return self.chemin_complet
    
    def sauvegarder_output(
        self,
        skill_name: str,
        categorie: str,
        donnees: Dict[str, Any],
        version: str = "1.0.0"
    ) -> str:
        """
        Sauvegarde l'output d'un skill.
        
        Args:
            skill_name: Nom du skill
            categorie: Catégorie du skill
            donnees: Données à sauvegarder
            version: Version du skill
        
        Returns:
            Chemin du fichier sauvegardé
        """
        if not self.chemin_complet:
            raise ValueError("Le contexte n'a pas été initialisé. Appelez initialiser() d'abord.")
        
        # Ajouter métadonnées
        output = {
            "signature_contexte": f"{skill_name}-v{version}",
            "timestamp": datetime.now().isoformat(),
            "categorie": categorie,
            "skill": skill_name,
            "version": version,
            "donnees": donnees
        }
        
        # Chemin du fichier
        chemin_categorie = os.path.join(self.chemin_complet, categorie)
        nom_fichier = f"{skill_name}-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
        chemin_fichier = os.path.join(chemin_categorie, nom_fichier)
        
        # Sauvegarder
        with open(chemin_fichier, 'w', encoding='utf-8') as f:
            json.dump(output, f, ensure_ascii=False, indent=2)
        
        # Créer/mettre à jour le lien "latest"
        chemin_latest = os.path.join(chemin_categorie, f"{skill_name}-latest.json")
        with open(chemin_latest, 'w', encoding='utf-8') as f:
            json.dump(output, f, ensure_ascii=False, indent=2)
        
        return chemin_fichier
    
    def charger_output(
        self,
        skill_name: str,
        categorie: Optional[str] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Charge le dernier output d'un skill.
        
        Args:
            skill_name: Nom du skill
            categorie: Catégorie du skill (optionnel, cherchera partout si non fourni)
        
        Returns:
            Données du skill ou None si non trouvé
        """
        if not self.chemin_complet:
            raise ValueError("Le contexte n'a pas été initialisé.")
        
        # Si catégorie fournie, chercher directement
        if categorie:
            chemin_latest = os.path.join(
                self.chemin_complet,
                categorie,
                f"{skill_name}-latest.json"
            )
            if os.path.exists(chemin_latest):
                with open(chemin_latest, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return None
        
        # Sinon, chercher dans toutes les catégories
        for cat in os.listdir(self.chemin_complet):
            chemin_cat = os.path.join(self.chemin_complet, cat)
            if not os.path.isdir(chemin_cat):
                continue
            
            chemin_latest = os.path.join(chemin_cat, f"{skill_name}-latest.json")
            if os.path.exists(chemin_latest):
                with open(chemin_latest, 'r', encoding='utf-8') as f:
                    return json.load(f)
        
        return None
    
    def lister_outputs(self, categorie: Optional[str] = None) -> List[Dict[str, str]]:
        """
        Liste tous les outputs disponibles.
        
        Args:
            categorie: Catégorie à filtrer (optionnel)
        
        Returns:
            Liste de dictionnaires avec info sur chaque output
        """
        if not self.chemin_complet:
            return []
        
        outputs = []
        
        # Déterminer les catégories à parcourir
        if categorie:
            categories = [categorie]
        else:
            categories = [
                d for d in os.listdir(self.chemin_complet)
                if os.path.isdir(os.path.join(self.chemin_complet, d))
            ]
        
        for cat in categories:
            chemin_cat = os.path.join(self.chemin_complet, cat)
            
            for fichier in os.listdir(chemin_cat):
                if fichier.endswith("-latest.json"):
                    skill_name = fichier.replace("-latest.json", "")
                    chemin_fichier = os.path.join(chemin_cat, fichier)
                    
                    try:
                        with open(chemin_fichier, 'r', encoding='utf-8') as f:
                            data = json.load(f)
                            outputs.append({
                                "skill": skill_name,
                                "categorie": cat,
                                "timestamp": data.get("timestamp", ""),
                                "version": data.get("version", ""),
                                "chemin": chemin_fichier
                            })
                    except Exception:
                        continue
        
        return sorted(outputs, key=lambda x: x["timestamp"], reverse=True)
    
    def verifier_prerequis(self, skills_requis: List[str]) -> Dict[str, bool]:
        """
        Vérifie si les prérequis (skills précédents) sont disponibles.
        
        Args:
            skills_requis: Liste des noms de skills requis
        
        Returns:
            Dictionnaire {skill: disponible}
        """
        resultats = {}
        for skill in skills_requis:
            resultats[skill] = self.charger_output(skill) is not None
        return resultats
    
    def creer_resume_session(self) -> str:
        """
        Crée un résumé de tous les outputs de la session.
        
        Returns:
            Texte formaté du résumé
        """
        outputs = self.lister_outputs()
        
        if not outputs:
            return "Aucun output disponible."
        
        lignes = [
            "╔═══════════════════════════════════════════════════════════════╗",
            "║           RÉSUMÉ DE LA SESSION HACIENDA                      ║",
            "╚═══════════════════════════════════════════════════════════════╝",
            ""
        ]
        
        # Grouper par catégorie
        par_categorie = {}
        for output in outputs:
            cat = output["categorie"]
            if cat not in par_categorie:
                par_categorie[cat] = []
            par_categorie[cat].append(output)
        
        for cat, items in sorted(par_categorie.items()):
            lignes.append(f"\n📁 {cat.upper().replace('-', ' ')}")
            lignes.append("─" * 65)
            for item in items:
                timestamp = item["timestamp"].split("T")[0] if "T" in item["timestamp"] else item["timestamp"]
                lignes.append(f"  ✓ {item['skill']} (v{item['version']}) - {timestamp}")
        
        lignes.append("\n" + "═" * 65)
        lignes.append(f"Total: {len(outputs)} skill(s) complété(s)")
        
        return "\n".join(lignes)


def formater_donnees_pour_affichage(donnees: Dict[str, Any], indent: int = 0) -> str:
    """
    Formate les données d'un output pour affichage lisible.
    
    Args:
        donnees: Dictionnaire de données
        indent: Niveau d'indentation
    
    Returns:
        Texte formaté
    """
    lignes = []
    prefix = "  " * indent
    
    for cle, valeur in donnees.items():
        if isinstance(valeur, dict):
            lignes.append(f"{prefix}• {cle}:")
            lignes.append(formater_donnees_pour_affichage(valeur, indent + 1))
        elif isinstance(valeur, list):
            lignes.append(f"{prefix}• {cle}:")
            for item in valeur:
                if isinstance(item, dict):
                    lignes.append(formater_donnees_pour_affichage(item, indent + 1))
                else:
                    lignes.append(f"{prefix}  - {item}")
        else:
            lignes.append(f"{prefix}• {cle}: {valeur}")
    
    return "\n".join(lignes)


if __name__ == "__main__":
    # Exemple d'utilisation
    print("=== Test utils_contexte.py ===\n")
    
    # Créer un gestionnaire de contexte de test
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdir:
        gc = GestionnaireContexte()
        chemin = gc.initialiser(tmpdir)
        print(f"Contexte initialisé: {chemin}")
        
        # Sauvegarder un output de test
        donnees_test = {
            "idee": "Application de productivité",
            "score_validation": 8.5,
            "marche_cible": "Entrepreneurs"
        }
        
        fichier = gc.sauvegarder_output(
            "validateur-idee-business",
            "strategie-fondation",
            donnees_test
        )
        print(f"\nOutput sauvegardé: {fichier}")
        
        # Charger l'output
        output = gc.charger_output("validateur-idee-business")
        print(f"\nOutput chargé: {output['signature_contexte']}")
        
        # Lister les outputs
        print("\n" + gc.creer_resume_session())
