import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

# Dosya yolları
converted_output_path = "/Users/seherova/Documents/projectss/formant/converted_output.txt"
format_shapes_path    = "/Users/seherova/Documents/projectss/formant/format_shapes_V02.txt"

# 1. Dosyaları Yüklencek
df_format = pd.read_csv(format_shapes_path, sep="\t", header=None, names=["time", "shape"])
df_conv   = pd.read_csv(converted_output_path, sep="\t", header=None, names=["time", "shape"])

# 2. Zaman Eşleştirme Fonksiyonu:
# format_shapes dosyasındaki her bir zaman değeri için, converted_output dosyasındaki en yakın zaman noktasının indeksini döndürür.
def find_nearest(time_value, conv_times):
    """
    Verilen time_value için conv_times (numpy array) içindeki en yakın indeksin döndürülmesi.
    """
    idx = np.abs(conv_times - time_value).argmin()
    return idx

# 3. Her iki dosyadaki zaman ve ağız şekillerini eşleştirerek yeni listeler oluşturma
aligned_format_shapes = []
aligned_conv_shapes   = []
conv_times = df_conv["time"].values

for i, row in df_format.iterrows():
    time_val = row["time"]
    shape_format = row["shape"]
    # converted_output dosyasındaki en yakın zamanı bul
    nearest_idx = find_nearest(time_val, conv_times)
    shape_conv = df_conv.iloc[nearest_idx]["shape"]
    
    aligned_format_shapes.append(shape_format)
    aligned_conv_shapes.append(shape_conv)

# 4. Benchmark Metriklerinin Hesaplanması
# Örneğin, doğruluk (accuracy) ve karmaşıklık matrisini (confusion matrix) hesaplayabiliriz.
accuracy = accuracy_score(aligned_conv_shapes, aligned_format_shapes)
cm = confusion_matrix(aligned_conv_shapes, aligned_format_shapes)

print("Doğruluk (Accuracy):", accuracy)
print("Karmaşıklık Matrisi (Confusion Matrix):\n", cm)

# Sınıf etiketlerini belirleme (hem converted_output hem de format_shapes'ten)
unique_labels = sorted(list(set(aligned_format_shapes + aligned_conv_shapes)))

# Seaborn ile daha açıklayıcı bir confusion matrix plot'u
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=unique_labels, yticklabels=unique_labels)
plt.xlabel("Lip Sync.")
plt.ylabel("Rhubarb Lip Sync.")
plt.title("Confusion Matrix")
plt.show()
