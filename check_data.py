
from pathlib import Path
from music21 import converter

# Folder containing the training MIDI files
DATA_DIR = Path("data")

# Find MIDI files
midi_files = list(DATA_DIR.glob("*.midi"))
midi_files += list(DATA_DIR.glob("*.mid"))

print(f"Found {len(midi_files)} MIDI files.")

# Test a few files
for file_path in midi_files[:5]:
    try:
        score = converter.parse(str(file_path))
        notes = score.flatten().notes
        print(f"OK: {file_path.name} — {len(notes)} notes/chords")
    except Exception as error:
        print(f"ERROR: {file_path.name} — {error}")
