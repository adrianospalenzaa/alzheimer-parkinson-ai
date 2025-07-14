import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

AUDIO_RAW = os.path.join(BASE_DIR, 'data', 'audio', 'raw')
AUDIO_SPECTRO = os.path.join(BASE_DIR, 'data', 'audio', 'spectrograms')
AUDIO_FEATURES = os.path.join(BASE_DIR, 'data', 'audio', 'features')
