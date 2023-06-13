import streamlit as st
import numpy as np
from scipy import stats

def main():
    st.title("Uji Hipotesis Rata-rata Dua Populasi")
    
    # Masukkan data dari pengguna
    st.subheader("Masukkan Data Populasi Pertama:")
    data_pop1 = st.text_area("Masukkan data populasi pertama, dipisahkan dengan koma (misal: 1,2,3,4)")
    
    st.subheader("Masukkan Data Populasi Kedua:")
    data_pop2 = st.text_area("Masukkan data populasi kedua, dipisahkan dengan koma (misal: 1,2,3,4)")
    
    # Mengonversi data menjadi array numpy
    try:
        pop1 = np.array([float(x.strip()) for x in data_pop1.split(",")])
        pop2 = np.array([float(x.strip()) for x in data_pop2.split(",")])
    except:
        st.error("Terjadi kesalahan dalam memproses data. Pastikan format input benar.")
        return
    
    # Menampilkan data
    st.subheader("Data Populasi Pertama:")
    st.write(pop1)
    
    st.subheader("Data Populasi Kedua:")
    st.write(pop2)
    
    # Menghitung statistik uji
    mean1 = np.mean(pop1)
    mean2 = np.mean(pop2)
    std1 = np.std(pop1, ddof=1)
    std2 = np.std(pop2, ddof=1)
    n1 = len(pop1)
    n2 = len(pop2)
    
    # Menghitung perbedaan rata-rata dan kesalahan standar perbedaan rata-rata
    diff_mean = mean1 - mean2
    se_diff = np.sqrt((std1**2 / n1) + (std2**2 / n2))
    
    # Menghitung z-score
    z_score = diff_mean / se_diff
    
    # Menghitung p-value
    p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))
    
    # Menampilkan hasil uji hipotesis
    st.subheader("Hasil Uji Hipotesis:")
    st.write("Rata-rata Populasi Pertama:", mean1)
    st.write("Rata-rata Populasi Kedua:", mean2)
    st.write("Perbedaan Rata-rata:", diff_mean)
    st.write("Kesalahan Standar Perbedaan Rata-rata:", se_diff)
    st.write("Z-Score:", z_score)
    st.write("Nilai p-value:", p_value)
    
if __name__ == "__main__":
    main()
