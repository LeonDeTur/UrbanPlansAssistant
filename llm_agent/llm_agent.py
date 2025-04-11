import json

import requests


class LlmAgent:
    """Large language model class"""

    def __init__(
            self,
            client_cert: str,
            client_key: str,
            ca_cert: str,
    ) -> None:

        self.client_cert = client_cert
        self.client_key = client_key
        self.ca_cert = ca_cert
        self.base_url="http://a.dgx:11434"
        self.headers = {
            "Content-Type": "application/json"
        }

    def request_from_llm(self, model: str, prompt: str) -> str:
        """
        Function extracts prompt from llm api
        Args:
            model (str): llm model name to extract request from
            prompt (str): prompt to execute
        Returns:
            str: request from llm
        """

        data = {
            "model": model,
            "prompt": prompt,
            "stream": False,
        }
        response = requests.post(
            url=f"{self.base_url}/api/generate",
            headers=self.headers,
            data=json.dumps(data),
            cert=(self.client_cert, self.client_key),
            verify=self.ca_cert
        )

        if response.status_code == 200:
            return response.json()["response"]
        return ""


client_cert = "20250129_IDU_ADGX_LeonTur.crt"
ca_cert = "onti-ca.crt"
client_key = "DECFILE"

tmp_llm_model = LlmAgent(client_cert, client_key, ca_cert)
