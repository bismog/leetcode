#!/usr/bin/env bash
#xxxxxx!/usr/bin/bash


INSTALL_SRC_ROOT=/mnt/isodir
LOCAL_DISK_ROOT=/mnt/sysimage
OPENCOS_INSTALL_SRC=$INSTALL_SRC_ROOT/opencos
OPENCOS_INSTALL_DST=$LOCAL_DISK_ROOT/home/opencos_install
PACKAGE_INSTALL_SRC=$INSTALL_SRC_ROOT/opencos_depend_packages
OPENCOS_PATCH_DST=$LOCAL_DISK_ROOT/home/opencos_patch

mkdir -p $OPENCOS_INSTALL_DST
mkdir -p $OPENCOS_PATCH_DST
