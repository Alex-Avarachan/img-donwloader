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

def download(url, pathname):
    """
    Downloads a file given an URL and puts it in the folder `pathname`
    """
    # if path doesn't exist, make that path dir
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    # download the body of response by chunk, not immediately
    response = requests.get(url, stream=True)

    if response.status_code != 200:
        return

    # get the total file size
    file_size = int(response.headers.get("Content-Length", 0))

    if file_size < 30000:
        return

    # get the file name
    filename = os.path.join(pathname, url.split("/")[-1])


    # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
    progress = tqdm(response.iter_content(1024), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress.iterable:
            # write data read to the file
            if(file_size!=0):
                f.write(data)
            # update the progress bar manually
            progress.update(len(data))



pool_size = 100
pool = Pool(pool_size)

for j in reversed(range (23,24)):
    for k in range (8,12):
        for l in range (1,32):
            for i in range(1,100):
                month = "0"+str(k) if k<10 else str(k)
                day = "0"+str(l) if l<10 else str(l)
                num = "0"+str(i) if i<10 else str(i)
                url = "https://indiansexservices.com/wp-content/uploads/20"+str(j)+"/"+str(month)+"/IMG-20"+str(j)+str(month)+str(day)+"-WA00"+str(num)+".jpg"
                path = "/Users/alex/Documents/PythonDownloadImg/IMG/ISS/"+str(k)
                pool.apply_async(download, (url,path,))

pool.close()
pool.join()






