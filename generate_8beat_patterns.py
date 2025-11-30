#!/usr/bin/env python3
"""
Generate 8-beat drum patterns with kick/snare/hihat variations
Groups:
- Group A: Basic 8-beat (50 patterns) - Simple combinations
- Group B: Syncopated 8-beat (50 patterns) - Syncopation emphasis
- Group C: Dense 8-beat (50 patterns) - More kick drums
"""

import json
import random
from pathlib import Path

def create_hihat_events():
    """Create standard 8th note hihat pattern"""
    events = []
    for i in range(8):
        events.append({
            "time": i * 0.5,
            "note": "hihat_closed",
            "velocity": 80
        })
    return events

def create_basic_snare():
    """Snare on 2 and 4 (backbeat), with 0-1 additional hits"""
    snare_events = []
    # Backbeat (positions 3 and 7 in 8th notes = beats 2 and 4)
    snare_events.append({"time": 1.0, "note": "snare", "velocity": 100})
    snare_events.append({"time": 3.0, "note": "snare", "velocity": 100})
    
    # Optional: add one extra snare
    if random.random() < 0.3:
        extra_positions = [0.5, 1.5, 2.0, 2.5, 3.5]
        pos = random.choice(extra_positions)
        snare_events.append({"time": pos, "note": "snare", "velocity": 90})
    
    return snare_events

def create_syncopated_snare():
    """Snare with syncopation - displaced or anticipated beats"""
    snare_events = []
    
    # Sometimes anticipate beat 2 or 4
    if random.random() < 0.5:
        # Anticipate beat 2 (move slightly earlier)
        snare_events.append({"time": 0.875, "note": "snare", "velocity": 95})
    else:
        snare_events.append({"time": 1.0, "note": "snare", "velocity": 100})
    
    if random.random() < 0.5:
        # Anticipate beat 4
        snare_events.append({"time": 2.875, "note": "snare", "velocity": 95})
    else:
        snare_events.append({"time": 3.0, "note": "snare", "velocity": 100})
    
    # Add 1-2 ghost notes or extra hits
    extra_count = random.randint(1, 2)
    extra_positions = [0.5, 1.5, 2.0, 2.5, 3.5]
    random.shuffle(extra_positions)
    for i in range(extra_count):
        pos = extra_positions[i]
        vel = random.choice([50, 60, 90])  # ghost notes or accents
        snare_events.append({"time": pos, "note": "snare", "velocity": vel})
    
    return snare_events

def create_basic_kick():
    """Simple kick patterns - 2-4 kicks per bar"""
    kick_events = []
    
    # Beat 1 is almost always there
    if random.random() < 0.9:
        kick_events.append({"time": 0.0, "note": "kick", "velocity": 110})
    
    # Add 1-3 more kicks at various positions
    possible_positions = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]
    num_kicks = random.randint(1, 3)
    positions = random.sample(possible_positions, num_kicks)
    
    for pos in positions:
        kick_events.append({"time": pos, "note": "kick", "velocity": 110})
    
    return kick_events

def create_syncopated_kick():
    """Syncopated kick with offbeat emphasis"""
    kick_events = []
    
    # Sometimes skip beat 1
    if random.random() < 0.7:
        kick_events.append({"time": 0.0, "note": "kick", "velocity": 110})
    
    # Focus on offbeats and syncopation
    offbeat_positions = [0.5, 1.5, 2.5, 3.5]
    onbeat_positions = [1.0, 2.0, 3.0]
    
    # Pick 2-3 offbeats
    num_offbeats = random.randint(2, 3)
    selected = random.sample(offbeat_positions, num_offbeats)
    
    # Maybe add 1 onbeat
    if random.random() < 0.5:
        selected.append(random.choice(onbeat_positions))
    
    for pos in selected:
        kick_events.append({"time": pos, "note": "kick", "velocity": 110})
    
    return kick_events

def create_dense_kick():
    """More kicks - 4-6 per bar"""
    kick_events = []
    
    # Beat 1 is always there
    kick_events.append({"time": 0.0, "note": "kick", "velocity": 110})
    
    # Add 3-5 more kicks
    possible_positions = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]
    num_kicks = random.randint(3, 5)
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
    
    # Create VexFlow notes for 8th notes
    notes = []
    for i in range(8):
        t = i * 0.5
        instruments = time_map.get(t, [])
        
        keys = []
        if "kick" in instruments:
            keys.append("f/4")
        if "snare" in instruments:
            keys.append("c/5")
        if "hihat_closed" in instruments:
            keys.append("g/5")
        
        if not keys:
            # Rest
            notes.append({"type": "rest", "duration": "8"})
        else:
            notes.append({
                "type": "note",
                "duration": "8",
                "keys": keys
            })
    
    return {
        "staves": [{
            "clef": "percussion",
            "time_signature": "4/4"
        }],
        "voices": [{
            "time": {"num_beats": 4, "beat_value": 4},
            "notes": notes
        }]
    }

def generate_pattern(group, index, snare_func, kick_func):
    """Generate a single pattern"""
    pattern_id = f"8beat_{group}_{index:03d}"
    
    # Combine all events
    events = []
    events.extend(create_hihat_events())
    events.extend(snare_func())
    events.extend(kick_func())
    
    # Sort by time
    events.sort(key=lambda x: x["time"])
    
    # Create pattern object
    pattern = {
        "id": pattern_id,
        "title": f"8-Beat {group.upper()} #{index}",
        "tags": ["8-beat", f"group-{group}"],
        "time_signature": "4/4",
        "bpm_default": 70,
        "loop_length_beats": 4,
        "events": events,
        "notation": {
            "vexflow": create_vexflow_notation(events)
        }
    }
    
    return pattern

def main():
    patterns_dir = Path("patterns")
    patterns_dir.mkdir(exist_ok=True)
    
    all_patterns = []
    
    # Group A: Basic 8-beat (50 patterns)
    print("Generating Group A: Basic 8-beat...")
    for i in range(1, 51):
        pattern = generate_pattern("a", i, create_basic_snare, create_basic_kick)
        filename = f"{pattern['id']}.json"
        filepath = patterns_dir / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(pattern, f, indent=2, ensure_ascii=False)
        all_patterns.append(filename)
        if i % 10 == 0:
            print(f"  Generated {i}/50")
    
    # Group B: Syncopated 8-beat (50 patterns)
    print("Generating Group B: Syncopated 8-beat...")
    for i in range(1, 51):
        pattern = generate_pattern("b", i, create_syncopated_snare, create_syncopated_kick)
        filename = f"{pattern['id']}.json"
        filepath = patterns_dir / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(pattern, f, indent=2, ensure_ascii=False)
        all_patterns.append(filename)
        if i % 10 == 0:
            print(f"  Generated {i}/50")
    
    # Group C: Dense 8-beat (50 patterns)
    print("Generating Group C: Dense 8-beat...")
    for i in range(1, 51):
        pattern = generate_pattern("c", i, create_basic_snare, create_dense_kick)
        filename = f"{pattern['id']}.json"
        filepath = patterns_dir / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(pattern, f, indent=2, ensure_ascii=False)
        all_patterns.append(filename)
        if i % 10 == 0:
            print(f"  Generated {i}/50")
    
    # Update index.json
    print("\nUpdating index.json...")
    
    # Read existing patterns
    index_file = patterns_dir / "index.json"
    if index_file.exists():
        with open(index_file, 'r', encoding='utf-8') as f:
            index_data = json.load(f)
            existing_patterns = index_data.get("patterns", [])
    else:
        existing_patterns = []
    
    # Add new patterns (avoid duplicates)
    for pattern in all_patterns:
        if pattern not in existing_patterns:
            existing_patterns.append(pattern)
    
    # Sort patterns
    existing_patterns.sort()
    
    # Write index
    index_data = {"patterns": existing_patterns}
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ Generated {len(all_patterns)} new patterns")
    print(f"✓ Total patterns in index: {len(existing_patterns)}")
    print("\nDone!")

if __name__ == "__main__":
    main()
