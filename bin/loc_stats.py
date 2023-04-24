from pathlib import Path
import pandas as pd
import json


# grab data
data_dir = Path(__file__).parent.parent / 'data'
with open(data_dir / 'repo_loc_info_230423.json', 'r') as f:
    data = json.load(f)

lang_set = set()
for repo in data.values():
    for lang in repo:
        if not isinstance(lang, dict):
            continue
        lang_set.add(lang['language'])

lang_detail_columns = set(lang.keys())
lang_detail_columns.remove('language')

index = pd.MultiIndex.from_product([lang_set, lang_detail_columns],names=['language', 'info'])
df = pd.DataFrame(index=index, columns=data.keys())
# -> reponame
# v  language / info

# fill out information
for reponame, info in data.items():
    for data_dict in info:
        if isinstance(data_dict, str):
            continue
        for data_key, value in data_dict.items():
            if data_key == 'language':
                continue

            df.loc[(data_dict['language'], data_key), reponame] = value

# sample queries
#: to get a repo's information
# print(df['pcdsdevices'].dropna().to_string())

#: flatten on reponame
# # Sum across columns
# sum_df = df.sum(axis=1, skipna=True)
# # Plot 