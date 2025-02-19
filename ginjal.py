import numpy as np
import joblib
import streamlit as st

# Load model yang telah disimpan
model = joblib.load('rf.sav')

# Atur layout agar lebih lebar
st.set_page_config(layout="wide")

# Tambahkan CSS untuk full screen + desain kustom
st.markdown("""
    <style>
    /* Mengatur tampilan utama */
    .stApp {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        width: 100vw;
        height: 100vh;
        margin: 0;
        overflow: hidden;
    }

    /* Kontainer utama */
    .block-container {
        padding: 2rem;
        max-width: 800px;
        margin: auto;
    }

    /* Header */
    h1, h2, h3, h4, h5, h6 {
        color: #212529;
        text-align: center;
        font-size: 26px;
        font-weight: bold;
        font-family: 'Arial', sans-serif;
    }

    /* Label teks */
    label {
        font-weight: bold;
        color: #333333;
        font-size: 18px;
    }

    /* Teks utama */
    body, p, div, span {
        color: #212529;
        font-size: 18px;
        font-family: 'Arial', sans-serif;
    }

    /* Gaya tombol */
    .stButton>button {
        background-color: #007bff;
        color: white;
        font-size: 18px;
        font-weight: bold;
        padding: 12px 24px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 2px 4px 10px rgba(0, 0, 0, 0.2);
    }

    /* Efek hover tombol */
    .stButton>button:hover {
        background-color: #0056b3;
        transform: scale(1.05);
    }

    /* Kotak input */
    .stTextInput>div>div>input {
        border: 2px solid #007bff;
        border-radius: 6px;
        padding: 10px;
        font-size: 16px;
    }

    /* Checkbox & Radio button */
    .stCheckbox, .stRadio {
        font-size: 18px;
        color: #212529;
    }

    /* Gaya Selectbox */
    .stSelectbox div[data-baseweb="select"] {
        color: #212529 !important;
        font-size: 18px;
        font-family: 'Arial', sans-serif;
    }

    /* Gaya untuk pilihan dalam Selectbox */
    .stSelectbox div[data-baseweb="select"] div {
        background-color: #ffffff !important;
        color: #212529 !important;
    }

    /* Dropdown items */
    .stSelectbox div[data-baseweb="select"] span {
        color: #212529 !important;
    }

    </style>
""", unsafe_allow_html=True)



# Judul aplikasi
st.title("Prediksi Penyakit Gagal Ginjal Kronis")

# Layout input dengan dua kolom
col1, col2 = st.columns(2)

with col1:
    age = st.number_input('Umur', min_value=0)
    gender = st.selectbox('Jenis Kelamin (0: Laki-laki, 1: Perempuan)', [0, 1])
    socioeconomic_status = st.selectbox('Status Sosial Ekonomi (0-3)', [0, 1, 2, 3])
    education_level = st.selectbox('Tingkat Pendidikan (0-3)', [0, 1, 2, 3])
    BMI = st.number_input('Indeks Massa Tubuh (BMI)', min_value=15.0, max_value=40.0, format="%.2f")
    smoking = st.selectbox('Merokok (0: Tidak, 1: Ya)', [0, 1])
    alcohol_consumption = st.number_input('Konsumsi Alkohol (0-20)', min_value=0.0, max_value=20.0)
    physical_activity = st.number_input('Frekuensi Aktivitas Fisik per Minggu (0-10)', min_value=0, max_value=10)
    diet_quality = st.number_input('Kualitas Pola Makan (0-10)', min_value=0, max_value=10)
    sleep_quality = st.number_input('Kualitas Tidur (4-10)', min_value=4, max_value=10)
    family_history_kidney_disease = st.selectbox('Riwayat Keluarga Penyakit Ginjal (0: Tidak, 1: Ya)', [0, 1])
    family_history_hypertension = st.selectbox('Riwayat Keluarga Hipertensi (0: Tidak, 1: Ya)', [0, 1])
    family_history_diabetes = st.selectbox('Riwayat Keluarga Diabetes (0: Tidak, 1: Ya)', [0, 1])
    previous_acute_kidney_injury = st.selectbox('Riwayat Cedera Ginjal Akut (0: Tidak, 1: Ya)', [0, 1])
    urinary_tract_infections = st.selectbox('Infeksi Saluran Kemih (0: Tidak, 1: Ya)', [0, 1])
    systolic_bp = st.number_input('Tekanan Darah Sistolik (mmHg)', min_value=90, max_value=180)
    diastolic_bp = st.number_input('Tekanan Darah Diastolik (mmHg)', min_value=60, max_value=200)
    fasting_blood_sugar = st.number_input('Gula Darah Puasa (mg/dL)', min_value=70.0, max_value=200.0, format="%.2f")
    hba1c = st.number_input('HbA1c (%)', min_value=4.0, max_value=10.0, format="%.2f")
    serum_creatinine = st.number_input('Kreatinin Serum (mg/dL)', min_value=0.5, max_value=5.0, format="%.2f")
    BUN_levels = st.number_input('Kadar BUN (mg/dL)', min_value=5.0, max_value=50.0, format="%.2f")
    GFR = st.number_input('Laju Filtrasi Glomerulus (GFR, mL/min)', min_value=15.0, max_value=120.0, format="%.2f")
    protein_in_urine = st.number_input('Protein dalam Urine (mg/dL)', min_value=0.0, max_value=5.0, format="%.2f")
    ACR = st.number_input('ACR (mg/g)', min_value=0.0, max_value=300.0, format="%.2f")
    serum_sodium = st.number_input('Natrium Serum (mmol/L)', min_value=135.0, max_value=145.0, format="%.2f")

with col2:
    serum_potassium = st.number_input('Kalium Serum (mmol/L)', min_value=3.5, max_value=5.5, format="%.2f")
    serum_calcium = st.number_input('Kalsium Serum (mg/dL)', min_value=8.5, max_value=10.5, format="%.2f")
    serum_phosphorus = st.number_input('Fosfor Serum (mg/dL)', min_value=2.5, max_value=4.5, format="%.2f")
    hemoglobin = st.number_input('Kadar Hemoglobin (g/dL)', min_value=10.0, max_value=18.0, format="%.2f")
    cholesterol_total = st.number_input('Kolesterol Total (mg/dL)', min_value=150.0, max_value=300.0, format="%.2f")
    cholesterol_LDL = st.number_input('Kolesterol LDL (mg/dL)', min_value=50.0, max_value=200.0, format="%.2f")
    cholesterol_HDL = st.number_input('Kolesterol HDL (mg/dL)', min_value=20.0, max_value=100.0, format="%.2f")
    cholesterol_triglycerides = st.number_input('Triglycerida (mg/dL)', min_value=50.0, max_value=400.0, format="%.2f")
    ACE_inhibitors = st.selectbox('Penggunaan ACE Inhibitors (0: Tidak, 1: Ya)', [0, 1])
    diuretics = st.selectbox('Penggunaan Diuretik (0: Tidak, 1: Ya)', [0, 1])
    NSAIDs_use = st.number_input('Penggunaan NSAIDs (0-10)', min_value=0, max_value=10)
    statins = st.selectbox('Penggunaan Statin (0: Tidak, 1: Ya)', [0, 1])
    antidiabetic_medications = st.selectbox('Penggunaan Obat Antidiabetes (0: Tidak, 1: Ya)', [0, 1])
    edema = st.selectbox('Edema (0: Tidak, 1: Ya)', [0, 1])
    fatigue_levels = st.number_input('Tingkat Kelelahan (0-10)', min_value=0, max_value=10)
    nausea_vomiting = st.number_input('Mual & Muntah (0-7)', min_value=0, max_value=7)
    muscle_cramps = st.number_input('Kram Otot (0-7)', min_value=0, max_value=7)
    itching = st.number_input('Gatal-gatal (0-10)', min_value=0, max_value=10)
    quality_of_life_score = st.number_input('Skor Kualitas Hidup (0-100)', min_value=0, max_value=100)
    heavy_metals_exposure = st.selectbox('Paparan Logam Berat (0: Tidak, 1: Ya)', [0, 1])
    occupational_exposure_chemicals = st.selectbox('Paparan Kimia di Tempat Kerja (0: Tidak, 1: Ya)', [0, 1])
    water_quality = st.selectbox('Kualitas Air (0: Baik, 1: Buruk)', [0, 1])
    medical_checkups_frequency = st.number_input('Frekuensi Pemeriksaan Medis per Tahun (0-4)', min_value=0, max_value=4)
    medication_adherence = st.number_input('Kepatuhan Pengobatan (0-10)', min_value=0, max_value=10)
    health_literacy = st.number_input('Literasi Kesehatan (0-10)', min_value=0, max_value=10)

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
