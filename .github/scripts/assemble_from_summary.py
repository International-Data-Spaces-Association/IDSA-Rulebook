#!/usr/bin/env python3
"""Concatenate the Markdown files listed in SUMMARY.md, in order, into one file.

Adapted from International-Data-Spaces-Association/.github's
scripts/assemble_from_summary.py for a single-repo layout: the combined file
is written back into the summary's own directory (not the repo root) so that
relative image links such as ./media/foo.png keep resolving without rewriting.
"""

from __future__ import annotations

import argparse
import os
import re

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def collect_referenced_files(summary_path: str) -> list[str]:
    summary_dir = os.path.dirname(os.path.normpath(summary_path))
    ordered: list[str] = []
    seen: set[str] = set()

    with open(summary_path, encoding="utf-8") as f:
        for line in f:
            match = LINK_RE.search(line)
            if not match:
                continue

            link = match.group(1).split("#", 1)[0].strip()
            if link.startswith("http://") or link.startswith("https://"):
                continue
            if not (link.endswith(".md") or link.endswith(".markdown")):
                continue

            path = os.path.normpath(os.path.join(summary_dir, link))
            if path not in seen:
                seen.add(path)
                ordered.append(path)

    return ordered


def frontmatter_first(paths: list[str]) -> list[str]:
    """Pin FrontMatter.md to the front for PDF output.

    SUMMARY.md lists it last for the published site's nav order; the PDF
    wants it as a cover/imprint page up front instead. Reordering here keeps
    SUMMARY.md itself untouched.
    """
    front = [p for p in paths if os.path.basename(p).lower() == "frontmatter.md"]
    rest = [p for p in paths if os.path.basename(p).lower() != "frontmatter.md"]
    return front + rest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--summary", required=True, help="Path to SUMMARY.md")
    parser.add_argument("--out", required=True, help="Path to write the combined Markdown file")
    parser.add_argument("--fail-on-missing", action="store_true")
    args = parser.parse_args()

    referenced = frontmatter_first(collect_referenced_files(args.summary))
    missing = [p for p in referenced if not os.path.exists(p)]
    if missing and args.fail_on_missing:
        raise SystemExit("Missing referenced Markdown files:\n" + "\n".join(missing))

    parts: list[str] = []
    for index, path in enumerate(referenced):
        if index > 0:
            # Start each top-level document on a fresh page.
            parts.append("\\newpage\n\n")
        if not os.path.exists(path):
            parts.append(f"<!-- MISSING: {path} -->\n\n")
            continue
        with open(path, encoding="utf-8") as f:
            parts.append(f.read().rstrip() + "\n\n")

    with open(args.out, "w", encoding="utf-8") as f:
        f.write("".join(parts).strip() + "\n")

    print(f"Assembled {len(referenced)} files into {args.out}")


if __name__ == "__main__":
    main()
