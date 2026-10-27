
import numpy as np
import tensorflow as tf
from pathlib import Path
from music21 import stream, note, tempo, meter, instrument

MODEL_PATH = Path("models/music_lstm.keras")
PITCH_PATH = Path("models/pitches.npy")
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

SEQUENCE_LENGTH = 50
NUM_NOTES_TO_GENERATE = 200
TEMPERATURE = 0.8

# Load the trained model and pitch vocabulary
model = tf.keras.models.load_model(MODEL_PATH)
pitches = np.load(PITCH_PATH)

# Start with a random sequence of valid pitch IDs
rng = np.random.default_rng()
current_sequence = rng.integers(
    0, len(pitches), size=SEQUENCE_LENGTH
).tolist()

generated_pitches = []

for _ in range(NUM_NOTES_TO_GENERATE):
    model_input = np.array([current_sequence], dtype=np.int32)
    probabilities = model.predict(model_input, verbose=0)[0]

    # Adjust the probability distribution using temperature
    probabilities = np.log(probabilities + 1e-8) / TEMPERATURE
    probabilities = np.exp(probabilities - np.max(probabilities))
    probabilities /= probabilities.sum()

    next_id = rng.choice(len(pitches), p=probabilities)
    generated_pitches.append(int(pitches[next_id]))

    current_sequence = current_sequence[1:] + [int(next_id)]

# Convert predicted pitches into a MIDI score
music = stream.Stream()
music.append(instrument.Piano())
music.append(tempo.MetronomeMark(number=100))
music.append(meter.TimeSignature("4/4"))

for pitch_value in generated_pitches:
    new_note = note.Note(pitch_value)
    new_note.quarterLength = 0.5
    music.append(new_note)

output_path = OUTPUT_DIR / "generated_music.mid"
music.write("midi", fp=str(output_path))

print("Music generation complete!")
print(f"Generated notes: {len(generated_pitches)}")
print(f"MIDI file saved to: {output_path.resolve()}")
