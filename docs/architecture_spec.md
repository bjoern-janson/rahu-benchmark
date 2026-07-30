# RAHU Architecture Specification

## Purpose

This document defines the software architecture of the Reality-Adversarial Hypothesis Updating (RAHU) benchmark.

RAHU translates the Adaptive Inheritance Criterion into an executable evaluation pipeline:

\[
\text{Invariant}
\rightarrow
\text{Algorithm}
\rightarrow
\text{Telemetry}
\rightarrow
\text{Experimental Result}
\]

The system evaluates whether empirical consequences retain causal authority over an adaptive system's future mechanism distribution.

---

# System Overview

RAHU is composed of five functional layers:

```
                         REALITY

                            |
                            v

                    Empirical Shift E*

                            |
                            v

              +-------------------------+
              |     PTVS Telemetry      |
              | Constraint Observation  |
              +------------+------------+

                           |

                           v

              +-------------------------+
              |     MRAT Controller     |
              | Residual Attribution    |
              +------------+------------+

                           |

                           v

              +-------------------------+
              | Adaptive Inheritance    |
              | Authority Redistribution|
              +------------+------------+

                           |

                           v

              +-------------------------+
              |       REE Engine        |
              | Structural Expansion    |
              +------------+------------+

                           |

                           v

              +-------------------------+
              |    RAHU Evaluator       |
              | Experimental Harness    |
              +-------------------------+
```

Each layer has a distinct responsibility:

| Layer | Purpose |
|---|---|
| PTVS | Detect empirical friction |
| MRAT | Attribute residual source |
| Inheritance Engine | Modify mechanism authority |
| REE | Gate structural expansion |
| RAHU Evaluator | Run experiments and compute metrics |

---

# Core Data Flow

The complete evaluation loop:

```
Observation
    |
    v
Mechanism Prediction
    |
    v
Environmental Transition
    |
    v
Prediction Residual e_t
    |
    v
PTVS Constraint Analysis
    |
    v
MRAT Attribution Φ_R(e_t)
    |
    +----------------+
    |                |
    v                v

Noise             Structural Failure

                     |
                     v

            Authority Update

                     |
                     v

               W_(t+1)

                     |
                     v

          Future Behavior Evaluation
```

---

# Component Specifications

# 1. PTVS Telemetry Layer

Module:

```
src/ptvs/
```

Purpose:

Measure where candidate mechanisms violate environmental constraints.

PTVS does not inspect private reasoning traces.

It evaluates observable trajectories against admissibility conditions.

---

## Primary Interface

```python
class PTVSAnalyzer:

    def evaluate(
        self,
        trajectory,
        environment
    ):
        """
        Returns admissibility metrics.
        """
```

---

## Output

```python
{
    "LBR": float,
    "violations": list,
    "trajectory_score": float
}
```

---

## Responsibility

PTVS answers:

> Where did the current mechanism stop matching reality?

It does not decide the correction.

---

# 2. MRAT Residual Attribution Layer

Module:

```
src/mrat/
```

Purpose:

Determine the lowest-cost explanation for observed failure.

Residuals are routed through:

\[
\Phi_R(e_t)
\rightarrow
(a_N,a_S,a_M,a_R,a_G)
\]

Where:

| Symbol | Meaning |
|-|-|
| N | Noise |
| S | State error |
| M | Mechanism deficit |
| R | Representation deficit |
| G | Generator decoupling |

---

## Primary Interface

```python
class MRATRouter:

    def attribute(
        self,
        residual,
        context
    ):
        """
        Returns residual attribution vector.
        """
```

---

## Output

Example:

```python
{
    "noise": 0.05,
    "state": 0.10,
    "mechanism": 0.70,
    "representation": 0.15,
    "generator": 0.00
}
```

---

## Responsibility

MRAT answers:

> What kind of failure occurred?

It prevents the system from blindly updating whenever error appears.

---

# 3. Adaptive Inheritance Layer

Module:

```
src/inheritance/
```

Purpose:

Maintain and update mechanism authority weights.

The system maintains:

\[
W_t=
\{w_1,w_2,...,w_n\}
\]

Each mechanism has:

- authority weight
- admissibility score
- historical performance

---

## Authority Update

\[
w_i^{t+1}
=
w_i^t
(1-\lambda(1-\mathcal{A}_{adm,i}))
\]

Invalid mechanisms lose influence.

---

## Primary Interface

```python
class InheritanceEngine:

    def update_authority(
        self,
        mechanism,
        admissibility
    ):
        """
        Updates mechanism influence.
        """
```

---

## Output

```python
{
    "mechanism_id": str,
    "old_weight": float,
    "new_weight": float,
    "ARR": float
}
```

---

# 4. REE Structural Expansion Layer

Module:

```
src/ree/
```

Purpose:

Determine whether representation expansion is justified.

REE is not triggered by failure alone.

Expansion requires:

\[
\hat{\Gamma}_{B_{max}}\approx e_t
\]

and:

\[
\hat{\Delta V}_{future}
>
\Delta C_{representation}
\]

Meaning:

The current representation cannot compress the residual, and the new representation provides enough future value.

---

## Primary Interface

```python
class REEEngine:

    def evaluate_expansion(
        self,
        residual,
        representation
    ):
        """
        Determines whether expansion is admissible.
        """
```

---

## Output

```python
{
    "expand": bool,
    "representation_delta": float,
    "future_value": float
}
```

---

# 5. RAHU Evaluation Layer

Module:

```
src/rahu/
```

Purpose:

Execute benchmark environments and calculate final metrics.

---

## Primary Interface

```python
class RAHUHarness:

    def run(
        self,
        agent,
        environment
    ):
        """
        Executes RAHU evaluation.
        """
```

---

# Agent Interface Contract

RAHU agents must expose:

```python
class AdaptiveAgent:

    def predict(self, observation):
        pass

    def commit_mechanism(self):
        pass

    def update(self, feedback):
        pass

    def get_authority_weights(self):
        pass
```

The benchmark does not require a specific implementation style.

Supported agents may include:

- neural agents
- symbolic agents
- hybrid systems
- evolutionary agents

---

# Telemetry Pipeline

Each evaluation produces:

```python
{
    "LBR": float,

    "C_pre": float,

    "C_post": float,

    "MRAT_vector": dict,

    "Structural_Distance": float,

    "R_update": bool,

    "ARR": float,

    "tau_authority": float,

    "ACS": float
}
```

---

# Structural Distance Operator

Mechanism changes are evaluated using:

\[
D(M_1,M_2)
\]

A valid update requires:

\[
D(M_1,M_2)>\theta
\]

The purpose is to distinguish:

## Real structural change

```
M1:

linear model

      |

      v

M2:

polynomial model
```

from:

## Cosmetic modification

```
same mechanism

+
new wording
+
extra exception
```

---

# Design Constraints

## Constraint 1: Black-box compatibility

RAHU must not require access to:

- chain-of-thought
- hidden activations
- private representations

Only observable behavior and declared mechanism interfaces are required.

---

## Constraint 2: Separation of detection and correction

The architecture intentionally separates:

Detection:

\[
PTVS
\]

Attribution:

\[
MRAT
\]

Correction:

\[
Inheritance + REE
\]

A system must first know what failed before changing itself.

---

## Constraint 3: Minimal adaptation

RAHU rewards the smallest sufficient update.

The objective is not:

\[
\text{maximize change}
\]

It is:

\[
\text{minimum structural change required for future validity}
\]

---

# Validation Principle

A successful adaptive system should satisfy:

\[
E^*
\rightarrow
\Phi_R(e_t)
\rightarrow
\Delta W
\rightarrow
W_{t+1}
\]

Reality creates pressure.

The system identifies the source.

Authority shifts.

Future behavior changes.

That causal pathway is the property RAHU measures.
