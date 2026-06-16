# Global Game Wiki 2026

Global Game Wiki 2026 is a structured documentation project for building a **maintainable game encyclopedia** with release timelines, platform information, genre classifications, source references, and multilingual page templates. The repository focuses on clean data organization and transparent citation practices.

The project is not an official database for any publisher. It is a community-maintained reference structure that can be expanded with verified information and clear editorial standards.

## Information Model

| Entity | Description |
|---|---|
| Game | A game title with release, platform, genre, and developer metadata. |
| Platform | A hardware, operating system, or storefront context. |
| Timeline | A chronological list of announcements, releases, and updates. |
| Reference | A source used to verify factual information. |
| Translation | A localized page derived from the same verified base record. |

## Repository Structure

| Path | Purpose |
|---|---|
| `data/games.json` | Example structured records. |
| `templates/game-entry.md` | Reusable game encyclopedia page template. |
| `docs/citation-policy.md` | Rules for citations and factual verification. |
| `docs/schema.md` | Suggested metadata fields. |
| `src/` | Optional scripts for validating or transforming records. |

## Citation Policy

Factual claims should be linked to official websites, publisher announcements, platform store pages, developer blogs, or reliable editorial sources. Unsourced claims should be treated as drafts until verified.

## Language Support

Multilingual pages are encouraged when they are reviewed by contributors who understand the target language. Machine translation may be used as a draft, but it should be clearly reviewed before publication.

## Roadmap

Planned improvements include a stricter JSON schema, automated link checking, a static index page, and sample pages for major genres and platforms.

## Contributing

Please contribute by improving records, adding citations, updating stale pages, or refining templates. Promotional copy, keyword stuffing, unsafe links, and unsupported claims are out of scope.

## License

This project is released under the MIT License.
