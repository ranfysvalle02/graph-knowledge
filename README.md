# graphRAG-from-scratch

![](https://i.ytimg.com/vi/-jkKlY9UA_Y/maxresdefault.jpg)

---

## **Connecting Concepts for Better Understanding**

In today’s world of machine learning, data science, and artificial intelligence (AI), **knowledge graphs** have become a powerful tool for structuring information. By connecting related concepts in a network of nodes and edges, knowledge graphs help visualize the relationships between ideas in a meaningful and intuitive way.

But how do knowledge graphs work, and how can you build one from scratch? In this post, we'll walk through a simple Python-based knowledge graph and explore how it can be used in practical applications.

### **What is a Knowledge Graph?**

A knowledge graph is a data structure that represents concepts (known as **nodes**) and the relationships between them (known as **edges**). You can think of it as a map where each point (node) represents an idea or entity, and each line (edge) shows how those ideas are connected. This allows you to visualize and navigate information in a network rather than in isolated bits.

In a knowledge graph:
- **Nodes** represent individual concepts, such as "AI" or "Machine Learning."
- **Edges** represent relationships between these concepts, such as "AI is related to Machine Learning."

Let’s break this down using an example in Python.

### **Building a Simple Knowledge Graph in Python**

Here’s a simple Python dictionary-based implementation of a knowledge graph, where each concept is a key, and its related concepts are values in a list:

```python
knowledge_graph = {
    "AI": ["ML", "Data Science", "NLP"],
    "ML": ["AI", "Deep Learning", "Statistics"],
    "Data Science": ["AI", "Statistics", "Data Engineering"],
    "NLP": ["AI", "Speech Recognition", "Text Processing"],
    "Deep Learning": ["ML", "Neural Networks"],
    "Statistics": ["ML", "Data Science"]
}
```

In this example:
- **"AI"** is connected to "Machine Learning (ML)", "Data Science", and "Natural Language Processing (NLP)".
- **"ML"** is connected back to "AI", but also to "Deep Learning" and "Statistics".
- The graph expands outward, connecting other related fields like "Data Engineering" and "Neural Networks".

### **Breaking Down the Knowledge Graph**

Each line in the `knowledge_graph` represents a concept (node) and its relationships (edges) to other concepts. For example, `"AI": ["ML", "Data Science", "NLP"]` means that AI is related to Machine Learning, Data Science, and NLP. 

These relationships form the **edges** of our graph, connecting each concept to other fields or subfields. As a result, you can easily navigate between concepts and explore how they interrelate.

### **Visualizing the Knowledge Graph**

To visualize this conceptually, imagine each key in the dictionary as a point (node), and each value as a line (edge) connecting to other nodes. Here's a simple diagram based on the example:

```
AI ----- ML ------ Deep Learning
 |        |             |
 |        |             Neural Networks
 |        |
 Data Science -------- Statistics
         |
   Data Engineering
```

### **Why Are Knowledge Graphs Useful?**

Knowledge graphs help us model the relationships between concepts in a way that is easy to navigate and understand. Here are a few key benefits:
- **Contextual Connections**: They show not just isolated facts, but how concepts relate to each other.
- **Data Exploration**: You can explore concepts by following connections, uncovering deeper insights as you move through the graph.
- **Improved Search and Retrieval**: Knowledge graphs are used in search engines and AI systems to retrieve more relevant information by understanding how different topics are linked.

### **How to Use This in Your Projects**

Let’s say you’re building an AI system that needs to understand different fields of machine learning. Instead of hardcoding specific rules about relationships, you can use a knowledge graph to model those relationships dynamically.

For example, if a user queries “AI”, your system could use the graph to explore related concepts like Machine Learning, Data Science, or NLP, returning relevant articles or resources based on those connections.

You can implement a **graph traversal** algorithm to explore the relationships in the graph, expanding outwards from a central concept like "AI":

```python
def explore_neighbors(graph, node):
    return graph.get(node, [])

# Example: Exploring the neighbors of "AI"
print("Neighbors of AI:", explore_neighbors(knowledge_graph, "AI"))
```

This simple function will output the neighbors (related concepts) of any node in the graph. For "AI", it would return:

```
Neighbors of AI: ['ML', 'Data Science', 'NLP']
```

This could be extended into more complex search and retrieval systems where you combine graph traversal with semantic search techniques.

### **Applications of Knowledge Graphs**

Here are just a few ways knowledge graphs are used in real-world applications:
- **Search Engines**: Search engines like Google use knowledge graphs to link related concepts and provide better search results.
- **Question-Answering Systems**: AI systems use knowledge graphs to understand the context of questions and generate more accurate answers.
- **Recommendation Systems**: By exploring relationships in a knowledge graph, recommendation systems can suggest products or content related to what a user has already explored.

### What Does the `explore_neighbors` Function Do?

In a **knowledge graph**, each concept (node) can have one or more related concepts (neighbors). The `explore_neighbors` function is designed to **retrieve** these related concepts for any given node. In simpler terms, if you want to know which concepts are directly related to "AI" in the graph, this function will return a list of those related concepts.

### The Code

```python
def explore_neighbors(graph, node):
    return graph.get(node, [])
```

Here’s what’s happening in this function:

1. **`graph`**: This is the **knowledge graph** itself, which is a dictionary where each key is a concept, and the values are lists of related concepts (neighbors).
2. **`node`**: This is the **specific concept** you’re interested in, like "AI" or "ML". You pass this to the function to find its neighbors.
3. **`graph.get(node, [])`**: The function uses the `get` method to look up the **node** in the `graph` dictionary:
   - If the **node** exists in the graph, it returns its list of neighbors.
   - If the **node** doesn't exist (for example, if you ask for a node that's not in the graph), it returns an empty list `[]`.

### Example in Action

Let’s say we want to explore the neighbors of the node `"AI"`. Here's how it works:

```python
# Our simple knowledge graph
knowledge_graph = {
    "AI": ["ML", "Data Science", "NLP"],
    "ML": ["AI", "Deep Learning", "Statistics"],
    "Data Science": ["AI", "Statistics", "Data Engineering"],
    "NLP": ["AI", "Speech Recognition", "Text Processing"],
}

# Call the explore_neighbors function to find neighbors of AI
print("Neighbors of AI:", explore_neighbors(knowledge_graph, "AI"))
```

In this case, we pass `"AI"` as the **node** argument, and the function looks up "AI" in the graph and finds its neighbors: `"ML"`, `"Data Science"`, and `"NLP"`.

The output will be:

```
Neighbors of AI: ['ML', 'Data Science', 'NLP']
```

This tells us that "AI" is directly connected to these three concepts in the knowledge graph.

### Why Is `get(node, [])` Used?

We use `get(node, [])` instead of just `graph[node]` because it’s safer. If you try to look up a node that **doesn't exist** in the graph using `graph[node]`, Python will raise a **KeyError**. By using `get()`, we can provide a **default value** (in this case, an empty list `[]`) to avoid errors if the node isn’t found in the graph.

### Summary of How It Works:
- **Input**: You give it a node (e.g., `"AI"`) from the knowledge graph.
- **Process**: The function looks for that node in the graph and retrieves its list of neighbors (e.g., related concepts).
- **Output**: A list of neighbors (e.g., `['ML', 'Data Science', 'NLP']`).

### Why It's Important

In a knowledge graph, the ability to **explore neighbors** is essential. It lets you see which concepts are directly connected to a given node, allowing you to navigate through the graph and understand how different ideas relate to each other.

---

### **Conclusion**

A knowledge graph is a powerful tool for structuring and exploring relationships between concepts. Even in this simple Python example, you can see how concepts in AI and machine learning can be connected in a meaningful way. As AI systems become more complex, knowledge graphs will play a key role in organizing and retrieving information in smarter, more efficient ways.

If you're interested in building your own knowledge graph, start small! You can expand your graph over time, adding more nodes and relationships as your system grows. The code examples provided in this post should give you a solid foundation to start building and exploring your own knowledge graph.

### ***Resources**

https://github.com/ranfysvalle02/mongodb-graph

## FULL CODE

```python
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
"""
Starting GraphRAG demo with query: AI
Exploring neighborhood of 'AI' up to depth 2: ['AI', 'ML', 'Data Science', 'NLP']
Best document in neighborhood: ML (Similarity: 1.00)
"""
```
