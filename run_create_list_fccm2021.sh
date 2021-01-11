

GRAPH=(
mac
simple
horner_bs
mults1
arf
conv3
motion_vec
fir2
fir1
fdback_pts
k4n4op
h2v2_smo
cosine1
ewf
Cplx8
Fir16
cosine2
FilterRGB
collapse_pyr
interpolate
w_bmp_head
matmul
invert_matrix
)

for ((i=0; i < ${#GRAPH[@]}; i++)) do
    echo "GRAPH "${GRAPH[i]}" TO LIST"
    python3 scripts/dot_to_list.py dot_fccm2021/${GRAPH[i]}.dot > list_fccm2021/${GRAPH[i]}.in 
done