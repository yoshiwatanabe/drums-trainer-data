#!/usr/bin/env python3
"""
Generate 8-beat drum roll patterns
Group I: Roll patterns (30 patterns)

Roll patterns using snare and toms in 8th note timing
Useful for practicing hand movement across drums even at slower tempo
"""

import json
from pathlib import Path

def create_roll_patterns():
    """Define 30 distinct roll patterns"""
    patterns = []
    
    # Category 1: Basic descending rolls (10 patterns)
    # Pattern 1: Full descending (snare -> high -> mid -> floor)
    patterns.append([
        {"time": 2.5, "note": "snare", "velocity": 100},
        {"time": 3.0, "note": "tom_high", "velocity": 100},
        {"time": 3.5, "note": "tom_mid", "velocity": 100},
        {"time": 3.5, "note": "tom_floor", "velocity": 100}  # Both at 3.5 for final hit
    ])
    
    # Pattern 2: Snare -> High -> Mid
    patterns.append([
        {"time": 2.5, "note": "snare", "velocity": 100},
        {"time": 3.0, "note": "tom_high", "velocity": 100},
        {"time": 3.5, "note": "tom_mid", "velocity": 100}
    ])
    
    # Pattern 3: Snare -> High -> Floor (skip mid)
    patterns.append([
        {"time": 2.5, "note": "snare", "velocity": 100},
        {"time": 3.0, "note": "tom_high", "velocity": 100},
        {"time": 3.5, "note": "tom_floor", "velocity": 100}
    ])
    
    # Pattern 4: Snare -> Mid -> Floor
    patterns.append([
        {"time": 2.5, "note": "snare", "velocity": 100},
        {"time": 3.0, "note": "tom_mid", "velocity": 100},
        {"time": 3.5, "note": "tom_floor", "velocity": 100}
    ])
    
    # Pattern 5: Extended - Snare, Snare, High, Mid, Floor
    patterns.append([
        {"time": 2.0, "note": "snare", "velocity": 100},
        {"time": 2.5, "note": "snare", "velocity": 95},
        {"time": 3.0, "note": "tom_high", "velocity": 100},
        {"time": 3.5, "note": "tom_mid", "velocity": 100}
    ])
    
    # Pattern 6: Double snare start
    patterns.append([
        {"time": 2.5, "note": "snare", "velocity": 100},
        {"time": 3.0, "note": "snare", "velocity": 95},
        {"time": 3.5, "note": "tom_high", "velocity": 100}
    ])
    
    # Pattern 7: Snare -> High, High -> Mid
    patterns.append([
        {"time": 2.0, "note": "snare", "velocity": 100},
        {"time": 2.5, "note": "tom_high", "velocity": 100},
        {"time": 3.0, "note": "tom_high", "velocity": 95},
        {"time": 3.5, "note": "tom_mid", "velocity": 100}
    ])
    
    # Pattern 8: Long roll - all four positions
    patterns.append([
        {"time": 1.5, "note": "snare", "velocity": 100},
        {"time": 2.0, "note": "tom_high", "velocity": 100},
        {"time": 2.5, "note": "tom_mid", "velocity": 100},
        {"time": 3.0, "note": "tom_floor", "velocity": 100},
        {"time": 3.5, "note": "tom_floor", "velocity": 105}
    ])
    
    # Pattern 9: Snare -> Floor direct
    patterns.append([
        {"time": 2.5, "note": "snare", "velocity": 100},
        {"time": 3.0, "note": "snare", "velocity": 95},
        {"time": 3.5, "note": "tom_floor", "velocity": 105}
    ])
    
    # Pattern 10: Triple tom ending
    patterns.append([
        {"time": 2.5, "note": "snare", "velocity": 100},
        {"time": 3.0, "note": "tom_high", "velocity": 100},
        {"time": 3.5, "note": "tom_mid", "velocity": 100},
        {"time": 3.5, "note": "tom_floor", "velocity": 100}
    ])
    
    # Category 2: Ascending rolls (5 patterns)
    # Pattern 11: Floor -> Mid -> High -> Snare
    patterns.append([
        {"time": 2.5, "note": "tom_floor", "velocity": 100},
        {"time": 3.0, "note": "tom_mid", "velocity": 100},
        {"time": 3.5, "note": "tom_high", "velocity": 100}
    ])
    
    # Pattern 12: Floor -> High -> Snare
    patterns.append([
        {"time": 2.5, "note": "tom_floor", "velocity": 100},
        {"time": 3.0, "note": "tom_high", "velocity": 100},
        {"time": 3.5, "note": "snare", "velocity": 100}
    ])
    
    # Pattern 13: Mid -> High -> Snare
    patterns.append([
        {"time": 2.5, "note": "tom_mid", "velocity": 100},
        {"time": 3.0, "note": "tom_high", "velocity": 100},
        {"time": 3.5, "note": "snare", "velocity": 100}
    ])
    
    # Pattern 14: Floor -> Mid -> High (no snare)
    patterns.append([
        {"time": 2.5, "note": "tom_floor", "velocity": 100},
        {"time": 3.0, "note": "tom_mid", "velocity": 100},
        {"time": 3.5, "note": "tom_high", "velocity": 100}
    ])
    
    # Pattern 15: Extended ascending
    patterns.append([
        {"time": 2.0, "note": "tom_floor", "velocity": 100},
        {"time": 2.5, "note": "tom_mid", "velocity": 100},
        {"time": 3.0, "note": "tom_high", "velocity": 100},
        {"time": 3.5, "note": "snare", "velocity": 100}
    ])
    
    # Category 3: Round-trip rolls (5 patterns)
    # Pattern 16: Snare -> Toms -> back to Snare
    patterns.append([
        {"time": 2.0, "note": "snare", "velocity": 100},
        {"time": 2.5, "note": "tom_high", "velocity": 100},
        {"time": 3.0, "note": "tom_mid", "velocity": 100},
        {"time": 3.5, "note": "snare", "velocity": 100}
    ])
    
    # Pattern 17: Down and up
    patterns.append([
        {"time": 2.0, "note": "tom_high", "velocity": 100},
        {"time": 2.5, "note": "tom_mid", "velocity": 100},
        {"time": 3.0, "note": "tom_floor", "velocity": 100},
        {"time": 3.5, "note": "tom_mid", "velocity": 100}
    ])
    
    # Pattern 18: V-shape
    patterns.append([
        {"time": 2.0, "note": "tom_high", "velocity": 100},
        {"time": 2.5, "note": "tom_floor", "velocity": 100},
        {"time": 3.0, "note": "tom_mid", "velocity": 100},
        {"time": 3.5, "note": "tom_high", "velocity": 100}
    ])
    
    # Pattern 19: Snare loop
    patterns.append([
        {"time": 2.0, "note": "snare", "velocity": 100},
        {"time": 2.5, "note": "tom_high", "velocity": 100},
        {"time": 3.0, "note": "tom_floor", "velocity": 100},
        {"time": 3.5, "note": "snare", "velocity": 105}
    ])
    
    # Pattern 20: Quick round trip
    patterns.append([
        {"time": 2.5, "note": "tom_mid", "velocity": 100},
        {"time": 3.0, "note": "tom_floor", "velocity": 100},
        {"time": 3.5, "note": "tom_high", "velocity": 100}
    ])
    
    # Category 4: Tom-to-tom movement patterns (10 patterns)
    # Pattern 21: High <-> Mid alternating
    patterns.append([
        {"time": 2.0, "note": "tom_high", "velocity": 100},
        {"time": 2.5, "note": "tom_mid", "velocity": 100},
        {"time": 3.0, "note": "tom_high", "velocity": 100},
        {"time": 3.5, "note": "tom_mid", "velocity": 100}
    ])
    
    # Pattern 22: Mid <-> Floor alternating
    patterns.append([
        {"time": 2.0, "note": "tom_mid", "velocity": 100},
        {"time": 2.5, "note": "tom_floor", "velocity": 100},
        {"time": 3.0, "note": "tom_mid", "velocity": 100},
        {"time": 3.5, "note": "tom_floor", "velocity": 100}
    ])
    
    # Pattern 23: High <-> Floor (skip mid)
    patterns.append([
        {"time": 2.0, "note": "tom_high", "velocity": 100},
        {"time": 2.5, "note": "tom_floor", "velocity": 100},
        {"time": 3.0, "note": "tom_high", "velocity": 100},
        {"time": 3.5, "note": "tom_floor", "velocity": 100}
    ])
    
    # Pattern 24: Double high, single mid
    patterns.append([
        {"time": 2.0, "note": "tom_high", "velocity": 100},
        {"time": 2.5, "note": "tom_high", "velocity": 95},
        {"time": 3.0, "note": "tom_mid", "velocity": 100},
        {"time": 3.5, "note": "tom_high", "velocity": 100}
    ])
    
    # Pattern 25: Triple toms pattern
    patterns.append([
        {"time": 2.0, "note": "tom_high", "velocity": 100},
        {"time": 2.5, "note": "tom_mid", "velocity": 100},
        {"time": 3.0, "note": "tom_floor", "velocity": 100},
        {"time": 3.5, "note": "tom_high", "velocity": 100}
    ])
    
    # Pattern 26: Floor focus
    patterns.append([
        {"time": 2.0, "note": "tom_floor", "velocity": 100},
        {"time": 2.5, "note": "tom_high", "velocity": 100},
        {"time": 3.0, "note": "tom_floor", "velocity": 100},
        {"time": 3.5, "note": "tom_floor", "velocity": 105}
    ])
    
    # Pattern 27: Cascading
    patterns.append([
        {"time": 1.5, "note": "tom_high", "velocity": 100},
        {"time": 2.0, "note": "tom_mid", "velocity": 100},
        {"time": 2.5, "note": "tom_floor", "velocity": 100},
        {"time": 3.0, "note": "tom_mid", "velocity": 100},
        {"time": 3.5, "note": "tom_high", "velocity": 100}
    ])
    
    # Pattern 28: Snare + tom combinations
    patterns.append([
        {"time": 2.0, "note": "snare", "velocity": 100},
        {"time": 2.5, "note": "tom_mid", "velocity": 100},
        {"time": 3.0, "note": "snare", "velocity": 100},
        {"time": 3.5, "note": "tom_floor", "velocity": 100}
    ])
    
    # Pattern 29: All drums touch
    patterns.append([
        {"time": 1.5, "note": "snare", "velocity": 100},
        {"time": 2.0, "note": "tom_high", "velocity": 100},
        {"time": 2.5, "note": "tom_mid", "velocity": 100},
        {"time": 3.0, "note": "tom_floor", "velocity": 100},
        {"time": 3.5, "note": "snare", "velocity": 105}
    ])
    
    # Pattern 30: Bouncing pattern
    patterns.append([
        {"time": 2.0, "note": "tom_high", "velocity": 100},
        {"time": 2.5, "note": "tom_floor", "velocity": 100},
        {"time": 3.0, "note": "tom_high", "velocity": 100},
        {"time": 3.5, "note": "tom_mid", "velocity": 100}
    ])
    
    return patterns

def create_basic_accompaniment():
    """Basic hihat and kick for context"""
    return [
        {"time": 0.0, "note": "hihat_closed", "velocity": 80},
        {"time": 0.0, "note": "kick", "velocity": 110},
        {"time": 0.5, "note": "hihat_closed", "velocity": 80},
        {"time": 1.0, "note": "hihat_closed", "velocity": 80},
        {"time": 1.0, "note": "snare", "velocity": 100},
        {"time": 1.5, "note": "hihat_closed", "velocity": 80},
        {"time": 2.0, "note": "hihat_closed", "velocity": 80},
        {"time": 2.0, "note": "kick", "velocity": 110},
        {"time": 2.5, "note": "hihat_closed", "velocity": 80},
        {"time": 3.0, "note": "hihat_closed", "velocity": 80},
        # No snare at 3.0 - replaced by roll
        {"time": 3.5, "note": "hihat_closed", "velocity": 80}
    ]

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

def generate_pattern(number, roll_events):
    """Generate a single pattern"""
    pattern_id = f"8beat_i_{number:03d}"

    events = []
    events.extend(create_basic_accompaniment())
    events.extend(roll_events)

    events.sort(key=lambda x: (x["time"], x["note"]))

    pattern = {
        "id": pattern_id,
        "name": f"8-Beat I #{number}",
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

    roll_patterns = create_roll_patterns()

    print("Generating Group I: Roll patterns...")
    for i in range(30):
        pattern = generate_pattern(i + 1, roll_patterns[i])
        filename = f"{pattern['id']}.json"
        filepath = patterns_dir / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(pattern, f, indent=2, ensure_ascii=False)
        if (i + 1) % 10 == 0:
            print(f"  Generated {i + 1}/30")

    print(f"\n✓ Generated 30 roll patterns (Group I)")
    print("  Categories: Descending (10), Ascending (5), Round-trip (5), Tom-to-tom (10)")
    print("  8th note timing - slower tempo for practicing hand movement patterns")
    print("\nDone!")

if __name__ == "__main__":
    main()
