---
name: inspect-pdf-visuals
description: Analyser visuellement les tableaux, schémas, figures et équations dans les PDF techniques. Utiliser lorsque les cellules, flèches, légendes, colonnes ou symboles portent les spécifications et interactions des instruments.
---

# Vérifier tableaux et schémas

## Confidentialité prioritaire

Traiter les PDF techniques et tous leurs dérivés comme confidentiels. Effectuer lecture, extraction, OCR, recherche, calcul des embeddings et inférence exclusivement dans un environnement local approuvé.

- Vérifier le lieu réel d'exécution du modèle et des outils avant d'accéder au contenu. Un dépôt privé, un terminal local ou une URL localhost ne prouve pas que le modèle est local.
- Dans un agent cloud ou un environnement indéterminé, ne pas ouvrir les PDF, afficher leurs pages ou lire leurs extraits dans le contexte du modèle. Travailler sur la méthode et les exemples fictifs. Autoriser uniquement un script local sans réseau qui écrit ses résultats dans un fichier local et ne restitue aucun contenu ni métadonnée confidentielle au modèle ; ne pas lire ensuite ce rapport avec les outils de l'agent.
- Ne transmettre aucun original, extrait, résumé, schéma, donnée structurée, embedding, prompt documentaire ou résultat de test dérivé à GitHub, ChatGPT, une API distante, un outil web ou un autre agent hébergé.
- Conserver documents, bases, index, contextes, journaux et fichiers temporaires dans un espace local approuvé, hors Git et hors synchronisation distante.
- Désactiver les envois réseau, la télémétrie et les sauvegardes distantes du traitement documentaire. Vérifier le fonctionnement hors ligne ; les instructions seules ne constituent pas une isolation réseau.
- Charger modèles et dépendances avant de rendre les documents accessibles. Refuser un repli automatique vers un service cloud.
- Ne publier dans le dépôt que méthodes, code générique et exemples fictifs vérifiés. Nettoyer les sorties et diffs avant toute publication.
- Pour une collaboration, garder les sous-agents dans la même frontière locale vérifiée. Ne pas déléguer les sources à un service distant.
- Ne jamais déclarer la confidentialité garantie sans avoir vérifié modèle, outils, réseau, journaux, caches et sauvegardes.

Cette règle prime sur les commandes et procédures ci-dessous. Si l'environnement ne permet pas de la respecter, préserver les fichiers sans les lire et signaler le blocage.

1. Identifier le PDF, la révision et les pages à examiner. Utiliser une page PDF en base 1 ; vérifier séparément la pagination imprimée.
2. Rendre les pages sélectionnées dans un dossier temporaire sans modifier l'original.

```bash
pdftoppm -f 12 -l 12 -r 150 -png '/chemin/spec.pdf' '/dossier/temp/page'
```

3. Ouvrir les images avec l'outil de visualisation disponible. Agrandir les parties illisibles. Si la visualisation ou le rendu n'est pas disponible, annoncer cette limite ; ne pas prétendre avoir lu le schéma.
4. Pour un tableau, relever titre, en-têtes, unités, cellules fusionnées, notes et continuation sur d'autres pages. Comparer les cellules critiques à l'extraction textuelle.
5. Pour un schéma, relever blocs, labels, flèches, ports, bus, légende, styles de traits et renvois. Distinguer connexion, flux de données, commande et dépendance seulement lorsque la notation le permet.
6. Pour une équation, transcrire les symboles, indices, unités, domaines et hypothèses ; garder une image de référence lorsque nécessaire.
7. Comparer le résultat au texte. Enregistrer les divergences sans choisir arbitrairement une version.

## Sortie

Pour chaque élément, produire fichier, révision, empreinte, page PDF, numéro de figure ou tableau, légende, contenu transcrit, relations proposées, ambiguïtés et statut de revue. Conserver si possible les coordonnées de l'élément et la méthode de rendu.

Ne pas inférer le sens d'une flèche illisible ou d'une couleur sans légende. Ne pas présenter une transcription visuelle comme un test validé. Envoyer les ambiguïtés vers `audit-spec-gaps`.
