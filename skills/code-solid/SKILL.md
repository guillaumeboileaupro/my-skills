---
name: code-solid
description: Appliquer et verifier des regles de codage SOLID, de qualite et de maintenabilite lors de toute creation, modification, revue ou refactorisation de code, notamment Python, TypeScript, Java, C et C++.
---

# Code SOLID - Regles de codage pour agents

## Objectif et priorite

Produire le changement le plus petit qui repond au besoin, reste facile a tester et preserve le comportement existant. Appliquer SOLID de facon pragmatique, en plus des conventions locales du depot. Ne jamais sacrifier la simplicite a une abstraction speculative.

## Protocole obligatoire

1. Avant toute modification, lire les fichiers concernes, leurs appelants, les tests et les regles du depot (AGENTS.md, linters, formatters, configuration CI).
2. Identifier le comportement attendu, les invariants, les contrats publics et les cas limites.
3. Proposer le changement minimal. Ne refactoriser hors perimetre que si cela est necessaire a la correction.
4. Ecrire ou adapter les tests correspondant au comportement modifie, y compris erreurs et cas limites.
5. Executer les outils de formatage, lint, typage, tests et controles de securite deja configures, lorsqu'ils sont disponibles.
6. A la fin, rapporter fichiers touches, justification, tests executes, limites et risques restants. Ne jamais annoncer des tests reussis sans les avoir executes.

## SOLID - Regles de revue

### S - Single Responsibility Principle

- Un module ou une classe a une responsabilite coherente et une raison principale de changer.
- Isoler les regles metier de la persistance, du transport, de la presentation et des effets de bord lorsque leurs evolutions sont independantes.
- Ne pas decouper artificiellement une fonction ou une classe uniquement pour reduire son nombre de lignes.
- Signal d'alerte : une modification fonctionnelle force a changer plusieurs responsabilites sans rapport.

### O - Open/Closed Principle

- Si plusieurs variantes sont etablies ou demandees, utiliser un point d'extension lisible (composition, strategie, fonction injectable, polymorphisme).
- Preferer une table de correspondance ou une fonction simple quand elle suffit.
- Ne pas creer de framework, fabrique ou hierarchie pour un seul cas stable.
- Signal d'alerte : chaque nouvelle variante necessite de modifier une longue chaine de conditions a haut risque.

### L - Liskov Substitution Principle

- Toute implementation d'un contrat respecte preconditions, postconditions, invariants, sorties et erreurs attendues.
- Ne pas renforcer les preconditions ni affaiblir les garanties des sous-types.
- Eviter les methodes heritees qui levent une erreur de type "non pris en charge" en situation normale.
- Tester les implementations via les memes tests de contrat quand plusieurs sous-types existent.

### I - Interface Segregation Principle

- N'exposer a un consommateur que les operations dont il a besoin.
- Preferer de petits protocoles/interfaces orientes usages plutot qu'une grande interface universelle.
- Ne pas multiplier des interfaces de facade sans consommateurs reels.
- Signal d'alerte : methodes vides, factices ou non pertinentes imposees par un contrat.

### D - Dependency Inversion Principle

- La logique metier depend de contrats stables plutot que de clients HTTP, bases de donnees ou SDK concrets quand ces dependances doivent varier ou etre simulees.
- Injecter les dependances au point de composition, expliciter leurs durees de vie et les effets de bord.
- Ne pas creer un conteneur d'injection ou une interface pour chaque classe par principe.
- Utiliser les fonctions et la composition pour les modules simples.

## Regles transversales de qualite

- **Lisibilite** : noms explicites, fonctions coherentes, controle de flux simple, commentaires expliquant le pourquoi plutot que paraphrasant le code.
- **Typage** : annotations ou types precis selon le langage; eviter `any`, casts non justifies et suppressions globales d'erreurs de type.
- **Erreurs** : valider les entrees aux frontieres, propager ou traiter les erreurs explicitement, ne pas masquer silencieusement les exceptions.
- **Etat** : limiter l'etat global mutable, rendre les dependances et mutations visibles.
- **DRY et duplication** : supprimer les duplications de logique reelles, sans fusionner des cas simplement ressemblants qui evoluent independamment.
- **KISS et YAGNI** : ne pas ajouter de configuration, d'interface, de couche, de dependance ni de generalisation sans besoin concret.
- **Compatibilite** : verifier les appelants avant de changer une API, un schema, un format ou une signature publique.
- **Securite** : ne jamais introduire de secret dans le depot; garder validation et autorisation aux bonnes frontieres.
- **Tests** : tester le comportement observable, y compris cas nominaux, erreurs et limites; eviter les tests attaches aux details prives d'implementation.
- **Maintenance** : supprimer imports inutiles et code devenu mort dans le perimetre modifie; respecter formatage et conventions existants.
- **Performance** : ne pas degrader les chemins critiques; mesurer avant une optimisation complexe.

## Specificites selon le langage

- **Python** : respecter les conventions du projet et le typage existant; utiliser `Protocol` ou des callables seulement si cela simplifie un contrat reel; gerer proprement context managers et exceptions.
- **TypeScript** : privilegier les types explicites aux frontieres, les unions discriminees et les interfaces fines; eviter `any` et les assertions de type non justifiees.
- **Java / C#** : utiliser interfaces et injection pour les dependances variables; favoriser composition plutot qu'heritage de commodite.
- **C++** : expliciter ownership et duree de vie, appliquer RAII, limiter les hierarchies virtuelles; privilegier la composition.
- **C** : exprimer les responsabilites par modules et API reduites, documenter ownership, erreurs et invariants; SOLID ne presuppose pas de classes.

## Checklist de sortie

- [ ] La modification repond au besoin avec une complexite proportionnee.
- [ ] Responsabilites, points d'extension et dependances sont coherents.
- [ ] Les contrats publics et les substitutions restent valides.
- [ ] Les erreurs, cas limites et effets de bord sont traites.
- [ ] Aucun code mort, duplication injustifiee ou abstraction speculative n'est ajoute.
- [ ] Les tests et verifications pertinents sont executes, ou les limites sont signalees.

## Format de reponse d'une revue SOLID

Pour chaque probleme reel, fournir : `fichier:ligne` (si connu), principe affecte, impact concret, correction minimale et test associe. Classer par severite. Ne pas inventer de probleme pour couvrir les cinq lettres. Si aucune violation significative n'est observee, le dire explicitement.
