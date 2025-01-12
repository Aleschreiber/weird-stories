# Weird Stories Project

## Overview
A comprehensive database and analysis tool for weird fiction stories, focusing on the Lovecraft Mythos and related works. This project aims to create a structured dataset of weird fiction stories, their interconnections, and mythological elements.

## Project Structure
```
weird-stories/
├── data/           # Raw data files
│   ├── stories/    # Story JSON files
│   ├── authors/    # Author information
│   └── entities/   # Mythos entities data
├── src/            # Source code
│   ├── validators/ # Data validation tools
│   ├── utils/      # Utility functions
│   └── generators/ # Data generators
└── tests/          # Test suite
```

## Current Dataset
Currently includes the following H.P. Lovecraft stories:
- "Dagon" (1917)
- "Beyond the Wall of Sleep" (1919)
- "The Statement of Randolph Carter" (1919)
- "The Terrible Old Man" (1920)
- "Nyarlathotep" (1920)

## Installation
```
# Clone the repository
git clone https://github.com/yourusername/weird-stories.git

# Install dependencies
python -m pip install -r requirements.txt
```

## Usage
### Running Tests
```
python -m pytest tests/ -v
```

### Validating Stories
```
from src.validators.story_validator import StoryValidator
validator = StoryValidator()
```

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Version
Current version: 0.1.0