docker run --rm -it \
    -e "OPENAI_API_KEY=$OPENAI_API_KEY" \
    -e "YOUTUBE_API_KEY=$YOUTUBE_API_KEY" \
    -v $(pwd)/../../source:/app/source:ro \
    -v $(pwd)/../../generated:/app/output \
    python_generator:0.0.2