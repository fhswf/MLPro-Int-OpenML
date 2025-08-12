import os
import httpx


def _get_file_info(dataset_id: int):
    """
    Versucht aus der OpenML-JSON-API die file_id + filename zu holen.
    Falls nicht vorhanden, nutzt er den 'url'-Fallback.
    """
    api_url = f"https://www.openml.org/api/v1/json/data/{dataset_id}"
    try:
        with httpx.Client(timeout=30.0, verify=False) as client:  # verify=True wenn möglich
            r = client.get(api_url)
            r.raise_for_status()
            data = r.json()
    except Exception as e:
        raise RuntimeError(f"Fehler beim Abrufen der Metadaten von {api_url}: {e}")

    desc = data.get("data_set_description", {})
    file_id = desc.get("file_id")
    filename = desc.get("file")
    url = desc.get("url")

    if file_id and filename:
        return file_id, filename, None
    elif url:
        return None, None, url
    else:
        raise ValueError(
            f"Dataset {dataset_id} hat weder file_id noch file noch url – möglicherweise nicht mehr verfügbar."
        )


def get_dataset_patched(dataset_id: int, download_dir: str = "./downloads"):
    """
    Lädt ein Dataset von OpenML herunter (mit robustem Fallback, falls file_id fehlt).
    Gibt den lokalen Dateipfad zurück.
    """
    print(f"Fetching metadata for dataset {dataset_id}...")
    file_id, filename, direct_url = _get_file_info(dataset_id)

    if direct_url:
        download_url = direct_url
    else:
        download_url = f"https://www.openml.org/data/download/{file_id}/{filename}"

    # Zielverzeichnis vorbereiten
    os.makedirs(download_dir, exist_ok=True)
    local_filename = os.path.join(download_dir, filename if filename else os.path.basename(download_url))

    print(f"Downloading dataset {dataset_id} from {download_url}...")
    try:
        with httpx.stream("GET", download_url, timeout=60.0, verify=False) as r:
            if r.status_code == 404:
                raise FileNotFoundError(f"Dataset-Datei unter {download_url} nicht gefunden (404).")
            r.raise_for_status()
            with open(local_filename, "wb") as f:
                for chunk in r.iter_bytes():
                    f.write(chunk)
    except Exception as e:
        raise RuntimeError(f"Fehler beim Download von {download_url}: {e}")

    print(f"Dataset gespeichert unter: {local_filename}")
    return local_filename


if __name__ == "__main__":
    # Beispielaufruf
    try:
        ds_path = get_dataset_patched(1477, download_dir="./downloads")
        print(f"✅ Download abgeschlossen: {ds_path}")
    except Exception as e:
        print(f"❌ Fehler: {e}")
