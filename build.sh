# Purge existing
./cleanup-containers.sh

# Run commands from the root of the repo, the project toml file is shared
docker build -f src/crawler/Dockerfile -t techpulse-crawler .
docker build -f src/web-api/Dockerfile -t techpulse-web-api .