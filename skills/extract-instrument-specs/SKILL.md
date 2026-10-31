---
name: extract-instrument-specs
description: Extraire des PDF de spécifications les instruments, exigences, entrées, sorties, interfaces, modes et acronymes avec leur provenance. Utiliser pour préparer une base de connaissances ou le contexte documentaire d'un LLM.
---

# Structurer les spécifications des instruments

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

## Parcours

1. Établir documents, révisions, configuration et périmètre. Utiliser `search-pdf-evidence` pour localiser et lire les preuves. Réexaminer visuellement les pages contenant des tableaux ou schémas.
2. Extraire les exigences avec leur texte exact et ID officiel. Distinguer obligation, exemple et description informative. Séparer les obligations multiples tout en conservant leur exigence parent.
3. Décrire les instruments, modes et transitions documentés. Extraire les préconditions, exceptions et dépendances.
4. Pour chaque entrée ou sortie, relever émetteur, récepteur, direction, déclencheur, message, champs, types, taille, unités, plage, encodage, cadence, délai et réaction aux erreurs lorsque ces informations sont présentes.
5. Relever acronymes, définition exacte et domaine d'emploi. Conserver plusieurs définitions si le contexte diffère.
6. Proposer les relations entre objets avec une preuve pour chaque lien. Marquer les inférences comme proposées ; conserver auteur et méthode de validation séparément.
7. Contrôler doublons, renvois absents, unités, révisions et contradictions. Transmettre les blocages à `audit-spec-gaps`.

## Format de sortie

Produire des enregistrements JSON ou YAML comprenant `id_interne`, `type`, `id_source`, `texte_source`, `description_normalisee`, `applicabilite`, `champs`, `sources`, `statut`, `hypotheses` et `manques`.

Pour chaque source, inclure fichier, empreinte, document, révision, page PDF et localisateur précis. Pour une relation, inclure origine, cible, type, preuve et statut. Éviter les objets contenant seulement une paraphrase sans extrait.

## Règles

- Conserver la valeur et l'unité originales avant toute conversion. Documenter formule et hypothèses d'une conversion.
- Distinguer absent, inconnu, contradictoire et non applicable. Ne pas transformer une case vide en zéro.
- Ne pas inventer type, timeout, criticité, protocole ou comportement d'erreur.
- Ne pas fusionner les variantes ou révisions.
- Ne pas importer automatiquement les candidats dans la BD validée. Utiliser le circuit de revue établi par le projet.
- Préparer des obligations testables ; laisser l'oracle manquant explicitement manquant.

Terminer par les volumes extraits, les sections réellement examinées et les limites de l'extraction.
