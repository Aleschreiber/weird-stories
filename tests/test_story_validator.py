import pytest
from src.validators.story_validator import StoryValidator
from pathlib import Path
import os

@pytest.fixture
def validator():
    return StoryValidator()

def test_validator_initialization(validator):
    """Test that validator is properly initialized"""
    assert isinstance(validator, StoryValidator)
    assert hasattr(validator, 'validate_story')
    assert hasattr(validator, 'validate_file')

def test_valid_story(validator):
    """Test validation of a correctly formatted story"""
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
    assert is_valid, f"Story should be valid but got errors: {errors}"
    assert len(errors) == 0

def test_invalid_story(validator):
    """Test validation of an incorrectly formatted story"""
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
    assert not is_valid, "Story should be invalid"
    assert len(errors) > 0
    assert any("Invalid type for title" in error for error in errors)

def test_missing_required_fields(validator):
    """Test validation of story with missing fields"""
    story_data = {
        "id": "test1",
        "title": {"original": "Test Story"}
        # Missing other required fields
    }
    is_valid, errors = validator.validate_story(story_data)
    assert not is_valid
    assert len(errors) > 0

@pytest.mark.skipif(not os.path.exists("data/stories"), 
                   reason="Stories directory not found")
def test_actual_story_files(validator):
    """Test validation of actual story files in the data directory"""
    stories_dir = Path("data/stories")
    json_files = list(stories_dir.glob("*.json"))
    assert len(json_files) > 0, "No JSON files found in data/stories"
    
    for story_file in json_files:
        is_valid, errors = validator.validate_file(story_file)
        assert is_valid, f"File {story_file} has errors: {errors}"