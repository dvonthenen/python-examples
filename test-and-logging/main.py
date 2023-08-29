# conda create -n python-examples
# conda activate python-examples
# pip install requests
from github import GitHub
import logging

logging.basicConfig(level=logging.INFO)

github = GitHub()
repo_url = github.get_top_repo()
logging.info(f"top repo: {repo_url}")
