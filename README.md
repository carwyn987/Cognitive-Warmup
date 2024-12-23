# Cognitive-Warmup

I choose to begin work early, so I can enjoy sunlight hours afterwards. However, I encountered an issue - every morning, I'm accosted by co-workers wanting to small talk about the weather and the winds. Despite my prior verbiage, I do want to talk to my coworkers in the morning, just not about that. Furthermore, when it's time for my response, I'm usually too tired to come up with answers that jolt people out of their rhythm and inspire thought provoking conversation. In other words, I'm a part of the problem. This repo is dedicated to developing a daily tool to warm up your cognitive abilities, speech patterns, and provide a jump-off point for interesting conversation.

This app will produce a "cognitive warmup" according to a cron schedule, likely once every day. Generated content will consist of various questions, possibly including fermi questions, soft-skill probing questions, interview-like questions, questions about documents uploaded to source folder. It will also include some related content to consume, likely scraped from the html sources included in this list, and related to personal documents uploaded. The Minimum Viable Product (MVP) will be text-based, providing content as a document. Then, an interactive speech-based tool will be developed to improve interactivity.

# Example MVP Generated Content (Real):
```
**Fermi Question:**

If we consider that the human brain has an approximate computational upper bound of 100 billion neurons and each neuron can form about 1,000 connections (synapses) with other neurons, how many total synapses could be formed in the human brain? 

Assuming that each synapse can transmit about one signal per second, how many total signals could the brain theoretically transmit in a 24-hour period? 

Please calculate the total number of synapses and the total number of signals transmitted in one day.
```

## Sources of generation (future)
 - Recent public github updates
 - Recent posts or status updates from various platforms - X, FB, LinkedIn
 - Documents uploaded to `source` folder
  - Shower thoughts
  - Philisophical questions - perhaps epistemological
 - Questions referring to recent consumed academic works - likely learned from scanning ones Obsidian Vault
 - Questions related to works in provided newsletters, or listed websites (LessWrong)

## System MVP
 - Load txt files from `./source` folder
 - Merge content in a `Content` object
 - Using `Content` object, generate various desirables
 - Return generated content to generated folder

## Full System Goal

 - Load Stage
  - Load txt files from `./source` folder
  - Load Obsidian notes
  - Load recent news http sources
  - Load recent github updates
  - Personal pdf documents
  - ...
 - Merge content in a `Content` object
 - Using `Content` object, generate initial desirables (probing questions)
 - Send these to OpenAI Realtime communicator
  - Provide interactive web app and record transcript
 - After conversation finish, prompt user with retrospective analysis of conversation
  - Speech improvement, filler words, repetitive words, content compression
 - Provide user with final "news-like" content for awareness and further prompting for the day

## Configuration

Only the OpenAI key is strictly necessary. Secrets are loaded from environment variables, which must be set with e.g.

`export OPENAI_API_KEY=<INSERT_OPENAI_KEY_HERE>`

## Project Links (For personal development, not public access)
 - https://platform.openai.com/settings/organization/usage
 - http://localhost:8080/job/cognitive_warmup_python_generator/