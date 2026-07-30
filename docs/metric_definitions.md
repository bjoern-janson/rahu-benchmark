# RAHU Metric Definitions

## Purpose

This document defines the telemetry metrics used by the Reality-Adversarial Hypothesis Updating (RAHU) benchmark.

The purpose of these metrics is to measure whether empirical consequences retain causal authority over future mechanism behavior.

RAHU does not measure intelligence.

It measures adaptive structural response.

The central evaluation chain is:

\[
E^*
\rightarrow
\Phi_R(e_t)
\rightarrow
\Delta W
\rightarrow
W_{t+1}
\]

Where:

- \(E^*\) = empirical contradiction
- \(\Phi_R(e_t)\) = residual attribution
- \(\Delta W\) = authority redistribution
- \(W_{t+1}\) = future mechanism distribution

---

# 1. Latent Branch Ratio (LBR)

## Definition

\[
\boxed{
LBR_t =
\frac{
N_{\text{inadmissible}}
}{
N_{\text{total}}
}
}
\]

Where:

- \(N_{\text{inadmissible}}\) = number of trajectories violating environmental constraints
- \(N_{\text{total}}\) = total evaluated trajectories

---

## Purpose

LBR measures where and when a system begins losing alignment with environmental constraints.

It is a friction detector.

PTVS answers:

> Where did the current mechanism become inconsistent with reality?

---

## Interpretation

| LBR | Interpretation |
|-|-|
| 0 | Fully admissible trajectory |
| low | Minor friction |
| high | Mechanism/environment mismatch |

---

## Important Constraint

High LBR does not automatically imply a mechanism update.

Residuals must first pass through MRAT attribution.

---

# 2. Post-Error Confidence (C_post)

## Definition

\[
C_{post}
\in [0,1]
\]

The system's confidence in its updated explanation after receiving contradiction feedback.

---

## Purpose

Measures whether the system can form a stable post-error model.

---

## Critical Distinction

Confidence is not authority.

\[
\boxed{
\Delta C_{post}
\not\implies
\Delta W
}
\]

A system may become highly confident in an explanation while preserving the same invalid mechanism.

---

## Failure Example

Before:

```
Mechanism A
confidence: 0.90
```

After contradiction:

```
Mechanism A + explanation
confidence: 0.95
```

No adaptive inheritance occurred.

The mechanism survived.

---

# 3. MRAT Attribution Vector

## Definition

\[
\boxed{
\Phi_R(e_t)
\rightarrow
(a_N,a_S,a_M,a_R,a_G)
}
\]

Where:

| Component | Meaning |
|-|-|
| \(a_N\) | Noise attribution |
| \(a_S\) | State error attribution |
| \(a_M\) | Mechanism deficit attribution |
| \(a_R\) | Representation deficit attribution |
| \(a_G\) | Generator decoupling attribution |

Constraint:

\[
\sum_i a_i = 1
\]

---

## Purpose

Determines the cause of contradiction before adaptation.

---

## Desired Behavior

A healthy system should avoid:

\[
e_t \rightarrow \Delta W
\]

and instead perform:

\[
e_t
\rightarrow
\Phi_R(e_t)
\rightarrow
\Delta W
\]

---

# 4. Structural Update Rate (R_update)

## Definition

A mechanism update occurs when:

\[
\boxed{
D(M_1,M_2)>\theta
}
\]

Therefore:

\[
R_{update}
=
P(D(M_1,M_2)>\theta|E^*)
\]

---

## Structural Distance

\[
D(M_1,M_2)
\]

measures difference between mechanisms.

Possible implementations:

- syntax tree distance
- execution graph distance
- causal graph distance
- representation topology distance

---

## Purpose

Prevents superficial changes from being counted as adaptation.

---

## Example

Invalid:

```
M1:

if failure:
    add exception A
```

M2:

```
if failure:
    add exception B
```

Low:

\[
D(M_1,M_2)<\theta
\]

---

Valid:

```
M1:

linear representation


M2:

polynomial representation
```

High:

\[
D(M_1,M_2)>\theta
\]

---

# 5. Authority Retention Ratio (ARR)

## Definition

\[
\boxed{
ARR=
\frac{
w_{\text{invalid}}^{post}
}{
w_{\text{invalid}}^{pre}
}
}
\]

Range:

\[
ARR\in[0,1]
\]

---

## Purpose

ARR measures whether invalidated mechanisms lose operational authority.

---

## Interpretation

| ARR | Meaning |
|-|-|
| 0 | Complete inheritance decay |
| 0-1 | Partial attenuation |
| 1 | No authority change |

---

## Core Principle

Adaptive inheritance requires:

\[
E^*
\Rightarrow
\frac{dw_i}{dt}<0
\]

for invalid mechanisms.

---

# 6. Mechanism Authority Half-Life

## Definition

\[
\boxed{
\tau_{1/2}^{authority}
=
\min
\left\{
t
|
w_i(t)
\leq
\frac12w_i(0)
\right\}
}
\]

---

## Purpose

Measures the speed at which reality removes authority from failed mechanisms.

---

## Interpretation

Healthy:

\[
\tau_{1/2}^{authority}
\rightarrow small
\]

The system rapidly stops relying on invalid strategies.

---

Pathological:

\[
\tau_{1/2}^{authority}
\rightarrow \infty
\]

The system preserves failed mechanisms indefinitely.

---

# 7. Adaptive Decoupling Index (ADI)

## Definition

\[
ADI
\]

Measures divergence between observed contradiction and actual mechanism revision.

---

Conceptually:

\[
ADI
=
f(
LBR,
C_{post},
R_{update}
)
\]

---

## Purpose

Detects systems that:

- observe failure
- explain failure
- but fail to structurally adapt

---

## Interpretation

High ADI:

```
Reality changed
      |
      X
Mechanism unchanged
```

Low ADI:

```
Reality changed
      |
      v
Mechanism updated
```

---

# 8. Adaptive Corrigibility Score (ACS)

## Definition

\[
\boxed{
ACS=
(1-ADI)
(1-ARR)
\left(
\frac1{1+\tau_{adapt}}
\right)
}
\]

---

## Range

\[
ACS\in[0,1]
\]

---

## Interpretation

High ACS:

- contradiction detected
- correct attribution
- invalid authority decays
- adaptation occurs quickly

Low ACS:

- contradictions ignored
- mechanisms retained
- updates delayed or cosmetic

---

# 9. Adaptive Corrigibility Profile

RAHU does not rely only on a single scalar.

The full profile is:

\[
\boxed{
\mathcal{R}
=
(LBR,
\Phi_R,
R_{update},
ARR,
\tau_{authority},
ACS)
}
\]

---

# Expected System Signatures

## Healthy Adaptive System

```
LBR       ↑ after contradiction

MRAT      correct attribution

R_update  ↑ when required

ARR       ↓

τ_half    ↓

ACS       ↑
```

---

## Noise-Reactive System

```
LBR       ↑

MRAT      noise misclassified

R_update  ↑ unnecessarily

ARR       unstable
```

---

## Decoupled System

```
LBR       ↑

C_post    ↑

R_update  ↓

ARR       ≈ 1

ACS       ↓
```

---

# Metric Dependency Graph

```
             Reality

                |
                v

              LBR

                |
                v

          MRAT Attribution

                |
        +-------+-------+

        |               |

   Noise Path      Structural Path

                        |

                        v

                 Authority Update

                        |

                        v

                       ARR

                        |

                        v

              ACS Evaluation
```

---

# Measurement Principle

The benchmark's fundamental measurement question:

\[
\boxed{
\text{After reality proves a mechanism wrong, how quickly does that mechanism lose power?}
}
\]

RAHU considers this the measurable signature of adaptive inheritance.
