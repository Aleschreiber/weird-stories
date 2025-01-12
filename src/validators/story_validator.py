import json
from datetime import datetime
from pathlib import Path

class StoryValidator:
    def __init__(self):
        self.required_fields = {
            'id': str,
            'title': dict,
            'author': dict,
            'publication': dict,
            'mythos': dict,
            'connections': dict,
            'metadata': dict
        }

    def validate_story(self, story_data: dict) -> tuple[bool, list]:
        errors = []
        
        # Check required fields
        for field, field_type in self.required_fields.items():
            if field not in story_data:
                errors.append(f"Missing required field: {field}")
            elif not isinstance(story_data[field], field_type):
                errors.append(f"Invalid type for {field}")
        
        # Validate publication year
        if 'publication' in story_data:
            try:
                year = int(story_data['publication']['year'])
                if year < 1800 or year > datetime.now().year:
                    errors.append(f"Invalid publication year: {year}")
            except (ValueError, KeyError):
                errors.append("Invalid or missing publication year")

        return len(errors) == 0, errors

    def validate_file(self, file_path: Path) -> tuple[bool, list]:
        try:
            with open(file_path, 'r') as f:
                story_data = json.load(f)
            return self.validate_story(story_data)
        except json.JSONDecodeError:
            return False, ["Invalid JSON format"]
        except Exception as e:
            return False, [f"Error reading file: {str(e)}"]
