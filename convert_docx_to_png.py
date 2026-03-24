import subprocess
import os
from PIL import Image
import fitz

source_docx = "Certificat_.docx"
temp_pdf = "temp_cert.pdf"
output_png = "PDF/certificat_cnil_rgpd_2026.png"

try:
    # Essayer de convertir DOCX en PDF avec LibreOffice
    print("📄 Conversion DOCX → PDF via LibreOffice...")
    result = subprocess.run([
        "soffice",
        "--headless",
        "--convert-to", "pdf",
        source_docx,
        "--outdir", "."
    ], capture_output=True, timeout=60)
    
    if result.returncode != 0 and not os.path.exists(temp_pdf):
        print("⚠️ LibreOffice non disponible, essai alternatif...")
        raise Exception("LibreOffice conversion failed")
    
    print("✓ DOCX converti en PDF")
    
    # Supprimer l'ancien PNG
    if os.path.exists(output_png):
        os.remove(output_png)
        print(f"✓ Ancien PNG supprimé")
    
    # Convertir PDF en PNG avec marge blanche
    doc = fitz.open(temp_pdf)
    page = doc[0]
    
    # Rendre à haute résolution (2x)
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    
    # Ajouter marge blanche 30px (plus généreuse pour certif)
    margin = 30
    new_width = img.width + (2 * margin)
    new_height = img.height + (2 * margin)
    img_with_margin = Image.new('RGB', (new_width, new_height), 'white')
    img_with_margin.paste(img, (margin, margin))
    
    # Sauvegarder
    img_with_margin.save(output_png, 'PNG', quality=95)
    print(f"✓ PNG généré avec cadrage: {os.path.abspath(output_png)}")
    
    # Nettoyer
    doc.close()
    if os.path.exists(temp_pdf):
        os.remove(temp_pdf)
    
    print("✓ Conversion complète!")
    
except Exception as e:
    print(f"✗ Erreur: {e}")
