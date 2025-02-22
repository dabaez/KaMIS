import os

# Replace 'your_directory' with the path of the directory you want to iterate through
directory = 'graphs/BHOSLIB'
out_directory = 'graphs/BHOSLIB_converted'

for root, dirs, files in os.walk(directory):
    print(f"Current directory: {root}")
    for file in files:
        print(f"File: {file}")
        with open(os.path.join(root, file), 'r') as f:
            lines = f.readlines()
            fl = 0
            while fl < len(lines) and lines[fl][0] == '#':
                fl += 1
            nodes, edges = lines[fl].split()
            nodes = [[] for _ in range(int(nodes))]
            real_edges = 0
            for line in lines[fl+1:]:
                    node1, node2 = line.split()
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