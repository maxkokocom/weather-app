#!/usr/bin/env bash

readonly PROGDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source "$PROGDIR/common.shlib"

if [ ! -e ".terraform/planfile-${CLOUD}-${ENV}" ]; then
    echo "Error: plan file not found, please run terraform plan first"
    exit 1
fi

terraform apply -input=false ".terraform/planfile-${CLOUD}-${ENV}" "$@"
