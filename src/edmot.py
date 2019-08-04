import community
import networkx as nx
from tqdm import tqdm

class EdMot(object):
    """
    Edge Motif Clustering Class.
    """
    def __init__(self, graph, component_count, cutoff):
        """
        :param graph: NetworkX object.
        :param component_count: Number of extract motif hypergraph components.
        :param cutoff: Motif edge cut-off value.
        """
        self.graph = graph
        self.component_count = component_count
        self.cutoff = cutoff
    
    def _overlap(self, node_1, node_2):
        """
        Calculating the neighbourhood overlap for a pair of nodes.
        :param node_1: Source node 1.
        :param node_2: Source node 2.
        :return neighbourhood overlap: Overlap score.
        """
        nodes_1 = self.graph.neighbors(node_1)
        nodes_2 = self.graph.neighbors(node_2)
        return len(set(nodes_1).intersection(set(nodes_2)))

    def _calculate_motifs(self):
        """
        Enumerating pairwise motif counts.
        """
        print("\nCalculating overlaps.\n")
        edges = [edge for edge in tqdm(self.graph.edges()) if self._overlap(edge[0], edge[1]) >= self.cutoff]
        self.motif_graph = nx.from_edgelist(edges)

    def _extract_components(self):
        """
        Extracting connected components from motif graph.
        """
        print("\nExtracting components.\n")
        components = list(nx.connected_component_subgraphs(self.motif_graph))
        components = [[len(c), c] for c in components]
        components.sort(key=lambda x: x[0], reverse = True )
        important_components = [components[component][1] for component  in range(self.component_count)]
        self.blocks = [[node for node in graph.nodes()] for graph in important_components]
        
    def _fill_blocks(self):
        """
        Filling the dense blocks of the adjacency matrix.
        """
        print("Adding edge blocks.\n")
        new_edges = [(node_1, node_2) for nodes in tqdm(self.blocks) for node_1 in nodes for node_2 in nodes]
        new_graph = nx.from_edgelist(new_edges)
        self.graph = nx.disjoint_union(self.graph,new_graph)

    def fit(self):
        """
        Clustering the target graph.
        """
        self._calculate_motifs()
        self._extract_components()
        self._fill_blocks()
        partition = community.best_partition(self.graph)
        return partition
