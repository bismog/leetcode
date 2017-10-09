#!/usr/bin/env bash
# -*- coding: utf-8 -*-

temp_json=$(mktemp)
python mysql2json_ex.py $temp_json
ansible-playbook -e "json_file=$temp_json" ssh_mutual_authorization.yml
