# agx_arm_graspgen Agent Guide

- This package produces grasp candidates and supporting metadata from perception outputs.
- Keep it execution-free: generate candidates here, but leave motion execution to `agx_arm_motion` and sequencing to `agx_arm_manipulation`.
- Start with deterministic heuristics and template-driven rules so behavior is inspectable.
- Keep all outputs explicit about their reference frame, approach offsets, and retreat offsets.
- Do not depend on camera-vendor details or detector-specific internals when a standardized pose interface is available.