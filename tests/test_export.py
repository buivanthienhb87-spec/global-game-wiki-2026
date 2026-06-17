from global_game_wiki_2026.records import GameRecord
from global_game_wiki_2026.export import export_wiki, load_wiki
import tempfile, os

def test_roundtrip():
    records = [GameRecord("Test Game", "test-game", ("PC",), ("Action",), ("https://example.com",))]
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        export_wiki(records, f.name)
        path = f.name
    loaded = load_wiki(path)
    os.unlink(path)
    assert loaded[0].title == "Test Game"
