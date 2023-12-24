#### Parameters

- mean: $\displaystyle \mu \in \mathbb{R}$
- standard deviation: $\displaystyle \sigma \in \mathbb{R}^+$

---

#### Support

$\displaystyle x \in \mathbb{R}$

---

#### Moments

- $\displaystyle \operatorname{E}(X) = \mu$
- $\displaystyle \operatorname{Var}(X) = \sigma^2$

---

#### Probability density function (PDF)

$$\displaystyle f(x|\mu,\sigma) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

---

#### Cumulative distribution function (CDF)

$$\displaystyle F(x|\mu,\sigma) = \frac{1}{2}\left[1 + \operatorname{erf}\left(\frac{x-\mu}{\sigma\sqrt{2}}\right)\right]$$

where $$\,\displaystyle \operatorname{erf}(x) = \frac{2}{\sqrt{\pi}}\int_{0}^{x} e^{-t^2} \, dt\,$$ is the [error function](https://en.wikipedia.org/wiki/Error_function).
