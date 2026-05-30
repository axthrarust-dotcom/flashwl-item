from PIL import Image
import os

# ============================================================
#  CONFIGURATION  -  modifie ces valeurs si besoin
# ============================================================
DOSSIER  = r"C:\Users\hugo2\Desktop\clth_image_images_only"
DIVISEUR = 8          # divise la taille par ce nombre (ex: 10 => 800 devient 80)
EXTENSIONS = {'.png', '.jpg', '.jpeg', '.bmp', '.tga'}
# ============================================================

def main():
    print(f"Dossier  : {DOSSIER}")
    print(f"Diviseur : /{DIVISEUR}")
    print("Scan des images en cours...\n")

    files = [
        os.path.join(dp, f)
        for dp, _, fn in os.walk(DOSSIER)
        for f in fn
        if os.path.splitext(f)[1].lower() in EXTENSIONS
    ]

    total   = len(files)
    erreurs = []

    print(f"{total} images trouvées — redimensionnement en cours...\n")

    for i, path in enumerate(files, 1):
        try:
            img = Image.open(path)
            w, h = img.size
            new_w = max(1, w // DIVISEUR)
            new_h = max(1, h // DIVISEUR)
            img = img.resize((new_w, new_h), Image.LANCZOS)
            img.save(path)
        except Exception as e:
            erreurs.append((path, str(e)))

        if i % 500 == 0 or i == total:
            print(f"  {i}/{total} traités...")

    print("\n=== TERMINÉ ===")
    print(f"  {total - len(erreurs)} images redimensionnées avec succès")
    if erreurs:
        print(f"  {len(erreurs)} erreur(s) :")
        for p, err in erreurs:
            print(f"    {p}  ->  {err}")

    input("\nAppuie sur Entrée pour fermer...")

if __name__ == "__main__":
    main()
