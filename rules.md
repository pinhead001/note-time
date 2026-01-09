# Task & Time Model — v1.4 (Frozen)

This document defines the canonical rules for task tracking, delegation, rollover, and rounding.
All application logic MUST conform to these rules.

---

## 1. Core Objects

### Task
A Task represents a unit of work that may span multiple days.

A Task has:
- an owner (you)
- an optional delegate
- a lifecycle state
- time entries recorded per day

There is no concept of "backlog" in this system.
If a task exists, it is either active, delegated, completed, or canceled.

---

## 2. Task States

Tasks MUST be in exactly one of the following states:

- ACTIVE  
  Eligible for time logging today.

- DELEGATED  
  Assigned to someone else, but still eligible for owner work.

- COMPLETED  
  Finished. No further time logging allowed.

- CANCELED  
  Abandoned. No time logging allowed.

State transitions:
- ACTIVE → COMPLETED | CANCELED | DELEGATED
- DELEGATED → ACTIVE | COMPLETED | CANCELED

No other transitions are valid.

Task creation ALWAYS results in an ACTIVE task.

---

## 3. Delegation Semantics

- Delegation does NOT remove ownership.
- Delegated tasks:
  - remain visible
  - remain part of summaries
  - are NOT auto-removed
  - may roll over
- Owner MAY log time normally on delegated tasks.
- Delegation has no effect on eligibility or totals.

There is no accept/decline workflow in v1.

---

## 4. Rollover Behavior

Rollover occurs at day boundary (local time).

Rules:
- ACTIVE and DELEGATED tasks automatically roll over to the next day.
- COMPLETED and CANCELED tasks never roll.

Rollover copies:
- task reference
- state
- delegation flag

Rollover does NOT copy:
- time entries
- notes

Rollover is implicit. There is no manual rollover action.

---

## 5. Time Tracking & Rounding

### Time Tracking
- Time is tracked in **exact minutes**.
- Time entries are never rounded at entry time.
- Multiple entries per task per day are allowed.

### Rounding (Summary Only)
- Rounding occurs ONLY when generating summaries.
- Daily task totals are rounded **UP** to the nearest **15-minute increment**.
- Minimum summarized time is 15 minutes if any time exists.

Examples:
- 1–15 min → 15 min
- 16–30 min → 30 min
- 31–45 min → 45 min
- 46–60 min → 60 min

Raw minutes are always preserved.

---

## 6. Invariants (Non-Negotiable)

- A task has exactly one state.
- Tasks are created ACTIVE.
- Time can only be logged to ACTIVE or DELEGATED tasks.
- COMPLETED and CANCELED tasks are immutable.
- Raw time is never mutated.
- Rounding is deterministic and summary-only.
- Rollover is automatic and irreversible per day.

This file is the source of truth.
