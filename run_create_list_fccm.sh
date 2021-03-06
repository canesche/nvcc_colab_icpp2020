

GRAPH=(
    'Cplx8' 
    'DCT'
'FilterRGB'
'Fir16'
'Fir64'
'arf'
'cjpeg_r2'
'collapse_pyr'
'conv2'
'conv3'
'cosine1'
'cosine2'
'ewf'
'feedback_points'
'fir1'
'fir2'
'h2v2_smooth'
'horner_bezier_surf'
'idctcol'
'interpolate_aux'
'jpeg_fdct_islow'
'jpeg_idct_ifast'
'k4n4op'
'mac'
'matmul'
'motion_vectors'
'mults1'
'simple'
'smooth_color_z'
)

for ((i=0; i < ${#GRAPH[@]}; i++)) do
    echo "GRAPH "${GRAPH[i]}" TO LIST"
    python3 scripts/dot_to_list.py dot_fccm/${GRAPH[i]}.dot > list_fccm/${GRAPH[i]}_zigzag.in 
done