---
name: ui-component-design
description: Concevoir et implementer des composants d'interface coherents et reutilisables sans sur-abstraction. Utiliser pour boutons, listes, selecteurs, sliders, controles media, modales, feedback, tokens visuels et etats de composants.
---

# UI Component Design

## Objectif

Construire des composants previsibles, coherents et adaptes au produit. Reutiliser lorsqu'une repetition ou un contrat commun existe reellement, sans transformer chaque fragment d'interface en abstraction generique.

## Avant de creer un composant

Verifier :

1. Existe-t-il deja un composant equivalent ?
2. Le besoin est-il repete ou suffisamment complexe pour meriter une frontiere ?
3. Quelles variantes sont reellement necessaires ?
4. Quels etats le composant doit-il gerer ?
5. Qui possede l'etat : composant, vue ou couche metier ?
6. Le composant doit-il fonctionner au clavier et au tactile ?

Ne pas creer une abstraction uniquement pour reduire quelques lignes de markup.

## Contrat

Un composant doit avoir :

- une responsabilite claire ;
- des proprietes nommees selon le domaine ou le comportement ;
- des valeurs par defaut raisonnables ;
- des etats explicites ;
- une sortie/evenement previsible ;
- aucune dependance implicite a une page particuliere lorsqu'il est presente comme reutilisable.

Eviter les props booleennes accumulees qui creent des combinaisons impossibles.

## Systeme visuel

Maintenir une coherence pour :

- espacements ;
- tailles de controles ;
- typographie ;
- rayons ;
- bordures ;
- icones ;
- focus ;
- transitions ;
- couleurs semantiques.

Preferer quelques tokens ou variables explicites a des valeurs legerement differentes copiees partout.

Ne pas construire un design system complet avant que le produit n'en ait besoin.

## Boutons et actions

- Une vue doit avoir une hierarchie claire entre action primaire, secondaire et destructive.
- Ne pas multiplier les styles de boutons pour des differences mineures.
- Les boutons iconiques exigent un nom accessible.
- Loading et disabled doivent etre distincts lorsqu'ils signifient des choses differentes.
- Eviter les doubles soumissions ou doubles commandes accidentelles.

## Listes et selection

- Rendre la selection visible autrement que par la couleur seule.
- Conserver une cle/identite stable pour l'element selectionne.
- Gerer liste vide, chargement, erreur et element devenu indisponible.
- Ne pas confondre hover et selection.

## Sliders et valeurs continues

- Afficher la valeur lorsque cela aide la precision ou la comprehension.
- Gerer clavier et tactile.
- Definir min, max, step et format explicitement.
- Ne pas envoyer une rafale non controlee d'actions couteuses si la couche metier ne le supporte pas.
- Distinguer valeur demandee, valeur en cours d'envoi et valeur confirmee lorsque le domaine l'exige.

## Modales et panneaux temporaires

- N'utiliser une modale que si l'interruption du contexte est justifiee.
- Gerer focus initial, fermeture clavier et restitution du focus.
- Ne pas cacher une action frequente derriere une modale.
- Preferer un panneau inline lorsque le contexte doit rester visible.

## Etats asynchrones

Un composant connecte a une operation asynchrone doit definir :

- idle ;
- pending/loading ;
- success si un feedback est necessaire ;
- error ;
- unavailable/disconnected si pertinent.

Ne pas afficher un succes avant la preuve requise par le domaine.

## Tests

Tester le comportement public du composant :

- activation ;
- selection ;
- clavier ;
- etats disabled/loading ;
- erreur ;
- donnees absentes ;
- valeurs limites ;
- changement de props/etat significatif.

Eviter les tests couples aux details CSS sans valeur de regression reelle.

## Revue

- Le composant resout-il un besoin reel ?
- Son API est-elle plus simple que copier le comportement ?
- Les variantes correspondent-elles a des cas du produit ?
- Tous les etats necessaires existent-ils ?
- Les styles sont-ils coherents avec les composants voisins ?
- Fonctionne-t-il au clavier et au tactile si necessaire ?
- L'etat metier reste-t-il dans la couche appropriee ?
- Une abstraction peut-elle etre supprimee sans perte ?

La reutilisabilite n'est pas un objectif superieur a la clarte du produit.