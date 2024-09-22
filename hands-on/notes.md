# Notes
## Hands-on-machine-learning -book notes

### I. The Fundamentals of Machine Learning
- Applying ML techniques to dig into large amounts of data can help discover patterns that were not immediately apparent. This is called *data mining.*

- A typical supervised learning task is classification.

- Some of the most important supervised learning algorithms
    - k-Nearest Neighbours
    - Linear Regression
    - Logistic Regression
    - Support Vector Machines (SVMs)
    - Decision Trees and Random Forests
    - Neural Networks

- Some of the most important unsupervised learning algorithms
    - Clustering
        - K-means
        - DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
        - HCA (Hierarchical Cluster Analysis)
    - Anomaly detection and novelty detection
        - One-class SVM
        - Isolation Forest
    - Visualization and dimensionality reduction
        - PCA (Principal Component Analysis)
        - Kernel PCA
        - LLE (Locally Linear Embedding)
        - t-SNE (t-Distributed Stochastic Neighbour Embedding)
    
    - Association rule learning
        - Apriori
        - Eclat

## Linear Regression

### Hypothesis

```math
h_w\left(x\right) = w_0 + w_1x_1 + w_2x_2 ...w_nx_n
```

### Mean Squared Error

```math
M.S.E = \frac{1}{2m} . \sum_{i=1}^m \left(h_w\left(x^i\right) - y^i \right)^2
```

### Gradient Descendent

till convergence {

```math
    w_j := w_j - \alpha \sum_{i=1}^m\left(h_w\left( x^i \right) - y^i \right) . x^i
```

}
