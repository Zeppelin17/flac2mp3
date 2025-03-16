# flac2mp3 File Converter

Python script to convert Flac files to Mp3. All files within the source directory (including any subdirectories) will be converted and copied with the same tree structure in the destination folder.

## Prepare the script

After cloning the repo, prepare virtual environment:

```bash
python -m venv .venv
```

Activate environment install dependencies and give permissions

```bash
source .venv/bin/activate
pip install -r requirements.txt
chmod +x main-flac-converter.py
```

## Modify script

Validate the path defined in SRC_DIR and DEST_DIR.

## Ready to proceed

You are ready to convert files:

```bash
python main-flac-converter.py
```
