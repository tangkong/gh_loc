from pathlib import Path
import asyncio
import aiohttp
import json
import requests
import time
import pandas as pd

with open(Path(__file__).parent.parent / 'data' / 'repo_names.json', 'r') as f:
    names = json.load(f) 

loc_url = 'https://api.codetabs.com/v1/loc?github={org}/{reponame}'

info_df = pd.DataFrame(columns=['repo_name', 'loc'])
# for reponame in names:
#     response = requests.get(loc_url.format(org='pcdshub', reponame=reponame))
#     print(reponame, response.status_code)

#     repo_info  = response.json()

#     break

start_time = time.time()
# need to delay requests by 5 s, server restrictions
next_delay = 0.1
delay = 5


async def make_request(session, reponame: str):
    global next_delay
    next_delay += delay
    await asyncio.sleep(next_delay)
    url = loc_url.format(org='pcdshub', reponame=reponame)
    async with session.get(url) as resp:
        loc_info = await resp.json(content_type=None)
        print(reponame, len(loc_info))
        return {reponame: loc_info}


async def main():
    with open(Path(__file__).parent.parent / 'repo_names.json', 'r') as f:
        names = json.load(f)

    final_info = {}
    async with aiohttp.ClientSession() as session:
        tasks = []
        for name in names:
            tasks.append(asyncio.ensure_future(make_request(session, name)))

        all_info = await asyncio.gather(*tasks)
        for info in all_info:
            final_info.update(info)
    # with open(Path(__file__).parent / 'repo_loc_info.json', 'w') as fw:
    #     json.dump(final_info, fw, indent=4)
    # print(final_info.keys())

    return final_info

info = asyncio.run(main())

print(f"{time.time() - start_time} seconds ")