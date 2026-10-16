# Average sensitivity: a Lean proof with coefficient 3.762

For every real polynomial `p` in `n ≥ 1` variables of total degree at most
`d ≥ 1`, its threshold function on the uniform sign cube satisfies

\[
\operatorname{AS}(\operatorname{sign}p)\le\frac{1881}{500}\,d\sqrt n.
\]

The convention is `sign(0) = 1`. The final theorem covers arbitrary real
polynomials, with an explicit parity reduction to multilinear form.

## Build and theorem

Lean **4.33.1**, Mathlib **0df444a360eaa60ab8c11dca51a86af692955474**.

```sh
lake update
lake exe cache get
lake build
```

The final declaration is
`AverageSensitivity.polynomial_bound_3762_general`, in
[`AverageSensitivity/Multilinearization.lean`](AverageSensitivity/Multilinearization.lean).
The default build prints its axioms: `propext`, `Classical.choice`, `Quot.sound`.
The complete proof uses no unproved mathematical hypotheses or computational
axioms.

## Proof and attribution

The weighted Walsh grading, matrix edge recovery, and original coefficient-eight
formalization are from [OpenAI's math release, fixed revision
1581d4cbdd69a0faf34b2089614fe2a814316a6a](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Combinatorics/GotsmanLinial).
The vendored `OAI/` modules have small Lean 4.33.1 compatibility changes.

The improved one-sided coupling estimate and dimension-degree bound
`AS ≤ 8 d b_n + 2 d²` are due to **Prathmesh Lagdive, Vaibhav Aglave, and
Suraj Damre**, [fixed manuscript/source revision
5e9f26cf74935f08be20f9ac4deb57b291d707d8](https://github.com/log-prathm/ptf-average-sensitivity/tree/5e9f26cf74935f08be20f9ac4deb57b291d707d8).
Their paper obtains the sufficient universal coefficient 3.83.

This repository supplies a Lean proof of that refined coupling bound, exact
binomial absolute moments, a sharper extraction of the uniform coefficient
**3.762**, and the connection to the full polynomial-threshold theorem.
The original matrix construction and the coupling refinement are attributed to
the sources above; the contribution here is their formal integration and the
explicit constant extraction. This does not assert an optimal constant or
exhaustive historical priority.

The extraction uses the inductive certificate, for all `k ≥ 10`,

\[
\left(4^{-k}\binom{2k}{k}\right)^2
\left(\frac{157}{50}k+\frac{1727}{2150}\right)\le1.
\]

It implies the needed estimate for every `n ≥ 20`. The remaining nontrivial
dimensions are 15 through 19. All inequalities, including these finite
computations, are checked by Lean's kernel.

Proof development and source preparation were assisted by OpenAI Codex.
The account publishing this repository is **Anchen0823**. No independent human
review is claimed. See `NOTICE` for source attribution and `Verification/` for
verification and provenance records.
