
import pandas as pd
import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Bike Sharing Analysis",
    layout="wide"
)

# Memuat dataset
@st.cache_data
def load_data():
    data = pd.read_csv("main_data.csv")
    data["dteday"] = pd.to_datetime(data["dteday"])
    data["tahun"] = data["dteday"].dt.year
    return data

df = load_data()

# Judul dashboard
st.title(" Bike Sharing Data Analysis")
st.write(
    "Dashboard analisis penyewaan sepeda berdasarkan jenis hari "
    "dan kondisi cuaca selama tahun 2011–2012."
)

# Filter tahun
pilihan_tahun = st.selectbox(
    "Pilih Tahun",
    ["Semua Tahun", 2011, 2012]
)

if pilihan_tahun == "Semua Tahun":
    data = df.copy()
else:
    data = df[df["tahun"] == pilihan_tahun].copy()


# Ringkasan data
total_penyewaan = int(data["cnt"].sum())
rata_penyewaan = data["cnt"].mean()

kolom1, kolom2, kolom3 = st.columns(3)

kolom1.metric("Jumlah Hari", f"{len(data):,}")
kolom2.metric("Total Penyewaan", f"{total_penyewaan:,}")
kolom3.metric(
    "Rata-rata Penyewaan per Hari",
    f"{rata_penyewaan:,.2f}"
)

st.divider()

# Analisis 1: Jenis hari
st.subheader("1. Penyewaan Berdasarkan Jenis Hari")
st.write(
    "Bagaimana perbedaan jumlah penyewaan sepeda antara "
    "hari kerja dan hari bukan kerja?"
)

rata_hari = (
    data.groupby("workingday")["cnt"]
    .mean()
    .reindex([0, 1])
)

rata_hari.index = ["Hari Bukan Kerja", "Hari Kerja"]
rata_hari.name = "Rata-rata Penyewaan"

st.bar_chart(rata_hari)

st.dataframe(
    rata_hari.rename_axis("Jenis Hari").reset_index(),
    hide_index=True,
    use_container_width=True
)

st.caption(
    "Nilai workingday: 0 = hari bukan kerja, 1 = hari kerja."
)

st.divider()


# Analisis 2: Kondisi cuaca
st.subheader("2. Penyewaan Berdasarkan Kondisi Cuaca")
st.write(
    "Bagaimana perbedaan jumlah penyewaan sepeda berdasarkan "
    "kondisi cuaca?"
)

rata_cuaca = (
    data.groupby("weathersit")["cnt"]
    .mean()
    .reindex([1, 2, 3])
)

label_cuaca = {
    1: "Cerah / sedikit berawan",
    2: "Berkabut / berawan",
    3: "Hujan ringan / cuaca buruk"
}

rata_cuaca.index = [
    label_cuaca[kategori] for kategori in rata_cuaca.index
]
rata_cuaca.name = "Rata-rata Penyewaan"

st.bar_chart(rata_cuaca)

st.dataframe(
    rata_cuaca.rename_axis("Kondisi Cuaca").reset_index(),
    hide_index=True,
    use_container_width=True
)

st.divider()

# Kesimpulan
st.subheader("Kesimpulan")

st.markdown(
    """
    - Rata-rata penyewaan dapat dibandingkan antara hari kerja
      dan hari bukan kerja.
    - Kondisi cuaca yang berbeda menunjukkan rata-rata penyewaan
      yang berbeda.
    - Informasi ini dapat membantu pengelola merencanakan
      ketersediaan sepeda dan operasional berdasarkan kondisi harian.
    """
)

st.caption(
    "Sumber: Bike Sharing Dataset, periode 2011-2012."
)
