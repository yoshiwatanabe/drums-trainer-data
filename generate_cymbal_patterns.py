#!/usr/bin/env python3
"""
Generate 30 cymbal practice patterns for Group I.
Crash and ride cymbals always play simultaneously with kick drum.
Includes variations: crash only, ride only, mixed, different kick patterns.
"""

import json
import os

def create_basic_accompaniment():
    """Create basic 8-beat hihat on all 8th notes + snare backbeat (beats 2, 4)"""
    events = []
    # Hihat on all 8th notes (closed)
    for i in range(8):
        events.append({
            "time": i * 0.5,
            "note": "hihat_closed",
            "velocity": 0.6
        })
    # Snare on beats 2 and 4
    events.append({"time": 1.0, "note": "snare", "velocity": 0.8})
    events.append({"time": 3.0, "note": "snare", "velocity": 0.8})
    return events

def create_vexflow_notation(all_events):
    """Generate VexFlow notation for complete pattern including hihat and snare"""
    # VexFlow note positions
    NOTE_POSITIONS = {
        'kick': 'f/4',
        'snare': 'c/5',
        'hihat_closed': 'g/5',
        'hihat_open': 'g/5',  # Same position, different symbol
        'crash': 'a/5',
        'ride': 'f/5',
        'tom_high': 'd/5',
        'tom_mid': 'b/4',
        'tom_floor': 'a/4'
    }
    
    # Group events by time
    events_by_time = {}
    for evt in all_events:
        time = evt["time"]
        if time not in events_by_time:
            events_by_time[time] = []
        events_by_time[time].append(evt["note"])
    
    # Generate notes for each 8th note position
    notes = []
    for i in range(8):  # 8 eighth notes in 4/4
        time = i * 0.5
        event_notes = events_by_time.get(time, [])
        
        if event_notes:
            keys = [NOTE_POSITIONS[note] for note in event_notes]
            # Remove duplicates and sort
            keys = sorted(list(set(keys)))
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
        "vexflow": {
            "staves": [
                {
                    "timeSignature": "4/4",
                    "voices": [
                        {
                            "clef": "percussion",
                            "notes": notes
                        }
                    ]
                }
            ]
        }
    }

def generate_pattern(number, kick_pattern, cymbal_type, description):
    """
    Generate a cymbal practice pattern.
    
    Args:
        number: Pattern number (1-30)
        kick_pattern: List of times for kick drum hits
        cymbal_type: "crash", "ride", or "mixed"
        description: Japanese description of the pattern
    """
    events = []
    
    # Add kick drum events
    kick_events = []
    for time in kick_pattern:
        kick_events.append({
            "time": time,
            "note": "kick",
            "velocity": 0.8
        })
    events.extend(kick_events)
    
    # Add cymbal events (always synchronized with kick)
    cymbal_events = []
    for time in kick_pattern:
        if cymbal_type == "crash":
            cymbal_events.append({
                "time": time,
                "note": "crash",
                "velocity": 0.9
            })
        elif cymbal_type == "ride":
            cymbal_events.append({
                "time": time,
                "note": "ride",
                "velocity": 0.7
            })
        elif cymbal_type == "mixed":
            # Alternate between crash and ride
            note = "crash" if (len(cymbal_events) % 2 == 0) else "ride"
            velocity = 0.9 if note == "crash" else 0.7
            cymbal_events.append({
                "time": time,
                "note": note,
                "velocity": velocity
            })
    events.extend(cymbal_events)
    
    # Add basic accompaniment (hihat + snare)
    events.extend(create_basic_accompaniment())
    
    # Sort by time
    events.sort(key=lambda e: (e["time"], e["note"]))
    
    # Generate VexFlow notation
    notation = create_vexflow_notation(events)
    
    pattern = {
        "name": f"8beat_i_{number:03d}",
        "description": description,
        "notation": notation,
        "events": events
    }
    
    return pattern

def main():
    patterns = []
    pattern_num = 1
    
    # Category 1: Crash only - Basic kick patterns (8 patterns)
    crash_kicks = [
        ([0.0, 2.0], "クラッシュ - 1拍目と3拍目"),
        ([0.0, 1.0, 2.0, 3.0], "クラッシュ - 全拍"),
        ([0.0], "クラッシュ - 1拍目のみ"),
        ([0.0, 0.5, 1.0, 1.5], "クラッシュ - 前半密集"),
        ([0.0, 1.5, 3.0], "クラッシュ - シンコペーション"),
        ([0.0, 2.5], "クラッシュ - 裏拍含む"),
        ([0.5, 2.5], "クラッシュ - 裏拍のみ"),
        ([0.0, 1.0, 2.5], "クラッシュ - 混合パターン"),
    ]
    
    for kicks, desc in crash_kicks:
        patterns.append(generate_pattern(pattern_num, kicks, "crash", desc))
        pattern_num += 1
    
    # Category 2: Ride only - Various kick patterns (8 patterns)
    ride_kicks = [
        ([0.0, 2.0], "ライド - 1拍目と3拍目"),
        ([0.0, 1.0, 2.0, 3.0], "ライド - 全拍"),
        ([0.0, 0.5, 2.0, 2.5], "ライド - 2回ずつ"),
        ([0.0, 1.5, 2.0, 3.5], "ライド - シンコペーション"),
        ([0.0, 2.5, 3.0], "ライド - 後半密集"),
        ([1.0, 3.0], "ライド - 2拍目と4拍目"),
        ([0.5, 1.5, 2.5, 3.5], "ライド - 全裏拍"),
        ([0.0, 1.0, 1.5, 3.0], "ライド - 不規則"),
    ]
    
    for kicks, desc in ride_kicks:
        patterns.append(generate_pattern(pattern_num, kicks, "ride", desc))
        pattern_num += 1
    
    # Category 3: Mixed (crash and ride alternating) - Complex patterns (8 patterns)
    mixed_kicks = [
        ([0.0, 1.0, 2.0, 3.0], "クラッシュ&ライド - 全拍交互"),
        ([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5], "クラッシュ&ライド - 全8分音符"),
        ([0.0, 1.0, 2.5], "クラッシュ&ライド - 混合A"),
        ([0.0, 1.5, 3.0], "クラッシュ&ライド - 混合B"),
        ([0.5, 1.5, 2.5, 3.5], "クラッシュ&ライド - 裏拍"),
        ([0.0, 0.5, 2.0, 2.5], "クラッシュ&ライド - 前後分割"),
        ([0.0, 1.0, 1.5, 2.0, 3.0, 3.5], "クラッシュ&ライド - 密集"),
        ([0.0, 2.0, 3.5], "クラッシュ&ライド - スパース"),
    ]
    
    for kicks, desc in mixed_kicks:
        patterns.append(generate_pattern(pattern_num, kicks, "mixed", desc))
        pattern_num += 1
    
    # Category 4: Advanced patterns (6 patterns)
    advanced = [
        ([0.0, 0.5, 1.0], "クラッシュ - 3連続", "crash"),
        ([2.0, 2.5, 3.0, 3.5], "ライド - 後半4連続", "ride"),
        ([0.0, 0.5, 1.5, 2.0, 2.5, 3.5], "クラッシュ&ライド - 複雑", "mixed"),
        ([1.0, 1.5, 2.0], "ライド - 中盤集中", "ride"),
        ([0.0, 1.0, 2.0, 2.5, 3.0], "クラッシュ - 5回", "crash"),
        ([0.5, 1.0, 2.0, 3.0, 3.5], "クラッシュ&ライド - 変則", "mixed"),
    ]
    
    for kicks, desc, cymbal_type in advanced:
        patterns.append(generate_pattern(pattern_num, kicks, cymbal_type, desc))
        pattern_num += 1
    
    # Save patterns to JSON files
    output_dir = "patterns"
    os.makedirs(output_dir, exist_ok=True)
    
    for i, pattern in enumerate(patterns, 1):
        filename = f"8beat_i_{i:03d}.json"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(pattern, f, indent=2, ensure_ascii=False)
        print(f"Generated {filename}")
    
    print(f"\nTotal: {len(patterns)} cymbal patterns generated")

if __name__ == "__main__":
    main()
