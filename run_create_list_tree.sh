GRAPH=('tree_n_15_t_1' 'tree_n_15_t_2' 'tree_n_15_t_3' 'tree_n_15_t_4'
       'tree_n_31_t_1' 'tree_n_31_t_2' 'tree_n_31_t_3' 'tree_n_31_t_4' 'tree_n_63_t_1' 'tree_n_63_t_2'
       'tree_n_63_t_3' 'tree_n_63_t_4')

for ((i=0; i < ${#GRAPH[@]}; i++)) do
    echo "GRAPH "${GRAPH[i]}" TO LIST"
    python3 scripts/dot_to_list_no_dic.py dot/${GRAPH[i]}.dot > list/${GRAPH[i]}_zigzag.in 
done
