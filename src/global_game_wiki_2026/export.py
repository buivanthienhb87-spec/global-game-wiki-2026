from __future__ import annotations
import json
from pathlib import Path
from .records import GameRecord

def export_wiki(records: list[GameRecord], output_path: str) -> None:
    data = [{"title": r.title, "slug": r.slug, "platforms": list(r.platforms), "genres": list(r.genres), "references": list(r.references)} for r in records]
    Path(output_path).write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

def load_wiki(path: str) -> list[GameRecord]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return [GameRecord(item["title"], item["slug"], tuple(item.get("platforms", [])), tuple(item.get("genres", [])), tuple(item.get("references", []))) for item in data]
