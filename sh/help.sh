#!/usr/bin/env bash

if [[ $# != 3 ]] || [[ $1 == '--help' ]]; then
    me="$(basename "$(test -L "$0" && readlink "$0" || echo "$0")")"
    echo "Usage: $me \$host \$protocol \$transaction."
    echo "       host: hostname or IP address on current node."
    echo "       protocol: two choices, http and https."
    echo "       transaction: mail, purchase, etc."
fi

