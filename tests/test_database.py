"""Unit tests for database helpers and model behavior."""

import pytest

from wordwall.database import WordResponse, connect_database


@pytest.mark.asyncio
async def test_connect_database_and_word_roundtrip(tmp_path) -> None:
    """A record can be inserted and retrieved from a temporary sqlite DB."""
    database_path = tmp_path / "nested" / "words"
    await connect_database(str(database_path), testing=True)

    assert (tmp_path / "nested").exists()

    created = WordResponse(wall_hash="wall123", player_id="player1", word="hello")
    await created.insert()

    records = await WordResponse.filter(wall_hash="wall123")

    assert len(records) == 1
    assert records[0].word == "hello"
    assert records[0].player_id == "player1"


@pytest.mark.asyncio
async def test_word_count_filtering_excludes_empty_words(tmp_path) -> None:
    """Count query using gt('word', '') should ignore empty values."""
    database_path = tmp_path / "counts" / "words"
    await connect_database(str(database_path), testing=True)

    await WordResponse(wall_hash="wallABC", player_id="p1", word="").insert()
    await WordResponse(wall_hash="wallABC", player_id="p2", word="idea").insert()
    await WordResponse(wall_hash="wallABC", player_id="p3", word="plan").insert()

    count = await WordResponse.filter(
        WordResponse.gt("word", ""),
        wall_hash="wallABC",
        count_rows=True,
    )

    assert count == 2


def test_wordresponse_primary_key_default_generates_unique_ids() -> None:
    """New model objects should get a non-empty UUID primary key by default."""
    first = WordResponse(wall_hash="w1", player_id="p1", word="one")
    second = WordResponse(wall_hash="w2", player_id="p2", word="two")

    assert first.id
    assert second.id
    assert first.id != second.id
