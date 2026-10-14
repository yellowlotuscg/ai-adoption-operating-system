# AI Adoption Operating System

Training materials for teams learning to use AI in ordinary work: safe-use rules, a short workshop, and a checklist for a supervised pilot. People need a workflow, a person accountable for the result, and a way to check the output. Picking a model comes after that.

## Get a copy

```bash
git clone https://github.com/yellowlotuscg/ai-adoption-operating-system.git
```

The files are Markdown. Read them on GitHub, or clone over HTTPS and read them locally. The workshop can be done on paper. No model account is required.

## Core lessons

- [Safe-use introduction](curriculum/01-safe-use.md): classify information before anyone pastes it into a tool.
- [Task decomposition exercise](curriculum/02-task-decomposition.md): when someone is stuck, ask for one small next step and wait.
- [Use-case canvas](templates/use-case-canvas.md): write down the workflow, the human decision, and the stop condition.
- [Research references](REFERENCES.md): external curricula and risk documents, and how to use them with these materials.

## Workshop and supervised pilot package

- [Facilitator guide and role variations](curriculum/03-facilitator-guide.md)
- [Synthetic source-checking lab, reusable prompt and answer key](curriculum/04-source-checking-lab.md)
- [Learner assessment and readiness rubric](templates/assessment.md)
- [Pilot measurement, feedback, incident and handoff record](templates/pilot-feedback-handoff.md)

Start with the facilitator guide, then complete the lab and the assessment before proposing a pilot that uses real business data. The guide is a proposed 60-minute session. Its examples are synthetic. The role variations are customer service, operations, and manager practice.

The facilitator guide links to the [Deployment Starter training guide](https://github.com/yellowlotuscg/small-business-deployment-starter/blob/main/docs/ai-training-guide.md) for a separate staff exercise on that sample application.

## Suggested sequence

1. Identify the repetitive work and any sensitive data.
2. Choose one low-risk workflow and fill in the use-case canvas.
3. Define the decision that stays with a person.
4. Practice on the synthetic lab. Use examples from real work only after data classification, an approved tool, and a named reviewer are set.
5. On a small sample, measure quality, time, rework, and exceptions.
6. Expand only after review.

This is a training and operating checklist. It is not a promise that every workflow should be automated.

## Checks and limits

From the repository root:

```bash
python3 scripts/check_materials.py
```

[`scripts/check_materials.py`](scripts/check_materials.py) checks that local Markdown links point at files, that the workshop files still contain the required phrases, and that no Markdown file contains an em dash. [`.github/workflows/materials.yml`](.github/workflows/materials.yml) runs that same script on Python 3.12 for every push and pull request.

These checks do not evaluate teaching quality or prove learning outcomes.

The materials are in this repository. No measured client training pilot is claimed. Detailed industry-specific courses and demonstrated business outcomes remain outside this public example.

## Optional training alongside deployment

Yellow Lotus Consulting Group offers practical AI training as an optional part of a small-business deployment. The aim is to help staff use the system in everyday work, check results, protect business information, and recognize when human review is needed. This describes an available service, not past client results.

## What the references cover

[REFERENCES.md](REFERENCES.md) lists the NIST AI Risk Management Framework, an ISO/IEC 42001 overview, the OWASP Top 10 for LLM Applications, and the MIT-licensed Microsoft AI for Beginners curriculum. The lessons in this repository add data classification, source checking, and human review. Those links are reading pointers for facilitators.

## License

[MIT License](LICENSE). Copyright (c) 2026 Matthew Coggins.
