import Mathlib.Data.Nat.Choose.Central
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Data.Real.Basic

open scoped BigOperators
namespace AverageSensitivity

noncomputable def rawMAD (n : ℕ) : ℝ :=
  ∑ j ∈ Finset.range (n+1), (n.choose j : ℝ)*|2*(j:ℝ)-(n:ℝ)|

noncomputable def central (k : ℕ) : ℝ := (Nat.centralBinom k:ℝ)/(4:ℝ)^k

noncomputable def mad (n : ℕ) : ℝ := rawMAD n/(2*(2:ℝ)^n)

end AverageSensitivity
