GRAPH=('tree_n_16_t_1' 'tree_n_16_t_2' 'tree_n_16_t_3' 'tree_n_16_t_4'
       'tree_n_32_t_1' 'tree_n_32_t_2' 'tree_n_32_t_3' 'tree_n_32_t_4' 'tree_n_64_t_1' 'tree_n_64_t_2'
       'tree_n_64_t_3' 'tree_n_64_t_4')

NODE=('15' '31' '63')
TREE=('1' '2' '3' '4')

for ((i=0; i < ${#NODE[@]}; i++)) do
	for ((j=0; j < ${#TREE[@]}; j++)) do
		python3 scripts/generate_tree_dot.py ${NODE[i]} ${TREE[j]}
	done 
done
