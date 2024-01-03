#### PDF

```cpp
#include <boost/math/distributions/normal.hpp>

#include <iostream>
#include <vector>

// Check prerequisites for the definition of this function
namespace dz {
    std::vector<double> linspace(const double start, const double end, const int num);
}

int main() {

    std::vector<double> x = dz::linspace({{{range_start}}}, {{{range_end}}}, 50);
    std::vector<double> pdf;
    pdf.reserve(x.size());

    const double mean = {{{mean}}};
    const double std = {{{std}}};
    boost::math::normal_distribution<> dist(mean, std);

    for (int i = 0; i < x.size(); ++i) {
        pdf.push_back(boost::math::pdf(dist, x[i]));
        std::cout << x[i] << ",\t" << pdf[i] << '\n';
    }

    return 0;
}
```


#### Log PDF

```cpp
#include <boost/math/distributions/normal.hpp>

#include <cmath>
#include <iostream>
#include <vector>

// Check prerequisites for the definition of this function
namespace dz {
    std::vector<double> linspace(const double start, const double end, const int num);
}

int main() {

    std::vector<double> x = dz::linspace({{{range_start}}}, {{{range_end}}}, 50);
    std::vector<double> logpdf;
    logpdf.reserve(x.size());

    const double mean = {{{mean}}};
    const double std = {{{std}}};
    boost::math::normal_distribution<> dist(mean, std);

    for (int i = 0; i < x.size(); ++i) {
        logpdf.push_back(std::log(boost::math::pdf(dist, x[i])));
        std::cout << x[i] << ",\t" << logpdf[i] << '\n';
    }

    return 0;
}
```


#### Random sample of size n

```cpp
#include <iostream>
#include <random>
#include <vector>

int main() {

    const std::size_t n = 50;
    std::vector<double> rvs;
    rvs.reserve(n);

    const double mean = {{{mean}}};
    const double std = {{{std}}};
    std::normal_distribution<> dist(mean, std);
    
    // Standard library random number generator
    std::mt19937 rng(std::random_device{}());

    for (auto i = 0ul; i < n; ++i) {
        rvs.push_back(dist(rng));
        std::cout << rvs[i] << '\n';
    }

    return 0;
}
```
