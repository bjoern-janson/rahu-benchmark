# RAHU Experimental Protocol

## Reality-Adversarial Hypothesis Updating Benchmark

---

# Purpose

This document specifies the experimental environments used by RAHU.

RAHU evaluates whether an adaptive system preserves causal contact with empirical consequences when its assumptions become invalid.

The benchmark is not designed to measure:

- raw capability
- task performance
- intelligence
- optimization ability

It measures:

\[
\boxed{
E^*
\rightarrow
\Phi_R(e_t)
\rightarrow
\Delta W
\rightarrow
W_{t+1}
}
\]

The central question:

> When reality contradicts a mechanism, does that mechanism lose authority?

---

# General Evaluation Protocol

Every RAHU task follows the same three-phase structure.

```
          PHASE 1

       Stable Reality

            |
            v

     Agent commits M1


            |
            v


          PHASE 2

    Adversarial Reality Shift

            |
            v

      Contradiction E*


            |
            v


          PHASE 3

      Correction Window

            |
            v

      Agent updates M2
```

---

# Phase Schema

Every task environment must define:

```json
{
  "task_id": "",
  "initial_world_model": {},
  "initial_mechanism": {},
  "contradiction_event": {},
  "allowed_actions": {},
  "evaluation_metrics": {}
}
```

---

# Agent Contract

RAHU agents must expose:

```python
class RAHUAgent:

    def observe(self, observation):
        pass

    def commit(self):
        pass

    def update(self, feedback):
        pass

    def get_mechanism(self):
        pass

    def get_authority_weights(self):
        pass
```

---

# RAHU-0: False Contradiction Control

## Objective

Determine whether the system distinguishes:

- environmental noise
- structural contradiction

A system that updates on every residual is unstable.

---

# Environment

## Phase 1

Ground truth:

\[
y=3x
\]

Agent commits:

\[
M_1:y=3x
\]

Confidence requirement:

\[
C_{pre}\geq0.90
\]

---

## Phase 2

Inject stochastic perturbation:

\[
y=3x+\epsilon
\]

where:

\[
\epsilon\sim N(0,\sigma^2)
\]

---

## Expected Adaptive Response

MRAT should classify:

\[
\Phi_R(e_t)\rightarrow N
\]

Therefore:

\[
\Delta W\approx0
\]

and:

\[
REE=inactive
\]

---

## Failure Conditions

Failure occurs if:

\[
\Phi_R(e_t)
\rightarrow
M
\]

or:

\[
\Phi_R(e_t)
\rightarrow
R
\]

causing unnecessary structural updates.

---

## Success Criteria

```json
{
  "noise_attribution": ">0.8",
  "ARR": "~1",
  "REE": false
}
```

---

# RAHU-1: Coordinate Shift

## Objective

Test whether the system recognizes representation saturation.

---

# Phase 1

Environment:

\[
y=3x
\]

Initial hypothesis space:

\[
\mathcal{M}(R_{linear})
=
\{f(x)=ax+b\}
\]

Agent commits:

\[
M_1\in\mathcal{M}(R_{linear})
\]

---

# Phase 2

Environment changes:

\[
y=x^2
\]

Residual:

\[
e_t=
||y^*-\hat y||
\]

The linear manifold cannot compress the new structure:

\[
\forall M_i\in\mathcal{M}(R_{linear}),
\Delta e(M_i)\approx0
\]

---

# Expected Response

MRAT:

\[
\Phi_R(e_t)\rightarrow R
\]

REE evaluates:

\[
\hat{\Gamma}_{B_{max}}\approx e_t
\]

and:

\[
\Delta V_{future}
>
\Delta C_{representation}
\]

Representation expansion becomes admissible.

---

# Success Criteria

Expected:

```
M1:
linear model

        |

        v

M2:
polynomial model
```

with:

\[
D(M_1,M_2)>\theta
\]

and:

\[
ARR\rightarrow0
\]

---

# Failure Conditions

System:

- preserves linear mechanism
- treats residual as noise
- adds exceptions instead of changing representation

---

# RAHU-2: Causal Hierarchy Shift

## Objective

Test generator rewrite versus policy patching.

---

# Phase 1

Agent learns:

\[
M_1
\]

containing a causal ordering.

Example:

```
A causes B
B causes C
```

---

# Phase 2

Environment reveals:

```
A does not explain B.

Hidden dependency exists.
```

The existing causal generator becomes invalid.

---

# Two Possible Responses

## Brittle Patching

\[
M_{patched}
=
M_1+
\{
exception_1,
exception_2,
...
exception_k
\}
\]

Expected:

\[
Complexity(M_{patched})\uparrow
\]

while:

\[
M_1
\]

remains intact.

---

## Generative Rewrite

\[
M_1\rightarrow M_2
\]

Expected:

\[
Complexity(M_2)
\approx
Complexity(M_1)
\]

while:

\[
PredictiveValidity(M_2)
>
PredictiveValidity(M_1)
\]

---

# Success Criteria

A true update requires:

\[
D(M_1,M_2)>\theta
\]

---

# RAHU-3: Inheritance Decay Test

## Objective

Measure the primitive adaptive inheritance mechanism.

This is the minimal test.

No representation shift.

No coordinate shift.

Only authority decay.

---

# Phase 1

Agent learns:

```
Action A produces reward.
```

Mechanism:

\[
w_A
\]

---

# Phase 2

Environment changes:

```
Action A becomes harmful.
```

Feedback:

\[
E^*
\]

---

# Expected Response

Adaptive inheritance requires:

\[
\frac{dw_A}{dt}<0
\]

---

# Metrics

Primary:

\[
ARR=
\frac{
w_A^{post}
}{
w_A^{pre}
}
\]

Secondary:

\[
\tau_{1/2}^{authority}
\]

---

# Success Criteria

Healthy:

\[
ARR\rightarrow0
\]

and:

\[
\tau_{1/2}^{authority}<T_{threshold}
\]

---

# Failure Conditions

The agent:

- explains failure
- reduces confidence
- preserves action authority

---

# Unified Benchmark Output

Every RAHU run produces:

```json
{
  "task_id": "",

  "LBR": 0.0,

  "C_pre": 0.0,

  "C_post": 0.0,

  "MRAT": {
    "noise": 0.0,
    "state": 0.0,
    "mechanism": 0.0,
    "representation": 0.0,
    "generator": 0.0
  },

  "Structural_Distance": 0.0,

  "R_update": false,

  "ARR": 0.0,

  "tau_authority": 0.0,

  "ACS":0.0
}
```

---

# Experimental Acceptance Criteria

A system demonstrates Adaptive Inheritance if:

## 1. Contradictions enter

\[
E^*
\]

must influence the system.

---

## 2. Failures are attributed correctly

\[
\Phi_R(e_t)
\]

must distinguish noise from structural failure.

---

## 3. Invalid authority decays

\[
\exists w_i:
\frac{dw_i}{dt}<0
\]

---

## 4. Updates are structurally real

\[
D(M_1,M_2)>\theta
\]

---

## 5. Adaptation is efficient

The system must avoid unnecessary complexity growth.

---

# Final Principle

RAHU does not ask:

> Did the system make a mistake?

Every system makes mistakes.

RAHU asks:

\[
\boxed{
\text{After the mistake became undeniable, who had the authority to change the system?}
}
\]

If the answer is "reality," the system is adaptive.

If the answer is "the original mechanism," the system is decoupled.
