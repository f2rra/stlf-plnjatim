# --- Konfigurasi Model ---
MODEL_PATH = "/app/../model/m48hybrid4pln.h5"  # Path model di dalam kontainer Docker
STATS_PATH = "/app/../model/train_data_stats.pkl" # Path untuk menyimpan train_mean dan train_std

# --- Konfigurasi Data Windowing ---
IN_STEPS = 48  # 24 jam data input (48 x 30 menit)
OUT_STEPS = 48 # 24 jam data prediksi (48 x 30 menit)