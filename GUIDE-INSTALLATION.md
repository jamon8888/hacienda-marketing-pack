# Guide d'Installation - Hacienda Marketing Pack

> Bibliothèque complète de 27 skills de stratégie business pour Claude Desktop

## 📋 Table des Matières

1. [Prérequis](#prérequis)
2. [Installation](#installation)
3. [Configuration Claude Desktop](#configuration-claude-desktop)
4. [Structure du Projet](#structure-du-projet)
5. [Utilisation](#utilisation)
6. [Parcours de Skills](#parcours-de-skills)
7. [Dépannage](#dépannage)

---

## 🔧 Prérequis

### Logiciels Requis

- **Claude Desktop** : Version récente installée
- **Python 3.8+** : Pour l'exécution des scripts d'analyse
- **Git** : Pour cloner le repository (optionnel)

### Connaissances Requises

- Aucune connaissance technique requise pour utiliser les skills
- Les scripts Python sont optionnels et documentés

---

## 💾 Installation

### Option 1 : Clone via Git

```bash
git clone https://github.com/jamon8888/hacienda-marketing-pack.git
cd hacienda-marketing-pack
```

### Option 2 : Téléchargement Direct

1. Télécharger le ZIP depuis GitHub
2. Extraire dans un dossier de votre choix
3. Naviguer vers le dossier extrait

### Vérification de l'Installation

```bash
# Vérifier la structure
ls -la

# Vous devriez voir :
# - skills/
# - instructions/
# - shared/
# - README.md
# - GUIDE-INSTALLATION.md
```

---

## ⚙️ Configuration Claude Desktop

### Étape 1 : Ajouter les Skills comme Capacités

1. Ouvrir **Claude Desktop**
2. Aller dans **Paramètres** → **Developer** → **Edit Config**
3. Ajouter le chemin vers les skills :

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/chemin/vers/hacienda-marketing-pack"]
    }
  }
}
```

**Remplacer** `/chemin/vers/hacienda-marketing-pack` par le chemin réel sur votre machine.

### Étape 2 : Configuration des Instructions Projet (Recommandé)

Pour une expérience optimale, créez un fichier d'instructions projet dans Claude Desktop :

1. Dans Claude Desktop, créer un nouveau projet
2. Nommer le projet : **"Hacienda Strategy"**
3. Ajouter les instructions suivantes :

```markdown
Tu as accès à la bibliothèque Hacienda Marketing Pack, une collection de 27 skills
de stratégie business.

## Localisation
Les skills sont dans : /chemin/vers/hacienda-marketing-pack/skills/

## Ton Rôle
Tu es un coach stratégique bienveillant qui guide l'utilisateur à travers les skills
en utilisant une approche socratique.

## Comment Utiliser un Skill
1. L'utilisateur demande un skill spécifique ou une aide stratégique
2. Tu lis le fichier SKILL.md correspondant
3. Tu suis exactement les instructions du skill
4. Tu poses UNE question à la fois
5. Tu sauvegardes les outputs dans .hacienda/

## Règles Importantes
- TOUJOURS lire le SKILL.md avant de commencer
- Suivre la posture socratique définie dans le skill
- Sauvegarder les outputs pour le chaînage
- Proposer le skill suivant logique à la fin

## Structure des Outputs
Tous les outputs vont dans : [projet-utilisateur]/.hacienda/[categorie]/
```

### Étape 3 : Redémarrer Claude Desktop

Redémarrer Claude Desktop pour que les changements prennent effet.

---

## 📁 Structure du Projet

```
hacienda-marketing-pack/
│
├── skills/                          # 27 skills organisés par catégorie
│   ├── strategie-fondation/         # 7 skills fondamentaux
│   ├── strategie-marche-produit/    # 4 skills marché & produit
│   ├── marketing-croissance/        # 7 skills marketing
│   ├── retention-metriques/         # 4 skills rétention
│   └── levee-fonds-operations/      # 5 skills levée de fonds
│
├── instructions/                     # 6 fichiers de chaînage
│   ├── chaineur-strategie-fondation.md
│   ├── chaineur-strategie-marche-produit.md
│   ├── chaineur-marketing-croissance.md
│   ├── chaineur-retention-metriques.md
│   ├── chaineur-levee-fonds-operations.md
│   └── chaineur-parcours-complet.md
│
├── shared/                          # Ressources partagées
│   ├── scripts/                     # Utilitaires Python
│   │   ├── utils_scoring.py
│   │   ├── utils_visualisation.py
│   │   └── utils_contexte.py
│   └── references/                  # Documentation
│       ├── glossaire-strategie.md
│       └── templates-rapports.md
│
├── README.md
└── GUIDE-INSTALLATION.md
```

### Structure d'un Skill

Chaque skill contient :

```
nom-du-skill/
├── SKILL.md              # Instructions complètes du skill
├── references/           # Frameworks et méthodologies
│   ├── framework-1.md
│   └── framework-2.md
└── scripts/              # Scripts Python optionnels
    └── script_analyse.py
```

---

## ⚠️ Important : Utilisation Responsable

### Les Skills sont des Guides, pas des Vérités Absolues

**Chaque skill génère des analyses et recommandations comme point de départ** - pas comme vérité absolue. Les outputs sont des drafts intelligents qui nécessitent votre validation.

📝 **Utilise ton esprit critique** :
- Les analyses sont des points de départ pour la réflexion
- Valide toujours avec des données réelles et du feedback terrain
- Adapte les frameworks à ton contexte spécifique
- Questionne ce qui ne résonne pas avec ton expérience

🧠 **Ton jugement est irremplaçable** :
- Tu connais ton marché, tes clients, ton équipe
- Les nuances de ton projet nécessitent ton expertise humaine
- Les skills sont des co-pilotes, pas des pilotes automatiques

💡 **Bonnes Pratiques** :
- Partage les outputs avec ton équipe et des mentors
- Teste les recommandations avec de vrais clients
- Itère en fonction des retours terrain
- Reviens sur les skills tous les 3-6 mois pour mettre à jour

---

## 🚀 Utilisation

### Démarrage Rapide

1. **Ouvrir Claude Desktop**
2. **Créer un nouveau chat** dans votre projet "Hacienda Strategy"
3. **Demander un skill** :

```
Je veux valider mon idée business avec Hacienda
```

ou

```
Lance le skill validateur-idee-business
```

### Flux de Travail Typique

```
┌─────────────────────────────────────┐
│ 1. Demander un skill                │
│    "Je veux analyser mon marché"    │
└─────────────────────────────────────┘
                │
                ▼
┌─────────────────────────────────────┐
│ 2. Claude lit le SKILL.md           │
│    et lance le questionnement       │
└─────────────────────────────────────┘
                │
                ▼
┌─────────────────────────────────────┐
│ 3. Dialogue socratique               │
│    Questions → Réponses → Exploration│
└─────────────────────────────────────┘
                │
                ▼
┌─────────────────────────────────────┐
│ 4. Génération du rapport            │
│    Sauvegarde dans .hacienda/       │
└─────────────────────────────────────┘
                │
                ▼
┌─────────────────────────────────────┐
│ 5. Proposition du skill suivant     │
└─────────────────────────────────────┘
```

### Sauvegarde des Outputs

Tous les outputs sont sauvegardés dans votre projet :

```
votre-projet/
└── .hacienda/
    ├── strategie-fondation/
    │   ├── validateur-idee-business-latest.json
    │   └── analyseur-opportunite-marche-latest.json
    ├── strategie-marche-produit/
    └── ...
```

Ces fichiers permettent le **chaînage** : chaque skill peut utiliser les résultats des skills précédents.

---

## 🗺️ Parcours de Skills

### Parcours Complet (27 Skills)

Pour un accompagnement complet de l'idée au lancement :

```
Utilise le chaineur-parcours-complet
```

### Parcours par Catégorie

#### 1️⃣ Stratégie Fondation (Semaines 1-4)

```
Utilise le chaineur-strategie-fondation
```

**Skills** : Validation d'idée → Analyse marché → Modèle business → Personas → Proposition de valeur → Positionnement → Veille concurrentielle

#### 2️⃣ Stratégie Marché & Produit (Semaines 5-6)

```
Utilise le chaineur-strategie-marche-produit
```

**Skills** : Priorisation fonctionnalités → Go-to-Market → Pricing → Roadmap

#### 3️⃣ Marketing & Croissance (Semaines 7-10)

```
Utilise le chaineur-marketing-croissance
```

**Skills** : Identité marque → Content marketing → Growth hacking → Social media → Email marketing → SEO → Communauté

#### 4️⃣ Rétention & Métriques (Semaines 11-12)

```
Utilise le chaineur-retention-metriques
```

**Skills** : Dashboard métriques → Optimisation rétention → Onboarding → Feedback client

#### 5️⃣ Levée de Fonds & Opérations (Semaines 13-16)

```
Utilise le chaineur-levee-fonds-operations
```

**Skills** : Modèle financier → Stratégie fundraising → Brief investisseur → Pitch deck → Playbook opérationnel

### Utilisation Ponctuelle

Vous pouvez aussi utiliser n'importe quel skill individuellement :

```
Je veux travailler sur ma stratégie de pricing
→ Lance architecte-strategie-prix

Je dois créer des personas clients
→ Lance constructeur-persona-client

J'ai besoin d'optimiser mon onboarding
→ Lance optimiseur-parcours-onboarding
```

---

## 🔬 Scripts Python (Optionnel)

Les scripts Python dans chaque skill sont **optionnels** mais peuvent être utiles pour :
- Calculs automatisés (RICE, ICE, TAM/SAM/SOM)
- Génération de visualisations
- Analyse de données

### Installation des Dépendances Python

Si vous souhaitez utiliser les scripts :

```bash
# Aucune dépendance externe requise !
# Les scripts utilisent uniquement la bibliothèque standard Python

# Tester un script
cd shared/scripts
python3 utils_scoring.py
```

### Exemple d'Utilisation

```python
from shared.scripts.utils_scoring import calculer_score_rice

score = calculer_score_rice(
    reach=1000,      # 1000 utilisateurs impactés
    impact=2.5,      # Impact élevé
    confidence=80,   # 80% de confiance
    effort=10        # 10 jours d'effort
)

print(f"Score RICE : {score}")
# Output: Score RICE : 200.0
```

---

## 🧪 Exemples de Commandes

### Démarrer un Nouveau Projet

```
Je lance un nouveau projet et je veux l'accompagnement complet Hacienda
```

Claude va :
1. Vous demander où sauvegarder les outputs
2. Créer le dossier `.hacienda/`
3. Lancer le premier skill : validateur-idee-business

### Reprendre une Session

```
Je veux reprendre mon analyse là où je l'avais laissée
```

Claude va :
1. Chercher les outputs existants dans `.hacienda/`
2. Afficher un résumé de ce qui a été fait
3. Proposer le prochain skill logique

### Accéder à un Skill Spécifique

```
Lance le skill expert-positionnement-produit
```

ou

```
J'ai besoin d'aide pour positionner mon produit
```

### Voir les Frameworks

```
Montre-moi le framework RICE pour la priorisation
```

Claude lira : `skills/strategie-marche-produit/framework-priorisation-fonctionnalites/references/framework-rice.md`

---

## 🆘 Dépannage

### Claude ne trouve pas les skills

**Solution** : Vérifier le chemin dans la config MCP :

1. Ouvrir la config : Settings → Developer → Edit Config
2. Vérifier que le chemin est absolu et correct
3. Redémarrer Claude Desktop

### Les outputs ne se sauvegardent pas

**Solution** : 

1. Vérifier que Claude a accès au système de fichiers
2. S'assurer que le dossier du projet existe
3. Donner les permissions nécessaires si sur macOS/Linux :

```bash
chmod -R 755 /chemin/vers/votre-projet
```

### Un skill ne suit pas l'approche socratique

**Solution** :

1. Vérifier que Claude lit bien le SKILL.md
2. Rappeler à Claude : "Suis l'approche socratique du skill"
3. Reformuler : "Pose-moi UNE question à la fois"

### Les scripts Python ne fonctionnent pas

**Solution** :

```bash
# Vérifier la version de Python
python3 --version
# Doit être 3.8 ou supérieur

# Les scripts n'ont pas de dépendances externes
# Si erreur, vérifier le chemin d'import
```

### Claude oublie le contexte entre sessions

**Solution** :

1. Utiliser les **Instructions Projet** (voir Configuration)
2. Au début de chaque session : "Utilise le contexte Hacienda"
3. Les outputs dans `.hacienda/` permettent de récupérer le contexte

---

## 📚 Ressources Supplémentaires

### Documentation

- **Glossaire** : `shared/references/glossaire-strategie.md`
- **Templates** : `shared/references/templates-rapports.md`
- **Frameworks** : Dans chaque `skills/*/references/`

### Support

- **Issues GitHub** : [github.com/jamon8888/hacienda-marketing-pack/issues](https://github.com/jamon8888/hacienda-marketing-pack/issues)
- **Discussions** : [github.com/jamon8888/hacienda-marketing-pack/discussions](https://github.com/jamon8888/hacienda-marketing-pack/discussions)

---

## 🎯 Prochaines Étapes

1. ✅ Installation terminée
2. ⏭️ Lancer votre premier skill :
   ```
   Je veux valider mon idée business
   ```
3. 📈 Suivre le parcours complet ou choisir des skills ponctuels
4. 🚀 Construire votre stratégie avec Hacienda !

---

## 📄 Licence

MIT License - © Hacienda

---

*Hacienda Marketing Pack v1.0.0 | Guide d'Installation*

**Prêt à démarrer ?** Ouvrez Claude Desktop et lancez votre premier skill ! 🎉
