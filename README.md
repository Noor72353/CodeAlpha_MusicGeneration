
# AI Music Generation with LSTM

## Overview
This project uses a Long Short-Term Memory (LSTM) neural network to learn pitch patterns from MIDI music files and generate a new sequence of musical notes. It was developed as part of the CodeAlpha AI Internship tasks.

## Features
- Reads MIDI files using music21.
- Extracts and preprocesses musical pitch sequences.
- Encodes pitches into numerical values for training.
- Trains an LSTM model using TensorFlow and Keras.
- Generates a sequence of 200 notes.
- Saves generated music as a MIDI file.

## Technologies
- Python
- TensorFlow / Keras
- NumPy
- music21

## Dataset
The model was trained using 20 MIDI files selected from the MAESTRO dataset. The dataset files are not included in this repository. Download the dataset from the official [MAESTRO dataset page](https://magenta.tensorflow.org/datasets/maestro) and place MIDI files in the `data/` folder.

## Project Structure
```text
CodeAlpha_MusicGeneration/
├── data/                  # Input MIDI files (not included)
├── models/                # Trained model and pitch vocabulary
├── output/                # Generated MIDI music
├── check_data.py          # Checks MIDI files
├── preprocess.py          # Extracts pitch sequences
├── prepare_training.py    # Prepares model training data
├── train_model.py         # Trains the LSTM model
├── generate_music.py      # Generates new MIDI music
├── requirements.txt       # Python dependencies
└── README.md
```

## Setup

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run the Project

1. Put your MIDI files in the `data/` folder.
2. Check the MIDI files:

   ```bash
   python check_data.py
   ```

3. Extract pitch sequences:

   ```bash
   python preprocess.py
   ```

4. Prepare training data:

   ```bash
   python prepare_training.py
   ```

5. Train the model:

   ```bash
   python train_model.py
   ```

6. Generate music:

   ```bash
   python generate_music.py
   ```

The generated file will be saved as `output/generated_music.mid`. Open it in a MIDI-compatible music application to listen to the result.

## Model Notes
The model predicts pitch sequences based on patterns learned from the training data. The current implementation uses fixed note durations and is an educational baseline; musical quality may vary between generations.

## Author
Noorwali Khan
