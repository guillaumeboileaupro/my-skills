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

## Methode de decision pour l'agent

Appliquer cet ordre a chaque changement :

1. **Contrat** : identifier entrees, sorties, erreurs, invariants, compatibilite et effets de bord.
2. **Diagnostic** : citer au moins un symptome observe avant de proposer une abstraction (duplication des regles, forte dependance, test difficile, cas incompatible).
3. **Choix** : comparer la correction locale avec une extraction/composition et prendre la solution la plus simple satisfaisante.
4. **Implementation** : modifier uniquement les composants necessaires; conserver l'API publique sauf demande explicite ou correction indispensable.
5. **Verification** : ajouter des tests de comportement, puis executer les commandes effectivement disponibles. Ne pas inventer des resultats.
6. **Bilan** : mentionner tout compromis, toute verification non executee et toute rupture volontaire.

Un principe SOLID n'impose **ni** une classe par fonction, **ni** une interface par service, **ni** un pattern partout. Quand une regle ne s'applique pas, l'agent ne doit pas fabriquer une violation.

## Exemples concrets avant/apres

Les exemples sont volontairement courts. Adapter nomenclature, politique d'erreur et architecture au projet.

### S - Responsabilite unique (SRP)

**Detecter** : un composant formate des factures, interroge la base et envoie des notifications; ces raisons de changer sont distinctes. Un simple grand nombre de lignes n'est **pas** une preuve de violation.

Avant - Python :

```python
class InvoiceService:
    def finalize(self, invoice):
        total = sum(item.price * item.quantity for item in invoice.items)
        database.save(invoice.id, total)
        email_client.send(invoice.customer_email, f"Total: {total}")
        return total
```

Apres - isoler les frontieres techniques, sans creer de couches superflues :

```python
from typing import Callable

def calculate_total(invoice) -> int:
    return sum(item.price * item.quantity for item in invoice.items)

class InvoiceService:
    def __init__(self, save_total: Callable[[str, int], None],
                 notify: Callable[[str, int], None]) -> None:
        self.save_total = save_total
        self.notify = notify

    def finalize(self, invoice) -> int:
        total = calculate_total(invoice)
        self.save_total(invoice.id, total)
        self.notify(invoice.customer_email, total)
        return total
```

**Verifier** : test unitaire du calcul sans IO; test d'orchestration avec deux fonctions factices. L'injection depend ici du besoin de remplacer les frontieres, pas d'une obligation universelle. Dans le vrai projet, utiliser un type monetaire adapte (par exemple Decimal) et des identifiants types correctement.

### O - Ouvert/ferme (OCP)

**Detecter** : une fonction centrale change a chaque ajout d'un mode d'expedition reel. Une condition sur deux cas stables ne justifie pas a elle seule une hierarchie.

Avant :

```python
def shipping_cost(method: str, weight: float) -> float:
    if method == "standard":
        return 4.0 + weight
    if method == "express":
        return 10.0 + 2 * weight
    raise ValueError("Unknown shipping method")
```

Apres - strategies par fonctions si les variantes sont extensibles :

```python
from collections.abc import Callable

ShippingRule = Callable[[float], float]

RULES: dict[str, ShippingRule] = {
    "standard": lambda w: 4.0 + w,
    "express": lambda w: 10.0 + 2 * w,
}

def shipping_cost(method: str, weight: float,
                  rules: dict[str, ShippingRule] = RULES) -> float:
    if weight < 0:
        raise ValueError("weight must be nonnegative")
    try:
        return rules[method](weight)
    except KeyError as exc:
        raise ValueError("Unknown shipping method") from exc
```

**Verifier** : ajouter un mode "pickup" dans un mapping fourni par l'appelant, sans modifier `shipping_cost`. Tester les modes existants, poids invalides et mode inconnu. La valeur par defaut du mapping doit etre traitee comme constante, sans mutation.

### L - Substitution de Liskov (LSP)

**Detecter** : un sous-type refuse une operation promise, change la signification d'un retour ou exige des preconditions plus strictes.

Avant :

```python
class FileStore:
    def read(self, key: str) -> bytes: ...
    def write(self, key: str, data: bytes) -> None: ...

class ReadOnlyStore(FileStore):
    def write(self, key: str, data: bytes) -> None:
        raise NotImplementedError("read only")
```

Apres - scinder le contrat, ne pas feindre une capacite :

```python
from typing import Protocol

class Reader(Protocol):
    def read(self, key: str) -> bytes: ...

class Writer(Protocol):
    def write(self, key: str, data: bytes) -> None: ...

def load_config(reader: Reader, key: str) -> bytes:
    return reader.read(key)
```

**Verifier** : executer les memes tests de lecture sur toutes les implementations de `Reader`; ne transmettre un store lecture seule qu'aux consommateurs du contrat `Reader`. Documenter les erreurs attendues (cle absente, IO) et les garantir dans chaque implementation.

### I - Segregation des interfaces (ISP)

**Detecter** : un client ne consomme qu'une petite partie d'une interface et certaines implementations doivent simuler des operations qui ne les concernent pas.

Avant - TypeScript :

```typescript
interface Workspace {
  read(path: string): Promise<string>;
  write(path: string, data: string): Promise<void>;
  delete(path: string): Promise<void>;
}

async function preview(workspace: Workspace, path: string) {
  return workspace.read(path);
}
```

Apres :

```typescript
interface ReadableWorkspace {
  read(path: string): Promise<string>;
}

interface WritableWorkspace {
  write(path: string, data: string): Promise<void>;
  delete(path: string): Promise<void>;
}

async function preview(workspace: ReadableWorkspace, path: string) {
  return workspace.read(path);
}
```

**Verifier** : `preview` fonctionne avec un objet qui implemente uniquement `read`. Ne pas fractionner une interface si tous ses consommateurs ont reellement besoin de toutes ses operations.

### D - Inversion des dependances (DIP)

**Detecter** : la logique metier construit elle-meme un client technique, ce qui bloque les tests ou impose un fournisseur.

Avant :

```python
class RegistrationService:
    def register(self, user):
        client = VendorMailSdk(api_key=get_secret())
        client.send(user.email, "Welcome")
```

Apres - dependance explicite au point d'entree :

```python
from typing import Protocol

class MailSender(Protocol):
    def send(self, recipient: str, message: str) -> None: ...

class RegistrationService:
    def __init__(self, mailer: MailSender) -> None:
        self.mailer = mailer

    def register(self, user) -> None:
        self.mailer.send(user.email, "Welcome")
```

**Verifier** : substituer un `FakeMailer` en test; instancier le SDK et adapter son API dans la couche de composition (hors logique metier). Ne pas forcer une interface quand un `Callable` suffit.

## Exigences concretes par dimension

| Dimension | Regle verifiable | Contre-exemple a eviter |
| --- | --- | --- |
| Frontieres | Parser/valider les donnees externes a l'entree; erreurs explicites | `except Exception: pass` |
| Typage | Typer les fonctions publiques et les frontieres suivant la configuration du depot | `Any` / `any` qui diffuse l'absence de contrat |
| Erreurs | Capturer seulement les erreurs dont on peut assurer le traitement | Capturer tout puis retourner `None` sans contrat |
| Tests | Couvrir nominal, limite et echec d'un comportement modifie | Tester uniquement l'implementation interne |
| Couplage | Metier independant du framework si besoin observable | Construire SDK et acces DB dans le calcul metier |
| Duplication | Mutualiser une regle de domaine identique | Abstraction prematuree de codes semblables |
| API | Verifier appelants, serialization, versions et compatibilite | Renommer une fonction publique sans migration |
| Securite | Ne jamais logger secrets ou donnees personnelles inutiles | Token code en dur dans les exemples ou tests |
| Performance | Preserver cout et complexite des parcours critiques | Ajouter N+1 requetes au refactoring |

**Seuils et conventions** : ne pas inventer de limites universelles (taille de fichier, nombre de methodes, taux de couverture). Appliquer d'abord celles du projet. En absence de seuil, signaler un risque concret avec son impact et un test, pas une alerte numerique arbitraire.

## Cas particuliers et choix de conception

- **Code fonctionnel** : SRP, OCP et DIP s'appliquent via fonctions pures, composition et injection de fonctions; ne pas imposer de classes.
- **C** : separer interfaces `.h` et implementation `.c`, documenter ownership et codes de retour; OCP/DIP via callbacks si un besoin concret existe.
- **C++** : preferer RAII, ownership explicite, references et composition; si polymorphisme, destructeur virtuel sur la base appropriee et contrat substituable.
- **Python** : preferer `Protocol` pour contrat structurel utilise, `Callable` pour une operation; ne pas introduire de classe abstraite pour une seule fonction.
- **TypeScript** : types unions discriminees pour variantes finies; interfaces fines aux frontieres; ne pas contourner le compilateur par `as any`.
- **Java** : constructeur et interfaces selon les besoins; eviter le service locator et les singletons mutables.
- **Applications existantes** : faire un refactoring incremental, tests avant/apres, migrations explicites; ne pas rearchitecturer sans demande.
- **Concurrency/async** : conserver garanties de concurrence, timeouts, annulation et ordre des effets; une extraction SOLID ne doit pas les casser.
- **Donnees** : integrite, transactions et idempotence peuvent primer sur la decoupe structurelle. Une operation transactionnelle doit rester coherente.

## Tests de contrat et controle du comportement

Exemple de test partagé du contrat `Reader` :

```python
import pytest

@pytest.mark.parametrize("factory", [MemoryReader, DiskReader])
def test_reader_returns_expected_bytes(factory):
    reader = factory({"config": b"ok"})
    assert reader.read("config") == b"ok"
```

Ce test est **illustratif** : `MemoryReader` et `DiskReader` sont des adaptateurs fictifs et doivent etre implementes ou remplaces par les vrais fixtures du depot avant execution. Ne jamais declarer cet exemple executable tel quel.

Pour chaque refactoring SOLID : ajouter un test de non-regression sur l'API publique, un test d'echec pertinent et, si necessaire, un test de substitution. Lorsque la compatibilite exige une migration, fournir les etapes precises.

## Revue : severites et format obligatoire

- **Bloquant** : changement de comportement non voulu, erreur de contrat, donnee corrompue, probleme de securite.
- **Important** : dependance impossible a tester, violation de substitution, risque eleve de regression lors des extensions connues.
- **Suggestion** : amelioration de lisibilite, decoupage ou extraction non indispensables.

Rapport sous cette forme :

```text
[Important] src/orders/service.py:42 - SRP/DIP
Constat : la methode calcule la remise et appelle directement le SDK de paiement.
Impact : un changement de fournisseur rend le calcul difficile a tester.
Correction minimale : injecter un PaymentGateway au point de composition.
Test : verifier la remise avec un faux gateway et un echec de paiement.
```

Toujours terminer par : **fichiers modifies**, **tests executes avec leurs resultats**, **tests non executes et pourquoi**, **risques restants**. Ne pas presenter les exemples didactiques comme les fichiers reels du projet.

## Checklist de sortie

- [ ] La modification repond au besoin avec une complexite proportionnee.
- [ ] Responsabilites, points d'extension et dependances sont coherents.
- [ ] Les contrats publics et les substitutions restent valides.
- [ ] Les erreurs, cas limites et effets de bord sont traites.
- [ ] Aucun code mort, duplication injustifiee ou abstraction speculative n'est ajoute.
- [ ] Les tests et verifications pertinents sont executes, ou les limites sont signalees.

## Format de reponse d'une revue SOLID

Pour chaque probleme reel, fournir : `fichier:ligne` (si connu), principe affecte, impact concret, correction minimale et test associe. Classer par severite. Ne pas inventer de probleme pour couvrir les cinq lettres. Si aucune violation significative n'est observee, le dire explicitement.
