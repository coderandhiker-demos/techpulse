#!/bin/bash

# Define the container names
CRAWLER_CONTAINER_NAME="crawler-container"
WEB_API_CONTAINER_NAME="web-api-container"

# Stop and remove the crawler container if it exists
if docker ps -a --filter "name=${CRAWLER_CONTAINER_NAME}" | grep -q ${CRAWLER_CONTAINER_NAME}; then
    docker stop ${CRAWLER_CONTAINER_NAME} >/dev/null 2>&1
    docker rm ${CRAWLER_CONTAINER_NAME} >/dev/null 2>&1
    echo "Removed ${CRAWLER_CONTAINER_NAME}"
else
    echo "${CRAWLER_CONTAINER_NAME} does not exist."
fi

# Stop and remove the web-api container if it exists
if docker ps -a --filter "name=${WEB_API_CONTAINER_NAME}" | grep -q ${WEB_API_CONTAINER_NAME}; then
    docker stop ${WEB_API_CONTAINER_NAME} >/dev/null 2>&1
    docker rm ${WEB_API_CONTAINER_NAME} >/dev/null 2>&1
    echo "Removed ${WEB_API_CONTAINER_NAME}"
else
    echo "${WEB_API_CONTAINER_NAME} does not exist."
fi
