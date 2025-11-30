#!/usr/bin/env python3
"""
Build index.json with group structure for lazy loading
"""

import json
from pathlib import Path
from collections import defaultdict

def main():
    patterns_dir = Path("patterns")
    
    # Read all pattern files
    pattern_files = sorted(patterns_dir.glob("*.json"))
    pattern_files = [f for f in pattern_files if f.name != "index.json"]
    
    # Group patterns
    groups = defaultdict(list)
    
    for filepath in pattern_files:
        filename = filepath.name
        
        # Determine group based on filename pattern
        if filename.startswith("8beat_a_"):
            groups["8beat-a"].append(filename)
        elif filename.startswith("8beat_b_"):
            groups["8beat-b"].append(filename)
        elif filename.startswith("8beat_c_"):
            groups["8beat-c"].append(filename)
        elif filename.startswith("patt_"):
            groups["misc"].append(filename)
        else:
            groups["other"].append(filename)
    
    # Build group metadata
    group_list = []
    
    if "8beat-a" in groups:
        group_list.append({
            "id": "8beat-a",
            "title": "8-Beat Group A (Basic)",
            "description": "Simple kick and snare combinations",
            "patterns": sorted(groups["8beat-a"])
        })
    
    if "8beat-b" in groups:
        group_list.append({
            "id": "8beat-b",
            "title": "8-Beat Group B (Syncopated)",
            "description": "Syncopation, anticipation, ghost notes",
            "patterns": sorted(groups["8beat-b"])
        })
    
    if "8beat-c" in groups:
        group_list.append({
            "id": "8beat-c",
            "title": "8-Beat Group C (Dense)",
            "description": "More kick drums (4-6 per bar)",
            "patterns": sorted(groups["8beat-c"])
        })
    
    if "misc" in groups:
        group_list.append({
            "id": "misc",
            "title": "Miscellaneous Patterns",
            "description": "Various practice patterns",
            "patterns": sorted(groups["misc"])
        })
    
    if "other" in groups:
        group_list.append({
            "id": "other",
            "title": "Other Patterns",
            "description": "Uncategorized patterns",
            "patterns": sorted(groups["other"])
        })
    
    # Create index structure
    index_data = {
        "version": "2.0",
        "groups": group_list
    }
    
    # Write index.json
    index_file = patterns_dir / "index.json"
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)
    
    # Print summary
    print("Index built successfully!")
    print(f"\nGroups:")
    for group in group_list:
        print(f"  {group['id']}: {len(group['patterns'])} patterns - {group['title']}")
    
    total_patterns = sum(len(g['patterns']) for g in group_list)
    print(f"\nTotal patterns: {total_patterns}")

if __name__ == "__main__":
    main()
