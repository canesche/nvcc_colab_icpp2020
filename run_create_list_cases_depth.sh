

GRAPH=(
'Cplx8'
'FilterRGB'
'Fir16'
'arf'
'collapse_pyr'
'conv3'
'cosine1'
'cosine2'
'ewf'
'feedback_points'
'fir1'
'fir2'
'h2v2_smooth'
'hal'
'horner_bezier_surf'
'idctcol'
'interpolate_aux'
'invert_matrix'
'jpeg_fdct_islow'
'jpeg_idct_ifast'
'k4n4op'
'mac'
'matmul'
'motion_vectors'
'mults1'
'simple'
'smooth_color_z'
'write_bmp_header'
)

for ((i=0; i < ${#GRAPH[@]}; i++)) do
    echo "GRAPH "${GRAPH[i]}" TO LIST"
    python3 scripts/dot_to_list.py dot_cases/${GRAPH[i]}.dot > list_cases/${GRAPH[i]}_depth.in 
done
