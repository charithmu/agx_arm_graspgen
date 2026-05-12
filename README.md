# agx_arm_graspgen

`agx_arm_graspgen` turns perception outputs into candidate grasp plans. The package should begin with deterministic heuristics and workspace-specific templates rather than jumping immediately to heavier grasp planners.

## Design Goals

- Consume detections or object poses and produce grasp candidates, not executed motion.
- Start with tag-aligned and template-based heuristics that are easy to inspect and debug.
- Emit grasp metadata that downstream manipulation code can rank, visualize, or reject.
- Keep grasp generation independent from specific camera vendors and detector internals.

## Planned Responsibilities

- Convert detected poses into approach, grasp, and retreat candidates.
- Carry known-object templates and workspace-specific grasp rules.
- Provide enough metadata for downstream packages to reason about quality and fallback behavior.

## Implementation Instructions

1. Start with deterministic, parameterized heuristics and make them debuggable.
2. Separate candidate generation from candidate selection so manipulation code can choose policies later.
3. Keep outputs frame-aware and explicit about reference frames.
4. Add known-object templates only after the tag-aligned path is working end to end.
5. Avoid embedding MoveIt execution logic in this package.

## Validation Targets

- Candidate generation from AprilTag poses in simulation
- Reproducible pre-grasp and retreat generation
- Visualizable outputs before closed-loop manipulation is added