from .llm_agent import tmp_llm_model


class OllamaClient:

    @staticmethod
    def chat(prompt, data):

        prompt = f"{prompt}\n\nДанные:\n{data}"
        response = tmp_llm_model.request_from_llm("llama3.3", prompt)
        return response


ollama_client = OllamaClient()
