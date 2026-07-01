import requests
import gzip
import shutil

print("Downloading dataset...")

url = "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE53nnn/GSE53757/matrix/GSE53757_series_matrix.txt.gz"

response = requests.get(url, verify=False)

with open("data.txt.gz", "wb") as f:
    f.write(response.content)

print("Unzipping...")
with gzip.open("data.txt.gz", "rb") as f_in:
    with open("data.txt", "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)

print("Done! Dataset saved as data.txt ✅")