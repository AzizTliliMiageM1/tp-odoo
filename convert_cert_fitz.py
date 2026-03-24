import fitz  # PyMuPDF
from PIL import Image
import os

source_pdf = "Certificat_ (1).pdf"
output_png = "PDF/certificat_cnil_rgpd_2026.png"

try:
    # Supprimer l'ancien PNG s'il existe
    if os.path.exists(output_png):
        os.remove(output_png)
        print(f"✓ Ancien PNG supprimé: {os.path.abspath(output_png)}")
except Exception as e:
    print(f"✗ Erreur suppression: {e}")

try:
    # Ouvrir le PDF avec fitz
    doc = fitz.open(source_pdf)
    page = doc[0]  # Première page
    
    # Convertir en image PNG à haute résolution
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # 2x zoom pour meilleure qualité
    
    # Créer PIL Image à partir du pixmap
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    
    # Ajouter une marge blanche de 20px
    margin = 20
    new_width = img.width + (2 * margin)
    new_height = img.height + (2 * margin)
    img_with_margin = Image.new('RGB', (new_width, new_height), 'white')
    img_with_margin.paste(img, (margin, margin))
    
    # Sauvegarder
    img_with_margin.save(output_png, 'PNG', quality=95)
    print(f"✓ Certificat converti avec succès: {os.path.abspath(output_png)}")
    
    doc.close()
    
except FileNotFoundError:
    print(f"✗ Fichier PDF non trouvé: {os.path.abspath(source_pdf)}")
except Exception as e:
    print(f"✗ Erreur lors de la conversion: {e}")
