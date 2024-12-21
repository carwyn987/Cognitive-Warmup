import os
from typing import List

class LoadSecrets:
    def __init__(self, search_attributes: List[str] = ['openai']):
        self.search_attributes = search_attributes
        self.load_secrets()
    
    def load_secrets(self):
        """
        Searches for API keys based on the attributes in `search_attributes`.
        It tries different case formats (all caps, all lowercase, with '_API_KEY' appended) and assigns the keys
        as object-level variables.
        """
        for attribute in self.search_attributes:
            # Create the possible variations of the environment variable names
            possible_keys = [
                f"{attribute.upper()}_API_KEY",    # Uppercase with '_API_KEY'
                f"{attribute.lower()}_api_key"     # Lowercase with '_api_key'
            ]
            
            # Check the system's environment for each variation
            for key in possible_keys:
                value = os.getenv(key)
                if value:  # If a value is found
                    # Dynamically set the attribute on the object
                    setattr(self, attribute, value)
                    break  # If one of the keys is found, stop searching further for this attribute