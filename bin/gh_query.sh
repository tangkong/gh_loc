#!/bin/bash
sudo gh api \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
    /orgs/pcdshub/repos > gh_loc/repo_info.json