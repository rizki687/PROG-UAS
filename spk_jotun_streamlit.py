
import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Dataset dummy
data = {
    "Nama Cat": ["Jotun Majestic", "Jotun Jotaplast", "Jotun Essence", "Jotun Ultra Resist", "Jotun EasyClean"],
    "Harga per Liter": [75000, 50000, 60000, 85000, 70000],
    "Daya Sebar (m2/liter)": [10, 8, 9, 11, 10],
    "Warna": ["Putih", "Biru Muda", "Abu-abu", "Hijau", "Krem"],
    "Kualitas": ["Premium", "Medium", "Medium", "Premium", "Medium"],
    "Cocok untuk": ["Kamar Tidur", "Ruang Tamu", "Dapur", "Ruang Keluarga", "Kamar Anak"],
    "Warna Dominan Furnitur": ["Cerah", "Netral", "Gelap", "Netral", "Cerah"]
}
df = pd.DataFrame(data)

# Sidebar input
st.sidebar.header("Input Kebutuhan")
budget = st.sidebar.number_input("Anggaran (Rp)", min_value=10000, step=10000)
luas = st.sidebar.number_input("Luas ruangan (m²)", min_value=1)
jenis_ruang = st.sidebar.selectbox("Jenis ruang", df["Cocok untuk"].unique())
warna_furnitur = st.sidebar.selectbox("Warna furnitur/korden/karpet", df["Warna Dominan Furnitur"].unique())

# Proses
df["Total Harga"] = df["Harga per Liter"] * (luas / df["Daya Sebar (m2/liter)"])
df_filtered = df[
    (df["Total Harga"] <= budget) &
    (df["Cocok untuk"] == jenis_ruang) &
    (df["Warna Dominan Furnitur"] == warna_furnitur)
]

st.title("Rekomendasi Cat Jotun")
if not df_filtered.empty:
    st.success("Ditemukan beberapa cat yang sesuai:")
    st.dataframe(df_filtered[["Nama Cat", "Warna", "Kualitas", "Total Harga"]])
else:
    st.warning("Tidak ada cat yang sesuai dengan kriteria.")
