import json
from pathlib import Path

for game in json.loads(Path('data/games.json').read_text(encoding='utf-8')):
    print(f"{game['title']} -> {', '.join(game['platforms'])}")
