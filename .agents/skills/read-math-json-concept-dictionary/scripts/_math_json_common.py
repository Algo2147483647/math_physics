from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any


STANDARD_FIELDS = ("define", "parents", "children", "properties")
REPO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_MATH_JSON_PATH = REPO_ROOT / "math" / "lib" / "math.json"


@dataclass(frozen=True)
class ConceptMatch:
    key: str
    score: float
    match_type: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["score"] = round(self.score, 4)
        return data


def load_concepts(path: Path | None = None) -> dict[str, dict[str, Any]]:
    json_path = Path(path) if path else DEFAULT_MATH_JSON_PATH
    return json.loads(json_path.read_text(encoding="utf-8-sig"))


def normalize_term(text: str) -> str:
    cleaned = re.sub(r"[_\-]+", " ", text.strip().casefold())
    cleaned = re.sub(r"[^\w\s]", " ", cleaned)
    return re.sub(r"\s+", " ", cleaned).strip()


def rank_concepts(
    query: str,
    concepts: dict[str, dict[str, Any]],
    *,
    max_matches: int = 5,
) -> list[ConceptMatch]:
    if not query.strip():
        return []

    keys = list(concepts.keys())
    lowered = {key.casefold(): key for key in keys}
    normalized = {normalize_term(key): key for key in keys}

    if query in concepts:
        return [ConceptMatch(query, 1.0, "exact")]

    lowered_query = query.casefold()
    if lowered_query in lowered:
        return [ConceptMatch(lowered[lowered_query], 1.0, "case_insensitive_exact")]

    normalized_query = normalize_term(query)
    if normalized_query in normalized:
        return [ConceptMatch(normalized[normalized_query], 1.0, "normalized_exact")]

    ranked: list[ConceptMatch] = []
    for key in keys:
        normalized_key = normalize_term(key)
        score = SequenceMatcher(None, normalized_query, normalized_key).ratio()
        if normalized_key.startswith(normalized_query):
            score += 0.15
        elif normalized_query and normalized_query in normalized_key:
            score += 0.08
        if key.casefold().startswith(lowered_query):
            score += 0.05
        ranked.append(ConceptMatch(key, min(score, 0.999), "fuzzy"))

    ranked.sort(key=lambda match: (-match.score, match.key))
    return ranked[:max_matches]


def resolve_concept(
    query: str,
    concepts: dict[str, dict[str, Any]],
    *,
    cutoff: float = 0.55,
    max_matches: int = 5,
) -> tuple[ConceptMatch | None, list[ConceptMatch]]:
    matches = rank_concepts(query, concepts, max_matches=max_matches)
    if not matches:
        return None, []

    best = matches[0]
    if best.match_type == "fuzzy" and best.score < cutoff:
        return None, matches
    return best, matches


def render_relation_map(relations: dict[str, str]) -> list[str]:
    if not relations:
        return ["- <empty>"]
    return [f"- {target} ({label})" for target, label in sorted(relations.items())]


def get_standard_field(node: dict[str, Any], field: str) -> Any:
    if field == "define":
        value = node.get("define", "")
        return value if isinstance(value, str) else ""
    if field in ("parents", "children"):
        value = node.get(field, {})
        return value if isinstance(value, dict) else {}
    if field == "properties":
        value = node.get("properties", [])
        return value if isinstance(value, list) else []
    raise KeyError(field)


def select_fields(node: dict[str, Any], fields: list[str] | None) -> dict[str, Any]:
    selected = STANDARD_FIELDS if not fields or "all" in fields else fields
    return {field: get_standard_field(node, field) for field in selected}


def iter_edges(
    concepts: dict[str, dict[str, Any]],
    *,
    fields: tuple[str, ...] = ("parents", "children"),
):
    for source, node in concepts.items():
        for field in fields:
            for target, label in get_standard_field(node, field).items():
                yield source, field, target, label
