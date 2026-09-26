---
name: ui-design-review
description: Auditer une interface existante et proposer des corrections UI/UX concretes, priorisees et localisees. Utiliser pour revue visuelle, detection de patterns IA generiques, hierarchie, densite, coherence, etats et dette d'interface.
---

# UI Design Review

## Objectif

Evaluer une interface comme un produit utilisable, pas comme une image decorative. Produire des constats localises, observables et actionnables sans redesigner arbitrairement l'ensemble du produit.

## Ordre de revue

Examiner dans cet ordre :

1. objectif de la vue ;
2. hierarchie fonctionnelle ;
3. parcours principal ;
4. etats applicatifs ;
5. densite et layout ;
6. typographie ;
7. controles et interactions ;
8. couleurs, bordures, rayons et ombres ;
9. responsive ;
10. accessibilite ;
11. finition visuelle.

Ne pas commencer par changer les couleurs ou les rayons si le probleme est structurel.

## Detecter les patterns generiques

Signaler lorsqu'ils n'ont pas de justification fonctionnelle :

- dashboard compose de cartes uniformes ;
- bento grid decorative ;
- sidebar vide ou surdimensionnee ;
- hero applicatif avec grand slogan ;
- multiples pills/badges ;
- gradients et glassmorphism ;
- ombres lourdes ;
- grandes zones vides destinees uniquement a produire une impression premium ;
- duplication d'une meme information dans plusieurs surfaces ;
- texte explicatif compensant un controle mal concu ;
- icones incoherentes ou emojis ;
- donnees factices servant a remplir le design.

Le probleme n'est pas l'existence d'une carte ou d'un badge, mais leur utilisation automatique sans semantique.

## Hierarchie

Verifier :

- ce que l'utilisateur regarde en premier ;
- si cela correspond a sa tache principale ;
- si l'action principale domine correctement ;
- si les actions secondaires restent accessibles sans concurrencer l'action principale ;
- si les details techniques occupent une place disproportionnee.

## Densite et espaces

- Rechercher les espacements incoherents avant d'ajouter des conteneurs.
- Distinguer respiration utile et espace perdu.
- Regrouper ce qui agit sur le meme objet.
- Separer ce qui appartient a des contextes differents.
- Verifier alignements, rythmes verticaux et largeurs.

## Etats

Une revue est incomplete sans examiner :

- initial ;
- loading ;
- empty ;
- partial ;
- success ;
- error ;
- disconnected/unavailable ;
- disabled ;
- selected.

Ne pas accepter un design qui fonctionne uniquement avec des donnees ideales.

## Interactions

Verifier :

- feedback apres action ;
- affordance des controles ;
- prevention des doubles actions accidentelles ;
- etats disabled/loading ;
- clavier et focus ;
- tactile aux petites largeurs ;
- transitions qui clarifient plutot qu'elles ne decorent.

## Format des constats

Pour chaque probleme significatif, donner :

- severite : bloquant, important ou finition ;
- emplacement ;
- observation concrete ;
- impact utilisateur ;
- correction minimale recommandee.

Eviter les jugements vagues comme `plus moderne`, `plus premium` ou `plus joli` sans expliquer le comportement visuel recherche.

## Revue avant validation

- L'interface communique-t-elle sa fonction en quelques secondes ?
- L'action principale est-elle evidente ?
- Peut-on supprimer des elements ?
- Les donnees et actions sont-elles groupees selon leur relation fonctionnelle ?
- Les etats non ideaux sont-ils concus ?
- La densite convient-elle a la plateforme ?
- Les conventions visuelles sont-elles coherentes ?
- Le responsive conserve-t-il le modele mental ?
- Les problemes d'accessibilite evidents sont-ils traites ?
- Les modifications proposees respectent-elles l'identite du produit plutot que de la remplacer ?

Une revue peut conclure qu'aucune refonte n'est necessaire. Ne pas produire des changements uniquement pour justifier la revue.