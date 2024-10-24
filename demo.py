import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Part 1: Create a Simple Knowledge Graph
knowledge_graph = {
    "AI": ["ML", "Data Science", "NLP"],
    "ML": ["AI", "Deep Learning", "Statistics"],
    "Data Science": ["AI", "Statistics", "Data Engineering"],
    "NLP": ["AI", "Speech Recognition", "Text Processing"],
    "Deep Learning": ["ML", "Neural Networks"],
    "Statistics": ["ML", "Data Science"]
}

def explore_neighbors(graph, node):
    """
    Function to explore the immediate neighbors of a node in the graph.
    """
    return graph.get(node, [])

# Part 2: Simulated Document Vectors (Now matching graph node names)
documents = {
    "AI": np.array([0.1, 0.2, 0.3]),
    "ML": np.array([0.4, 0.5, 0.6]),
    "Data Science": np.array([0.7, 0.8, 0.9]),
    "NLP": np.array([0.2, 0.3, 0.4]),
    "Deep Learning": np.array([0.3, 0.4, 0.5]),
    "Statistics": np.array([0.5, 0.6, 0.7])
}

query_vector = np.array([0.35, 0.45, 0.55])

def nearest_neighbor(documents, query_vector):
    """
    Function to perform nearest neighbor search on document vectors using cosine similarity.
    """
    doc_names = list(documents.keys())
    doc_vectors = np.array([documents[doc] for doc in doc_names])
    
    similarities = cosine_similarity([query_vector], doc_vectors).flatten()
    nearest_idx = np.argmax(similarities)
    
    return doc_names[nearest_idx], similarities[nearest_idx]

# Part 3: Combine Graph Traversal and Vector Search
def traverse_graph(graph, node, depth, visited=None):
    """
    Recursive graph traversal function to explore a graph neighborhood up to a given depth.
    """
    if visited is None:
        visited = set()
    
    if depth == 0 or node in visited:
        return []
    
    visited.add(node)
    neighbors = graph.get(node, [])
    
    result = [node]
    for neighbor in neighbors:
        result += traverse_graph(graph, neighbor, depth - 1, visited)
    
    return result

def graph_rag(query, query_vector, graph, documents, depth=2):
    """
    Function to perform graph RAG by traversing the knowledge graph and performing nearest neighbor search
    on documents from the neighborhood.
    """
    # Explore the graph to find all neighbors within the specified depth
    extended_neighborhood = traverse_graph(graph, query, depth)
    print(f"Exploring neighborhood of '{query}' up to depth {depth}: {extended_neighborhood}")
    
    # Collect documents from the neighbors
    neighbor_documents = {node: documents.get(node) for node in extended_neighborhood if node in documents}
    
    if not neighbor_documents:
        print("No documents found in the neighborhood.")
        return
    
    # Perform nearest neighbor search within the neighborhood
    best_doc, best_similarity = nearest_neighbor(neighbor_documents, query_vector)
    print(f"Best document in neighborhood: {best_doc} (Similarity: {best_similarity:.2f})")

# Part 4: Running the Demo
if __name__ == "__main__":
    # Query example: "AI"
    query = "AI"
    print("Starting GraphRAG demo with query:", query)
    
    # Run the graph RAG demo for the query
    graph_rag(query, query_vector, knowledge_graph, documents, depth=2)
