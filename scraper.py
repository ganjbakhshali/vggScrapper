import glob
import os
import requests
from urllib.error import HTTPError
from urllib.request import urlretrieve
import time

def load_requests(source_url, sink_path):
    """
    Load a file from an URL (e.g. http).

    Parameters
    ----------
    source_url : str
        Where to load the file from.
    sink_path : str
        Where the loaded file is stored.
    """
    import requests
    r = requests.get(source_url, stream=True,timeout=15)
    if r.status_code == 200:
        with open(sink_path, 'wb') as f:
            for chunk in r:
                f.write(chunk)

txt_files = glob.glob("*.txt")
print(txt_files)
for item in txt_files:
    print(item)
    name=item.split(".")
    tic = time.perf_counter()
    with open(item) as f:
        content = f.readlines()
        for line in content:
            li=line.split()
            nametosave=name[0]+"_"+li[0]+".jpg"
            url=li[1]
            print(li[0])
            if "blogspot" in url or "moviefanatic" in url or "sabideli" in url or "kansascity" in url:
                continue
            try:
                # urlretrieve(url, nametosave)
                load_requests(url,nametosave)
            except FileNotFoundError as err:
                print(err)   # something wrong with local path
            except HTTPError as err:
                print(err)  # something wrong with url
            except IOError:
                print ('Failed to open url. IOError')
            except ConnectionError:
                print ('Failed to open url.')
    
    toc = time.perf_counter()
    print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")
