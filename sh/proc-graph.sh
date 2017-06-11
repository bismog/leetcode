#!/usr/bin/env bash
# -*- coding:utf-8 -*-

echo "digraph proc { `ps axo ppid,pid | sed "s/\b / -> /g" | grep -v "PID"` } " >> proc.gv
dot -T png proc.gv -o proc.png
