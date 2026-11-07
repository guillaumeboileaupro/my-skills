---
name: evidence-driven-development
description: "Piloter les projets logiciels avec une seule mission active, des preuves CI et materiel distinctes, des corrections minimales et un tableau de temps restant qui diminue. Utiliser pour toute planification, investigation, correction, revue, validation et passation Codex ou Claude, sur GitHub ou GitLab."
---

# Developpement guide par les preuves

## But
Livrer le comportement utile avec le moins de travail inutile possible. Un controle ne devient pas une tache parce qu'il est imaginable : il faut un defaut observe, une exigence explicite du proprietaire ou une obligation de securite/CI deja applicable.

Ce skill s'applique a tous les projets de developpement, quelles que soient la plateforme (GitHub/GitLab/local), la pile (Python, Rust, Android, web, etc.) et la nature des tests. Les regles locales de `AGENTS.md`, `CLAUDE.md` et les obligations de securite/CI prevalentes restent applicables. Ne pas deduire une autorisation d'agir a partir de ce skill.

## Principes obligatoires

1. **Une seule mission active, un seul agent actif.** Identifier le responsable avant de commencer. Ne pas lancer deux agents sur le meme sujet, ni un diagnostic pendant une correction en cours. Une seule PR/MR ouverte pour le flux coordonne, sauf derogation explicite du proprietaire. Ne pas modifier la branche ou les fichiers non integres d'un autre agent.
2. **Roles explicites, jamais supposes.** Dans le workflow de reference, Claude mene l'investigation et les tests materiels ; Codex realise les corrections et le developpement. Cette repartition est configurable par projet et mission. Les prompts doivent nommer exactement un agent et ne jamais contenir des instructions contradictoires.
3. **Observation avant correction.** Reproduire ou documenter le probleme, distinguer faits et hypotheses, isoler la cause, puis proposer le plus petit changement utile. Une absence de preuve ne justifie pas un refactoring, une dependance, un audit supplementaire ou une nouvelle fonctionnalite.
4. **Le proprietaire decide.** Lui seul autorise les fusions, les changements de priorite et les operations sur les appareils, comptes, secrets, reseaux ou donnees personnelles. Une CI verte rend eventuellement la PR admissible, jamais automatiquement fusionnee.
5. **Ne pas gonfler le travail restant.** Ne pas recreer une tache terminee, ajouter des travaux speculatifs ou compter deux fois une meme installation, correction ou validation. Retirer les lignes validees ou explicitement hors perimetre.
6. **Economiser le temps et les tokens sans contourner les garde-fous.** Chercher les fichiers precis, reutiliser les preuves encore valides, lancer les tests cibles puis les controles obligatoires. Ne jamais omettre un audit, un test ou une verification rendus obligatoires par le depot.

## Preuve et vocabulaire

Toute affirmation de fonctionnement doit preciser la nature et les limites de sa preuve :

| Statut | Signification | Ce que cela ne prouve pas |
|---|---|---|
| IMPLEMENTED | Code present | Ni tests ni resultat reel |
| CI PASS | Tests automatises verts, sur SHA identifie | Fonctionnement sur appareil reel |
| MERGED | PR/MR integree a la branche cible | Installation ou validation materielle |
| INSTALLED | Build identifie installe dans l'environnement cite | Fonctionnalite testee |
| HARDWARE PASS | Comportement effectivement observe sur l'appareil | Generalisation a tous les appareils et scenarios |
| PARTIAL | Une partie du scenario seulement est confirmee | Validation complete |
| FAIL | Echec observe et reproductible ou consigne | Cause racine necessairement connue |
| NOT RUN | Controle non effectue | Echec ou succes |
| BLOCKED | Controle empeche, raison documentee | Echec fonctionnel |

Conserver pour chaque preuve le scenario, la date, le SHA/build, l'environnement et le resultat. Ne pas requalifier un `CI PASS` en `HARDWARE PASS`. `sent`, `queued` ou `acknowledged` ne signifient pas que l'action a eu l'effet visible attendu. Un test ancien realise avant installation d'un nouveau recepteur reste une preuve de l'ancien environnement.

## Cycle de mission

### 1. Cadrer une seule mission
- Enoncer le comportement attendu, l'ecart constate, la preuve existante, le responsable, le perimetre et les criteres de sortie.
- Lire les instructions locales et le dernier bilan. Reutiliser les faits fiables plutot que reprendre tous les historiques.
- Verifier les missions/PR/MR deja ouvertes. Ne pas en ouvrir une deuxieme pour gagner artificiellement du temps.
- Distinguer urgent, utile plus tard et hors perimetre. Un souhait abandonne par le proprietaire ne reste pas dans le backlog actif.

### 2. Diagnostiquer au minimum utile
- Reconstituer le chemin du signal : evenement UI -> adaptateur -> service -> transport -> destinataire -> effet observable, selon l'architecture.
- Etablir une table `Observation | Preuve | Hypothese | Verification minimale | Conclusion`.
- Commencer par logs sanitaires, tests reproduisant le symptome et inspection locale non destructive.
- S'arreter quand la cause est identifiee ou quand un manque de preuve exige une autorisation materielle.
- Ne pas lancer d'ADB, commandes reseau vers un appareil, microphone, installation ou modification du systeme sans l'accord requis.
- Si aucun defaut n'est confirme, conclure `aucune correction` et terminer la mission. Ne jamais ouvrir une PR de complaisance.

### 3. Corriger seulement le defaut confirme
- Confier au developpeur un prompt unique : cause, fichiers concernes, comportement attendu, test de regression, limites et interdictions.
- Preferer une correction minimale. Pas de refonte ou migration hors sujet.
- Ajouter le test cible qui prouve le bug et sa resolution. Executer ensuite les controles CI et securite obligatoires.
- Ouvrir au plus une PR/MR coherente ; attendre la decision du proprietaire pour la fusion.
- Ne pas confondre commentaires de revue automatises et veto bloquant ; traiter les vrais echec de CI ou remarques valides selon les regles du depot.

### 4. Valider sans refaire le travail
- Reutiliser les tests et preuves sur le meme SHA et environnement tant qu'ils couvrent le changement.
- Retester exactement les chemins affectes par le changement et les regressions plausibles ; ne pas repasser toute la recette materielle sans justification.
- Identifier ce qui reste `NOT RUN` plutot que de le presenter comme une anomalie.
- Un changement fonctionnel peut etre `MERGED` et encore `NOT RUN` sur appareil.
- Un defaut confirme en recette cree une seule tache ciblee, sans recopier les validations deja prevues.

### 5. Clore et passer le relais
- Produire un bilan bref : fait, preuve, SHA/PR/MR, limites, prochaine action et responsable.
- Marquer les travaux termines comme termines puis les retirer du **tableau du temps restant**, tout en gardant un historique consultable.
- Ne pas creer de PR pour mettre a jour un tableau si un travail de code utile permet de le faire dans sa prochaine PR autorisee.
- Nettoyer uniquement les caches, worktrees et artefacts identifies comme temporaires et non necessaires. Preserver branches et fichiers de travail d'autrui, secrets et resultats materiels.

## Tableau unique du temps restant

Toujours tenir **une seule table globale**, avec une seule colonne `Temps restant (min / max / med.)`, en heures, et sans trois colonnes de chiffres separees :

| Priorite | Travail restant | Responsable | Temps restant (min / max / med.) |
|---|---|---|---|
| P1/P2 | Tache non terminee et prouvee necessaire | Agent designe | 0,5 / 1,5 / 1 h |
| **TOTAL** | **Somme des lignes** | | **0,5 / 1,5 / 1 h** |

Les valeurs ci-dessus sont **un exemple de format**, pas des estimations par defaut. Le coordinateur chiffre les travaux a partir du perimetre et des preuves disponibles ; les agents rapportent les faits, sans inventer des heures. Ne pas creer une ligne pour un travail non demande, deja valide ou abandonne. Ne pas imputer aux validations existantes le temps d'un test supplementaire. Les sommes min, max et mediane doivent etre arithmetiquement coherentes. Signaler quand l'incertitude interdit une estimation serieuse.

A chaque point, rapprocher le tableau precedent du travail effectue :
- **Fusion seule** : supprimer le temps de correction termine, conserver uniquement la recette effectivement encore a faire.
- **Validation materielle PASS** : supprimer la ligne couverte.
- **CI PASS sans test materiel** : decrire `NOT RUN`, sans transformer automatiquement ce statut en nouvelle mission.
- **Defaut nouveau confirme** : ajouter seulement sa correction ou validation indispensable, en expliquant tout changement du total.
- **Tache abandonnee** : supprimer immediatement.
- **Temps restant en hausse** : expliquer precisement quelle observation nouvelle le justifie.

Ne jamais presenter la baisse d'estimation comme un gain de productivite mesure : elle peut aussi provenir de la suppression de doublons ou de travaux hors perimetre.

## Contrat de prompt entre agents

Toute passation tient en un prompt copiable qui contient :
```text
MISSION :
AGENT UNIQUE :
ETAT / SHA / PR OU MR :
FAITS OBSERVES :
CE QUI EST DEJA VALIDE :
OBJECTIF ET CRITERE DE SORTIE :
PERIMETRE AUTORISE :
INTERDICTIONS ET AUTORISATIONS MATERIELLES :
TESTS CIBLES ET CONTROLES OBLIGATOIRES :
LIVRABLE (PREUVES, CAUSE, FICHIERS, ETAT, SUITE) :
```

Le diagnostic ne doit pas demander en meme temps a Codex de programmer si Claude est l'agent unique, et inversement. Finir la mission active avant de transmettre la suivante. Les prompts restent concis et directement copiables dans un bloc `text`.

## Adaptation par projet
- **GitHub** : PR, checks GitHub Actions, SHA et protections de branche.
- **GitLab** : MR, pipeline GitLab CI, SHA et regles de protection.
- **Local / hors forge** : branche, commit, tests locaux et validation explicite du proprietaire.
- **Application avec appareils** : consigner `HARDWARE PASS` par appareil et par scenario.
- **Bibliotheque ou backend sans appareils** : remplacer la recette materielle par une preuve d'integration ou d'execution reelle adaptee.

Ne pas imposer d'appareil, de langage, de framework, de seuil de couverture ou de CI qui n'existe pas dans le projet. Les politiques de securite, confidentialite, licence et conformite obligatoires ne sont jamais facultatives.

## Definition de termine
Une mission est terminee lorsque son livrable annonce est produit, avec preuves et limites explicites. Un diagnostic peut se terminer par `aucun defaut confirme`; un developpement par `CI PASS, materiel NOT RUN` si la recette materielle n'etait pas son objectif. Le projet entier n'est dit termine que lorsque les objectifs effectivement retenus par le proprietaire sont satisfaits.
