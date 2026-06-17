from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class GameRecord:
    title: str
    slug: str
    platforms: tuple[str, ...] = field(default_factory=tuple)
    genres: tuple[str, ...] = field(default_factory=tuple)
    references: tuple[str, ...] = field(default_factory=tuple)

    def has_reference(self) -> bool:
        return bool(self.references)


def slugify(title: str) -> str:
    return "-".join(title.lower().strip().replace(":", "").split())
