from __future__ import annotations

import json
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any


STANDARD_FIELDS = ("define", "parents", "children", "properties")


@dataclass
class ConceptMatch:
    key: str
    match_type: str
    score: float

    def to_dict(self) -> dict[str, object]:
        return {
            "key": self.key,
            "match_type": self.match_type,
            "score": self.score,
        }


def load_concepts(path: str | Path) -> dict[str, Any]:
    json_path = Path(path)
    if not json_path.exists():
        raise FileNotFoundError(f"JSON file not found: {json_path}")

    try:
        payload = json.loads(json_path.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Failed to parse JSON file: {json_path}") from exc

    if not isinstance(payload, dict):
        raise ValueError(f"Top-level JSON value must be an object: {json_path}")
    return payload


def get_standard_field(node: dict[str, Any], field: str) -> Any:
    default_map = {
        "define": "",
        "parents": {},
        "children": {},
        "properties": [],
    }
    value = node.get(field, default_map[field])
    if field in ("parents", "children") and not isinstance(value, dict):
        return {}
    if field == "properties" and not isinstance(value, list):
        return []
    if field == "define" and not isinstance(value, str):
        return ""
    return value


def render_relation_map(relations: dict[str, str]) -> list[str]:
    if not relations:
        return ["- <empty>"]
    return [f"- {key}: {label}" for key, label in sorted(relations.items())]


def select_fields(node: dict[str, Any], fields: list[str] | None) -> dict[str, Any]:
    if not fields or "all" in fields:
        names = STANDARD_FIELDS
    else:
        names = tuple(dict.fromkeys(fields))
    return {name: get_standard_field(node, name) for name in names}


def resolve_concept(
    term: str,
    concepts: dict[str, Any],
    *,
    max_matches: int = 5,
) -> tuple[ConceptMatch | None, list[ConceptMatch]]:
    if not concepts:
        return None, []

    normalized = term.strip().lower()
    if not normalized:
        return None, []

    scored: list[ConceptMatch] = []
    for key in concepts:
        key_lower = key.lower()
        words_lower = key.replace("_", " ").lower()
        if normalized == key_lower or normalized == words_lower:
            score = 1.0
            match_type = "exact"
        elif normalized in key_lower or normalized in words_lower:
            score = 0.95
            match_type = "substring"
        else:
            score = max(
                SequenceMatcher(None, normalized, key_lower).ratio(),
                SequenceMatcher(None, normalized, words_lower).ratio(),
            )
            match_type = "fuzzy"
        scored.append(ConceptMatch(key=key, match_type=match_type, score=score))

    scored.sort(key=lambda item: (-item.score, item.key))
    candidates = scored[:max_matches]
    if not candidates:
        return None, []

    best = candidates[0]
    if best.score < 0.4:
        return None, candidates
    return best, candidates
