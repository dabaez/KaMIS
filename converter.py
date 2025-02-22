import os

# Replace 'your_directory' with the path of the directory you want to iterate through
directory = 'graphs/BHOSLIB_ascii'
out_directory = 'graphs/BHOSLIB'

for root, dirs, files in os.walk(directory):
    print(f"Current directory: {root}")
    for file in files:
        print(f"File: {file}")
        with open(os.path.join(root, file), 'r') as f:
            lines = f.readlines()
            _, _, nodes, edges = lines[0].split()
            nodes = [[] for _ in range(int(nodes))]
            real_edges = 0
            for line in lines[1:]:
                if line[0] == 'e':
                    _, node1, node2 = line.split()
                    node1, node2 = int(node1), int(node2)
                    nodes[node1-1].append(node2)
                    nodes[node2-1].append(node1)
                    real_edges += 1
            if real_edges != int(edges):
                print(f"Edges mismatch: {real_edges} != {edges}")
        with open(os.path.join(out_directory, file), 'w') as f:
            f.write(f"{len(nodes)} {real_edges}\n")
            for node in nodes:
                f.write(' '.join(map(str, node)) + '\n')