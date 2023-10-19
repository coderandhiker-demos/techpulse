#!/bin/bash

# Check if the PostgreSQL service is running, start if not
if systemctl is-active --quiet postgresql; then
    echo "PostgreSQL service is running."
else
    echo "PostgreSQL service is not running. Restart using: sudo service postgresql restart"
    exit 1
fi

ERRORS=""
RED='\033[0;31m'
YELLOW='\033[1;33m'
NO_COLOR='\033[0m'

# PostgreSQL connection parameters
DB_HOST="127.0.0.1"
DB_PORT="5432"
DB_USERNAME="postgres"
DB_NAME="techpulse"

# Define the PostgreSQL connection string
PG_PYTHON_DBCONNECTION="postgresql://$DB_USERNAME@$DB_HOST:$DB_PORT/$DB_NAME"

# Check for psql tool
if ! command -v psql &> /dev/null; then
    ERRORS="${ERRORS}${RED}\nError: psql command is not found.${NO_COLOR}"
    ERRORS="${ERRORS}${YELLOW}\nPlease install it on Ubuntu using the following command:"
    ERRORS="${ERRORS}\nsudo apt update && sudo apt install postgresql-client${NO_COLOR}"
fi

if [ ! -z "$ERRORS" ]; then
    echo -e "$ERRORS"
    exit 1
fi

# Create the database if it doesn't exist
echo "Creating database $DB_NAME if it doesn't exist..."
createdb $DB_NAME

# Get a list of all .sql scripts in the current directory, sorted by their prefix number
SQL_SCRIPTS=$(ls | grep -E '^[0-9]+_.*\.sql$' | sort -n)

# Count scripts for the final message
NumScripts=$(echo "$SQL_SCRIPTS" | wc -l)

# Loop through and execute each SQL script
for script in $SQL_SCRIPTS; do
    echo "Executing $script..."
    psql "${PG_PYTHON_DBCONNECTION}" -f "$script"
    if [ $? -ne 0 ]; then
        echo "Error executing $script. Aborting."
        exit 1
    fi
done

# Display only the hostname and database name in the final message
echo "$NumScripts scripts have been executed in database $DB_NAME."
