#!/usr/bin/env bash

K=29   # number of topics

#alpha=`echo "scale=3;10/$K"|bc`
alpha = 0.01
beta=0.2
niter=5
save_step=501

input_dir=../Test_Data/
output_dir=../output/
model_dir=${output_dir}model/
mkdir -p $output_dir/model

# the input docs for testing
doc_pt=${input_dir}dataset.txt

echo "=============== Index Docs ============="
# docs after indexing
dwid_pt=${output_dir}test/doc_wids.txt
# vocabulary file
voca_pt=${output_dir}train/voca.txt
python3 indexDocs_Test.py $doc_pt $dwid_pt $voca_pt

## infer p(z|d) for each doc
echo "================ Infer P(z|d)==============="
echo "../src/btm inf sum_b $K $dwid_pt $model_dir"
../src/btm inf sum_b $K $dwid_pt $model_dir

