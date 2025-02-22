#!/bin/bash

NCORES=4

cd build
make -j $NCORES
cd ..

cp ./mmwis/deploy/mmwis deploy/
cp ./mmwis/deploy/struction deploy/
cp ./build/redumis deploy/
cp ./build/graphchecker deploy/
cp ./build/sort_adjacencies deploy/
cp ./build/online_mis deploy/
cp ./build/wmis/branch_reduce  deploy/weighted_branch_reduce
#cp ./build/wmis/merge_graph_weights deploy/
cp ./build/wmis/weighted_ls deploy/weighted_local_search