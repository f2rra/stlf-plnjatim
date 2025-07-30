import numpy as np
import pandas as pd
import pickle
import config

def load_stats(stats_path):
    """Memuat statistik (mean dan std) untuk normalisasi."""
    with open(stats_path, 'rb') as f:
        stats = pickle.load(f)
    return stats['mean'], stats['std']

def preprocess_input(raw_input: list, stats_path: str = config.STATS_PATH):
    """
    Melakukan pra-pemrosesan pada data input mentah.
    1. Mengubah ke DataFrame.
    2. Normalisasi menggunakan statistik data latih.
    3. Mengubah menjadi format numpy array yang siap untuk prediksi.
    """
    # Muat statistik normalisasi
    train_mean, train_std = load_stats(stats_path)

    # Ubah input (list) menjadi DataFrame
    df = pd.DataFrame(raw_input, columns=['Beban Listrik (MW)'])

    # Normalisasi data
    normalized_df = (df - train_mean) / train_std

    # Ubah menjadi format input untuk model [batch_size, timesteps, features]
    # batch_size = 1, timesteps = IN_STEPS, features = 1
    model_input = np.array(normalized_df).reshape(1, config.IN_STEPS, 1)

    return model_input

def postprocess_output(prediction: np.ndarray, stats_path: str = config.STATS_PATH):
    """
    Mengembalikan data prediksi ke skala aslinya (de-normalisasi).
    """
    # Muat statistik normalisasi
    train_mean, train_std = load_stats(stats_path)

    # De-normalisasi hasil prediksi
    # Ambil nilai mean dan std spesifik untuk 'Beban Listrik (MW)'
    mean_val = train_mean['Beban Listrik (MW)']
    std_val = train_std['Beban Listrik (MW)']

    original_scale_prediction = (prediction * std_val) + mean_val

    # Bulatkan ke 3 angka desimal seperti di notebook Anda
    return np.round(original_scale_prediction, 3).flatten().tolist()