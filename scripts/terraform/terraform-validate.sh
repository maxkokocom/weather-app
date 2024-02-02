#!/usr/bin/env bash

readonly PROGDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source "$PROGDIR/common.shlib"

terraform validate