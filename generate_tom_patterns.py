#!/usr/bin/env python3
"""
Generate 8-beat drum patterns with tom variations
Group E: Single Tom patterns (25 patterns)
Group F: Two Toms patterns (25 patterns)
Group G: Three Toms patterns (20 patterns)
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
    """Snare on 2 and 4 (backbeat)"""
    return [
        {"time": 1.0, "note": "snare", "velocity": 100},
        {"time": 3.0, "note": "snare", "velocity": 100}
    ]

def create_varied_kick():
    """Various kick patterns with different densities"""
    pattern_type = random.randint(1, 5)
    
    if pattern_type == 1:
        # Basic rock beat
        return [
            {"time": 0.0, "note": "kick", "velocity": 110},
            {"time": 2.0, "note": "kick", "velocity": 110}
        ]
    elif pattern_type == 2:
        # Four on the floor
        return [
            {"time": 0.0, "note": "kick", "velocity": 110},
            {"time": 1.0, "note": "kick", "velocity": 110},
            {"time": 2.0, "note": "kick", "velocity": 110},
            {"time": 3.0, "note": "kick", "velocity": 110}
        ]
    elif pattern_type == 3:
        # Syncopated
        return [
            {"time": 0.0, "note": "kick", "velocity": 110},
            {"time": 0.5, "note": "kick", "velocity": 105},
            {"time": 2.0, "note": "kick", "velocity": 110},
            {"time": 3.5, "note": "kick", "velocity": 105}
        ]
    elif pattern_type == 4:
        # Sparse
        return [
            {"time": 0.0, "note": "kick", "velocity": 110},
            {"time": 1.5, "note": "kick", "velocity": 105},
            {"time": 2.5, "note": "kick", "velocity": 110}
        ]
    else:
        # Dense
        return [
            {"time": 0.0, "note": "kick", "velocity": 110},
            {"time": 0.5, "note": "kick", "velocity": 105},
            {"time": 1.5, "note": "kick", "velocity": 105},
            {"time": 2.0, "note": "kick", "velocity": 110},
            {"time": 3.0, "note": "kick", "velocity": 110}
        ]

def create_single_tom_fill():
    """Tom fill using only high tom - 1 to 3 hits"""
    tom_events = []
    num_hits = random.randint(1, 3)
    
    # Possible positions (avoid conflict with snare at 1.0 and 3.0)
    positions = [0.5, 1.5, 2.0, 2.5, 3.5]
    selected = random.sample(positions, num_hits)
    
    for pos in selected:
        tom_events.append({
            "time": pos,
            "note": "tom_high",
            "velocity": random.choice([95, 100, 105])
        })
    
    return tom_events

def create_two_tom_fill():
    """Tom fill using high and mid tom - 2 to 4 hits total"""
    tom_events = []
    num_hits = random.randint(2, 4)
    
    positions = [0.5, 1.5, 2.0, 2.5, 3.5]
    selected = random.sample(positions, num_hits)
    
    for i, pos in enumerate(sorted(selected)):
        # Alternate or create descending patterns
        if random.random() < 0.5:
            tom_type = "tom_high" if i % 2 == 0 else "tom_mid"
        else:
            # Descending pattern
            tom_type = "tom_high" if i < num_hits // 2 else "tom_mid"
        
        tom_events.append({
            "time": pos,
            "note": tom_type,
            "velocity": random.choice([95, 100, 105])
        })
    
    return tom_events

def create_three_tom_fill():
    """Tom fill using all three toms - 3 to 5 hits total"""
    tom_events = []
    num_hits = random.randint(3, 5)
    
    positions = [0.5, 1.5, 2.0, 2.5, 3.0, 3.5]
    selected = random.sample(positions, num_hits)
    
    toms = ["tom_high", "tom_mid", "tom_floor"]
    
    for i, pos in enumerate(sorted(selected)):
        if random.random() < 0.7:
            # Descending pattern (most common)
            tom_idx = min(i, 2)
            tom_type = toms[tom_idx]
        else:
            # Random
            tom_type = random.choice(toms)
        
        tom_events.append({
            "time": pos,
            "note": tom_type,
            "velocity": random.choice([95, 100, 105, 110])
        })
    
    return tom_events

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
        if "tom_high" in instruments:
            keys.append("d/5")
        if "tom_mid" in instruments:
            keys.append("b/4")
        if "tom_floor" in instruments:
            keys.append("a/4")
        if "hihat_closed" in instruments:
            keys.append("g/5")
        
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

def generate_pattern(group, number, tom_fill_func):
    """Generate a single pattern"""
    pattern_id = f"8beat_{group}_{number:03d}"
    
    events = []
    events.extend(create_hihat_events())
    events.extend(create_basic_snare())
    events.extend(create_varied_kick())
    events.extend(tom_fill_func())
    
    events.sort(key=lambda x: x["time"])
    
    pattern = {
        "id": pattern_id,
        "name": f"8-Beat {group.upper()} #{number}",
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
    
    # Group E: Single Tom (25 patterns)
    print("Generating Group E: Single Tom...")
    for i in range(1, 26):
        pattern = generate_pattern("e", i, create_single_tom_fill)
        filename = f"{pattern['id']}.json"
        filepath = patterns_dir / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(pattern, f, indent=2, ensure_ascii=False)
        if i % 10 == 0:
            print(f"  Generated {i}/25")
    
    # Group F: Two Toms (25 patterns)
    print("Generating Group F: Two Toms...")
    for i in range(1, 26):
        pattern = generate_pattern("f", i, create_two_tom_fill)
        filename = f"{pattern['id']}.json"
        filepath = patterns_dir / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(pattern, f, indent=2, ensure_ascii=False)
        if i % 10 == 0:
            print(f"  Generated {i}/25")
    
    # Group G: Three Toms (20 patterns)
    print("Generating Group G: Three Toms...")
    for i in range(1, 21):
        pattern = generate_pattern("g", i, create_three_tom_fill)
        filename = f"{pattern['id']}.json"
        filepath = patterns_dir / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(pattern, f, indent=2, ensure_ascii=False)
        if i % 10 == 0:
            print(f"  Generated {i}/20")
    
    print(f"\n Generated 70 tom patterns (E: 25, F: 25, G: 20)")
    print("\nDone!")

if __name__ == "__main__":
    main()
