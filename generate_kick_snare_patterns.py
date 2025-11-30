#!/usr/bin/env python3
"""
Generate 8-beat drum patterns with kick and snare only
Group H: Kick and Snare combinations (30 patterns)

Focus on exploring all meaningful kick/snare combinations in 8-beat context
"""

import json
from pathlib import Path

def create_basic_snare():
    """Snare on 2 and 4 (backbeat) - standard for most patterns"""
    return [
        {"time": 1.0, "note": "snare", "velocity": 100},
        {"time": 3.0, "note": "snare", "velocity": 100}
    ]

def create_kick_patterns():
    """Define 30 distinct kick patterns"""
    patterns = [
        # Basic patterns (1-5)
        [{"time": 0.0, "note": "kick", "velocity": 110}],  # Minimal
        [{"time": 0.0, "note": "kick", "velocity": 110}, {"time": 2.0, "note": "kick", "velocity": 110}],  # Basic rock
        [{"time": 0.0, "note": "kick", "velocity": 110}, {"time": 1.5, "note": "kick", "velocity": 105}, {"time": 2.0, "note": "kick", "velocity": 110}],  # Classic
        [{"time": 0.0, "note": "kick", "velocity": 110}, {"time": 2.0, "note": "kick", "velocity": 110}, {"time": 2.5, "note": "kick", "velocity": 105}],  # Driving
        [{"time": 0.0, "note": "kick", "velocity": 110}, {"time": 0.5, "note": "kick", "velocity": 105}, {"time": 2.0, "note": "kick", "velocity": 110}],  # Syncopated
        
        # Four-on-floor variations (6-8)
        [{"time": 0.0, "note": "kick", "velocity": 110}, {"time": 1.0, "note": "kick", "velocity": 110}, {"time": 2.0, "note": "kick", "velocity": 110}, {"time": 3.0, "note": "kick", "velocity": 110}],  # Four-on-floor
        [{"time": 0.0, "note": "kick", "velocity": 110}, {"time": 1.0, "note": "kick", "velocity": 105}, {"time": 2.0, "note": "kick", "velocity": 110}, {"time": 3.0, "note": "kick", "velocity": 105}],  # Four-on-floor light
        [{"time": 0.5, "note": "kick", "velocity": 110}, {"time": 1.5, "note": "kick", "velocity": 110}, {"time": 2.5, "note": "kick", "velocity": 110}, {"time": 3.5, "note": "kick", "velocity": 110}],  # Offbeat four
        
        # Syncopated patterns (9-15)
        [{"time": 0.0, "note": "kick", "velocity": 110}, {"time": 0.5, "note": "kick", "velocity": 105}, {"time": 2.0, "note": "kick", "velocity": 110}, {"time": 3.5, "note": "kick", "velocity": 105}],  # Sync 1
        [{"time": 0.0, "note": "kick", "velocity": 110}, {"time": 1.5, "note": "kick", "velocity": 105}, {"time": 2.5, "note": "kick", "velocity": 105}],  # Sync 2
        [{"time": 0.0, "note": "kick", "velocity": 110}, {"time": 0.5, "note": "kick", "velocity": 105}, {"time": 1.5, "note": "kick", "velocity": 105}, {"time": 2.0, "note": "kick", "velocity": 110}],  # Sync 3
        [{"time": 0.0, "note": "kick", "velocity": 110}, {"time": 2.0, "note": "kick", "velocity": 110}, {"time": 3.5, "note": "kick", "velocity": 105}],  # Sync 4
        [{"time": 0.0, "note": "kick", "velocity": 110}, {"time": 0.5, "note": "kick", "velocity": 105}, {"time": 2.5, "note": "kick", "velocity": 105}, {"time": 3.0, "note": "kick", "velocity": 110}],  # Sync 5
        [{"time": 0.5, "note": "kick", "velocity": 105}, {"time": 1.5, "note": "kick", "velocity": 105}, {"time": 2.0, "note": "kick", "velocity": 110}],  # Sync 6
        [{"time": 0.0, "note": "kick", "velocity": 110}, {"time": 1.5, "note": "kick", "velocity": 105}, {"time": 2.0, "note": "kick", "velocity": 110}, {"time": 3.5, "note": "kick", "velocity": 105}],  # Sync 7
        
        # Dense patterns (16-20)
        [{"time": 0.0, "note": "kick", "velocity": 110}, {"time": 0.5, "note": "kick", "velocity": 105}, {"time": 1.5, "note": "kick", "velocity": 105}, {"time": 2.0, "note": "kick", "velocity": 110}, {"time": 3.0, "note": "kick", "velocity": 110}],  # Dense 1
        [{"time": 0.0, "note": "kick", "velocity": 110}, {"time": 0.5, "note": "kick", "velocity": 105}, {"time": 2.0, "note": "kick", "velocity": 110}, {"time": 2.5, "note": "kick", "velocity": 105}, {"time": 3.5, "note": "kick", "velocity": 105}],  # Dense 2
        [{"time": 0.0, "note": "kick", "velocity": 110}, {"time": 1.0, "note": "kick", "velocity": 105}, {"time": 1.5, "note": "kick", "velocity": 105}, {"time": 2.0, "note": "kick", "velocity": 110}, {"time": 3.0, "note": "kick", "velocity": 110}],  # Dense 3
        [{"time": 0.0, "note": "kick", "velocity": 110}, {"time": 0.5, "note": "kick", "velocity": 105}, {"time": 1.0, "note": "kick", "velocity": 105}, {"time": 2.0, "note": "kick", "velocity": 110}, {"time": 2.5, "note": "kick", "velocity": 105}],  # Dense 4
        [{"time": 0.0, "note": "kick", "velocity": 110}, {"time": 1.5, "note": "kick", "velocity": 105}, {"time": 2.0, "note": "kick", "velocity": 110}, {"time": 2.5, "note": "kick", "velocity": 105}, {"time": 3.5, "note": "kick", "velocity": 105}],  # Dense 5
        
        # Sparse patterns (21-25)
        [{"time": 0.0, "note": "kick", "velocity": 110}, {"time": 2.5, "note": "kick", "velocity": 105}],  # Sparse 1
        [{"time": 0.0, "note": "kick", "velocity": 110}, {"time": 3.5, "note": "kick", "velocity": 105}],  # Sparse 2
        [{"time": 0.5, "note": "kick", "velocity": 105}, {"time": 2.0, "note": "kick", "velocity": 110}],  # Sparse 3
        [{"time": 1.5, "note": "kick", "velocity": 105}, {"time": 2.5, "note": "kick", "velocity": 105}],  # Sparse 4
        [{"time": 0.0, "note": "kick", "velocity": 110}, {"time": 1.5, "note": "kick", "velocity": 105}],  # Sparse 5
        
        # Double kick patterns (26-30)
        [{"time": 0.0, "note": "kick", "velocity": 110}, {"time": 0.5, "note": "kick", "velocity": 105}, {"time": 1.0, "note": "kick", "velocity": 105}, {"time": 2.0, "note": "kick", "velocity": 110}],  # Double 1
        [{"time": 0.0, "note": "kick", "velocity": 110}, {"time": 2.0, "note": "kick", "velocity": 110}, {"time": 2.5, "note": "kick", "velocity": 105}, {"time": 3.0, "note": "kick", "velocity": 105}],  # Double 2
        [{"time": 0.0, "note": "kick", "velocity": 110}, {"time": 0.5, "note": "kick", "velocity": 105}, {"time": 2.0, "note": "kick", "velocity": 110}, {"time": 3.0, "note": "kick", "velocity": 110}, {"time": 3.5, "note": "kick", "velocity": 105}],  # Double 3
        [{"time": 0.5, "note": "kick", "velocity": 105}, {"time": 1.0, "note": "kick", "velocity": 105}, {"time": 2.5, "note": "kick", "velocity": 105}, {"time": 3.0, "note": "kick", "velocity": 110}],  # Double 4
        [{"time": 0.0, "note": "kick", "velocity": 110}, {"time": 1.0, "note": "kick", "velocity": 105}, {"time": 2.0, "note": "kick", "velocity": 110}, {"time": 2.5, "note": "kick", "velocity": 105}, {"time": 3.0, "note": "kick", "velocity": 110}],  # Double 5
    ]
    
    return patterns

def create_vexflow_notation(events):
    """Create VexFlow notation for the pattern"""
    time_map = {}
    for evt in events:
        t = evt["time"]
        if t not in time_map:
            time_map[t] = []
        time_map[t].append(evt["note"])

    notes = []
    for i in range(8):
        t = i * 0.5
        instruments = time_map.get(t, [])

        keys = []
        if "kick" in instruments:
            keys.append("f/4")
        if "snare" in instruments:
            keys.append("c/5")

        if keys:
            notes.append({
                "keys": keys,
                "duration": "8"
            })
        else:
            notes.append({
                "keys": ["b/4"],
                "duration": "8r"
            })

    return {
        "staves": [{
            "timeSignature": "4/4",
            "voices": [{
                "clef": "percussion",
                "time": {"num_beats": 4, "beat_value": 4},
                "notes": notes
            }]
        }]
    }

def generate_pattern(number, kick_events):
    """Generate a single pattern"""
    pattern_id = f"8beat_h_{number:03d}"

    events = []
    events.extend(create_basic_snare())
    events.extend(kick_events)

    events.sort(key=lambda x: x["time"])

    pattern = {
        "id": pattern_id,
        "name": f"8-Beat H #{number}",
        "bpm": 70,
        "timeSignature": "4/4",
        "events": events,
        "notation": {
            "vexflow": create_vexflow_notation(events)
        }
    }

    return pattern

def main():
    script_dir = Path(__file__).parent
    patterns_dir = script_dir / "patterns"
    patterns_dir.mkdir(exist_ok=True)

    kick_patterns = create_kick_patterns()

    print("Generating Group H: Kick and Snare only patterns...")
    for i in range(30):
        pattern = generate_pattern(i + 1, kick_patterns[i])
        filename = f"{pattern['id']}.json"
        filepath = patterns_dir / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(pattern, f, indent=2, ensure_ascii=False)
        if (i + 1) % 10 == 0:
            print(f"  Generated {i + 1}/30")

    print(f"\n✓ Generated 30 kick and snare patterns (Group H)")
    print("  Covering basic, four-on-floor, syncopated, dense, sparse, and double kick variations")
    print("\nDone!")

if __name__ == "__main__":
    main()
