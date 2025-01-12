import pytest
from src.validators.story_validator import StoryValidator
from pathlib import Path

@pytest.fixture
def validator():
    return StoryValidator()

def test_valid_story(validator):
    story_data = {
        "id": "test1",
        "title": {"original": "Test Story"},
        "author": {"name": "Test Author"},
        "publication": {"year": 1920},
        "mythos": {"entities": []},
        "connections": {"relatedstories": []},
        "metadata": {"verified": False}
    }
    is_valid, errors = validator.validate_story(story_data)
    assert is_valid
    assert len(errors) == 0

def test_invalid_story(validator):
    story_data = {
        "id": "test1",
        "title": "Invalid Title Format",  # Should be dict
        "author": {"name": "Test Author"},
        "publication": {"year": 2030},  # Future year
        "mythos": {"entities": []},
        "connections": {"relatedstories": []},
        "metadata": {"verified": False}
    }
    is_valid, errors = validator.validate_story(story_data)
    assert not is_valid
    assert len(errors) > 0
