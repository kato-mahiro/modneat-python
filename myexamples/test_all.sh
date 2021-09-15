#!/bin/bash

python neat_example.py > /dev/null
if [ $? -ne 0 ]; then
    echo "=========================================="
    echo " 😡 Oops... run neat_example.py FAILED"
    echo "=========================================="
    exit 1
fi
echo "😁 neat_example.py is OK"

python exneat_example.py > /dev/null
if [ $? -ne 0 ]; then
    echo "=========================================="
    echo " 😡 Oops... run exneat_example.py FAILED"
    echo "=========================================="
    exit 1
fi
echo "😁 exneat_example.py is OK"

python modneat_example.py > /dev/null
if [ $? -ne 0 ]; then
    echo "=========================================="
    echo " 😡 Oops... run modneat_example.py FAILED"
    echo "=========================================="
    exit 1
fi
echo "😁 modneat_example.py is OK"

python exmod_example.py > /dev/null
if [ $? -ne 0 ]; then
    echo "=========================================="
    echo " 😡 Oops... run exmod_example.py FAILED"
    echo "=========================================="
    exit 1
fi
echo "😁 exmod_example.py is OK"

echo "======================================="
echo " 😁😁😁 ALL TESTS ARE PASSED !!  "
echo "======================================="
