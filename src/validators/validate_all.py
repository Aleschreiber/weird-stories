from pathlib import Path
from src.validators.story_validator import StoryValidator
import json
import sys
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('validation.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

def validate_all_stories():
    validator = StoryValidator()
    stories_dir = Path("data/stories")
    all_valid = True
    story_connections = {}

    # Validate each story
    for story_file in stories_dir.glob("*.json"):
        logging.info(f"Validating {story_file.name}")
        
        try:
            with open(story_file, 'r') as f:
                story_data = json.load(f)
            
            is_valid, errors = validator.validate_story(story_data)
            
            if not is_valid:
                all_valid = False
                logging.error(f"Validation errors in {story_file.name}:")
                for error in errors:
                    logging.error(f"  - {error}")
            
            # Track connections
            story_connections[story_data['id']] = story_data['connections']['relatedstories']
                
        except Exception as e:
            all_valid = False
            logging.error(f"Error processing {story_file.name}: {str(e)}")
    
    return all_valid, story_connections

if __name__ == "__main__":
    logging.info("Starting validation of all stories")
    valid, connections = validate_all_stories()
    
    if valid:
        logging.info("All stories validated successfully")
    else:
        logging.error("Validation failed for some stories")
        sys.exit(1)
