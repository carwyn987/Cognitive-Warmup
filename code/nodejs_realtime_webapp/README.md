Web application supporting the UI for the "cognitive warmup".

In particular:
 - An ephemeral server is spun up in order for the client to mint ephemeral tokens.
 - An nginx web server is spun up containing a basic web ui, accessing the microphone and enabling comms with the OpenAI realtime service.

# Jenkins Job
http://localhost:8080/job/cognitive_warmup_nodejs_realtime/

# WebRTC
https://platform.openai.com/docs/guides/realtime-webrtc

# Ephemeral Server
https://platform.openai.com/docs/guides/realtime-webrtc#creating-an-ephemeral-token

# OpenAI Pricing
https://openai.com/api/pricing/