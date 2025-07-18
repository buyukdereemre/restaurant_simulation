from PIL import Image
import os

# Ayarlar
input_folder = "baklava"
output_folder = "yeniden_boyutlandirilmis"
target_size = (224, 224)  # İstediğiniz boyut

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith((".jpg", ".jpeg", ".png")):
        img = Image.open(os.path.join(input_folder, filename))
        img = img.resize(target_size, Image.LANCZOS)  # Yüksek kaliteli algoritma
        # JPG olarak kaydet (kalite=90)
        img.save(os.path.join(output_folder, filename), "JPEG", quality=90)

print("Tüm fotolar yeniden boyutlandırıldı!")