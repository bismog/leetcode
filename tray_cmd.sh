#!/bin/sh
ERRTRAP()
{
  echo "[LINE:$1] Error: Command or function exited with status $?"
}
foo()
{
  return 7;
}
trap 'ERRTRAP $LINENO' ERR
abc
foo
