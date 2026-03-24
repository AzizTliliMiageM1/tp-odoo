import os
import sys
from PIL import Image
import fitz

# Utiliser le PDF existant et bien le cadrer
source_pdf = "Certificat_ (1).pdf"
output_png = "PDF/certificat_cnil_rgpd_2026.png"

try:
    # Supprimer l'ancien PNG
    if os.path.exists(output_png):
        os.remove(output_png)
        print(f"✓ Ancien PNG supprimé")
    
    # Ouvrir le PDF
    doc = fitz.open(source_pdf)
    page = doc[0]
    
    # Rendre à très haute résolution (3x pour meilleure qualité)
    pix = page.get_pixmap(matrix=fitz.Matrix(3, 3))
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    
    # Ajouter marge blanche généreuse 40px pour cadrage professionnel
    margin = 40
    new_width = img.width + (2 * margin)
    new_height = img.height + (2 * margin)
    img_with_margin = Image.new('RGB', (new_width, new_height), 'white')
    img_with_margin.paste(img, (margin, margin))
    
    # Sauvegarder en haute qualité
    img_with_margin.save(output_png, 'PNG', quality=95)
    print(f"✓ PNG généré avec cadrage professionnel: {os.path.abspath(output_png)}")
    print(f"✓ Résolution: {img_with_margin.width}x{img_with_margin.height}px")
    
    # Nettoyer
    doc.close()
    
except Exception as e:
    print(f"✗ Erreur: {e}")
