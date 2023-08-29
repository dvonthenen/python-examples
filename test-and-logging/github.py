# conda create -n python-examples
# conda activate python-examples
# pip install requests
import requests
import logging

class GitHub:

    def __init__(self):
        self.base_url = "https://api.github.com"

    def get_top_repo(self):
        url = f"{self.base_url}/search/repositories"
        url += "?q=language:python+sort:stars+stars:>10000"
        headers = {"Accept": "application/vnd.github.v3+json"}

        res = requests.get(url, headers=headers)
        logging.debug(f"Status: {res.status_code}")

        response_dict = res.json()
        logging.debug(response_dict.keys())

        logging.debug("\n")

        # for key, value in response_dict.items():
        #     logging.debug(f"{key}: {value}")
        # logging.debug("\n")

        repo_dicts = response_dict["items"]
        repo_dict = repo_dicts[0]
        for key, value in repo_dict.items():
            logging.debug(f"{key}: {value}")
        logging.debug("\n\n")
        logging.debug(f"git_url: {response_dict['items'][0]['url']}")
        logging.debug(f"git_url: {response_dict['items'][0]['git_url']}")
        logging.debug(f"git_url: {response_dict['items'][0]['owner']}")

        return response_dict["items"][0]["url"]
