# Notes

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
