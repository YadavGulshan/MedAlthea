#!/usr/bin/env bash

export $(cat .env | xargs)
echo "Environment variables exported"
