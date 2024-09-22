## About

---

### Shared Nearest Neighbor Clustering Algorithm

The Shared Nearest Neighbor clustering algorithm [1], also known as SNN, is an extension of DBSCAN that aims to overcome its limitation of not being able to correctly create clusters of different densities. This work provides a Python 3 implementation for SNN following the conventions of the scikit-learn library, and compares its results to multiple datasets with other, more traditional clustering methods.

The shared nearest neighbor graph connects a point with all its nearest neighbors if they have at least one shared neighbor. The number of shared neighbors can be used as an edge weight. Javis and Patrick (1973) use a slightly modified (see parameter jp) shared nearest neighbor graph for clustering.

### References

---

R. A. Jarvis and E. A. Patrick. 1973. Clustering Using a Similarity Measure Based on Shared Near Neighbors. IEEE Trans. Comput. 22, 11 (November 1973), 1025-1034. tools:::Rd_expr_doi("10.1109/T-C.1973.223640")