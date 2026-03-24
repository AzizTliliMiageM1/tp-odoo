from pdf2image import convert_from_path
from PIL import Image
import os

# Chemin du PDF et du PNG de sortie
pdf_path = r"C:\Users\mdazi\Desktop\Marketing numérique\TP1\PDF\certificat_cnil_rgpd_2026.pdf"
png_output_path = r"C:\Users\mdazi\Desktop\Marketing numérique\TP1\PDF\certificat_cnil_rgpd_2026.png"

# Supprimer le PDF existant
if os.path.exists(pdf_path):
    os.remove(pdf_path)
    print(f"✓ Ancien PDF supprimé: {pdf_path}")

# Convertir le nouveau PDF en images (il pourrait y avoir plusieurs pages)
# Pour cette étape, on utilise le fichier attaché
# D'abord on doit le copier depuis le répertoire racine
source_pdf = r"C:\Users\mdazi\Desktop\Marketing numérique\TP1\Certificat_ (1).pdf"

if os.path.exists(source_pdf):
    # Convertir le PDF en images
    images = convert_from_path(source_pdf, dpi=150)
    
    if images:
        # Prendre la première page
        img = images[0]
        
        # Ajouter des marges pour un meilleur cadrage
        margin = 20
        new_width = img.width + (2 * margin)
        new_height = img.height + (2 * margin)
        
        # Créer une image avec marges (fond blanc)
        img_with_margin = Image.new('RGB', (new_width, new_height), 'white')
        img_with_margin.paste(img, (margin, margin))
        
        # Sauvegarder en PNG
        img_with_margin.save(png_output_path, 'PNG', quality=95)
        print(f"✓ PNG créé avec succès: {png_output_path}")
        print(f"  Dimensions: {new_width}x{new_height} pixels")
    else:
        print("✗ Erreur: Impossible de convertir le PDF")
else:
    print(f"✗ Fichier non trouvé: {source_pdf}")
