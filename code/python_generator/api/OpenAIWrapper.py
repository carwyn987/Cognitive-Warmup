from openai import OpenAI
from typing import AnyStr, Dict

def text_request(api_key, question_content: str, model: str = "gpt-4o-mini", role_content: str = "You are a helpful assistant.", temperature: float = 2.0) -> str:
    """
    Calls the OpenAI API to generate a text completion based on a system/user message pair.
    """
    try:
        client = OpenAI(api_key=api_key)
        completion = client.chat.completions.create(model=model,
        messages=[
            {"role": "system", "content": role_content},
            {"role": "user", "content": question_content}
        ],
        temperature=temperature)
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error during API call: {e}")
        return ""

def real_time_request(api_key, endpoint: str, parameters: Dict[str, AnyStr]) -> Dict:
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