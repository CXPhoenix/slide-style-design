# ADR 0004 — Preserve trial revisions and corrected verdicts

Status: accepted as implementation of the existing approved evidence policy.
Date: 2026-10-04.

## Context

T13 CT04's initial pass overlooked an unrequested appearance choice in applied
settings. T14 independent review corrected it and performed one affected test on
a new Gates candidate. A successful retry must not erase the failed revision.

## Decision

Retain raw observations and the original verdict documents. Mark the active old
case failed with reason; record changed product hashes and a new candidate/result.
Release criteria reference qualifying revision-specific cases, with explicit delta
and oracle reasoning for older unchanged behavior. Per-case semantic review checks
optional accepted preferences independently from core/source compliance.

## Consequences

Evidence requires more storage and visible historical failures, but release claims
remain auditable. A later pass is not a pass for the original failed revision;
static integrity and model behavior remain distinct. This records existing spec
policy, does not authorize unlimited reruns, mixing, production or MCP work.
