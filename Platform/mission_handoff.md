# Mission review handoff

Proposal: **Average sensitivity 3.762: refined coupling and a complete Lean proof**

ID: `f1d5911a-0f78-458d-a466-efe14879e460`

Current status: **In review**. Intended visibility: public. Type: Research Paper.

The human owner confirmed all five items and clicked **Submit Proposal** on
2026-10-16. The API confirms all five human-confirmation timestamps and status
**In review**. No further owner submission is pending. A moderator's approval
turns it into a live public mission. Its owner can inspect it under
[My missions](https://prove2.me/my-missions/f1d5911a-0f78-458d-a466-efe14879e460).

The ordered contents are:

| Position | Item | Role | Platform status |
| --- | --- | --- | --- |
| 1 | GotsmanLinial | Definition: sign cube, flips, threshold convention, sensitivity | Definition |
| 2 | AverageSensitivity_Constants3762 | Definition: exact binomial moments and central coefficient | Definition |
| 3 | AverageSensitivity.finite_coupling_refined | Milestone: finite one-sided coupling | Proved |
| 4 | AverageSensitivity.extract_constant | Milestone: universal coefficient 3.762 | Proved |
| 5 | AverageSensitivity.polynomial_bound_3762_general | Goal: AS(sign p) ≤ 3.762 d √n | Proved |

All items reference existing published nodes. The theorem graph has no open
nodes, and both milestones feed the accepted goal reduction. The introduction
records the input distribution, positive dimension and degree, sign at zero,
arbitrary-polynomial scope, source attributions, proof verification, and limits
of the optimality and priority claims.

Review especially that the cube is uniform on signs, `thresholdSign 0 = 1`,
and the goal quantifies over every real polynomial with total degree at most
`d`, for `n,d ≥ 1`. The coupling statement requires equality of weighted laws;
it is a finite version of the cited paper's estimate. The scalar coefficient
extraction is credited to this development, not to that paper.

The official captain instructions reserve the final step for the human:
“You cannot self-audit or launch — those are human-only, done in the web app.”
No item has been marked human-confirmed by the agent.
