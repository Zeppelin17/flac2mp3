import os
import sys
import concurrent.futures
import subprocess
from pathlib import Path
from tqdm import tqdm

# Directorios de origen y destino
SRC_DIR = Path.home() / "Downloads" / "SOURCE_DIRECTORY_NAME"
DEST_DIR = Path.home() / "Downloads" / "DESTINATION_DIRECTORY_NAME"

# Crear la carpeta destino si no existe
DEST_DIR.mkdir(parents=True, exist_ok=True)


def convert_flac_to_mp3(flac_file):
    """Convierte un archivo FLAC a MP3 manteniendo la estructura de carpetas."""
    relative_path = flac_file.relative_to(SRC_DIR)
    mp3_file = DEST_DIR / relative_path.with_suffix(".mp3")

    # Crear la carpeta destino si no existe
    mp3_file.parent.mkdir(parents=True, exist_ok=True)

    # Ejecutar ffmpeg para la conversión
    command = [
        "ffmpeg",
        "-y",
        "-i",
        str(flac_file),
        "-b:a",
        "320k",
        "-map_metadata",
        "0",
        "-id3v2_version",
        "3",
        str(mp3_file),
    ]
    result = subprocess.run(
        command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )

    if result.returncode == 0:
        return f"✅ Convertido: {flac_file} → {mp3_file}"
    else:
        return f"❌ ERROR: No se pudo convertir {flac_file}"


def main():
    """Encuentra todos los archivos FLAC y los convierte en paralelo."""
    flac_files = list(SRC_DIR.rglob("*.flac"))

    if not flac_files:
        print("❌ No se encontraron archivos FLAC en la carpeta de origen.")
        sys.exit(1)

    print(
        f"🔍 Encontrados {len(flac_files)} archivos FLAC. Iniciando conversión..."
    )

    with concurrent.futures.ThreadPoolExecutor(
        max_workers=os.cpu_count()
    ) as executor:
        results = list(
            tqdm(
                executor.map(convert_flac_to_mp3, flac_files),
                total=len(flac_files),
            )
        )

    for result in results:
        print(result)

    print("🚀 Conversión completada.")


if __name__ == "__main__":
    main()
