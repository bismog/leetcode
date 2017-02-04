#!/usr/bin/env bash

# http://unix.stackexchange.com/questions/281309/shell-syntax-how-to-correctly-use-to-break-lines
# If the statement would be correct without continuation, you need to use \. Therefore, the following works without a backslash, as you can't end a command with a &&:
# echo 1 &&
# echo 2
# Here, you need the backslash:
# echo 1 2 3 \
# 4
# or
# echo 1 \
# && echo 2
# Otherwise, bash would execute the command right after processing the first line without waiting for the next one.

for x in "a b c d e f g h i j k l m n
          o p q r s t u v w x y z";do
    echo $x
done
