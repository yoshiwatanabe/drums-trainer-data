#!/usr/bin/env python3
"""
Generate 8-beat drum patterns with open/closed hihat variations
Group D: Hihat Open/Close patterns (30 patterns)
"""

import json
import random
from pathlib import Path

def create_hihat_open_close_events():
    """Create hihat pattern with open and closed variations"""
    events = []
    
    # 8th note positions
    positions = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]
    
    # Randomly choose 1-2 positions for open hihat
    num_opens = random.randint(1, 2)
    open_positions = random.sample(positions, num_opens)
    
    for pos in positions:
        if pos in open_positions:
            events.append({
                "time": pos,
                "note": "hihat_open",
                "velocity": 75
            })
        else:
            events.append({
                "time": pos,
                "note": "hihat_closed",
                "velocity": 80
            })
    
    return events

def create_basic_snare_simple():
    """Simple snare on 2 and 4 (backbeat only)"""
    return [
        {"time": 1.0, "note": "snare", "velocity": 100},
        {"time": 3.0, "note": "snare", "velocity": 100}
    ]

def create_basic_kick_simple():
    """Simple kick patterns - 2-3 kicks per bar"""
    kick_events = []
    
    # Beat 1 is always there
    kick_events.append({"time": 0.0, "note": "kick", "velocity": 110})
    
    # Add 1-2 more kicks
    possible_positions = [0.5, 1.5, 2.0, 2.5, 3.0, 3.5]
    num_kicks = random.randint(1, 2)
    positions = random.sample(possible_positions, num_kicks)
    
    for pos in positions:
        kick_events.append({"time": pos, "note": "kick", "velocity": 110})
    
    return kick_events

def create_vexflow_notation(events):
    """Create VexFlow notation for the pattern"""
    # Group events by time
    time_map = {}
    for evt in events:
        t = evt["time"]
        if t not in time_map:
            time_map[t] = []
        time_map[t].append(evt["note"])
    
    # Use 8th notes (8 notes per bar)
    notes = []
    for i in range(8):
        t = i * 0.5
        instruments = time_map.get(t, [])
        
        keys = []
        if "kick" in instruments:
            keys.append("f/4")
        if "snare" in instruments:
            keys.append("c/5")
        if "hihat_open" in instruments:
            keys.append("g/5")  # Open hihat - VexFlow will show it
        elif "hihat_closed" in instruments:
            keys.append("g/5")
        
        if keys:
            notes.append({
                "keys": keys,
                "duration": "8"
            })
        else:
            # Rest
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

def generate_pattern(group, number):
    """Generate a single pattern"""
    pattern_id = f"8beat_{group}_{number:03d}"
    
    # Combine events
    events = []
    events.extend(create_hihat_open_close_events())
    events.extend(create_basic_snare_simple())
    events.extend(create_basic_kick_simple())
    
    # Sort by time
    events.sort(key=lambda x: x["time"])
    
    # Create pattern object
    pattern = {
        "id": pattern_id,
        "name": f"8-Beat D #{number}",
        "bpm": 70,
        "timeSignature": "4/4",
        "events": events,
        "notation": {
            "vexflow": create_vexflow_notation(events)
        }
    }
    
    return pattern

def main():
    # Setup
    script_dir = Path(__file__).parent
    patterns_dir = script_dir / "patterns"
    patterns_dir.mkdir(exist_ok=True)
    
    all_patterns = []
    
    # Group D: Hihat Open/Close (30 patterns)
    print("Generating Group D: Hihat Open/Close...")
    for i in range(1, 31):
        pattern = generate_pattern("d", i)
        filename = f"{pattern["id"]}.json"
        filepath = patterns_dir / filename
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(pattern, f, indent=2, ensure_ascii=False)
        all_patterns.append(filename)
        if i % 10 == 0:
            print(f"  Generated {i}/30")
    
    print(f"\n Generated {len(all_patterns)} new patterns")
    print("\nDone!")

if __name__ == "__main__":
    main()

