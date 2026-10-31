#!/usr/bin/env python3
"""Read PDF pages and locate literal terms; never perform OCR or interpretation."""
from __future__ import annotations

import argparse
import hashlib
import json
import logging
from pathlib import Path
import sys
import warnings


def positive(value: str) -> int:
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("La valeur doit être positive.")
    return number


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--output", type=Path,
                        help="Écrire le rapport localement sans afficher son contenu")
    parser.add_argument("--include-text", action="store_true",
                        help="Afficher le texte uniquement dans un environnement local approuvé")
    parser.add_argument("--query", help="Terme littéral, insensible à la casse")
    parser.add_argument("--page", type=positive, help="Page PDF, base 1")
    parser.add_argument("--limit", type=positive, default=20)
    args = parser.parse_args()
    if args.output:
        logging.disable(logging.CRITICAL)
        warnings.simplefilter("ignore")
    if args.query is not None and not args.query.strip():
        parser.error("La recherche ne peut pas être vide.")
    try:
        from pypdf import PdfReader
    except ImportError:
        print("Dépendance manquante : pypdf.", file=sys.stderr)
        return 2
    try:
        path = args.pdf.resolve(strict=True)
        if args.output and args.output.resolve() == path:
            raise ValueError("Le rapport ne peut pas remplacer le PDF source.")
        reader = PdfReader(path)
        if reader.is_encrypted and not reader.decrypt(""):
            raise ValueError("PDF chiffré : utiliser une copie lisible autorisée.")
        count = len(reader.pages)
        if args.page is not None and args.page > count:
            raise ValueError(f"Page {args.page} hors du document ({count} pages).")
        with path.open("rb") as stream:
            digest = hashlib.file_digest(stream, "sha256").hexdigest()
        pages = [args.page - 1] if args.page else range(count)
        matches = []
        sparse = []
        errors = []
        examined = []
        query = args.query.casefold() if args.query else None
        for index in pages:
            examined.append(index + 1)
            try:
                text = reader.pages[index].extract_text() or ""
            except Exception as exc:
                errors.append({"page_pdf": index + 1, "error": str(exc)})
                continue
            if len(text.strip()) < 30:
                sparse.append(index + 1)
            if query is None or query in text.casefold():
                item = {"page_pdf": index + 1}
                if args.include_text:
                    item["text"] = text
                matches.append(item)
        result = {
            "file": str(path), "sha256": digest, "extractor": "pypdf",
            "document_revision": None, "page_count": count,
            "query": args.query, "pages_examined": examined,
            "text_included": args.include_text,
            "matching_pages": len(matches), "returned_pages": len(matches[:args.limit]),
            "truncated": len(matches) > args.limit, "results": matches[:args.limit],
            "sparse_text_pages": sparse, "extraction_errors": errors,
            "warnings": [
                "Recherche textuelle littérale, sans OCR ni analyse des schémas.",
                "Ne pas utiliser sur des sources confidentielles dans un agent cloud.",
                "Les métadonnées peuvent aussi être confidentielles.",
                "Une absence de résultat ne démontre pas une absence documentaire.",
                "Les pages peu textuelles peuvent nécessiter une lecture visuelle.",
            ],
        }
        serialized = json.dumps(result, ensure_ascii=False, indent=2)
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(serialized + "\n", encoding="utf-8")
            print("Rapport écrit localement. Contenu non affiché.")
        else:
            print(serialized)
        return 1 if errors else 0
    except Exception as exc:
        if args.output:
            print("Échec du traitement local. Aucun contenu affiché.", file=sys.stderr)
        else:
            print(f"Erreur : {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
