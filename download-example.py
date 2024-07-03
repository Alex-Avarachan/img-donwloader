import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
from multiprocessing.pool import ThreadPool as Pool
import imghdr

def is_jpeg(file_path):
  """Returns True if the file is a JPEG image, False otherwise."""
  return imghdr.what(file_path) == 'jpeg'

def download():

    url = "https://hyd69.com/wp-content/uploads/2023/10/IMG-20231002-WA0003.jpg"
    print(url)
    pathname = "/Users/alex/Documents/PythonDownloadImg/IMG/"
    """
    Downloads a file given an URL and puts it in the folder `pathname`
    """
    # if path doesn't exist, make that path dir
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    # download the body of response by chunk, not immediately
    response = requests.get(url, stream=True)
    print("url " + url)

    print(response.status_code)

    if(response.status_code != 200):
        return

    # get the total file size
    file_size = int(response.headers.get("Content-Length", 0))
    print(file_size)

    # get the file name
    filename = os.path.join(pathname, url.split("/")[-1])


    # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
    progress = tqdm(response.iter_content(1024), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress.iterable:
            # write data read to the file
            f.write(data)
            # update the progress bar manually
            progress.update(len(data))
    if is_jpeg:
        

if __name__ == "__main__":
    download()