docker run --rm \
    -e "OPENAI_API_KEY=$OPENAI_API_KEY" \
    -e "YOUTUBE_API_KEY=$YOUTUBE_API_KEY" \
    -v $(pwd)/source:/app/source:ro \
    -v $(pwd)/output:/app/output \
    -v $(pwd)/config:/app/config:ro \
    python_generator