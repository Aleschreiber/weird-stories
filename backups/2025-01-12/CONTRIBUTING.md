
# Contributing to Weird Stories Project

## How to Contribute
1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Run tests (`python -m pytest tests/ -v`)
5. Commit your changes (`git commit -am 'Add new feature'`)
6. Push to the branch (`git push origin feature/your-feature`)
7. Create a Pull Request

## Data Contribution Guidelines
### Adding New Stories
- Use the established JSON format
- Include complete metadata
- Verify historical accuracy
- Add connections to existing stories
- Include sources

### JSON Format
```
{
  "id": "uniqueid",
  "title": {
    "original": "Story Title",
    "translated": null,
    "alternate": null
  },
  "author": {
    "name": "Author Name",
    "birthdeath": "YYYY-YYYY",
    "nationality": "Nationality"
  }
}
```

## Code Style
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions
- Comment complex logic

## Testing
- Add tests for new features
- Maintain test coverage
- Run full test suite before submitting PR