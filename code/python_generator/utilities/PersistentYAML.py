import yaml

class PersistentYAML:
    def __init__(self, file_path: str):
        """
        Loads a YAML file into a dictionary-like object that persists.
        
        Args:
            file_path (str): Path to the YAML file.
        """
        self.file_path = file_path
        self.data = self._load_yaml(file_path)

    def _load_yaml(self, file_path: str) -> dict:
        """
        Loads the YAML content into a dictionary.
        
        Args:
            file_path (str): Path to the YAML file.
        
        Returns:
            dict: The parsed YAML content as a dictionary.
        """
        try:
            with open(file_path, 'r') as file:
                return yaml.safe_load(file)
        except Exception as e:
            print(f"Error loading YAML file: {e}")
            return {}

    def __getattr__(self, name):
        """
        Allows access to YAML data via dot notation (e.g., my_yaml.attribute.subattribute).
        This method handles dynamic attribute access.
        
        Args:
            name (str): The attribute name to access.
        
        Returns:
            The attribute value, or raises an AttributeError if not found.
        """
        # Check if the name exists in the data
        if name in self.data:
            return self.data[name]
        
        # Handle nested attributes if the name is not found directly
        def get_nested_attribute(keys):
            result = self.data
            for key in keys:
                result = result.get(key, None)
                if result is None:
                    return None
            return result

        # Split the name into nested attributes (dot-separated)
        nested_keys = name.split('.')
        return get_nested_attribute(nested_keys)

    def reload(self):
        """
        Reloads the YAML file to refresh the data.
        """
        self.data = self._load_yaml(self.file_path)