#!/bin/bash

# Default values
NO_CACHE=""

# Function to display usage information
show_help() {
  echo "Usage: $0 [options]"
  echo "Options:"
  echo "  -h, --help     Display this help message."
  echo "  --no-cache     Build Docker images without using cache."
}

# Parse command-line arguments
while [[ $# -gt 0 ]]; do
  case "$1" in
    --no-cache)
      NO_CACHE="--no-cache"
      shift
      ;;
    -h|--help)
      show_help
      exit 0
      ;;
    *)
      echo "Unknown option: $1"
      show_help
      exit 1
      ;;
  esac
done

# Purge existing
./cleanup-containers.sh

# Build Docker images with optional --no-cache flag
docker build $NO_CACHE -f src/crawler/Dockerfile -t techpulse-crawler:dev .
docker build $NO_CACHE -f src/web-api/Dockerfile -t techpulse-web-api:dev .
