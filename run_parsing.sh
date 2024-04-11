#!/bin/bash
python parsing.py gpu-bench/gpu-l2-cache/amdmi200/workloads/omni-data/amd-l2-cache-0 omnidata/amd_l2_cache_0_k0
# Define the range of k values you want to iterate over
for k in {0..1}; do
    for i in {0,1,2,3,5,6};do	
    # Execute the parsing.py command with the current k value
    	python parsing.py gpu-bench/gpu-l2-cache/amdmi200/workloads/omni-data/amd-l2-cache-${i}_k${k} ./omnidata/amd_l2_cache_${i}_k${k}
    done
done
