The main script generates the content for a "cognitive warmup".

Input:
 - config/tasking.yaml :: A list of tasks, complete with prompt, model, temperature, role, and other configuration information.
 - source/* :: A variety of source material populated by the user to tailor the warmup content.

Output:
 - output/* :: A unique text file is generated for each task, usually containing a question.