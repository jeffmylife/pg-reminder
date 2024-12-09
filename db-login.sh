#!/bin/bash
set -a
source .env
set +a
PGPASSWORD="$DB_PASSWORD" psql "postgres://$DB_USER@$DB_HOST:$DB_PORT/$DB_NAME?sslmode=require"