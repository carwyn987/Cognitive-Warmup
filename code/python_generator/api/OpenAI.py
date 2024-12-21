import openai
from typing import AnyStr, Dict

class OpenAI:
    def __init__(self, api_key: str):
        """
        Initializes the OpenAI client with the provided API key.
        """
        openai.api_key = api_key

    def text_request(self, question_content: str, model: str = "gpt-4o-mini", role: str = "system", role_content: str = "You are a helpful assistant.") -> str:
        """
        Calls the OpenAI API to generate a text completion based on a system/user message pair.
        """
        try:
            completion = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": role, "content": role_content},
                    {"role": "user", "content": question_content}
                ]
            )
            return completion.choices[0].message['content']
        except Exception as e:
            print(f"Error during API call: {e}")
            return ""

    def real_time_request(self, endpoint: str, parameters: Dict[str, AnyStr]) -> Dict:
        """
        Sends a real-time API request to OpenAI, allowing for flexible interaction with different endpoints.
        """
        # try:
        #     response = openai.api_request(endpoint, params=parameters)
        #     return response
        # except Exception as e:
        #     print(f"Error during real-time API request: {e}")
        #     return {}
        return NotImplementedError()