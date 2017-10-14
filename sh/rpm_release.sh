#!/usr/bin/env bash
# -*- coding: utf-8 -*-

package=$1              # Path to package file, such as /tmp/scsi-target-utils-1.0.46-3.el7.x86_64.rpm
project=$2              # 'projectxxx' or 'project0xxx'
branch=$3               # For projectxxx, it may be
                        # For project0xxx, it may be 'p8', 'dev' or 'dev3.0'

REPOBASE=10.43.177.198
package_name=$(rpm --query-format '%{NAME}' -qp ${package})

case $project in
    projectxxx)
    target_path=/var/www/html/repo/yum/projectxxx
    case $branch in
        usf)
        list_name=contrib_rpm.usf.list
        tar_name=contrib_rpm.usf.tar.gz
        ;;

        p8b*)
        list_name=contrib_rpm.list
        tar_name=contrib_rpm.tar.gz
        ;;

        *)
        # help_for_me
        ;;

    project0xxx)
    case $branch in
        p8)
        target_path=/var/www/html/repo/yum/project0xxx/20
        list_name=p8_rpm_needs_package.list
        tar_name=contrib_rpm_p8.tar.gz
        ;;

        dev)
        target_path=/var/www/html/repo/yum/project0xxx/20
        list_name=dev_rpm_needs_package.list
        tar_name=contrib_rpm_dev.tar.gz
        ;;

        dev3.0)
        target_path=/var/www/html/repo/yum/project0xxx/30
        list_name=dev30_rpm_needs_package.list
        tar_name=contrib_rpm_dev30.tar.gz
        ;;

        *)
        # help_for_me
        ;;

    *)
    # help_for_me
    ;;
esac
# if [ "$project" == "projectxxx" ];then
#     target_path=/var/www/html/repo/yum/projectxxx
# else if [ "$branch" == "dev3.0" ];then
#     target_path=/var/www/html/repo/yum/project0xxx/30
#     alias_id=dev30
# else
#     target_path=/var/www/html/repo/yum/project0xxx/20
#     alias_id=
# else
#     echo "Unsure what project and branch you mean."
#     # help_for_me

cat <<EOF >/tmp/update_rpm_publish.sh
# Update package list
cd ${target_path}
for listfile in \$(ls -1 *.list);do
    sed -i '/$package/c\\\$(basename $package)' \$listfile
done
# Remove tar ball
rm -f ${tar_name}

# Create new tar ball
tar czf ${tar_name} -T ${list_name}
# Update repodata
createrepo -p --update -o . .
EOF

# Copy package file to repobase
## rsync -P --rsh=ssh $package root@$REPOBASE:${target_path}
rsync -P --rsh=ssh /tmp/update_rpm_publish.sh root@$REPOBASE:${target_path}
## ssh root@$REPOBASE sh ${target_path}/update_rpm_publish.sh
