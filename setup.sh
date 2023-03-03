#!/bin/bash

if [ $# != 1 ] || [ $1 = "" ]; then
  echo "Parameter required: string for API Key (ex. 12345a6b7c8d9012345678901234567e8)"
  echo ""
  echo "example command:"
  echo "source setup.sh 12345a6b7c8d9012345678901234567e8"
  exit
fi

ARG_API_KEY=$1

export API_KEY=$ARG_API_KEY
export BASE_URL='https://financialmodelingprep.com'
export PYTHONPATH=$(pwd)

ADDED_API_KEY=$(echo $API_KEY)

if [ $ADDED_API_KEY != $ARG_API_KEY ]; then
  echo "Failed to setup API Key"
fi
echo "API Key setup is successfully."