import tensorflow as tf
import config
from data_preprocessing import preprocess_input, postprocess_output

# Muat model saat aplikasi dimulai untuk efisiensi
model = tf.keras.models.load_model(config.MODEL_PATH)

def make_prediction(raw_input: list) -> dict:
    """
    Melakukan peramalan end-to-end: pra-pemrosesan, prediksi, dan pasca-pemrosesan.
    """
    # 1. Pra-pemrosesan input
    model_input = preprocess_input(raw_input)

    # 2. Lakukan prediksi dengan model
    prediction_result = model.predict(model_input)

    # 3. Pasca-pemrosesan output
    final_prediction = postprocess_output(prediction_result)

    return {"forecast": final_prediction}