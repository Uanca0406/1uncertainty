import numpy as np
import pandas as pd

# Data Kalibrasi (x = kons mg/L, y = absorbansi)
x = np.array([0, 5, 10, 15, 20, 25])
y = np.array([0.0115, 0.2259, 0.4418, 0.6877, 0.9236, 1.1335])

# Hitung regresi linear
n = len(x)
slope, intercept = np.polyfit(x, y, 1)

# Data sampel
sampel_abs = np.array([0.4118, 0.4397, 0.4537, 0.4530])
sampel_bobot = np.array([0.01, 0.0101, 0.0102, 0.0102])
volume = 0.1  # Liter

# Hitung konsentrasi & kadar
c_terukur = (sampel_abs - intercept) / slope
csampel = (c_terukur * volume) / sampel_bobot  # mg/kg

# Rata-rata kadar
rata2_csampel = np.mean(csampel)

# Ketidakpastian
ureg = 0.2713        # Ketidakpastian dari kalibrasi (mg/L)
uLT = 0.134          # Ketidakpastian volume (mL)
uM = 0.00028         # Ketidakpastian neraca (g)
uPM = 3401.55        # Ketidakpastian presisi metode (mg/kg)

# Nilai rerata untuk estimasi ketidakpastian
xr = np.mean(c_terukur)
weight_avg = np.mean(sampel_bobot)

# Komponen relatif
rel_ureg = (ureg / xr) ** 2
rel_uLT = (uLT / (volume * 1000)) ** 2
rel_uM = (uM / weight_avg) ** 2
rel_uPM = (uPM / rata2_csampel) ** 2

# Ketidakpastian gabungan
ucsx_rel = rel_ureg + rel_uLT + rel_uM + rel_uPM
ucsx = np.sqrt(ucsx_rel) * rata2_csampel

# Ketidakpastian diperluas (k = 2)
U = ucsx * 2

# Output
print(f\"Hasil Perhitungan Penetapan Thiamin:\")
print(f\"Slope: {slope:.4f}\")
print(f\"Intercept: {intercept:.4f}\")
print(f\"Rata-rata Kadar Sampel: {rata2_csampel:.2f} mg/kg\")
print(f\"Ketidakpastian Gabungan: ±{ucsx:.2f} mg/kg\")
print(f\"Ketidakpastian Diperluas (k=2): ±{U:.2f} mg/kg\")
print(f\"Pelaporan: ({rata2_csampel:.2f} ± {U:.2f}) mg/kg\")

