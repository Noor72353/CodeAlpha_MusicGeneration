
import numpy as np
import tensorflow as tf
from pathlib import Path

# Make results more reproducible
np.random.seed(42)
tf.random.set_seed(42)

DATA_FILE = Path("training_data.npz")
MODEL_DIR = Path("models")
MODEL_DIR.mkdir(exist_ok=True)

# Load prepared training data
data = np.load(DATA_FILE)
X = data["X"]
y = data["y"]
pitches = data["pitches"]

num_pitches = len(pitches)

# Build the LSTM model
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(X.shape[1],)),
    tf.keras.layers.Embedding(
        input_dim=num_pitches,
        output_dim=64,
    ),
    tf.keras.layers.LSTM(128),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(num_pitches, activation="softmax"),
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)

model.summary()

# Train and save the model
model.fit(
    X,
    y,
    epochs=10,
    batch_size=128,
    validation_split=0.1,
)

model.save(MODEL_DIR / "music_lstm.keras")
np.save(MODEL_DIR / "pitches.npy", pitches)

print("\nTraining complete!")
print("Model saved to: models/music_lstm.keras")
print("Pitch vocabulary saved to: models/pitches.npy")
