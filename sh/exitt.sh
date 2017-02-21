#!/usr/bin/env bash


function xxx_l2()
{
    echo "xxx level2 in"
    exit 1
    echo "xxx level2 out"
}


function xxx_l1()
{
    echo "xxx level1 in"
    xxx_l2
    echo "xxx level1 out"
}

echo exitt in
xxx_l1
echo exitt out
