

GRAPH=(
apex7
9symml
alu2
term1
alu4
k2
ex5p
misex3
ex1010
apex2
toolarge
spla
pdc
)

for ((i=0; i < ${#GRAPH[@]}; i++)) do
    echo "GRAPH "${GRAPH[i]}" TO LIST"
    python3 scripts/dot_to_list.py dot_dac/fpga/${GRAPH[i]}.dot > list_dac/fpga/${GRAPH[i]}.in 
done
