GRAPH=('accumulate' 'cap' 'conv2' 'conv3' 'mac' 'mac2' 'matrixmultiply' 'mults1'
       'mults2' 'nomem1' 'simple2' 'sum' 'twoloops1' 'twoloops2')

for ((i=0; i < ${#GRAPH[@]}; i++)) do
    echo "GRAPH "${GRAPH[i]}" TO LIST"
    python3 scripts/dot_to_list.py dot_cgrame/cgrame_${GRAPH[i]}.dot > list_cgrame/cgrame_${GRAPH[i]}_zigzag.in 
done