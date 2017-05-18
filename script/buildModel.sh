#!/bin/bash
# run an toy example for BTM

K=29   # number of topics

#alpha=`echo "scale=3;10/$K"|bc`
alpha=0.01
beta=0.2
niter=5
save_step=501

input_dir=../Train_Data/
output_dir=../output/
model_dir=${output_dir}model/
mkdir -p $output_dir/model

# the input docs for training
doc_pt=${input_dir}dataset.txt

echo "=============== Index Docs ============="
# docs after indexing
dwid_pt=${output_dir}train/doc_wids.txt
# vocabulary file
voca_pt=${output_dir}train/voca.txt
python3 indexDocs.py $doc_pt $dwid_pt $voca_pt

## learning parameters p(z) and p(w|z)
echo "=============== Topic Learning ============="
W=`wc -l < $voca_pt` # vocabulary size
make -C ../src
echo "../src/btm est $K $W $alpha $beta $niter $save_step $dwid_pt $model_dir"
../src/btm est $K $W $alpha $beta $niter $save_step $dwid_pt $model_dir