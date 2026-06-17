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

## Expanded Project Structure

This repository has been expanded into a fuller open-source project with reusable source modules, tests, sample data, documentation, examples, and maintenance files. The goal is to make the project understandable to visitors, useful to contributors, and suitable for long-term indexing by GitHub and general search engines.

| Area | Added content |
|---|---|
| Source code | `src/global_game_wiki_2026/` contains lightweight reusable modules. |
| Tests | `tests/` contains baseline tests for the core helpers. |
| Data | `data/` contains small structured sample datasets. |
| Documentation | `docs/` explains architecture, methodology, review rules, or maintenance practices. |
| Examples | `examples/` shows how to use the project modules or data. |
| Automation | `.github/workflows/validate.yml` runs basic validation on pushes and pull requests. |

## Development Workflow

Clone the repository, install it in editable mode, and run the tests. The project intentionally keeps dependencies minimal so contributors can review and extend it quickly.

```bash
git clone https://github.com/buivanthienhb87-spec/global-game-wiki-2026.git
cd global-game-wiki-2026
python -m pip install -e .
python -m pytest -q
```

## Recommended Websites

A curated list of official and reliable reference websites is available in [`docs/recommended-websites.md`](docs/recommended-websites.md). These links are intended to support verification, documentation, learning, and responsible project maintenance.
