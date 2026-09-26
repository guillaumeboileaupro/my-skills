---
name: ui-responsive-app
description: Concevoir et implementer des interfaces applicatives adaptatives entre desktop, tablette et mobile sans simplement reduire la vue desktop. Utiliser pour responsive layout, reflow, densite, breakpoints, tactile et hierarchie multi-ecrans.
---

# Responsive Application UI

## Objectif

Preserver le meme modele mental et les memes fonctions essentielles sur des tailles d'ecran differentes tout en adaptant hierarchie, disposition, densite et interaction a chaque contexte.

Une interface responsive n'est pas une interface desktop compressee.

## Demarche

1. Identifier les fonctions indispensables et leur ordre de priorite.
2. Concevoir les plus petites largeurs visees sans supposer la presence d'une souris.
3. Concevoir ensuite l'usage de l'espace supplementaire sur desktop.
4. Choisir les breakpoints en fonction des ruptures du contenu, pas d'une liste arbitraire d'appareils.
5. Verifier chaque etat applicatif aux tailles critiques.
6. Tester avec du contenu court, long, absent et partiel.

## Hierarchie adaptative

Prioriser :

1. contexte courant ;
2. action principale ;
3. controles frequents ;
4. informations secondaires ;
5. diagnostics et details rares.

Aux petites largeurs :

- empiler lorsque cela clarifie le parcours ;
- masquer ou deplacer les informations secondaires ;
- conserver les actions principales visibles ;
- eviter le scroll horizontal pour l'interface principale ;
- ne pas reduire les controles jusqu'a les rendre difficiles a utiliser.

Aux grandes largeurs :

- utiliser l'espace pour clarifier les relations ;
- ne pas etirer arbitrairement les contenus ;
- limiter les largeurs de lecture lorsque necessaire ;
- ne pas ajouter des panneaux simplement parce que l'espace existe.

## Breakpoints

- Choisir un breakpoint lorsqu'un groupe de controles ne tient plus proprement ou que la hierarchie devient confuse.
- Eviter de multiplier les breakpoints pour corriger des dimensions rigides mal choisies.
- Preferer flex, grid, min/max/clamp et dimensions intrinsèques lorsque cela simplifie le comportement.
- Tester juste avant et juste apres chaque breakpoint.

## Tactile, souris et clavier

- Les actions principales doivent fonctionner au tactile et a la souris.
- Ne pas rendre une fonction dependante du hover.
- Conserver des cibles tactiles suffisamment grandes.
- Le clavier doit rester utilisable sur desktop.
- Les controles glissants doivent rester manipulables sans precision excessive.

## Contenu variable

Tester :

- noms courts et longs ;
- valeurs absentes ;
- messages d'erreur ;
- localisation avec textes plus longs ;
- listes vides et longues ;
- titres media ou appareils longs ;
- valeurs numeriques extremes plausibles.

Eviter les hauteurs fixes qui cassent des que le contenu change.

## Densite

Le mobile n'exige pas de supprimer toute information et le desktop n'exige pas d'afficher tout simultanement.

- Garder la densite compatible avec la frequence d'usage.
- Utiliser la divulgation progressive pour les details secondaires.
- Ne pas transformer chaque groupe en carte pour faciliter le responsive.
- Conserver les relations spatiales entre controles lies.

## Etats systeme

Verifier aux tailles critiques :

- loading ;
- empty ;
- partial ;
- error ;
- disconnected ;
- selection ;
- clavier ouvert sur mobile si des champs existent.

Les messages d'erreur longs ne doivent pas casser le layout.

## Revue

Avant validation :

- Le produit conserve-t-il le meme modele mental entre desktop et mobile ?
- L'action principale reste-t-elle visible ?
- Les controles frequents restent-ils accessibles ?
- Existe-t-il un scroll horizontal involontaire ?
- Les cibles restent-elles utilisables au tactile ?
- Les textes longs cassent-ils le layout ?
- Les grands ecrans contiennent-ils de l'espace vide utile plutot que des composants decoratifs ajoutes ?
- Les breakpoints correspondent-ils a de vraies ruptures de contenu ?
- Les etats d'erreur et deconnexion sont-ils aussi robustes que le happy path ?

Documenter les tailles reellement testees. Ne pas declarer une plateforme validee uniquement parce que le CSS est responsive.