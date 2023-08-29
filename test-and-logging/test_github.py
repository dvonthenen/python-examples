# conda create -n python-examples
# conda activate python-examples
# pip install requests
from github import GitHub

def test_get_top_repo():
    github = GitHub()
    repo_url = github.get_top_repo()
    assert repo_url == "https://api.github.com/repos/public-apis/public-apis"
