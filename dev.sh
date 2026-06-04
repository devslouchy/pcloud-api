#!/bin/bash

echo "Starting Personal Cloud Environment..."

if [-d "venc" ]; then
    echo "Avtivating Virtual environment"
    source .venv/bin/activate
fi

docker compose up -d --build

docker compose logs -f
