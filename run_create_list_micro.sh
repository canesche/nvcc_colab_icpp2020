

GRAPH=(
    "merge_stream_join"
    "merge_tradicional"
    "resparsify_stream_join"
    "resparsify_tradicional"
    "sparse_vec_mult_stream_join"
    "sparse_vec_mult_tradicional"
    "stream_db_join_stream_join"
    "stream_db_join_tradicional")

for ((i=0; i < ${#GRAPH[@]}; i++)) do
    echo "GRAPH "${GRAPH[i]}" TO LIST"
    python3 scripts/dot_to_list.py dot_micro/${GRAPH[i]}.dot > list_micro/${GRAPH[i]}_zigzag.in 
done