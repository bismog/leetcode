#!/usr/bin/env bash

me="$(basename "$(test -L "$0" && readlink "$0" || echo "$0")")"
me=${0##*/}

# Default configuration
# This can be ignore if you set via command arguments
# Source image file should be restricted to name: daisy-base.tar.gz
_source_img="./daisy-base.tar.gz"
_source_spec="./daisy-base.spec"
_version="1.0.0"
_release="20170105.el7"

echo "Your input: $@"

if [[ $# -ne 0 ]];then
    while true
    do
        case $1 in
        -i | --image)
        _SOURCEIMG=$2
        shift 2
        ;;

        -c | --spec)
        _SOURCESPEC=$2
        shift 2
        ;;

        -v | --version)
        _VERSION=$2
        shift 2
        ;;

        -r | --release)
        _RELEASE=$2
        shift 2
        ;;

        -* | --* | -h | --help | help)
        echo "Command usage:"
        echo "    -i    Path to image file(daisy-base.tar.gz)"
        echo "    -c    Path to spec file(daisy-base.spec)"
        echo "    -v    version item mapping to rpm file"
        echo "    -r    release item mapping to rpm file"
        echo "e.g.:"
        echo "    $me -i path/to/daisy-base.tar.gz -c /path/to/spec"
        exit 1
        ;;

        *)
        break
        ;;

        esac
    done
fi

echo "source image is:$_SOURCEIMG"
if [[ $_SOURCEIMG == "" ]];then
    _SOURCEIMG=$_source_img
fi
if [[ $_SOURCESPEC == "" ]];then
    _SOURCESPEC=$_source_spec
fi
if [[ $_VERSION == "" ]];then
    _VERSION=$_version
fi
if [[ $_RELEASE == "" ]];then
    _RELEASE=$_release
fi

anchor="daisy-base-1.0.0"
tmpdir=$(mktemp -d)
mkdir -p $tmpdir/$anchor
cp $_SOURCEIMG $tmpdir/$anchor/
cd $tmpdir/
tar -czvf $anchor.tar.gz -C $tmpdir $anchor
mv $anchor.tar.gz /root/rpmbuild/SOURCES/
cd /root/rpmbuild/SPECS/


# Please run this script below /root/rpmbuild/SPECS
# Here double quote is needed for variables quotation
rpmbuild -bb --define "_arch x86_64" --define "_topdir /root/rpmbuild" --define "_version $_VERSION" --define "_release $_RELEASE" $_SOURCESPEC

# Automatically send rpm package to repo repository
if [[ $? -eq 0 ]];then
    rsync ../RPMS/x86_64/daisy-base-$_VERSION-$_RELEASE.x86_64.rpm root@cml04:/data/yum.repo/daisy/daisy-compile/
    ssh root@cml04 'cd /data/yum.repo/daisy/daisy-compile/;createrepo -p --update -o . .'

    rsync ../RPMS/x86_64/daisy-base-$_VERSION-$_RELEASE.x86_64.rpm root@repobase:/var/www/html/repo/yum/daisy/
    ssh root@repobase 'cd /var/www/html/repo/yum/daisy/;createrepo -p --update -o . .'
fi
