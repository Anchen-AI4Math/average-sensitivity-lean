This submits a sufficient universal coefficient **C = 1881/500 = 3.762** for the average-sensitivity board, improving the listed 3.83 claim.

For every real polynomial p in n >= 1 variables of total degree at most d >= 1, on the uniform sign cube and with sign(0) = 1,

$$\operatorname{AS}(\operatorname{sign}p)\le\frac{1881}{500}\,d\sqrt n.$$

This covers the board's full range 1 <= d <= n. The final theorem has no multilinearity assumption; the proof includes a degree-preserving parity reduction of arbitrary polynomials.

## Fixed source and reproducibility

- Repository: https://github.com/Anchen0823/average-sensitivity-lean
- Fixed source: https://github.com/Anchen0823/average-sensitivity-lean/tree/a0d88dedd8e56f371e40bf1dfcd533afb51e3d04
- Final theorem: `AverageSensitivity.polynomial_bound_3762_general` in `AverageSensitivity/Multilinearization.lean`.
- Lean 4.33.1; Mathlib `0df444a360eaa60ab8c11dca51a86af692955474`.
- Reproduce with `lake update`, `lake exe cache get`, `lake build`, then `lake env lean AxiomAudit.lean`.
- The local complete theorem passes and has exactly the permitted axioms `propext`, `Classical.choice`, `Quot.sound`. The build does not use platform theorem placeholders.
- Independent Linux build: https://github.com/Anchen0823/average-sensitivity-lean/actions/runs/38903817629 — **success**, including the final-theorem axiom check.

## Prove2Me

- Finite coupling refinement, accepted: https://prove2.me/theorems/d868ab6f-94bc-4ede-a132-0fda2ff6ba88
- Constant extraction, accepted: https://prove2.me/theorems/958e04fd-0cb0-438e-bda6-fe21332f6929
- Complete arbitrary-polynomial theorem: https://prove2.me/theorems/e1a9c1cb-97c1-4ea0-a4ad-d43e8412ac61
- Main submission `0f539328-c783-4509-a78e-a86ac777468c` is **ACCEPTED** (2026-10-16 12:57 UTC). Both supporting theorems above are also ACCEPTED.

## Attribution and contribution

The weighted Walsh grading, matrix edge recovery, and coefficient-eight formalization are from OpenAI/math at `1581d4cbdd69a0faf34b2089614fe2a814316a6a`.

The refined finite one-sided coupling estimate and the dimension-degree estimate `AS <= 8 d b_n + 2 d^2` are due to Prathmesh Lagdive, Vaibhav Aglave and Suraj Damre, source `log-prathm/ptf-average-sensitivity` at `5e9f26cf74935f08be20f9ac4deb57b291d707d8`.

This contribution, published by Anchen0823 with assistance from OpenAI Codex, supplies a Lean formalization of the refinement, a sharper extraction of the sufficient universal coefficient 3.762, and the complete connection to the polynomial-threshold statement. It does not assert an optimal constant or exhaustive historical priority.

The extraction uses an exact central-binomial induction certificate starting at k = 10, which controls every dimension n >= 20; the remaining nontrivial dimensions are 15 through 19. All computations in the closed proof are checked by Lean's kernel.

Please review this result for import into the average-sensitivity leaderboard. The evidence level should follow your own review policy; the repository does not self-assign Big O's Lean Verified status.
