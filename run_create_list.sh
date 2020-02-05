#GRAPH=('arf' 'conv3' 'cosine1' 'cosine2' 'Cplx8' 'ewf' 'feedback_points' 'FilterRGB' 'fir1'
#       'fir2' 'Fir16' 'h2v2_smooth' 'horner_bezier_surf' 'interpolate_aux' 'k4n4op' 'mac'
#      'motion_vectors' 'mults1' 'simple')
GRAPH=('mults1')

for ((i=0; i < ${#GRAPH[@]}; i++)) do
    echo "GRAPH "${GRAPH[i]}" TO LIST"
    python3 scripts/dot_to_list.py dot/${GRAPH[i]}.dot > list/${GRAPH[i]}.in 
done