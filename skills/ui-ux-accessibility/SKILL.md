---
name: ui-ux-accessibility
description: Concevoir, implementer et relire l'accessibilite d'interfaces web, desktop et responsives. Utiliser pour navigation clavier, focus, semantique, ARIA, contrastes, formulaires, controles iconiques, etats dynamiques et interactions tactiles.
---

# UI UX Accessibility

## Objectif

Rendre une interface utilisable sans supposer une souris, une vision parfaite, une perception des couleurs complete ou une interaction tactile precise. L'accessibilite fait partie du comportement du produit et ne doit pas etre ajoutee comme finition visuelle.

## Demarche

1. Identifier les parcours principaux et les controles interactifs.
2. Verifier d'abord la semantique native disponible avant d'ajouter ARIA.
3. Parcourir l'interface au clavier uniquement.
4. Verifier focus, ordre de navigation, activation et fermeture des composants.
5. Examiner les contrastes, tailles de cibles et informations communiquees uniquement par la couleur.
6. Verifier les etats loading, error, disabled, selected, expanded et disconnected.
7. Tester les changements dynamiques qui doivent etre annonces aux technologies d'assistance.
8. Ajouter des tests automatises pertinents sans les presenter comme preuve exhaustive d'accessibilite.

## Semantique

- Preferer les elements natifs `button`, `input`, `select`, `label`, listes et titres aux divs rendues interactives.
- Conserver une hierarchie de titres logique.
- Associer explicitement les labels et descriptions aux champs.
- Utiliser ARIA uniquement lorsqu'un equivalent natif ne suffit pas.
- Ne jamais utiliser ARIA pour masquer une semantique native correcte.
- Donner un nom accessible aux boutons uniquement iconiques.

## Clavier et focus

- Toute action disponible a la souris doit etre atteignable et activable au clavier lorsqu'elle est pertinente sur la plateforme.
- Conserver un indicateur de focus visible.
- Ne pas supprimer `outline` sans remplacement accessible.
- Respecter un ordre de focus correspondant a l'ordre visuel et logique.
- Ne pas creer de piege clavier.
- Restituer le focus de facon logique apres fermeture d'une modale ou d'un panneau temporaire.
- Ne pas deplacer automatiquement le focus sans raison fonctionnelle.

## Couleur et contraste

- Ne jamais communiquer succes, erreur, selection ou disponibilite uniquement par la couleur.
- Verifier le contraste du texte, des icones fonctionnelles, bordures utiles et focus.
- Les textes secondaires doivent rester lisibles. `muted` ne signifie pas presque invisible.
- Tester les etats hover, disabled et selected, pas uniquement l'etat normal.

## Cibles et gestes

- Garder des cibles suffisamment grandes et espacees pour un usage tactile fiable.
- Ne pas exiger un geste complexe lorsqu'une action simple peut exister.
- Fournir une alternative aux interactions dependantes uniquement du hover.
- Ne pas placer deux actions destructives ou opposees trop proches sans justification.

## Contenu dynamique

- Afficher visuellement les etats loading, succes, erreur et deconnexion.
- Annoncer les changements importants aux technologies d'assistance lorsque necessaire.
- Eviter les mises a jour frequentes et bavardes des live regions.
- Un spinner seul ne suffit pas : le contexte de chargement doit etre comprehensible.

## Formulaires et erreurs

- Expliquer l'erreur pres du champ concerne.
- Ne pas effacer une saisie valide a cause d'une erreur sur un autre champ.
- Indiquer clairement les contraintes avant ou au moment de la saisie lorsque possible.
- Les placeholders ne remplacent pas les labels.
- Les erreurs doivent etre comprehensibles sans code couleur.

## Mouvement

- Garder les animations fonctionnelles courtes et sobres.
- Respecter les preferences de reduction de mouvement lorsque la plateforme les expose.
- Ne pas rendre une information accessible uniquement pendant une animation.
- Eviter clignotements et mouvements decoratifs continus.

## Etats a verifier

Pour chaque composant interactif, verifier si applicable :

- default ;
- hover ;
- focus ;
- active ;
- selected ;
- disabled ;
- loading ;
- error ;
- disconnected/unavailable.

## Revue

Avant validation :

- Le parcours principal fonctionne-t-il sans souris ?
- Le focus est-il toujours visible et previsible ?
- Les controles iconiques ont-ils un nom accessible ?
- Une information depend-elle uniquement d'une couleur ?
- Les textes secondaires restent-ils lisibles ?
- Les cibles tactiles sont-elles utilisables ?
- Les erreurs indiquent-elles quoi faire ?
- Les mises a jour importantes sont-elles perceptibles sans surveillance visuelle constante ?
- Les tests automatises sont-ils completes par une verification manuelle des parcours critiques ?

Documenter ce qui a ete teste reellement et ce qui reste a verifier. Ne jamais declarer une interface totalement accessible sur la seule base d'un linter.