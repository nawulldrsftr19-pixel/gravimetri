import streamlit as st

# Judul dan Deskripsi
st.set_page_config(page_title="Web Analisis Kimia", layout="wide")
st.title("🔬 Web Perhitungan Analisis Kimia")
st.markdown("Platform interaktif untuk menghitung **kadar air, abu, sulfat, Fe, dan Ba** dalam sampel.")

# Sidebar untuk input data
st.sidebar.header("📥 Input Data Sampel")
sample_name = st.sidebar.text_input("Nama Sampel", "Sampel A")
weight_initial = st.sidebar.number_input("Berat Awal Sampel (g)", min_value=0.0, value=5.0)
weight_dry = st.sidebar.number_input("Berat Setelah Pengeringan (g)", min_value=0.0, value=4.5)
weight_ash = st.sidebar.number_input("Berat Abu (g)", min_value=0.0, value=0.2)
weight_baso4 = st.sidebar.number_input("Berat Endapan BaSO₄ (g)", min_value=0.0, value=0.5)
weight_fe2o3 = st.sidebar.number_input("Berat Endapan Fe₂O₃ (g)", min_value=0.0, value=0.3)

# Perhitungan
kadar_air = ((weight_initial - weight_dry) / weight_initial) * 100
kadar_abu = (weight_ash / weight_initial) * 100
kadar_sulfat = (weight_baso4 * 96.06 / 233.39 / weight_initial) * 100   # M(SO4)=96.06, M(BaSO4)=233.39
kadar_fe = (weight_fe2o3 * (2*55.85) / (2*55.85+3*16) / weight_initial) * 100  # M(Fe)=55.85, M(Fe2O3)=159.7
kadar_ba = (weight_baso4 * 137.33 / 233.39 / weight_initial) * 100   # M(Ba)=137.33

# Hasil
st.subheader("📊 Hasil Perhitungan")
results = {
    "Kadar Air (%)": round(kadar_air, 2),
    "Kadar Abu (%)": round(kadar_abu, 2),
    "Kadar Sulfat (%)": round(kadar_sulfat, 2),
    "Kadar Fe (%)": round(kadar_fe, 2),
    "Kadar Ba (%)": round(kadar_ba, 2),
}
df = pd.DataFrame.from_dict(results, orient="index", columns=["Nilai"])
st.table(df)

# Visualisasi
st.subheader("📈 Visualisasi Hasil")
fig, ax = plt.subplots()
ax.bar(results.keys(), results.values(), color=["#4CAF50","#FFC107","#2196F3","#9C27B0","#FF5722"])
ax.set_ylabel("Persentase (%)")
ax.set_title(f"Hasil Analisis {sample_name}")
st.pyplot(fig)

# Simulasi
st.subheader("🧪 Simulasi Perubahan Berat")
weights = [weight_initial, weight_dry, weight_ash]
labels = ["Awal", "Setelah Pengeringan", "Abu"]
fig2, ax2 = plt.subplots()
ax2.plot(labels, weights, marker="o", linestyle="--", color="red")
ax2.set_ylabel("Berat (g)")
ax2.set_title("Simulasi Proses Analisis")
st.pyplot(fig2)

st.success("✅ Perhitungan dan simulasi selesai. Data dapat digunakan untuk laporan praktikum.")
