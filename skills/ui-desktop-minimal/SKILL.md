---
name: ui-desktop-minimal
description: Concevoir, implementer ou relire des interfaces d'application desktop et responsives minimalistes, compactes et haut de gamme, en evitant les archetypes generiques de dashboards IA. Utiliser pour les interfaces Tauri, TypeScript, desktop, mobile responsive, telecommandes et outils applicatifs.
---

# Minimal Desktop UI

## Objectif

Concevoir des interfaces applicatives calmes, precises, compactes et immediatement comprehensibles. Privilegier l'usage, la hierarchie et la lisibilite avant la decoration.

Ce skill concerne des applications. Ne pas appliquer par defaut les conventions visuelles d'une landing page ou d'un site marketing.

## Principes fondamentaux

- Faire passer la fonction avant la decoration.
- Preferer une surface principale claire a une collection de cartes.
- Utiliser l'espace pour etablir la hierarchie sans gaspiller l'ecran.
- Exiger une raison fonctionnelle pour chaque element visible.
- Rendre l'action principale identifiable immediatement.
- Utiliser la divulgation progressive pour les actions secondaires.
- Preferer la manipulation directe aux panneaux de configuration.
- Conserver une densite adaptee a une application desktop, sans transformer le minimalisme en grands espaces vides.

## Eviter les interfaces IA generiques

Ne pas utiliser par defaut :

- grilles de cartes de dashboard ;
- bento grids sans justification fonctionnelle ;
- hero sections ;
- titres demesures de site marketing ;
- gradients decoratifs ;
- glassmorphism ;
- ombres lourdes ;
- multiplication de conteneurs arrondis ;
- pills et badges decoratifs omnipresents ;
- sidebar pour une petite application qui n'en a pas besoin ;
- panneaux imbriques sans necessite ;
- emojis comme icones d'interface ;
- statistiques ou donnees factices destinees uniquement a remplir l'ecran ;
- texte marketing decoratif.

Ne pas transformer chaque information en carte. Essayer d'abord l'espacement, l'alignement, la typographie et les separateurs.

## Typographie et hierarchie

- Utiliser une seule famille sans-serif coherente, sauf exigence produit contraire.
- Construire la hierarchie avec la taille, le poids, l'espacement et le contraste.
- Garder les labels applicatifs compacts.
- Reserver les grandes tailles aux informations reellement dominantes.
- Ne pas utiliser une echelle typographique de landing page dans une vue applicative.
- Utiliser des contrastes accessibles sans rendre inutilement tout le texte noir pur.

## Couleurs

- Privilegier une interface claire par defaut lorsque le produit ne demande pas explicitement un theme sombre.
- Utiliser une base neutre et un accent fonctionnel principal.
- Employer la couleur d'abord pour communiquer une action, un etat, une selection ou une alerte.
- Eviter les palettes decoratives multicolores sans semantique.
- Conserver un contraste accessible pour le texte et les controles.

## Surfaces, bordures et rayons

Preferer :

- espace blanc ;
- alignement ;
- separateurs ;
- bordures fines et discretes ;

aux cartes imbriquees et aux ombres.

Choisir un systeme coherent de rayons. Ne pas melanger arbitrairement angles vifs, petits rayons et grandes capsules.

Une ombre n'est acceptable que si elle exprime une elevation ou une superposition reelle.

## Controles

- Les controles principaux doivent etre comprehensibles sans texte explicatif superflu.
- Grouper spatialement les actions qui agissent sur le meme objet.
- Donner une priorite visuelle proportionnelle a la frequence et a l'importance de l'action.
- Conserver des cibles tactiles utilisables aux largeurs mobiles.
- Concevoir explicitement les etats hover, focus clavier, active, disabled et loading.
- Utiliser des micro-interactions sobres et rapides. Ne pas animer pour decorer.
- Utiliser des icones SVG coherentes plutot que des emojis.

## Responsive

Desktop et mobile doivent conserver le meme modele mental, mais ne pas simplement reduire la vue desktop.

Prioriser dans cet ordre :

1. contexte courant ;
2. action principale ;
3. controles frequents ;
4. informations secondaires.

Aux petites largeurs, reordonner ou masquer les informations secondaires plutot que compresser tous les elements.

## Etats applicatifs

Concevoir explicitement :

- etat initial ;
- chargement ;
- absence de donnees ;
- donnees partielles ;
- succes ;
- appareil ou service indisponible ;
- erreur recuperable ;
- deconnexion.

Ne jamais inventer de donnees pour rendre une maquette plus complete.

Les details techniques internes appartiennent a une vue de diagnostic lorsqu'ils ne sont pas utiles a l'utilisateur normal.

## Accessibilite et interaction

- Conserver un ordre de focus logique.
- Fournir un focus clavier visible.
- Ne pas communiquer un etat uniquement par la couleur.
- Utiliser des libelles accessibles pour les controles iconiques.
- Respecter les tailles de cibles et contrastes necessaires a l'usage reel.
- Ne pas sacrifier l'accessibilite pour obtenir une interface visuellement plus epuree.

## Methode de travail

1. Lire le besoin produit, les vues existantes et les contraintes techniques avant de dessiner.
2. Identifier le contexte principal, l'action principale et les controles frequents.
3. Construire d'abord la hierarchie et le flux sans decoration.
4. Supprimer les conteneurs et textes qui ne sont pas necessaires.
5. Definir ensuite typographie, espacement, rayons, bordures, icones et accent.
6. Verifier tous les etats applicatifs, pas seulement le happy path.
7. Verifier les largeurs desktop et mobile pertinentes.
8. Tester l'interface reelle lorsque l'environnement le permet, sans confondre rendu visuel et validation fonctionnelle du materiel.
9. Comparer le resultat aux regles de ce skill et simplifier encore si possible.

## Checklist de revue

Avant d'accepter une interface, verifier :

- Peut-on retirer un element sans perdre de fonctionnalite ou de comprehension ?
- L'action principale est-elle evidente ?
- Les controles lies sont-ils regroupes naturellement ?
- Une information est-elle affichee plusieurs fois ?
- Des conteneurs sont-ils utilises la ou l'espacement suffirait ?
- L'interface ressemble-t-elle a une application plutot qu'a une landing page ?
- Reste-t-elle comprehensible sans texte decoratif ?
- Les etats loading, empty, error, disconnected et partial sont-ils prevus ?
- Le clavier et le tactile restent-ils utilisables ?
- Le layout fonctionne-t-il aux largeurs desktop et telephone visees ?
- Les choix visuels servent-ils la fonction plutot qu'une mode graphique ?

## Adaptation au produit

Ce skill fournit des principes, pas une identite visuelle universelle. Lire les regles du projet avant toute implementation et respecter en priorite :

- l'identite graphique validee ;
- les composants existants qui sont encore pertinents ;
- les contraintes de plateforme ;
- les exigences d'accessibilite ;
- la hierarchie fonctionnelle specifique au produit.

Ne pas copier l'apparence d'une marque tierce. Une reference visuelle sert a comprendre une qualite de hierarchie, de densite ou d'interaction, pas a reproduire son design.