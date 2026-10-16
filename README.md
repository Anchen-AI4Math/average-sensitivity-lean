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

## Published verification

- [Complete theorem on Prove2Me](https://prove2.me/theorems/e1a9c1cb-97c1-4ea0-a4ad-d43e8412ac61): **ACCEPTED**, submission `0f539328-c783-4509-a78e-a86ac777468c`.
- [Finite coupling refinement](https://prove2.me/theorems/d868ab6f-94bc-4ede-a132-0fda2ff6ba88): **ACCEPTED**.
- [Exact constant extraction](https://prove2.me/theorems/958e04fd-0cb0-438e-bda6-fe21332f6929): **ACCEPTED**.
- [Independent Linux build and axiom check](https://github.com/Anchen0823/average-sensitivity-lean/actions/runs/38903817629): **success**, proof revision `a0d88dedd8e56f371e40bf1dfcd533afb51e3d04`.
- [Submission to Big O Speedrun](https://github.com/bigospeedrun/site/issues/3): requested reviewed import. Big O listing and its evidence level are decided by its maintainers.

## Prove2Me mission proposal

The completed theorem tree is organized into the public-intended Research Paper
proposal **Average sensitivity 3.762: refined coupling and a complete Lean proof**
(`f1d5911a-0f78-458d-a466-efe14879e460`). The account owner confirmed all five
items and submitted it on 2026-10-16. Its current status is **In review**,
awaiting moderator approval before it becomes a live public mission.

The two definition references come first, followed by these accepted theorem
references:

1. **Lemma 2 — Refined finite one-sided coupling** (milestone).
2. **Theorem extract_constant — Universal coefficient 3.762** (milestone).
3. **AverageSensitivity.polynomial_bound_3762_general** (goal).

Both milestones are verified dependencies of the goal's accepted reduction.
The proposal creates no duplicate theorem or definition statements. See
[`Platform/mission_description.md`](Platform/mission_description.md) for the
full introduction and [`Verification/mission_audit.json`](Verification/mission_audit.json)
for the checked structure.

The submitted proposal is visible to its owner under
[My missions](https://prove2.me/my-missions/f1d5911a-0f78-458d-a466-efe14879e460).
The required human self-audit and submission are complete. The existing theorems
and accepted proofs are already public independently of mission approval.

## Big O automatic-verifier preparation

Big O's public proof form currently accepts only `dft`, `3sum`, and `apsp`.
Average sensitivity first needs a maintainer-reviewed trusted statement and
verifier-owned profile, as described in its
[statement contribution guide](https://github.com/bigospeedrun/verifier/blob/main/docs/new-statements.md).
The site issue above is a record-import request; it is not an automatic proof
submission or a Big O verification receipt.

The missing trusted target is proposed in
[bigospeedrun/verifier PR #15](https://github.com/bigospeedrun/verifier/pull/15).
That PR contains only the frozen model, separate parameterized statement,
provenance and licensing; maintainer review and verifier-owned enabling remain
pending. The [standalone candidate's Linux build](https://github.com/Anchen0823/average-sensitivity-lean/actions/runs/38911800062)
passed, including the exact `Race.bound` permitted-axiom guard, at proof revision
`cb8c10538e613329be16f9a949d0d75a4c7c67f0`.

[`Submission.lean`](Submission.lean) is a complete standalone candidate for the
proposed average-sensitivity target, exporting
`Race.bound : BigOSpeedrun.AverageSensitivity.Bound (1881 / 500 : ℚ)`.
It imports only Mathlib, includes all required proof sources, and checks the
final permitted-axiom list. The CI runs it with `autoImplicit=false`.
Regenerate it with `python prepare_bigo.py`; the source order and output hash
are recorded in `Verification/bigo_candidate.json`.

This candidate targets the board's range `1 ≤ d ≤ n`, directly using the stronger
arbitrary-polynomial theorem proved above. Its parameterized target is in
[`Platform/bigo_Statement.lean`](Platform/bigo_Statement.lean). It is a proposed
interface until Big O maintainers approve and enable it. Compilation here does
not replace their Comparator and receipt pipeline.

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
