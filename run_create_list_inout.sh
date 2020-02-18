GRAPH=('arf' 'conv3' 'cosine1' 'cosine2' 'Cplx8' 'ewf' 'feedback_points' 'FilterRGB' 'fir1'
       'fir2' 'Fir16' 'h2v2_smooth' 'horner_bezier_surf' 'interpolate_aux' 'k4n4op' 'mac'
       'motion_vectors' 'mults1' 'simple' 'tree_n_16_t_1' 'tree_n_16_t_2' 'tree_n_16_t_3' 'tree_n_16_t_4'
       'tree_n_32_t_1' 'tree_n_32_t_2' 'tree_n_32_t_3' 'tree_n_32_t_4' 'tree_n_64_t_1' 'tree_n_64_t_2'
       'tree_n_64_t_3' 'tree_n_64_t_4')

for ((i=0; i < ${#GRAPH[@]}; i++)) do
    echo "GRAPH "${GRAPH[i]}" TO LIST"
    python3 scripts/dot_to_list_inout.py dot/${GRAPH[i]}.dot > list/${GRAPH[i]}_inout.in 
done
