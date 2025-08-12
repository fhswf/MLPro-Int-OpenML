import httpx
import os
import sys

def get_dataset_patched(dataset_id, download_dir="./downloads", timeout=10):
    """
    Einfacher OpenML-Dataset-Downloader ohne Range-Requests.
    Holt Metadaten über die API und lädt die Datei in einem Rutsch.
    """

    base_meta_url = f"https://api.openml.org/v1/json/data/{dataset_id}"
    print(f"Fetching metadata for dataset {dataset_id}...")

    try:
        with httpx.Client(timeout=timeout) as client:
            meta_resp = client.get(base_meta_url)
            meta_resp.raise_for_status()
            meta_json = meta_resp.json()
    except Exception as e:
        print(f"❌ Fehler beim Abrufen der Metadaten: {e}")
        sys.exit(1)

    # File-ID und Name ermitteln
    try:
        file_id = meta_json['data_set_description']['file_id']
        file_name = meta_json['data_set_description']['file_id'] + ".arff"
    except KeyError:
        print(f"❌ Metadaten enthalten keine gültigen Dateiinfos für Dataset {dataset_id}")
        sys.exit(1)

    # Download-URL
    url = f"https://api.openml.org/data/v1/download/{file_id}/{file_name}"
    print(f"Downloading dataset {dataset_id} from {url}...")

    os.makedirs(download_dir, exist_ok=True)
    file_path = os.path.join(download_dir, file_name)

    try:
        with httpx.Client(timeout=timeout) as client:
            r = client.get(url)
            if r.status_code == 404:
                print(f"❌ Datei nicht gefunden (404): {url}")
                sys.exit(1)
            r.raise_for_status()
            with open(file_path, "wb") as f:
                f.write(r.content)
    except Exception as e:
        print(f"❌ Fehler beim Download: {e}")
        sys.exit(1)

    print(f"✅ Dataset {dataset_id} gespeichert unter: {file_path}")
    return file_path


if __name__ == "__main__":
    # Beispielaufruf
    get_dataset_patched(1477, download_dir="./downloads")
