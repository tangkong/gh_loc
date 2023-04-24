from pathlib import Path
import asyncio
import aiohttp
import json
import requests
import time
import pandas as pd

with open(Path(__file__).parent.parent / 'data' /  'repo_names.json', 'r') as f:
    names = json.load(f) 

loc_url = 'https://api.codetabs.com/v1/loc?github={org}/{reponame}'
info_df = pd.DataFrame(columns=['repo_name', 'loc'])
start_time = time.time()
def make_request(reponame: str):
    url = loc_url.format(org='pcdshub', reponame=reponame)
    resp = requests.get(url)
    loc_info = resp.json()
    print(reponame, len(loc_info))
    return {reponame: loc_info}


def main():
    names = []
    with open(Path(__file__).parent / 'gh_repolist.json', 'r') as f:
        for line in f:
            names.append(line.strip().strip('\"'))
    print(f'found {len(names)} repos')

    final_info = {}
    for name in names:
        info = make_request(name)
        final_info.update(info)
    with open(Path(__file__).parent / 'repo_loc_info.json', 'w') as fw:
        json.dump(final_info, fw, indent=4)
    print(len(final_info.keys()))

    return final_info

info = main()
print(f"{time.time() - start_time} seconds ")