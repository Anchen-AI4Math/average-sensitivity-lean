import OAI.Combinatorics.GotsmanLinial.ScalarIncrements
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Tactic

/-! The finite one-sided refinement from Lagdive--Aglave--Damre,
`An elementary improvement ...`, Lemma 2. The proof here uses a single
pointwise majorant and cancellation of equal-marginal potential sums. -/
open scoped BigOperators
open OAI.LeanBlast.GotsmanLinial

namespace AverageSensitivity

theorem displacement_majorant (m a u v : ℝ) (ha : 0 ≤ a)
    (hstep : v-u ≤ a) :
    (u-v)^2 ≤ 4 * (couplingPotential m u - couplingPotential m v) +
      2*a*(|u-m|+|v-m|) + a^2 := by
  have hsum : 0 ≤ |u-m|+|v-m| := add_nonneg (abs_nonneg _) (abs_nonneg _)
  by_cases huv : u ≤ v
  · have h := (couplingPotential_increment_bounds m huv).2
    have hprod := mul_nonneg (sub_nonneg.mpr hstep) hsum
    have hsq := mul_nonneg (sub_nonneg.mpr hstep) (show 0 ≤ a+(v-u) by linarith)
    nlinarith
  · have hvu : v ≤ u := le_of_not_ge huv
    have h := (couplingPotential_increment_bounds m hvu).1
    have hprod := mul_nonneg ha hsum
    nlinarith [sq_nonneg a]

theorem finite_coupling_refined {Ω : Type*} [Fintype Ω]
    (w U V : Ω → ℝ) (m a : ℝ)
    (hw : ∀ i, 0 ≤ w i) (hprob : ∑ i, w i = 1)
    (hsame : ∀ φ : ℝ → ℝ, ∑ i, w i * φ (U i) = ∑ i, w i * φ (V i))
    (ha : 0 ≤ a) (hstep : ∀ i, w i ≠ 0 → V i-U i ≤ a) :
    ∑ i, w i*(U i-V i)^2 ≤ 4*a*(∑ i, w i*|U i-m|)+a^2 := by
  have hpoint : ∀ i, w i*(U i-V i)^2 ≤
      w i*(4*(couplingPotential m (U i)-couplingPotential m (V i)) +
        2*a*(|U i-m|+|V i-m|)+a^2) := by
    intro i
    by_cases hi : w i = 0
    · simp [hi]
    · exact mul_le_mul_of_nonneg_left (displacement_majorant m a _ _ ha (hstep i hi)) (hw i)
  have h := Finset.sum_le_sum (fun i (_ : i ∈ Finset.univ) => hpoint i)
  have hp := hsame (couplingPotential m)
  have habs := hsame (fun t => |t-m|)
  have heq : (∑ i, w i*(4*(couplingPotential m (U i)-couplingPotential m (V i)) +
        2*a*(|U i-m|+|V i-m|)+a^2)) =
      4*((∑ i, w i*couplingPotential m (U i))-(∑ i, w i*couplingPotential m (V i))) +
      2*a*((∑ i, w i*|U i-m|)+(∑ i, w i*|V i-m|)) + a^2*(∑ i,w i) := by
    simp only [mul_add, mul_sub, Finset.mul_sum, Finset.sum_add_distrib,
      Finset.sum_sub_distrib]
    simp only [mul_left_comm, mul_comm, mul_assoc]
  rw [heq, hp, sub_self, mul_zero, zero_add, hprob, mul_one, ← habs] at h
  nlinarith

end AverageSensitivity
