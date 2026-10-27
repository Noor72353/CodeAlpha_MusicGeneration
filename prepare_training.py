
import json
import numpy as np
from pathlib import Path

DATA_FILE = Path("note_sequences.json")
SEQUENCE_LENGTH = 50

with DATA_FILE.open("r", encoding="utf-8") as file:
    sequences = json.load(file)

# Build one shared pitch vocabulary from all pieces.
unique_pitches = sorted({
    pitch
    for sequence in sequences
    for pitch in sequence
})

pitch_to_int = {
    pitch: index
    for index, pitch in enumerate(unique_pitches)
}

X = []
y = []

# Create training examples separately for each piece.
for sequence in sequences:
    if len(sequence) <= SEQUENCE_LENGTH:
        continue

    encoded = [
        pitch_to_int[pitch]
        for pitch in sequence
    ]

    for start in range(len(encoded) - SEQUENCE_LENGTH):
        X.append(encoded[start:start + SEQUENCE_LENGTH])
        y.append(encoded[start + SEQUENCE_LENGTH])

X = np.array(X, dtype=np.int32)
y = np.array(y, dtype=np.int32)

np.savez_compressed(
    "training_data.npz",
    X=X,
    y=y,
    pitches=np.array(unique_pitches, dtype=np.int32),
)

print("Training data prepared successfully!")
print(f"Number of training examples: {len(X)}")
print(f"Unique pitches: {len(unique_pitches)}")
print(f"Input shape: {X.shape}")
print(f"Target shape: {y.shape}")
print("Saved to: training_data.npz")
