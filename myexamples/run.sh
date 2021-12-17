#!/bin/bash

set -euo pipefail
ln -sf ../utils/parse_options.sh ./parse_options.sh

# requred args
model=''
config=''
task=''

# non required args
job_no=1
generation=10


. ../utils/parse_options.sh

echo $model