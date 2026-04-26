---
name: math-system-onboarding
description: Onboard Codex to the `math` subsystem inside `math_physics`. Use when working in `math/`, editing concept Markdown notes, syncing `math/lib/math.json`, changing graph import/export/validation tooling in `math/scripts/`, applying ontology rules in `math/rules/`, or deciding where math-specific logic and verification should live before making changes.
---

# Math System Onboarding

## Overview

Read this skill before changing the `math` subsystem. Treat it as the local operating manual for the repository's pure-math knowledge graph, supporting scripts, and graph-maintenance rules.

Prefer repository facts over generic assumptions. If a workflow detail is unclear, verify it from the referenced files or by running the local CLI/service in dry-run or validation mode.

## Project Map

Start with these files:

- `ReadMe.md`: repository-level map, reading order, maintenance principles, and the intended role of `math/` versus `applied mathematics/` and `physics/`.
- `math/Set.md`, `math/Logic.md`, `math/Relation.md`: conceptual entry points into the math graph.
- `math/scripts/ReadMe.md`: the authoritative map of the maintained graph tooling.

Treat the main `math` areas as follows:

| Path | Role | Use It When |
| --- | --- | --- |
| `math/*.md` | Canonical concept notes, one file per concept node | Add or revise mathematical content, definitions, properties, parents, or children |
| `math/assets/` | Images used by concept notes | Check linked figures or add supporting media for notes |
| `math/lib/math.json` | Canonical graph JSON snapshot used by tooling | Validate, diff, repair, or inspect graph structure programmatically |
| `math/rules/*.md` | Ontology, node, edge, and schema policies | Decide whether a concept should be a node, what relations to keep, and how to structure data |
| `math/scripts/*.py` | Import/export, lookup, validation, CRUD, and service tooling | Change automation behavior or investigate sync/graph bugs |
| `math/scripts/sync.html` | Local manual UI for service-driven operations | Inspect or support the browser-facing sync flow |
| `history/` | Historical JSON/XLSX artifacts and converters | Compare older snapshots or inspect legacy conversion data |

Keep the system boundary clear:

- Use `math/` for pure mathematical ontology and concept graph work.
- Use `applied mathematics/` for problem-oriented material.
- Use `physics/` for physics notes.
- Do not place pure-math graph tooling under `applied mathematics/` or `physics/`.

## Core Entry Points

Read the right entry point for the task:

- Read `math/scripts/graph.py` first for the maintained CLI entry point.
- Read `math/scripts/graph_cli.py` for real command behavior and option parsing.
- Read `math/scripts/service_app.py` for the maintained HTTP service entry point.
- Read `math/scripts/markdown_import.py` for Markdown-to-JSON sync behavior.
- Read `math/scripts/markdown_export.py` for JSON-to-Markdown sync behavior.
- Read `math/scripts/graph_validate_core.py` for validation and repair behavior.
- Read `math/scripts/graph_store.py` and `math/scripts/graph_model.py` for graph mutation and storage rules.

Use this file-to-problem map:

| Question | Read First |
| --- | --- |
| "Where should this new math concept live?" | `math/rules/Math Concept.md`, `math/rules/Math Concept Node Policy.md` |
| "Should these two concepts have an edge?" | `math/rules/Math Concept Edge Policy.md` |
| "What fields must every node contain?" | `math/rules/Math Concept Node Schema.md`, `math/scripts/graph_store.py` |
| "Why did Markdown import/export behave this way?" | `math/scripts/markdown_import.py`, `math/scripts/markdown_export.py`, `math/scripts/markdown_parse.py` |
| "Why is the graph inconsistent?" | `math/scripts/graph_validate_core.py`, `math/lib/math.json` |
| "How do I query or mutate the graph safely?" | `math/scripts/ReadMe.md`, `math/scripts/graph_cli.py`, `math/scripts/service_app.py` |
| "Which note should answer this concept question?" | The target concept note in `math/*.md`, then its listed `Parents` and `Include` neighbors |

## System Rules And Conventions

Follow these content rules:

- Keep one mathematical concept per Markdown file.
- Keep the filename stem equal to the concept key. Example: `math/Set.md` maps to `Set` in `math/lib/math.json`.
- Use the standard note sections: `## Define`, `## Properties`, `## Include`, and `## Parents`.
- Put the minimal identifying definition in `Define`.
- Put theorems, formulas, remarks, examples, and extended discussion in `Properties`.
- Use `Include` and `Parents` for structural graph relations, not loose cross-references.

Follow these graph rules:

- Treat the retained graph as a sparse backbone DAG, not a full semantic web.
- Create standalone nodes primarily for mathematical objects or object classes.
- Keep non-object material such as properties, methods, theorems, and representations inside object notes unless the local rule docs explicitly justify otherwise.
- Prefer direct, non-redundant structural edges.
- Keep `parents` and `children` mirrored whenever possible.

Follow these JSON/schema rules:

- Keep all four node fields: `define`, `parents`, `children`, `properties`.
- Use `""`, `{}`, and `[]` for empty values; do not use `null`.
- Preserve relation labels when editing parent/child maps.

Follow these code and module conventions:

- Treat `math/scripts/graph.py` as a thin executable wrapper and `graph_cli.py` as the real CLI implementation.
- Extend core behavior in the focused modules instead of adding new wrapper scripts unless a new entry point is truly necessary.
- Prefer repository-relative paths in docs, commands, and code examples. Do not treat any machine-specific absolute path as a required contract.
- Preserve the current separation of concerns:
  - `graph_model.py`: in-memory graph mutations
  - `graph_store.py`: file IO, normalization, atomic writes, JSON CRUD
  - `markdown_parse.py`: Markdown parsing helpers
  - `markdown_import.py`: Markdown ingestion and diff
  - `markdown_export.py`: Markdown regeneration
  - `concept_lookup_core.py`: concept lookup
  - `graph_validate_core.py`: validation and repair
  - `service_app.py`: Flask API surface

Respect current repository facts:

- No dedicated automated test directory or conventional test suite was found in the current snapshot.
- No dependency manifest such as `requirements.txt` or `pyproject.toml` was found in the current snapshot.
- No committed `math.index.json` sidecar was found; the import/rename flows can generate it.
- `ReadMe.md` still shows `python service.py`, but the maintained service file present in the repo is `math/scripts/service_app.py`. Verify actual entry points from `math/scripts/ReadMe.md` and the script directory before changing service instructions.

## Existing Capabilities

Assume the system already supports these workflows before building anything new:

| Capability | Existing Implementation |
| --- | --- |
| List, read, create, update, delete, and rename concept nodes | `math/scripts/graph_cli.py`, `math/scripts/graph_store.py`, `math/scripts/graph_model.py` |
| Add or remove parent/child relations | `graph.py` / `graph_cli.py` commands plus JSON-backed store functions |
| Build `math/lib/math.json` from Markdown notes | `math/scripts/markdown_import.py` |
| Regenerate Markdown notes from JSON | `math/scripts/markdown_export.py` |
| Compare Markdown and JSON snapshots | `math/scripts/markdown_import.py::diff_markdown_vs_json` |
| Validate graph shape and mirrored edges | `math/scripts/graph_validate_core.py` |
| Repair mirrored-edge inconsistencies | `math/scripts/graph_validate_core.py::repair_math_json` |
| Resolve concept names by exact, substring, or fuzzy lookup | `math/scripts/concept_lookup_core.py` |
| Call graph operations over HTTP | `math/scripts/service_app.py` |
| Drive manual sync operations in a browser page | `math/scripts/sync.html` |

Reuse the existing functions instead of re-implementing them:

- Use `build_graph_json_from_markdown_folder()` for Markdown import.
- Use `build_markdown_from_graph_json()` for Markdown export.
- Use `validate_math_json()` and `repair_math_json()` for structural checks.
- Use `lookup_concept()` for concept resolution.
- Use the JSON-backed `*_in_json()` helpers in `graph_store.py` for CRUD-style graph mutations.

## Recommended Working Paths

### For Note Content Changes

1. Read `ReadMe.md` and the target note.
2. Read the relevant rule docs if the change affects node boundaries or edge semantics.
3. Edit the concept Markdown file in `math/*.md`.
4. Check neighboring notes named in `Include` and `Parents` for mirrored structural intent.
5. Run diff/import/validate commands before considering the change done.

Prefer Markdown-first edits for mathematical content. Use JSON-side mutation only when the task is explicitly about graph tooling, repair, or service-driven CRUD.

### For Graph Policy Changes

1. Read `math/rules/Math Concept Graph.md`.
2. Read the specific policy file being changed.
3. Check whether the policy change implies updates to note structure, validation logic, or skill guidance.
4. Validate the effect on representative concepts rather than changing many nodes blindly.

### For Tooling Changes

1. Read `math/scripts/ReadMe.md` before editing code.
2. Change the narrowest module that owns the behavior.
3. Update CLI wiring in `graph_cli.py` only if the command surface changes.
4. Update `service_app.py` only if the HTTP surface changes.
5. Keep documentation aligned with the actual maintained entry points.

### For Sync Or Data Integrity Bugs

Use this diagnosis order:

1. Inspect the target Markdown note.
2. Inspect `math/lib/math.json`.
3. Run diff or validate.
4. Inspect `markdown_import.py`, `markdown_export.py`, or `graph_validate_core.py` based on the failing stage.
5. Repair only after understanding whether Markdown or JSON is the intended source for the task at hand.

## Verification Path

Use concrete validation instead of assumptions.

Run the maintained CLI from `math/scripts/` and prefer paths relative to that working directory:

```powershell
cd math/scripts
python graph.py diff .. ..\lib\math.json --json
python graph.py import-markdown .. ..\lib\math.json --dry-run --json
python graph.py validate ..\lib\math.json --json
python graph.py lookup manifold --path ..\lib\math.json --field define --json
```

Use the local service only when HTTP behavior matters:

```powershell
python service_app.py --host 127.0.0.1 --port 5000
```

When uncertain:

- Verify whether a Markdown file is even part of import. `markdown_import.py` ignores `lib`, `rules`, `scripts`, hidden directories, `_tmp*`, and `ReadMe.md`.
- Verify whether a concept already exists before creating a new note.
- Verify whether a relation is already represented transitively before adding a new edge.
- Verify mirrored `parents` and `children` instead of assuming one side is authoritative.
- Verify service behavior from `service_app.py`, not from stale command examples.

## Safe Default Decisions

If the task is ambiguous, default to the smaller and safer change:

- Prefer editing an existing concept note over creating a new node.
- Prefer storing a theorem, method, invariant, or representation inside `Properties` over creating a new standalone note.
- Prefer direct parent relations over extra transitive links.
- Prefer dry-run, diff, and validate before apply/export/repair.
- Prefer marking missing information as `Pending` rather than inventing repository behavior.

## Pending Items

Treat these as unresolved repository facts until confirmed:

- Test strategy beyond CLI/service validation: `Pending`
- Python runtime/version policy for `math/scripts/`: `Pending`
- Whether `math/lib/math.json` or Markdown is intended as the human-approved source of truth for every maintenance workflow: `Pending`, but current repository guidance favors Markdown-first conceptual maintenance plus graph synchronization
