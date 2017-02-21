#!/usr/bin/env bash


function find_latest_commit_component()
{
    local __latest_update_component=$1
    local git_repo_mix_list=""
    local commit_date_list=""
    for component in $(ls);do
        if [[ ! -d $component || -L $component ]];then
            continue
        fi
        cd $component >/dev/null
        if git log -1 &>/dev/null;then
            local commit_date=$(git log -1 | grep Date | sed 's/^Date:\s//')
            local commit_date_no_tz_w=${commit_date%-*}
            local commit_date_no_tz_e=${commit_date_no_tz_w%+*}
            local commit_date_numeric=$(date -d "$commit_date_no_tz_e" +"%Y%m%d%H%M%s")
            commit_date_list=$commit_date_list" "$commit_date_numeric
            git_repo_mix_list=$git_repo_mix_list" "$component":"$commit_date_numeric
        fi
        cd - >/dev/null
    done

    echo $commit_date_list
    local latest_commit=
    for date in $commit_date_list;do
        if [[ $date > $latest_commit ]];then
            latest_commit=$date
        fi
    done

    echo "latest commit is: $latest_commit"
    for mix in $git_repo_mix_list;do
        local mix_date=$(echo $mix | awk -F ":" '{print $2}')
        if [[ $mix_date -eq $latest_commit ]];then
            local latest_module=$(echo $mix | awk -F ":" '{print $1}')
            echo "related component is: $latest_module"
            break
        fi
    done

    eval $__latest_update_component="'$latest_module'"
}


find_latest_commit_component which_one
echo $which_one
