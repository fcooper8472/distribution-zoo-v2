:warning: This is a work in progress. Visit the [existing zoo](https://ben18785.shinyapps.io/distribution-zoo/) instead. :warning:

# Distribution Zoo v2 concept

[Link to preview the app](https://distribution-zoo.streamlit.app/)

This is the repository for a version of the Distribution Zoo, built in Streamlit.

## Distributions supported

|                           | Plots | Formulae | LaTeX | Tips | C++  | Julia | Mathematica | MATLAB | Python | R | Stan |
|---------------------------|-------|----------|-------|------|------|-------|-------------|--------|--------|---|------|
| **Continuous Univariate** |       |          |       |      |      |       |             |        |        |   |      |
| Beta                      |       |          |       |      |      |       |             |        |        |   |      |
| Cauchy                    |       |          |       |      |      |       |             |        |        |   |      |
| Exponential               |       |          |       |      |      |       |             |        |        |   |      |
| Gamma                     | :+1:  |          |       |      |      |       |             |        |        |   |      |
| Half-Cauchy               |       |          |       |      |      |       |             |        |        |   |      |
| Inverse-Chi-Squared       |       |          |       |      |      |       |             |        |        |   |      |
| Inverse-Gamma             |       |          |       |      |      |       |             |        |        |   |      |
| Logit-Normal              |       |          |       |      |      |       |             |        |        |   |      |
| Log-Normal                |       |          |       |      |      |       |             |        |        |   |      |
| Normal                    | :+1:  | :+1:     | :+1:  | :+1: | :+1: |       |             |        | :+1:   |   |      |
| Student-t                 |       |          |       |      |      |       |             |        |        |   |      |
| Uniform                   |       |          |       |      |      |       |             |        |        |   |      |
| **Discrete Univariate**   |       |          |       |      |      |       |             |        |        |   |      |
| Bernoulli                 |       |          |       |      |      |       |             |        |        |   |      |
| Beta-Binomial             |       |          |       |      |      |       |             |        |        |   |      |
| Binomial                  |       |          |       |      |      |       |             |        |        |   |      |
| Discrete-Uniform          |       |          |       |      |      |       |             |        |        |   |      |
| Negative-Binomial         |       |          |       |      |      |       |             |        |        |   |      |
| Poisson                   |       |          |       |      |      |       |             |        |        |   |      |
| **Multivariate**          |       |          |       |      |      |       |             |        |        |   |      |
| Dirichlet                 |       |          |       |      |      |       |             |        |        |   |      |
| Inverse-Wishart           |       |          |       |      |      |       |             |        |        |   |      |
| LKJ                       |       |          |       |      |      |       |             |        |        |   |      |
| Multinomial               |       |          |       |      |      |       |             |        |        |   |      |
| Multivariate-Normal       |       |          |       |      |      |       |             |        |        |   |      |
| Multivariate-Student-t    |       |          |       |      |      |       |             |        |        |   |      |
| Wishart                   |       |          |       |      |      |       |             |        |        |   |      |


## Testing

The code relating to each distribution is tested:
- to ensure each code block compiles/runs
- to ensure each code from each language is generating the same distribution (i.e. no mis-parameterisations)

## Adding a new distribution

As of now, only Continuous Univariate distributions have been added.
- Copy [normal.py](./distribution_zoo/cont_uni/normal.py) and the corresponding data directory [normal](./distribution_zoo/cont_uni/normal)
- Update parameters, and the methods in the distribution: `sliders`, `plot`, `update_code_substitutions`
- Modify the markdown files describing the static content, and code snippets

## Testing a new distribution

- Edit [tests/utils.py](./tests/utils.py) to add an `AppTest` fixture for the distribution
- Add a method to [tests/extract.py](./tests/extract.py), copying `test_extract_normal`
- Add a method to [tests/validate_code_output.py](./tests/validate_code_output.py), copying `test_validate_normal`
