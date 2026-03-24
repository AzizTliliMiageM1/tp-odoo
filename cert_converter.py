import os
from PIL import Image
import fitz

# Utiliser le PDF existant mais avec MEILLEUR CADRAGE
source_pdf = "Certificat_ (1).pdf"
output_png = "PDF/certificat_cnil_rgpd_2026.png"

try:
    print("🔄 Conversion du certificat...")
    
    # Supprimer l'ancien PNG
    if os.path.exists(output_png):
        os.remove(output_png)
        print("✓ Ancien PNG supprimé")
    
    # Ouvrir le PDF
    doc = fitz.open(source_pdf)
    
    # Prendre la première page
    page = doc[0]
    
    # Rendre à haute résolution 3x pour qualité maximale
    print("📐 Rendu haute résolution (3x)...")
    pix = page.get_pixmap(matrix=fitz.Matrix(3, 3))
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    
    # Ajouter cadre blanc ÉPAIS pour meilleure présentation (50px)
    margin = 50
    new_width = img.width + (2 * margin)
    new_height = img.height + (2 * margin)
    
    print(f"📋 Cadrage: {img.width}x{img.height} → {new_width}x{new_height}px")
    
    img_with_margin = Image.new('RGB', (new_width, new_height), 'white')
    img_with_margin.paste(img, (margin, margin))
    
    # Optimiser pour le web - très haute qualité
    img_with_margin.save(output_png, 'PNG', quality=95, optimize=True)
    
    file_size = os.path.getsize(output_png) / 1024
    print(f"✅ PNG créé avec succès!")
    print(f"📁 {os.path.abspath(output_png)}")
    print(f"💾 Taille: {file_size:.1f} KB")
    
    doc.close()
    
except Exception as e:
    print(f"✗ Erreur: {e}")
    import traceback
    traceback.print_exc()
