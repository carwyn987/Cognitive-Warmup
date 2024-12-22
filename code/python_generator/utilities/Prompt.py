class Prompt:
    def __init__(self, generator_name, command, content):
        """
        Initialize with the generator name (combiner), command, and content.
        """
        self.combiners = {
            "combine_with_context": self.combine_with_context,
            "combine_simple": self.combine_simple
        }
        self.generator_name = generator_name  # Name of the combiner
        self.command = command
        self.content = content
        self.prompt = self.combine()

    def combine(self):
        """Select the appropriate combiner based on the generator name."""
        # Default to a simple combiner if the specified one isn't found
        combiner = self.combiners.get(self.generator_name, self.combine_simple)
        return combiner()

    def combine_with_context(self):
        """Combine command and content with additional context."""
        return (
            f"{self.command} Use the following context for inspiration, "
            f"which begins and ends with \"\"\" and follows the format filename\\n content:\n"
            f"\"\"\"\n{self.content}\n\"\"\""
        )

    def combine_simple(self):
        """Combine command and content without additional context."""
        return f"{self.command}:\n{self.content}"

    def get_prompt(self):
        """Return the combined prompt."""
        return self.prompt
