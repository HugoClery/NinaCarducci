import os
from PIL import Image

# Dossier contenant les images à redimensionner
input_folder = './assets/images/gallery/portraits'
# Dossier de sortie pour les images redimensionnées
output_folder = './assets/images/gallery/portraits'

# Créer le dossier de sortie s'il n'existe pas
os.makedirs(output_folder, exist_ok=True)

# Tailles à redimensionner
sizes = [(1200, 'large'), (300, 'small')]

# Parcourir les fichiers dans le dossier d'entrée
for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.webp')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Redimensionner et sauvegarder les images
        for size, label in sizes:
            resized_img = img.resize((size, int((size / img.width) * img.height)))
            resized_img.save(os.path.join(output_folder, f"{os.path.splitext(filename)[0]}-{label}.webp"))

print("Redimensionnement terminé.")