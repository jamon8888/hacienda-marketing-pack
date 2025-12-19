#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur de skills pour Hacienda Marketing Pack
Crée automatiquement la structure complète des skills restants
"""

import os
import json

# Définition de tous les skills à créer
SKILLS_CONFIG = {
    "strategie-fondation": [
        {
            "nom": "analyseur-opportunite-marche",
            "titre": "Analyseur d'Opportunité Marché",
            "description": "Analyse socratique du marché avec TAM/SAM/SOM et forces de Porter",
            "temps": "45-60 minutes",
            "frameworks": ["framework-tam-sam-som.md", "framework-porter-5-forces.md", "framework-pestel.md"],
            "script": "calcul_tam_sam_som.py",
            "prerequis": "validateur-idee-business",
            "sortie": "concepteur-modele-business"
        },
        {
            "nom": "concepteur-modele-business",
            "titre": "Concepteur de Modèle Business",
            "description": "Co-construction socratique du Business Model Canvas et Lean Canvas",
            "temps": "60-75 minutes",
            "frameworks": ["framework-business-model-canvas.md", "framework-lean-canvas.md"],
            "script": "analyse_flux_revenus.py",
            "prerequis": "analyseur-opportunite-marche",
            "sortie": "constructeur-persona-client"
        },
        {
            "nom": "constructeur-persona-client",
            "titre": "Constructeur de Persona Client",
            "description": "Création socratique de personas avec Jobs-to-be-Done et Empathy Map",
            "temps": "50-65 minutes",
            "frameworks": ["framework-jobs-to-be-done.md", "framework-empathy-map.md"],
            "script": "generateur_persona.py",
            "prerequis": "concepteur-modele-business",
            "sortie": "artisan-proposition-valeur"
        },
        {
            "nom": "artisan-proposition-valeur",
            "titre": "Artisan de Proposition de Valeur",
            "description": "Élaboration socratique de la proposition de valeur avec Value Proposition Canvas",
            "temps": "40-55 minutes",
            "frameworks": ["framework-value-proposition-canvas.md"],
            "script": "scoring_proposition_valeur.py",
            "prerequis": "constructeur-persona-client",
            "sortie": "expert-positionnement-produit"
        },
        {
            "nom": "expert-positionnement-produit",
            "titre": "Expert en Positionnement Produit",
            "description": "Positionnement stratégique socratique selon April Dunford",
            "temps": "45-60 minutes",
            "frameworks": ["framework-april-dunford.md"],
            "script": "matrice_positionnement.py",
            "prerequis": "artisan-proposition-valeur",
            "sortie": "veille-concurrentielle"
        },
        {
            "nom": "veille-concurrentielle",
            "titre": "Veille Concurrentielle",
            "description": "Analyse socratique de la concurrence avec SWOT et Porter",
            "temps": "50-65 minutes",
            "frameworks": ["framework-swot.md", "framework-porter-5-forces.md"],
            "script": "analyse_concurrentielle.py",
            "prerequis": "expert-positionnement-produit",
            "sortie": "framework-priorisation-fonctionnalites"
        }
    ],
    "strategie-marche-produit": [
        {
            "nom": "framework-priorisation-fonctionnalites",
            "titre": "Framework de Priorisation de Fonctionnalités",
            "description": "Priorisation socratique avec RICE et ICE",
            "temps": "40-55 minutes",
            "frameworks": ["framework-rice.md", "framework-ice.md"],
            "script": "calcul_rice_ice.py",
            "prerequis": "veille-concurrentielle",
            "sortie": "planificateur-go-to-market"
        },
        {
            "nom": "planificateur-go-to-market",
            "titre": "Planificateur Go-to-Market",
            "description": "Stratégie socratique de lancement avec GTM Canvas",
            "temps": "60-75 minutes",
            "frameworks": ["framework-gtm-canvas.md"],
            "script": "planification_gtm.py",
            "prerequis": "framework-priorisation-fonctionnalites",
            "sortie": "architecte-strategie-prix"
        },
        {
            "nom": "architecte-strategie-prix",
            "titre": "Architecte de Stratégie de Prix",
            "description": "Détermination socratique du pricing avec Van Westendorp",
            "temps": "45-60 minutes",
            "frameworks": ["framework-van-westendorp.md", "framework-pricing-strategies.md"],
            "script": "analyse_prix.py",
            "prerequis": "planificateur-go-to-market",
            "sortie": "constructeur-roadmap-strategique"
        },
        {
            "nom": "constructeur-roadmap-strategique",
            "titre": "Constructeur de Roadmap Stratégique",
            "description": "Construction socratique de roadmap avec OKRs",
            "temps": "50-65 minutes",
            "frameworks": ["framework-okr.md"],
            "script": "generateur_roadmap.py",
            "prerequis": "architecte-strategie-prix",
            "sortie": "concepteur-identite-marque"
        }
    ],
    "marketing-croissance": [
        {
            "nom": "concepteur-identite-marque",
            "titre": "Concepteur d'Identité de Marque",
            "description": "Création socratique de l'identité de marque avec archétypes",
            "temps": "60-75 minutes",
            "frameworks": ["framework-pyramide-marque.md", "framework-archetypal-branding.md", "guide-psychologie-couleurs.md"],
            "script": "scoring_coherence_marque.py",
            "prerequis": "constructeur-roadmap-strategique",
            "sortie": "strategiste-marketing-contenu"
        },
        {
            "nom": "strategiste-marketing-contenu",
            "titre": "Stratégiste Marketing de Contenu",
            "description": "Stratégie socratique de contenu avec piliers thématiques",
            "temps": "50-65 minutes",
            "frameworks": ["framework-content-pillars.md"],
            "script": "calendrier_editorial.py",
            "prerequis": "concepteur-identite-marque",
            "sortie": "guide-growth-hacking"
        },
        {
            "nom": "guide-growth-hacking",
            "titre": "Guide Growth Hacking",
            "description": "Identification socratique des canaux de croissance avec Bullseye",
            "temps": "55-70 minutes",
            "frameworks": ["framework-traction-bullseye.md"],
            "script": "evaluation_canaux.py",
            "prerequis": "strategiste-marketing-contenu",
            "sortie": "strategiste-reseaux-sociaux"
        },
        {
            "nom": "strategiste-reseaux-sociaux",
            "titre": "Stratégiste Réseaux Sociaux",
            "description": "Stratégie socratique social media avec matrice de plateformes",
            "temps": "45-60 minutes",
            "frameworks": ["framework-social-media-matrix.md"],
            "script": "calendrier_social.py",
            "prerequis": "guide-growth-hacking",
            "sortie": "architecte-email-marketing"
        },
        {
            "nom": "architecte-email-marketing",
            "titre": "Architecte Email Marketing",
            "description": "Conception socratique de séquences email",
            "temps": "40-55 minutes",
            "frameworks": ["framework-email-sequences.md"],
            "script": "generateur_sequences.py",
            "prerequis": "strategiste-reseaux-sociaux",
            "sortie": "planificateur-seo-contenu"
        },
        {
            "nom": "planificateur-seo-contenu",
            "titre": "Planificateur SEO et Contenu",
            "description": "Stratégie socratique SEO avec clusters de mots-clés",
            "temps": "50-65 minutes",
            "frameworks": ["framework-keyword-clusters.md"],
            "script": "analyse_seo.py",
            "prerequis": "architecte-email-marketing",
            "sortie": "strategiste-communaute"
        },
        {
            "nom": "strategiste-communaute",
            "titre": "Stratégiste Communauté",
            "description": "Stratégie socratique de community building",
            "temps": "45-60 minutes",
            "frameworks": ["framework-community-engagement.md"],
            "script": "metriques_communaute.py",
            "prerequis": "planificateur-seo-contenu",
            "sortie": "concepteur-tableau-bord-metriques"
        }
    ],
    "retention-metriques": [
        {
            "nom": "concepteur-tableau-bord-metriques",
            "titre": "Concepteur de Tableau de Bord Métriques",
            "description": "Définition socratique des métriques AARRR et North Star",
            "temps": "50-65 minutes",
            "frameworks": ["framework-aarrr.md", "framework-north-star-metric.md"],
            "script": "calcul_metriques.py",
            "prerequis": "strategiste-communaute",
            "sortie": "expert-optimisation-retention"
        },
        {
            "nom": "expert-optimisation-retention",
            "titre": "Expert en Optimisation de Rétention",
            "description": "Analyse socratique de la rétention avec cohortes",
            "temps": "45-60 minutes",
            "frameworks": ["framework-cohort-analysis.md"],
            "script": "analyse_cohortes.py",
            "prerequis": "concepteur-tableau-bord-metriques",
            "sortie": "optimiseur-parcours-onboarding"
        },
        {
            "nom": "optimiseur-parcours-onboarding",
            "titre": "Optimiseur de Parcours Onboarding",
            "description": "Optimisation socratique de l'activation utilisateur",
            "temps": "40-55 minutes",
            "frameworks": ["framework-activation-funnel.md"],
            "script": "analyse_onboarding.py",
            "prerequis": "expert-optimisation-retention",
            "sortie": "framework-feedback-client"
        },
        {
            "nom": "framework-feedback-client",
            "titre": "Framework Feedback Client",
            "description": "Collecte socratique de feedback avec NPS, CSAT, CES",
            "temps": "40-55 minutes",
            "frameworks": ["framework-nps-csat-ces.md"],
            "script": "analyse_feedback.py",
            "prerequis": "optimiseur-parcours-onboarding",
            "sortie": "architecte-modele-financier"
        }
    ],
    "levee-fonds-operations": [
        {
            "nom": "architecte-modele-financier",
            "titre": "Architecte de Modèle Financier",
            "description": "Construction socratique des projections financières",
            "temps": "60-90 minutes",
            "frameworks": ["framework-projections-financieres.md"],
            "script": "modele_financier.py",
            "prerequis": "framework-feedback-client",
            "sortie": "planificateur-strategie-levee-fonds"
        },
        {
            "nom": "planificateur-strategie-levee-fonds",
            "titre": "Planificateur Stratégie Levée de Fonds",
            "description": "Stratégie socratique de fundraising par étapes",
            "temps": "55-70 minutes",
            "frameworks": ["framework-fundraising-stages.md"],
            "script": "planification_levee.py",
            "prerequis": "architecte-modele-financier",
            "sortie": "redacteur-brief-investisseur"
        },
        {
            "nom": "redacteur-brief-investisseur",
            "titre": "Rédacteur de Brief Investisseur",
            "description": "Rédaction socratique du one-pager investisseur",
            "temps": "40-55 minutes",
            "frameworks": ["framework-one-pager.md"],
            "script": "generateur_brief.py",
            "prerequis": "planificateur-strategie-levee-fonds",
            "sortie": "constructeur-pitch-deck-investisseur"
        },
        {
            "nom": "constructeur-pitch-deck-investisseur",
            "titre": "Constructeur de Pitch Deck Investisseur",
            "description": "Construction socratique du pitch deck",
            "temps": "75-90 minutes",
            "frameworks": ["framework-pitch-deck-structure.md"],
            "script": "generateur_pitch.py",
            "prerequis": "redacteur-brief-investisseur",
            "sortie": "createur-playbook-operationnel"
        },
        {
            "nom": "createur-playbook-operationnel",
            "titre": "Créateur de Playbook Opérationnel",
            "description": "Création socratique du playbook des opérations",
            "temps": "60-75 minutes",
            "frameworks": ["framework-operations-playbook.md"],
            "script": "generateur_playbook.py",
            "prerequis": "constructeur-pitch-deck-investisseur",
            "sortie": "null"
        }
    ]
}

def creer_skill_complet(categorie, skill_info, base_path):
    """Crée un skill complet avec tous ses fichiers."""
    
    nom = skill_info["nom"]
    skill_path = os.path.join(base_path, "skills", categorie, nom)
    
    # Créer les répertoires
    os.makedirs(os.path.join(skill_path, "references"), exist_ok=True)
    os.makedirs(os.path.join(skill_path, "scripts"), exist_ok=True)
    
    # Créer SKILL.md (version optimisée <600 lignes)
    skill_md = generer_skill_md(skill_info, categorie)
    with open(os.path.join(skill_path, "SKILL.md"), 'w', encoding='utf-8') as f:
        f.write(skill_md)
    
    # Créer les fichiers de framework
    for framework in skill_info["frameworks"]:
        framework_content = generer_framework(framework, skill_info)
        framework_path = os.path.join(skill_path, "references", framework)
        with open(framework_path, 'w', encoding='utf-8') as f:
            f.write(framework_content)
    
    # Créer le script Python
    script_content = generer_script(skill_info)
    script_path = os.path.join(skill_path, "scripts", skill_info["script"])
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    print(f"✓ Créé: {categorie}/{nom}")

def generer_skill_md(skill_info, categorie):
    """Génère le contenu du SKILL.md avec approche socratique."""
    
    return f"""---
nom: {skill_info['nom']}
description: {skill_info['description']}
auteur: Hacienda
version: 1.0.0
categorie: {categorie}
tags: []
tempsEstime: {skill_info['temps']}
prerequis: {skill_info['prerequis'] or 'null'}
sortieVers: {skill_info['sortie'] or 'null'}
references:
  {chr(10).join(f'- references/{fw}' for fw in skill_info['frameworks'])}
scripts:
  - scripts/{skill_info['script']}
---

# {skill_info['titre']}

Tu es un coach stratégique bienveillant et expérimenté. Tu guides l'utilisateur par le questionnement socratique pour {skill_info['description'].lower()}.

## Posture

- **Curieux et authentiquement intéressé**
- **Jamais de jugement**, toujours encourageant
- **Questions ouvertes** qui font réfléchir en profondeur
- **Reformulation** pour valider ta compréhension
- **Encouragement** et valorisation des réflexions
- **UNE question à la fois** - attends toujours la réponse

## Framework Utilisé

> **Référence** : Consulter les frameworks dans `references/` pour le détail complet.

[Voir les fichiers de référence pour les frameworks détaillés]

## Flux de Travail

### Étape 0 : Accueil

```
═══════════════════════════════════════════════════════════════
   HACIENDA : {skill_info['titre'].upper()}
═══════════════════════════════════════════════════════════════
⏱️ Temps: {skill_info['temps']} | 📁 {categorie}
═══════════════════════════════════════════════════════════════
```

"Bonjour ! Je suis ravi de t'accompagner pour {skill_info['description'].lower()}. 🎯

Nous allons explorer ce sujet ensemble à travers un dialogue constructif.

**Pour commencer, dis-moi : [question d'ouverture adaptée au contexte]**"

### Étape 1 : Configuration Projet

Demander le répertoire de sauvegarde et initialiser avec `utils_contexte.py`.

### Étape 2 : Détection Contexte

Chercher les outputs précédents dans `.hacienda/{categorie}/`.

Si trouvés, proposer de reprendre ou recommencer.

### Étape 3 : Exploration Socratique

**Phase 1 : Compréhension**
- Poser des questions ouvertes pour comprendre le contexte
- Reformuler pour valider
- Approfondir avec curiosité authentique

**Phase 2 : Analyse**
- Explorer les différentes dimensions du sujet
- Faire réfléchir avec des questions stimulantes
- Identifier les patterns et insights

**Phase 3 : Co-construction**
- Synthétiser ensemble ce qui a été découvert
- Valider les conclusions avec l'utilisateur
- Créer un plan d'action concret

### Étape Finale : Livrable

Générer le rapport complet en Markdown dans `.hacienda/{categorie}/`.

Utiliser le template approprié de `shared/references/templates-rapports.md`.

Proposer le skill suivant : **{skill_info['sortie'] or 'Parcours terminé'}**

## Contrôles Qualité

- [ ] Approche socratique respectée (questions ouvertes)
- [ ] Reformulations et validations effectuées
- [ ] UNE question à la fois
- [ ] Rapport sauvegardé dans .hacienda/
- [ ] Skill suivant proposé

## Données de Chaînage

```yaml
signature_contexte: {skill_info['nom']}-v1.0.0
donnees_transmises:
  # [Données spécifiques à transmettre au skill suivant]
sortie_vers: {skill_info['sortie'] or 'null'}
```

---

*Hacienda Marketing Pack | {skill_info['nom']}-v1.0.0*
"""

def generer_framework(nom_fichier, skill_info):
    """Génère le contenu d'un fichier framework."""
    
    framework_name = nom_fichier.replace('.md', '').replace('framework-', '').replace('-', ' ').title()
    
    return f"""# {framework_name}

## Vue d'Ensemble

Ce framework fait partie du skill **{skill_info['titre']}** et fournit une méthodologie structurée pour {skill_info['description'].lower()}.

## Principes Fondamentaux

### Principe 1 : [À définir selon le contexte]
Description du premier principe clé du framework.

### Principe 2 : [À définir selon le contexte]
Description du deuxième principe.

### Principe 3 : [À définir selon le contexte]
Description du troisième principe.

## Méthodologie

### Étape 1
[Description détaillée de la première étape]

### Étape 2
[Description détaillée de la deuxième étape]

### Étape 3
[Description détaillée de la troisième étape]

## Outils et Templates

[Templates ou outils associés à ce framework]

## Exemples d'Application

### Exemple 1
[Cas d'usage concret]

### Exemple 2
[Autre cas d'usage]

## Pièges à Éviter

- ❌ Piège 1 : [Description]
- ❌ Piège 2 : [Description]
- ❌ Piège 3 : [Description]

## Ressources Complémentaires

- Voir aussi : `shared/references/glossaire-strategie.md`
- Templates : `shared/references/templates-rapports.md`

---

*Framework {framework_name} - Hacienda Marketing Pack v1.0.0*
"""

def generer_script(skill_info):
    """Génère le contenu du script Python."""
    
    titre = skill_info['titre']
    
    return f"""#!/usr/bin/env python3
# -*- coding: utf-8 -*-
\"\"\"
Script pour {titre}
Hacienda Marketing Pack
\"\"\"

import sys
import os

# Ajouter le chemin vers les utilitaires partagés
script_dir = os.path.dirname(os.path.abspath(__file__))
shared_scripts = os.path.abspath(os.path.join(script_dir, '../../../../shared/scripts'))
sys.path.insert(0, shared_scripts)

from utils_scoring import calculer_score_composite, evaluer_niveau
from utils_visualisation import creer_barre_progression, creer_graphique_barres, creer_boite_info


def executer_analyse(donnees):
    \"\"\"
    Exécute l'analyse principale pour ce skill.
    
    Args:
        donnees: Dictionnaire avec les données d'entrée
    
    Returns:
        Dictionnaire avec les résultats
    \"\"\"
    # TODO: Implémenter la logique spécifique
    return {{
        'resultat': 'Analyse complétée',
        'donnees': donnees
    }}


def afficher_resultat(resultat_data):
    \"\"\"
    Affiche les résultats de manière visuelle.
    \"\"\"
    print("\\n" + "═" * 70)
    print(f"   RÉSULTAT : {{resultat_data.get('titre', 'ANALYSE')}}")
    print("═" * 70)
    
    # Affichage des résultats
    for cle, valeur in resultat_data.items():
        if cle != 'titre':
            print(f"• {{cle}}: {{valeur}}")
    
    print("═" * 70 + "\\n")


def exemple_utilisation():
    \"\"\"
    Exemple d'utilisation du script.
    \"\"\"
    print("=== EXEMPLE : {titre} ===\\n")
    
    # Données exemple
    donnees = {{
        'param1': 'valeur1',
        'param2': 'valeur2'
    }}
    
    # Exécution
    resultat = executer_analyse(donnees)
    
    # Affichage
    afficher_resultat(resultat)


if __name__ == "__main__":
    exemple_utilisation()
"""

def main():
    """Fonction principale."""
    base_path = "/home/runner/work/hacienda-marketing-pack/hacienda-marketing-pack"
    
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║     GÉNÉRATION DES SKILLS - HACIENDA MARKETING PACK          ║")
    print("╚═══════════════════════════════════════════════════════════════╝")
    print()
    
    total_skills = sum(len(skills) for skills in SKILLS_CONFIG.values())
    created = 0
    
    for categorie, skills in SKILLS_CONFIG.items():
        print(f"\\n📁 Catégorie: {categorie}")
        print("─" * 70)
        
        for skill in skills:
            creer_skill_complet(categorie, skill, base_path)
            created += 1
    
    print()
    print("═" * 70)
    print(f"✅ {created} skills créés avec succès!")
    print("═" * 70)

if __name__ == "__main__":
    main()
