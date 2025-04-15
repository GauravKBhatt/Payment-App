import requests
from pathlib import Path

#accepts the url from where to download and accepts the path where the dowloading is going to be performed. Ocassionally creates parent directory if it does not exist. 

def download_to_local(url:str, out_path:Path, parent_mkdir:bool=True):
    if not isinstance(out_path,Path):
        raise ValueError(f"{out_path} must be a valid pathlib.path object")
    if parent_mkdir:
        out_path.parent.mkdir(parents=True,exist_ok=True)
    try:
        response = requests.get(url)
        response.raise_for_status()
        #Write the file out in binary mode to prevent any conversions
        out_path.write_bytes(response.content)
        return True
    except requests.RequestException as e:
        print(f'Failed to download {url}:{e}')
        return False
    # Now we will make custom DJango Management Command to Pull Vendor Files.