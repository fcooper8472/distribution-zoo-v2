#### Moments

```latex
\operatorname{E}(X) = \mu
```

```latex
\operatorname{Var}(X) = \sigma^2
```

---

#### Probability density function (PDF)

```latex
f(x|\mu,\sigma) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
```

---

#### Cumulative distribution function (CDF)

```latex
F(x|\mu,\sigma) = \frac{1}{2}\left[1 + \operatorname{erf}\left(\frac{x-\mu}{\sigma\sqrt{2}}\right)\right]
```

```latex
\operatorname{erf}(x) = \frac{2}{\sqrt{\pi}}\int_{0}^{x} e^{-t^2} \, dt
```
