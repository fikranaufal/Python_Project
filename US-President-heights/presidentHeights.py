import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

# Baca data dari file csv
data = pd.read_csv('president_heights.csv')

# Menampilkan 5 baris pertama dari data
#print(data.head())

# Menampilkan 5 baris terakhir dari data
#print(data.tail())

# Menampilkan kolom-kolom dari data
#print(data.columns)

# Menampilkan info dari data
#print(data.info())

# Menampilkan deskripsi dari 

# Memilih kolom height(cm) dan mengubahnya dalam array numpy
heights = np.array(data['height(cm)'])
#print(heights)

# Menampilkan mean dari heights
print(f'mean heights = {np.mean(heights)}')

# Menampilkan variansi dari heights
print(f'variansi dari heigths = {np.var(heights)}')

# Menampilkan nilai maksimum dari heights
print(f'nilai maksimum dari heights = {np.max(heights)}')

# Menampilkan nilai minimum dari heights
print(f'nilai minimum dari heights = {np.min(heights)}')

# Menampilkan median dari heights
print(f'median dari heights = {np.median(heights)}')

# Menampilkan persentil 25 dari heights 
print(f'persentil 25 dari heights = {np.percentile(heights, 25)}')

# Menampilkan persentil 75 dari heights
print(f'persentil 75 dari heights = {np.percentile(heights, 75)}')

plt.hist(heights)
plt.title('Distribusi dari Tinggi Presiden Amerika Serikat')
plt.xlabel('Tinggi (cm)')
plt.ylabel('Jumlah')
plt.show()