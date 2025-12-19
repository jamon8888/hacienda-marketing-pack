# Hacienda Marketing Pack

**27 Skills de Stratégie Business pour Claude Desktop**

> Accompagnement socratique intelligent pour entrepreneurs et stratèges

## 🎯 Description

Hacienda Marketing Pack est une bibliothèque complète de skills pour Claude Desktop qui guide les entrepreneurs à travers tout le parcours de création et développement d'entreprise - de la validation d'idée jusqu'à la levée de fonds.

**Approche unique** : Chaque skill utilise une méthode socratique, posant des questions ouvertes qui font réfléchir plutôt que de simplement collecter des données.

## 📦 Contenu

### 27 Skills répartis en 5 catégories :

| Catégorie | Skills | Durée | Description |
|-----------|--------|-------|-------------|
| **Stratégie Fondation** | 7 | 6-8h | Validation, marché, modèle business, personas |
| **Stratégie Marché & Produit** | 4 | 3-4h | Priorisation, GTM, pricing, roadmap |
| **Marketing & Croissance** | 7 | 6-8h | Branding, contenu, growth, social, email, SEO |
| **Rétention & Métriques** | 4 | 3-4h | Dashboard, rétention, onboarding, feedback |
| **Levée de Fonds & Opérations** | 5 | 5-7h | Financier, fundraising, pitch deck |

**Total** : 27 skills | ~25-35 heures | 8-16 semaines

## ✨ Caractéristiques

### Approche Socratique 🧠
- Questions ouvertes qui font réfléchir
- UNE question à la fois
- Reformulation et validation
- Co-construction des réponses
- Pas de jugement, seulement de la curiosité

### Chaînage Intelligent 🔗
- Chaque skill sauvegarde son output dans `.hacienda/`
- Les skills suivants utilisent le contexte précédent
- Progression trackable et reprise automatique
- 6 parcours guidés (chaineurs)

### Frameworks Reconnus 📚
- 40+ frameworks de référence documentés
- Business Model Canvas, Lean Canvas
- TAM/SAM/SOM, Porter, PESTEL, SWOT
- RICE, ICE, OKR, AARRR
- April Dunford, Jobs-to-be-Done, Value Proposition Canvas

### Scripts Python Utilitaires 🐍
- 27 scripts d'analyse (un par skill)
- 3 utilitaires partagés (scoring, visualisation, contexte)
- Calculs automatisés (RICE, TAM/SAM/SOM, scores composites)
- Visualisations ASCII pour le terminal

## 🚀 Démarrage Rapide

### 1. Installation

```bash
git clone https://github.com/jamon8888/hacienda-marketing-pack.git
cd hacienda-marketing-pack
```

### 2. Configuration Claude Desktop

Voir [GUIDE-INSTALLATION.md](GUIDE-INSTALLATION.md) pour la configuration complète.

### 3. Premier Skill

Ouvrez Claude Desktop et tapez :

```
Je veux valider mon idée business avec Hacienda
```

ou

```
Lance le skill validateur-idee-business
```

### 4. Parcours Complet

Pour un accompagnement de A à Z :

```
Je veux faire le parcours complet Hacienda
```

## 📋 Les 27 Skills

### Stratégie Fondation (7 skills)

1. **Validateur Idée Business** - Validation 10 dimensions
2. **Analyseur Opportunité Marché** - TAM/SAM/SOM, Porter, PESTEL
3. **Concepteur Modèle Business** - BMC, Lean Canvas
4. **Constructeur Persona Client** - Jobs-to-be-Done, Empathy Map
5. **Artisan Proposition Valeur** - Value Proposition Canvas
6. **Expert Positionnement Produit** - Framework April Dunford
7. **Veille Concurrentielle** - SWOT, analyse concurrentielle

### Stratégie Marché & Produit (4 skills)

8. **Framework Priorisation Fonctionnalités** - RICE, ICE
9. **Planificateur Go-to-Market** - GTM Canvas
10. **Architecte Stratégie Prix** - Van Westendorp
11. **Constructeur Roadmap Stratégique** - OKR

### Marketing & Croissance (7 skills)

12. **Concepteur Identité Marque** - Archétypes, pyramide de marque
13. **Stratégiste Marketing Contenu** - Content pillars
14. **Guide Growth Hacking** - Traction Bullseye
15. **Stratégiste Réseaux Sociaux** - Social media matrix
16. **Architecte Email Marketing** - Séquences email
17. **Planificateur SEO Contenu** - Keyword clusters
18. **Stratégiste Communauté** - Community engagement

### Rétention & Métriques (4 skills)

19. **Concepteur Tableau Bord Métriques** - AARRR, North Star
20. **Expert Optimisation Rétention** - Analyse de cohortes
21. **Optimiseur Parcours Onboarding** - Funnel d'activation
22. **Framework Feedback Client** - NPS, CSAT, CES

### Levée de Fonds & Opérations (5 skills)

23. **Architecte Modèle Financier** - Projections financières
24. **Planificateur Stratégie Levée Fonds** - Stages de fundraising
25. **Rédacteur Brief Investisseur** - One-pager
26. **Constructeur Pitch Deck Investisseur** - Pitch deck complet
27. **Créateur Playbook Opérationnel** - Documentation opérationnelle

## 🗂️ Structure du Projet

```
hacienda-marketing-pack/
├── skills/                      # 27 skills organisés par catégorie
│   ├── strategie-fondation/     # 7 skills
│   ├── strategie-marche-produit/# 4 skills
│   ├── marketing-croissance/    # 7 skills
│   ├── retention-metriques/     # 4 skills
│   └── levee-fonds-operations/  # 5 skills
├── instructions/                # 6 fichiers de chaînage
├── shared/                      # Ressources partagées
│   ├── scripts/                 # Utilitaires Python
│   └── references/              # Glossaire et templates
├── GUIDE-INSTALLATION.md        # Guide complet
└── README.md                    # Ce fichier
```

Chaque skill contient :
- `SKILL.md` - Instructions complètes avec approche socratique
- `references/` - Frameworks et méthodologies détaillés + glossaire et templates
- `scripts/` - Script Python d'analyse + utilitaires locaux

**Note** : Chaque skill est **complètement autonome** avec tous les utilitaires et références nécessaires copiés localement. Pas de dépendance au dossier `shared/`.

## 📖 Documentation

- **[GUIDE-INSTALLATION.md](GUIDE-INSTALLATION.md)** - Installation et configuration
- **[Glossaire](shared/references/glossaire-strategie.md)** - Tous les concepts clés
- **[Templates](shared/references/templates-rapports.md)** - Templates de rapports

### Parcours Guidés (Chaineurs)

- [Chaineur Stratégie Fondation](instructions/chaineur-strategie-fondation.md)
- [Chaineur Stratégie Marché & Produit](instructions/chaineur-strategie-marche-produit.md)
- [Chaineur Marketing & Croissance](instructions/chaineur-marketing-croissance.md)
- [Chaineur Rétention & Métriques](instructions/chaineur-retention-metriques.md)
- [Chaineur Levée de Fonds & Opérations](instructions/chaineur-levee-fonds-operations.md)
- [Chaineur Parcours Complet](instructions/chaineur-parcours-complet.md)

## 🎓 Utilisation

### Pour Entrepreneurs Solo

Idéal pour structurer et valider votre idée étape par étape.

```
Lance le parcours Stratégie Fondation
```

### Pour Équipes Startup

Alignez votre équipe sur la stratégie avec des outputs partagés.

```
Nous sommes 3 cofondateurs, comment organiser le parcours Hacienda ?
```

### Pour Mentors/Advisors

Guidez vos mentorés avec une méthodologie éprouvée.

### Pour Accélérateurs/Incubateurs

Framework structuré pour accompagner plusieurs startups.

## 🔧 Technologies

- **Language** : Markdown + Python 3.8+
- **Platform** : Claude Desktop
- **MCP** : Model Context Protocol pour accès fichiers
- **Aucune dépendance externe** : Bibliothèque standard Python uniquement

## 🤝 Contribution

Les contributions sont les bienvenues ! Ce projet est open-source.

### Comment Contribuer

1. Fork le projet
2. Créez une branche feature (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📄 Licence

MIT License - © Hacienda

Vous êtes libre d'utiliser, modifier et distribuer ce projet.

## 🙏 Remerciements

- Frameworks inspirés par April Dunford, Ash Maurya, Alexander Osterwalder
- Méthodologie socratique adaptée au coaching entrepreneurial
- Communauté open-source

## 📞 Contact & Support

- **Issues** : [GitHub Issues](https://github.com/jamon8888/hacienda-marketing-pack/issues)
- **Discussions** : [GitHub Discussions](https://github.com/jamon8888/hacienda-marketing-pack/discussions)

---

**Prêt à transformer votre idée en stratégie complète ?** 

[Commencez maintenant](GUIDE-INSTALLATION.md) avec Hacienda Marketing Pack ! 🚀

---

*Hacienda Marketing Pack v1.0.0 - Accompagnement stratégique intelligent pour entrepreneurs*