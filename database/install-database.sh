#!/bin/bash

ERRORS=""
RED='\033[0;31m'
YELLOW='\033[1;33m'
NO_COLOR='\033[0m'

# Check for PG_PYTHON_DBCONNECTION environment variable
if [ -z "${PG_PYTHON_DBCONNECTION}" ]; then
    ERRORS="${ERRORS}${RED}Error: PG_PYTHON_DBCONNECTION is not set.${NO_COLOR}"
    ERRORS="${ERRORS}${YELLOW}\nPlease set it using the following command:"
    ERRORS="${ERRORS}\nexport PG_PYTHON_DBCONNECTION='your_connection_string_here'${NO_COLOR}"
fi

# Add extra newline if ERRORS is already set
if [ ! -z "$ERRORS" ]; then
    ERRORS="${ERRORS}\n"
fi

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

# Get a list of all .sql scripts in the current directory, sorted by their prefix number
SQL_SCRIPTS=$(ls | grep -E '^[0-9]+_.*\.sql$' | sort -n)

# Count scripts for final message
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
echo "$NumScripts scripts have been executed."
