from urllib import request
from pathlib import Path
from zipfile import ZipFile

def download_and_unzip(url: str, base_dir: str = "artifacts", sub_dir: str = "data_ingestion"):
    # Step 1: Create the base and sub directories (artifacts/data_ingestion)
    base_path = Path(base_dir)
    data_ingestion_path = base_path / sub_dir
    data_ingestion_path.mkdir(parents=True, exist_ok=True)

    # Step 2: Download the file into data_ingestion subfolder
    zip_file_path = data_ingestion_path / "downloaded_data.zip"
    print(f"Downloading data from {url}...")
    
    # Use urllib to download the file
    request.urlretrieve(url, zip_file_path)
    
    print(f"Downloaded file saved to {zip_file_path}")

    # Step 3: Unzip the file into the same data_ingestion folder
    print(f"Unzipping file to {data_ingestion_path}...")
    with ZipFile(zip_file_path, "r") as zip_ref:
        zip_ref.extractall(data_ingestion_path)
    
    print(f"Files extracted to {data_ingestion_path}")

    # Optional: Remove the zip file after extraction
    zip_file_path.unlink()

# Example usage
# download_and_unzip("http://example.com/path/to/your/file.zip")
