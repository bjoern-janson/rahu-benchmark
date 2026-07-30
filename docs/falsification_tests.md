# RAHU Falsification Tests

## Purpose

This document defines the conditions under which the RAHU benchmark, Adaptive Inheritance hypothesis, or its measurement framework would be considered unsupported.

A scientific framework must define not only what evidence supports it, but what evidence would defeat it.

RAHU is designed around a falsifiable claim:

\[
\boxed{
E^*
\Longrightarrow
\exists w_i \in W_{invalid}:
\frac{dw_i}{dt}<0
}
\]

The claim:

> When a mechanism is repeatedly contradicted by empirical reality, an adaptive system should reduce that mechanism's future causal authority.

Failure to observe this behavior weakens the framework.

---

# 1. Metric Validity Tests

Before testing agents, the measurement system itself must be validated.

---

# F1: ARR Does Not Track Authority

## Hypothesis

The Authority Retention Ratio:

\[
ARR=
\frac{
w_{invalid}^{post}
}{
w_{invalid}^{pre}
}
\]

should measure retained mechanism influence.

---

## Falsification Condition

If:

\[
ARR\approx0
\]

but the mechanism continues controlling future behavior, then ARR is not measuring authority.

---

## Result

Framework metric invalid.

---

# F2: Structural Distance Does Not Separate Real Updates

## Hypothesis

Structural distance:

\[
D(M_1,M_2)
\]

should distinguish genuine mechanism revision from cosmetic modification.

---

## Falsification Condition

If systems with:

```
same mechanism
+
different wording
```

regularly produce:

\[
D(M_1,M_2)>\theta
\]

or systems with:

```
different mechanisms
```

produce:

\[
D(M_1,M_2)<\theta
\]

then the operator fails.

---

## Result

Replace structural distance implementation.

---

# 2. RAHU-0 Falsification

## False Contradiction Control

Purpose:

Test whether RAHU distinguishes noise from structural failure.

---

## Expected Behavior

Environment:

\[
y=3x+\epsilon
\]

where:

\[
\epsilon\sim N(0,\sigma^2)
\]

Expected:

\[
\Phi_R(e_t)\rightarrow N
\]

and:

\[
\Delta W\approx0
\]

---

## Falsification Conditions

### Case A: Noise Always Causes Updates

If healthy systems consistently update mechanisms under pure stochastic noise:

\[
P(R_{update}|Noise)\approx1
\]

then RAHU rewards instability.

---

### Case B: Structural Failure Looks Like Noise

If true model failure:

\[
E^*
\]

is consistently classified as noise:

\[
P(N|StructuralFailure)\approx1
\]

then MRAT fails.

---

# 3. RAHU-1 Falsification

## Coordinate Shift Test

Purpose:

Determine whether systems can detect representation saturation.

---

## Expected Behavior

Initial:

\[
R_{linear}
\]

Reality:

\[
R_{polynomial}
\]

Expected:

\[
\Phi_R(e_t)\rightarrow R
\]

and:

\[
REE=active
\]

---

## Falsification Conditions

---

## Case A: Infinite Patching Works Forever

If a linear system can maintain equivalent predictive performance indefinitely through local patches without increasing complexity:

\[
Complexity(M_{patched})
\nrightarrow\infty
\]

then representation expansion may not be required.

---

## Case B: Expansion Always Wins

If systems expand representation even when:

\[
\hat{\Gamma}_{B_{max}}<e_t
\]

then REE is too permissive.

---

# 4. RAHU-2 Falsification

## Causal Hierarchy Rewrite Test

Purpose:

Test whether systems rewrite generators or accumulate exceptions.

---

## Expected Behavior

Brittle:

\[
M_{patched}
=
M_1+\{exceptions\}
\]

Adaptive:

\[
M_1\rightarrow M_2
\]

---

## Falsification Conditions

---

## Case A: Patching Is Always Optimal

If patch accumulation produces:

\[
PredictiveValidity(M_{patched})
>
PredictiveValidity(M_2)
\]

with lower complexity cost, then generator rewrite is not generally preferable.

---

## Case B: Generator Rewrite Cannot Be Detected

If:

\[
D(M_1,M_2)
\]

cannot distinguish generator changes from patch accumulation, the benchmark lacks resolution.

---

# 5. RAHU-3 Falsification

## Inheritance Decay Test

Purpose:

Test the primitive Adaptive Inheritance Criterion.

---

## Expected Behavior

After invalidation:

\[
\frac{dw_i}{dt}<0
\]

---

## Falsification Conditions

---

## Case A: Successful Agents Preserve Invalid Mechanisms

If high-performing adaptive agents maintain:

\[
ARR\approx1
\]

while still responding successfully, then authority decay is not necessary.

---

## Case B: Authority Decay Causes Harm

If reducing invalid mechanism authority consistently decreases long-term performance:

\[
ARR\downarrow
\Rightarrow
Performance\downarrow
\]

then the adaptation criterion is incomplete.

---

# 6. Global Framework Falsification

These tests challenge the central thesis.

---

# G1: Capability Predicts Adaptive Corrigibility

## Hypothesis

Adaptive corrigibility is a distinct axis from capability.

---

## Falsification

If:

\[
Capability
\approx
ACS
\]

across sufficiently diverse systems, then a separate benchmark may not add information.

---

# G2: Static Evaluation Already Captures Adaptation

## Hypothesis

Existing benchmarks fail to measure mechanism revision.

---

## Falsification

If standard evaluations reliably predict:

- authority decay
- structural updates
- contradiction handling

then RAHU measures a redundant property.

---

# G3: No System Exhibits Adaptive Inheritance Failure

## Hypothesis

Adaptive decoupling is a meaningful failure mode.

---

## Falsification

If all tested systems:

\[
E^*
\rightarrow
\Delta W
\]

without exception, then Adaptive Inheritance Failure may not be practically relevant.

---

# G4: Reality Does Not Need Causal Authority

## Strongest Challenge

The framework assumes:

\[
E^*
\rightarrow
W_{future}
\]

is required for robust adaptation.

---

## Falsification

If systems with permanently fixed mechanisms achieve equal or superior long-horizon adaptation, then causal openness to reality is not necessary.

---

# Benchmark Failure Modes

RAHU itself may fail through:

| Failure | Meaning |
|-|-|
| Wrong attribution | MRAT misclassifies residuals |
| Wrong threshold | \(\theta\) misidentifies updates |
| Wrong authority proxy | ARR does not track influence |
| Overfitting | Tasks reward benchmark gaming |
| Missing variables | Important adaptive pathways ignored |

---

# Required Scientific Standard

RAHU should not claim:

> This is the definition of intelligence.

It should claim only:

> This is a measurable property of adaptive systems, and these experiments test whether it exists.

---

# Final Falsification Statement

The strongest possible disproof of RAHU would be:

\[
\boxed{
Systems\ without\ reality\text{-}driven\ mechanism\ revision
adapt\ equally\ well\ or\ better
than\ systems\ with\ it
}
\]

If that result occurs consistently, the framework fails.

That is the standard the benchmark must survive.
