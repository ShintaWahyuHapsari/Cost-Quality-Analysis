import pandas as pd

# Membuat data dummy
data = {
    "Bulan": ["Januari", "Februari", "Maret", "April", "Mei", "Juni"],
    "Prevention Cost": [10000, 15000, 20000, 25000, 30000, 35000],
    "Failure Cost": [9000, 16000, 19000, 26000, 31000, 34000]
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Menambahkan kolom perbedaan
df["Dif"] = df["Prevention Cost"] - df["Failure Cost"]

# Menyimpan DataFrame ke file CSV
df.to_csv("C:/Users/DELL/AppData/Local/cost_quality.csv", index=False)

# Membaca data dari file CSV
df = pd.read_csv("C:/Users/DELL/AppData/Local/cost_quality.csv")

# Menampilkan data
print(df)

# Melakukan analisis sederhana
total_preventioncost = df["Prevention Cost"].sum()
total_failurecost = df["Failure Cost"].sum()
total_dif = df["Perbedaan"].sum()

print(f"Total Prevention Cost: {total_preventioncost}")
print(f"Total Failure Cost: {total_aktual}")
print(f"Total Dif: {total_dif}")

import matplotlib.pyplot as plt

# Plot Prevention Cost vs Failure Cost
plt.figure(figsize=(10, 6))
plt.plot(df["Bulan"], df["Prevention Cost"], marker='o', label="Prevention Cost")
plt.plot(df["Bulan"], df["Failure Cost"], marker='o', label="Failure Cost")
plt.xlabel("Bulan")
plt.ylabel("Nilai")
plt.title("Perbandingan Prevention Cost vs Failure Cost")
plt.legend()
plt.grid(True)
plt.show()

# Plot Perbedaan
plt.figure(figsize=(10, 6))
plt.bar(df["Bulan"], df["Dif"], color='orange')
plt.xlabel("Bulan")
plt.ylabel("Dif")
plt.title("Perbedaan antara Prevention Cost dan Failure Cost")
plt.grid(True)
plt.show()

# Menambahkan kolom perbedaan
df["Dif"] = df["Prevention Cost"] - df["Failure Cost"]

# Menyimpan DataFrame ke file CSV
df.to_csv("C:/Users/DELL/AppData/Local/cost_quality.csv", index=False)

# Membaca data dari file CSV
df = pd.read_csv("C:/Users/DELL/AppData/Local/cost_quality.csv")

# Plot Column Chart untuk Prevention Cost dan Failure Cost
plt.figure(figsize=(10, 6))
width = 0.4  # Lebar dari setiap bar
x = range(len(df["Bulan"]))  # Lokasi untuk setiap bar

# Membuat bar untuk Prevention Cost dan Failure Cost
plt.bar(x, df["Prevention Cost"], width=width, label="Prevention Cost", align='center')
plt.bar([p + width for p in x], df["Failure Cost"], width=width, label="Failure Cost", align='center')

# Mengatur posisi x-ticks
plt.xticks([p + width / 2 for p in x], df["Bulan"])

# Menambahkan label dan judul
plt.xlabel("Bulan")
plt.ylabel("Nilai")
plt.title("Perbandingan Prevention Cost dan Failure Cost")
plt.legend()

# Menampilkan grid
plt.grid(axis='y')

# Menampilkan chart
plt.show()

# Plot Column Chart untuk Perbedaan
plt.figure(figsize=(10, 6))
plt.bar(df["Bulan"], df["Dif"], color='orange', width=0.4)
plt.xlabel("Bulan")
plt.ylabel("Dif")
plt.title("Perbedaan antara Prevention Cost dan Failure Cost")
plt.grid(axis='y')

# Menampilkan chart
plt.show()

# Menampilkan data dalam bentuk tabel menggunakan Matplotlib
fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('tight')
ax.axis('off')

# Membuat tabel
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

# Menampilkan tabel
plt.title("Tabel Prevention Cost vs Failure Cost")
plt.show()

# Membuat area chart
plt.figure(figsize=(10, 6))

# Plot area untuk Prevention Cost
plt.fill_between(df["Bulan"], df["Prevention Cost"], alpha=0.5, label='Prevention Cost')

# Plot area untuk Failure Cost
plt.fill_between(df["Bulan"], df["Failure Cost"], alpha=0.5, label='Failure Cost')

# Menambahkan judul dan label
plt.title("Area Chart Prevention Cost vs Failure Cost")
plt.xlabel("Bulan")
plt.ylabel("Nilai")
plt.legend()

# Menampilkan grid
plt.grid(True)

# Menampilkan plot
plt.show()