

GRAPH=(
    'cosine2_exp'
    'ewf_exp'
)

for ((i=0; i < ${#GRAPH[@]}; i++)) do
    echo "GRAPH "${GRAPH[i]}" TO LIST"
    python3 scripts/dot_to_list.py dot_exp/${GRAPH[i]}.dot > list_exp/${GRAPH[i]}_zigzag.in 
done