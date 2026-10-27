
from pathlib import Path
import json
from music21 import converter, note, chord

DATA_DIR = Path("data")
OUTPUT_FILE = Path("note_sequences.json")

midi_files = list(DATA_DIR.glob("*.mid")) + list(DATA_DIR.glob("*.midi"))

all_sequences = []
successful_files = 0

for midi_file in midi_files:
    try:
        score = converter.parse(str(midi_file))
        pitches = []

        for element in score.flatten().notes:
            if isinstance(element, note.Note):
                pitches.append(element.pitch.midi)
            elif isinstance(element, chord.Chord):
                # Use each chord's individual pitches
                pitches.extend(pitch.midi for pitch in element.pitches)

        if len(pitches) >= 50:
            all_sequences.append(pitches)
            successful_files += 1
            print(f"Processed: {midi_file.name} ({len(pitches)} pitches)")

    except Exception as error:
        print(f"Skipped: {midi_file.name} — {error}")

with OUTPUT_FILE.open("w", encoding="utf-8") as file:
    json.dump(all_sequences, file)

total_pitches = sum(len(sequence) for sequence in all_sequences)

print("\nPreprocessing complete!")
print(f"Successfully processed files: {successful_files}")
print(f"Total pitch values: {total_pitches}")
print(f"Saved to: {OUTPUT_FILE}")
