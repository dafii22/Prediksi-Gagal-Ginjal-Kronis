import numpy as np
import joblib
import streamlit as st

# Load model yang telah disimpan
model = joblib.load('rf.sav')

# Tambahkan CSS untuk tampilan yang lebih menarik
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        max-width: 800px;
        margin: auto;
    }
    h1 {
        color: #004b8d;
        text-align: center;
    }
    label {
        font-weight: bold;
        color: #333333;
    }
    .stButton>button {
        background-color: #004b8d;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #003366;
    }
    </style>
""", unsafe_allow_html=True)

# Judul aplikasi
st.title("Prediksi Penyakit Gagal Ginjal Kronis")

# Layout input dengan dua kolom
col1, col2 = st.columns(2)

with col1:
    age = st.number_input('Umur', min_value=0)
    gender = st.selectbox('Jenis Kelamin (0: Perempuan, 1: Laki-laki)', [0, 1])
    socioeconomic_status = st.selectbox('Status Sosial Ekonomi (1-5)', [1, 2, 3, 4, 5])
    education_level = st.selectbox('Tingkat Pendidikan (1-5)', [1, 2, 3, 4, 5])
    BMI = st.number_input('Indeks Massa Tubuh (BMI)', min_value=0.0, format="%.2f")
    smoking = st.selectbox('Merokok (0: Tidak, 1: Ya)', [0, 1])
    alcohol_consumption = st.selectbox('Konsumsi Alkohol (0: Tidak, 1: Ya)', [0, 1])
    physical_activity = st.number_input('Frekuensi Aktivitas Fisik per Minggu', min_value=0)
    diet_quality = st.number_input('Kualitas Pola Makan (1-5)', min_value=1, max_value=5)
    sleep_quality = st.number_input('Kualitas Tidur (1-5)', min_value=1, max_value=5)
    family_history_kidney_disease = st.selectbox('Riwayat Keluarga Penyakit Ginjal (0: Tidak, 1: Ya)', [0, 1])
    family_history_hypertension = st.selectbox('Riwayat Keluarga Hipertensi (0: Tidak, 1: Ya)', [0, 1])
    family_history_diabetes = st.selectbox('Riwayat Keluarga Diabetes (0: Tidak, 1: Ya)', [0, 1])
    previous_acute_kidney_injury = st.selectbox('Riwayat Cedera Ginjal Akut (0: Tidak, 1: Ya)', [0, 1])
    urinary_tract_infections = st.selectbox('Infeksi Saluran Kemih (0: Tidak, 1: Ya)', [0, 1])
    systolic_bp = st.number_input('Tekanan Darah Sistolik (mmHg)', min_value=0)
    diastolic_bp = st.number_input('Tekanan Darah Diastolik (mmHg)', min_value=0)
    fasting_blood_sugar = st.number_input('Gula Darah Puasa (mg/dL)', min_value=0.0, format="%.2f")
    hba1c = st.number_input('HbA1c (%)', min_value=0.0, format="%.2f")
    serum_creatinine = st.number_input('Kreatinin Serum (mg/dL)', min_value=0.0, format="%.2f")
    BUN_levels = st.number_input('Kadar BUN (mg/dL)', min_value=0.0, format="%.2f")
    GFR = st.number_input('Laju Filtrasi Glomerulus (GFR, mL/min)', min_value=0.0, format="%.2f")
    protein_in_urine = st.number_input('Protein dalam Urine (mg/dL)', min_value=0.0, format="%.2f")
    ACR = st.number_input('ACR (mg/g)', min_value=0.0, format="%.2f")
    serum_sodium = st.number_input('Natrium Serum (mmol/L)', min_value=0.0, format="%.2f")

with col2:
    serum_potassium = st.number_input('Kalium Serum (mmol/L)', min_value=0.0, format="%.2f")
    serum_calcium = st.number_input('Kalsium Serum (mg/dL)', min_value=0.0, format="%.2f")
    serum_phosphorus = st.number_input('Fosfor Serum (mg/dL)', min_value=0.0, format="%.2f")
    hemoglobin = st.number_input('Kadar Hemoglobin (g/dL)', min_value=0.0, format="%.2f")
    cholesterol_total = st.number_input('Kolesterol Total (mg/dL)', min_value=0.0, format="%.2f")
    cholesterol_LDL = st.number_input('Kolesterol LDL (mg/dL)', min_value=0.0, format="%.2f")
    cholesterol_HDL = st.number_input('Kolesterol HDL (mg/dL)', min_value=0.0, format="%.2f")
    cholesterol_triglycerides = st.number_input('Triglycerida (mg/dL)', min_value=0.0, format="%.2f")
    ACE_inhibitors = st.selectbox('Penggunaan ACE Inhibitors (0: Tidak, 1: Ya)', [0, 1])
    diuretics = st.selectbox('Penggunaan Diuretik (0: Tidak, 1: Ya)', [0, 1])
    NSAIDs_use = st.selectbox('Penggunaan NSAIDs (0: Tidak, 1: Ya)', [0, 1])
    statins = st.selectbox('Penggunaan Statin (0: Tidak, 1: Ya)', [0, 1])
    antidiabetic_medications = st.selectbox('Penggunaan Obat Antidiabetes (0: Tidak, 1: Ya)', [0, 1])
    edema = st.selectbox('Edema (0: Tidak, 1: Ya)', [0, 1])
    fatigue_levels = st.number_input('Tingkat Kelelahan (1-5)', min_value=1, max_value=5)
    nausea_vomiting = st.selectbox('Mual & Muntah (0: Tidak, 1: Ya)', [0, 1])
    muscle_cramps = st.selectbox('Kram Otot (0: Tidak, 1: Ya)', [0, 1])
    itching = st.selectbox('Gatal-gatal (0: Tidak, 1: Ya)', [0, 1])
    quality_of_life_score = st.number_input('Skor Kualitas Hidup (1-5)', min_value=1, max_value=5)
    heavy_metals_exposure = st.selectbox('Paparan Logam Berat (0: Tidak, 1: Ya)', [0, 1])
    occupational_exposure_chemicals = st.selectbox('Paparan Kimia di Tempat Kerja (0: Tidak, 1: Ya)', [0, 1])
    water_quality = st.number_input('Kualitas Air (1-5)', min_value=1, max_value=5)
    medical_checkups_frequency = st.number_input('Frekuensi Pemeriksaan Medis per Tahun', min_value=0)
    medication_adherence = st.number_input('Kepatuhan Pengobatan (1-5)', min_value=1, max_value=5)
    health_literacy = st.number_input('Literasi Kesehatan (1-5)', min_value=1, max_value=5)

# Tombol untuk memprediksi
if st.button('Prediksi Penyakit Ginjal'):
    # Data input dalam bentuk array
    input_data = np.array([
        age, gender, socioeconomic_status, education_level, BMI, smoking, alcohol_consumption, 
        physical_activity, diet_quality, sleep_quality, family_history_kidney_disease, 
        family_history_hypertension, family_history_diabetes, previous_acute_kidney_injury, 
        urinary_tract_infections, systolic_bp, diastolic_bp, fasting_blood_sugar, hba1c, 
        serum_creatinine, BUN_levels, GFR, protein_in_urine, ACR, serum_sodium, serum_potassium, 
        serum_calcium, serum_phosphorus, hemoglobin, cholesterol_total, cholesterol_LDL, 
        cholesterol_HDL, cholesterol_triglycerides, ACE_inhibitors, diuretics, NSAIDs_use, 
        statins, antidiabetic_medications, edema, fatigue_levels, nausea_vomiting, muscle_cramps, 
        itching, quality_of_life_score, heavy_metals_exposure, occupational_exposure_chemicals, 
        water_quality, medical_checkups_frequency, medication_adherence, health_literacy
    ]).reshape(1, -1)

    # Lakukan prediksi
    prediction = model.predict(input_data)

    # Menampilkan hasil prediksi
    if prediction[0] == 1:
        st.error('Prediksi: Pasien Berisiko Mengalami Penyakit Ginjal Kronis')
    else:
        st.success('Prediksi: Pasien Tidak Berisiko Penyakit Ginjal Kronis')
