These examples require the following packages:
- [boost](https://www.boost.org/), specifically the [Math Toolkit](https://www.boost.org/doc/libs/release/libs/math/)

which can be installed with

- [vcpkg](https://vcpkg.io/en/) (cross-platform):
  ```bash
  vcpkg install boost-math
  ```

- apt (Ubuntu/Debian):
  ```bash
  sudo apt install libboost-math-dev
  ```

- [Homebrew](https://brew.sh/) (macOS):
  ```bash
  brew install boost
  ```

- [boost getting started guide](https://www.boost.org/more/getting_started/index.html)


For convenience, many examples use the following function to generate a vector of evenly-spaced values:

```cpp
#include <vector>

namespace dz {

std::vector<double> linspace(const double start, const double end, const int num) {
    std::vector<double> result;
    if (num <= 0) {
        return result;
    } 
    else if (num == 1) {
        result.push_back(start);
        return result;
    }

    const double step = (end - start) / (num - 1);
    for (int i = 0; i < num - 1; ++i) {
        result.push_back(start + i * step);
    }

    result.push_back(end);

    return result;
}

} // namespace dz
```
