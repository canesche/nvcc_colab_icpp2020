

GRAPH=(
mac
simple
horner_bezier_surf
conv3
arf
mults1
motion_vectors
ewf
fir2
fir1
Cplx8
Fir16
h2v2_smooth
feedback_points
FilterRGB
k4n4op
cosine1
cosine2
interpolate_aux
jpeg_idct_ifast
jpeg_fdct_islow
)

for ((i=0; i < ${#GRAPH[@]}; i++)) do
    echo "GRAPH "${GRAPH[i]}" TO LIST"
    python3 scripts/dot_to_list.py dot_dac/cgra/${GRAPH[i]}.dot > list_dac/cgra/${GRAPH[i]}.in 
done
