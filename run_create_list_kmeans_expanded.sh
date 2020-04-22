
K=('4' '5' '6' '7' '8')
N=('4' '5' '6' '7' '8')

set -e

for ((i=0; i < ${#K[@]}; i++)) do
    for ((j=0; j < ${#N[@]}; j++)) do
        python3 scripts/dot_to_list.py dot_kmeans_expanded/K${K[i]}N${N[j]}.dot > list_kmeans_expanded/K${K[i]}N${N[j]}_exp_zigzag.in
    done
done