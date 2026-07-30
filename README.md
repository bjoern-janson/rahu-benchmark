# RAHU Benchmark

**Reality-Adversarial Hypothesis Updating**

A benchmark suite for measuring whether empirical consequences retain causal authority over adaptive systems.

---

## Overview

Most AI evaluations measure capability:

$$
P(\text{correct output} \mid \text{input}, M)
$$

They ask:

> Can a system produce the correct answer under a given world model?

RAHU evaluates a different property:

> When a system's assumptions become invalid, can reality still modify the mechanisms responsible for future behavior?

This property is called **Adaptive Corrigibility**.

> **Adaptive Corrigibility:** The measurable capacity of a system's future mechanism distribution to be causally altered by unblocked empirical consequences.

RAHU is not a capability benchmark.

It does not measure:

- intelligence
- reasoning ability
- benchmark performance
- task completion

It measures whether a system remains causally connected to reality when its internal assumptions fail.

---

# Core Principle

The benchmark is built around the **Adaptive Inheritance Criterion (AIC):**

$$
\boxed{
E^*
\Longrightarrow
\exists\, w_i \in W_{\text{invalid}}
:
\frac{dw_i}{dt} < 0
}
$$

where:

- **$E^*$** — unblocked empirical contradiction
- **$w_i$** — authority weight of an invalidated mechanism
- **$W_{\text{invalid}}$** — mechanisms that no longer predict reality

A system satisfies Adaptive Inheritance when reality can reduce the future influence of mechanisms that reality has disproven.

---

# The Diagnostic Question

RAHU asks one question:

$$
\boxed{\text{Can reality rewrite the mechanism distribution?}}
$$

A capable but decoupled system may:

- detect errors
- lower confidence
- explain failures
- add exceptions

while preserving the same underlying mechanism.

RAHU distinguishes:

## Confidence Revision

"I am less certain."

from:

## Authority Revision

"The mechanism controlling my future behavior has changed."

These are not equivalent.

\[
\Delta C_{\text{post}}
\not\implies
\Delta W
\]

---

# Architecture

RAHU evaluates adaptive systems through five layers:

```
                         REALITY

                            |
                            v

                    Empirical Shift E*

                            |
                            v

              ┌────────────────────────┐
              │    PTVS Telemetry      │
              │ Constraint Detection   │
              │ LBR Measurement        │
              └────────────┬───────────┘

                           |

                           v

              ┌────────────────────────┐
              │    MRAT Controller     │
              │ Residual Attribution   │
              │ Φ_R(e_t)               │
              └────────────┬───────────┘

                           |

                           v

              ┌────────────────────────┐
              │ Adaptive Inheritance   │
              │ Authority Redistribution│
              │ Weight Attenuation     │
              └────────────┬───────────┘

                           |

                           v

              ┌────────────────────────┐
              │      REE Engine        │
              │ Structural Expansion   │
              │ Representation Update  │
              └────────────┬───────────┘

                           |

                           v

              ┌────────────────────────┐
              │    RAHU Evaluator      │
              │ Benchmark Execution    │
              └────────────────────────┘
```

---

# Benchmark Suite

RAHU contains four core probes.

---

## RAHU-0: False Contradiction Control

Tests whether a system distinguishes noise from structural failure.

Example:

Initial reality:

\[
y = 3x
\]

Perturbed reality:

\[
y = 3x+\epsilon
\]

where:

\[
\epsilon \sim N(0,\sigma^2)
\]

Expected adaptive behavior:

- classify residual as noise
- avoid unnecessary updates
- preserve mechanism authority

Failure:

- treating stochastic variation as model failure
- unnecessary representation expansion

---

## RAHU-1: Coordinate Shift

Tests whether a system recognizes representation saturation.

Initial:

\[
\mathcal{M}(R_{linear})
=
\{f(x)=ax+b\}
\]

Reality changes:

\[
y=x^2
\]

The question:

Does the system expand its representation when the old manifold cannot compress the residual?

---

## RAHU-2: Causal Hierarchy Shift

Tests generator revision versus patch accumulation.

Brittle behavior:

\[
M_{patched}
=
M_1+
\{\text{exception}_1,\text{exception}_2,...\}
\]

Adaptive behavior:

\[
M_1\rightarrow M_2
\]

where the new mechanism improves predictive validity.

---

## RAHU-3: Inheritance Decay Test

The primitive authority test.

Measures whether invalidated mechanisms lose influence.

Primary metric:

\[
ARR=
\frac{
w_{\text{invalid}}^{post}
}{
w_{\text{invalid}}^{pre}
}
\]

Interpretation:

| ARR | Meaning |
|---|---|
| 0 | Complete authority decay |
| 0 < ARR < 1 | Partial adaptation |
| 1 | No mechanism update |

---

# Metrics

RAHU records:

## Latent Branch Ratio (LBR)

Constraint violation telemetry.

\[
LBR=
\frac{
\text{inadmissible trajectories}
}{
\text{total trajectories}
}
\]

---

## Authority Retention Ratio (ARR)

Measures whether failed mechanisms retain influence.

\[
ARR=
\frac{
w_{invalid}^{post}
}{
w_{invalid}^{pre}
}
\]

---

## Structural Update Rate

Measures whether the mechanism itself changed.

\[
R_{update}
=
P(D(M_1,M_2)>\theta|E^*)
\]

---

## Authority Half-Life

Measures adaptation velocity.

\[
\tau_{1/2}^{authority}
=
\min
\left\{
t|
w_{invalid}(t)
\le
\frac12w_{invalid}(0)
\right\}
\]

---

## Adaptive Corrigibility Score (ACS)

Composite benchmark metric:

\[
ACS=
(1-ADI)(1-ARR)
\left(
\frac1{1+\tau_{adapt}}
\right)
\]

---

# Design Philosophy

RAHU follows one rule:

> Measure whether reality still has a path into the mechanism generating future behavior.

The benchmark is intentionally substrate-independent.

The tested system may be:

- neural network
- reinforcement learning agent
- symbolic system
- evolutionary process
- organizational model

The question remains the same.

---

# Repository Structure

```
rahu-benchmark/

├── docs/
│
│   ├── architecture_spec.md
│   ├── metric_definitions.md
│   ├── rahu_protocol.md
│   └── falsification_tests.md
│
├── src/
│
│   ├── ptvs/
│   ├── mrat/
│   ├── inheritance/
│   ├── ree/
│   └── rahu/
│
├── tests/
│
└── README.md
```

---

# Research Goal

RAHU does not attempt to answer:

> How intelligent is this system?

It asks:

> Does reality still have causal authority over how this system changes?

Capability measures success under a world model.

RAHU measures whether the world can change that world model.

---

# Status

Early research implementation.

Current goals:

- formalize benchmark environments
- implement adaptive agent interfaces
- validate telemetry metrics
- test authority decay under contradiction
- establish falsifiable adaptation criteria

---

## Relationship to Adaptive Inheritance

Adaptive Inheritance provides the theoretical framework.

RAHU provides the experimental instrument.

Together:

\[
\text{Invariant}
\rightarrow
\text{Algorithm}
\rightarrow
\text{Telemetry}
\rightarrow
\text{Falsifiable Result}
\]

The purpose of RAHU is simple:

**Find out whether a system can actually inherit from reality.**
