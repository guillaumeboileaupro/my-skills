---
name: audit-spec-gaps
description: Auditer les PDF techniques pour identifier informations manquantes, contradictions, références absentes et obstacles à la conception de tests. Utiliser pour évaluer ce qui est exploitable dans les documents et ce qui manque à une base de connaissances.
---

# Auditer exploitabilité et manques

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

1. Définir les documents, révisions et sections examinés. Utiliser les preuves de `search-pdf-evidence` et les objets proposés par `extract-instrument-specs`. Inspecter les éléments visuels déterminants.
2. Pour chaque obligation, vérifier acteur, mode, préconditions, stimulus, résultat observable, unité, tolérance, délai et comportement en erreur.
3. Vérifier interfaces, transitions, acronymes et références externes. Chercher les informations dans les sections liées avant de déclarer un manque.
4. Distinguer manque documentaire, moyen de test inconnu ou absent, et décision organisationnelle non établie. L'absence d'un banc dans un PDF ne démontre pas que le banc n'existe pas.
5. Comparer les sources contradictoires en conservant leurs révisions et applicabilités. Appliquer la règle d'autorité du projet si elle est connue ; sinon soumettre l'arbitrage.
6. Classer exploitable directement, après revue, après clarification, ou bloqué avec les moyens actuels.
7. Établir l'impact sur les scénarios de test et une question de clarification précise. Proposer un responsable par rôle lorsque la personne n'est pas connue.

## Registre de sortie

Produire ID, catégorie, objet ou exigence, sources, périmètre examiné, constat, impact, question, rôle responsable, priorité proposée, état et condition de résolution. Pour un manque d'oracle, préciser quelle mesure ou règle manque pour déterminer pass/fail.

Donner trois listes : informations exploitables, éléments nécessitant revue, blocages et recherches supplémentaires. Ne pas chiffrer une couverture globale sans dénominateur vérifié. Ne pas inventer seuil, délai ou tolérance pour débloquer un scénario.

Déclarer un élément absent uniquement dans le périmètre effectivement examiné ; conserver "à rechercher" pour les sources non disponibles. Relier toute résolution ultérieure à sa preuve et aux objets concernés.
