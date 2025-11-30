# Drums Trainer - Pattern Data Repository

This repository contains drum practice pattern data for the [Drums Trainer](https://github.com/yoshiwatanabe/drums-trainer) web application.

## Structure

```
drums-trainer-data/
├── patterns/
│   ├── index.json       # Pattern manifest
│   ├── patt_001.json    # Syncopated HH Open Variation
│   ├── patt_002.json    # Basic Rock Beat
│   └── patt_003.json    # Ride Cymbal Groove
└── README.md
```

## Adding New Patterns

1. Create a new JSON file in `patterns/` folder (e.g., `patt_004.json`)
2. Add the filename to `patterns/index.json`
3. Commit and push to GitHub
4. GitHub Pages will serve the updated data automatically

## Pattern JSON Format

```json
{
  "id": "patt_xxx",
  "title": "Pattern Name",
  "tags": ["tag1", "tag2"],
  "time_signature": "4/4",
  "bpm_default": 70,
  "loop_length_beats": 4,
  "events": [
    { "time": 0, "note": "kick", "velocity": 100 }
  ],
  "notation": {
    "vexflow": {
      "staves": [...]
    }
  }
}
```

## GitHub Pages URL

Patterns are served at: `https://yoshiwatanabe.github.io/drums-trainer-data/patterns/`

## License

Same as parent project.
