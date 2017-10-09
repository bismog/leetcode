#!/usr/bin/env bash


echo "current script is ${BASH_SOURCE[0]}"
echo "Also we can say current script is ${BASH_SOURCE}."

path_from_bash_source="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
path_from_param_0="$( cd "$( dirname "$0" )" && pwd )"


echo "path_from_bash_source: $path_from_bash_source"
echo "path_from_param_0: $path_from_param_0"

current_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
current_script="$(basename "${BASH_SOURCE[0]}")"

echo "current directory: $current_dir"
echo "current script: $current_script"
