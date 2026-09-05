# AI Adoption Operating System

A practical training and governance framework for helping teams use AI better without treating adoption as a tool rollout.

## Philosophy

AI adoption is a workflow and management problem before it is a model-selection problem. People need safe-use rules, context practices, verification habits, role-specific examples, and a way to improve the workflow after the pilot.

## Included today

- [Safe-use introduction](curriculum/01-safe-use.md)
- [Task decomposition exercise](curriculum/02-task-decomposition.md)
- [Use-case canvas](templates/use-case-canvas.md)
- [Research references](REFERENCES.md)

## Workshop and supervised pilot package

- [Facilitator guide and role variations](curriculum/03-facilitator-guide.md)
- [Synthetic source-checking lab, reusable prompt and answer key](curriculum/04-source-checking-lab.md)
- [Learner assessment and readiness rubric](templates/assessment.md)
- [Pilot measurement, feedback, incident and handoff record](templates/pilot-feedback-handoff.md)

Run the offline exercise without any model account. Start with the facilitator guide, then complete the lab and assessment before proposing a real pilot.

## Verification and limits

Run `python3 scripts/check_materials.py` to check local Markdown links, workshop section presence and punctuation. CI runs the same structural checks. These checks do not evaluate teaching quality or prove learning outcomes.

The materials are implemented, but no measured client training pilot is claimed. Detailed industry-specific courses and demonstrated business outcomes remain outside this public example.

## Optional training alongside deployment

Yellow Lotus Consulting Group offers practical AI training as an optional part of a small-business deployment. The aim is to help staff use the system in everyday work, check results, protect business information and recognize when human review is needed. This describes an available service, not past client results.

## Suggested sequence

1. identify repetitive work and sensitive data;
2. choose a low-risk workflow;
3. define the human decision that remains;
4. train the role with examples from its real work;
5. measure quality, time, rework, and exceptions;
6. expand only after review.

This is a training and operating framework, not a promise that every workflow should be automated. It references NIST AI RMF, ISO/IEC 42001 concepts, data classification, change management, role-based access, and human oversight.
