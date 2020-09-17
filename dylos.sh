#!/bin/bash

while [[ /bin/true ]]; do
    python3 dylos.py | tee latest.json
    if [[ -s latest.json ]]; then
        echo "data found:"
        cp latest.json previous.json
        cat previous.json | jq ". += {\"dylos\": true, \"hostname\": \"$(hostname)\"} | {\"dict\" : . } | . += {\"name\" : \"dylos\"}" > payload.json
        curl -XPOST -H "X-PMETRICS-API-KEY: <thekey>"  \
             http://upside-down-research.com/pmetrics/api/v1/event \
             -d  @payload.json
    fi
done
