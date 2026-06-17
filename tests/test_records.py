from global_game_wiki_2026.records import GameRecord, slugify


def test_slugify():
    assert slugify("Example Game: Deluxe Edition") == "example-game-deluxe-edition"


def test_record_reference_status():
    assert not GameRecord("Example", "example").has_reference()
    assert GameRecord("Example", "example", references=("https://example.com",)).has_reference()
