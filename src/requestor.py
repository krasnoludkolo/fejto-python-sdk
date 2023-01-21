import json
from typing import Dict, List

import requests

base_url = "https://api.hejto.pl"


class Requestor:

    def make_request(self, path_parts: List[str], query_params=None) -> Dict:
        if query_params is None:
            query_params = {}
        final_path = base_url
        if len(path_parts) > 0:
            final_path += "/" + "/".join(path_parts)
        if len(query_params) > 0:
            final_path += "?" + "&".join([f"{key}={value}" for key, value in query_params.items()])
        response = requests.get(final_path)
        print(f"final_path:{final_path}")
        print(f"response:{response.text}")
        return json.loads(response.text)
