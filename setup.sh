#!/bin/bash

if [ $# != 2 ] || [ $1 = "" ]; then
  echo "Parameter required: string for API Key"
  echo ""
  echo "example command:"
  echo "source setup.sh '12345a6b7c8d9012345678901234567e8' '0123abcd456789012345678901234567e8'"
  exit
fi

ARG_API_KEY=$1
ARG_SEARCH_API_KEY=$2

export API_KEY=$ARG_API_KEY
export SEARCH_API_KEY=$ARG_SEARCH_API_KEY
export BASE_URL='https://financialmodelingprep.com'

ADDED_API_KEY=$(echo $API_KEY)
ADDED_SEARCH_API_KEY=$(echo $SEARCH_API_KEY)

if [ $ADDED_API_KEY != $ARG_API_KEY ] || [ $ADDED_SEARCH_API_KEY != $ARG_SEARCH_API_KEY ]; then
  echo "Failed to setup API Key"
fi
echo "API Key setup is successfully."