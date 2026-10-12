# EduPulse
EduPulse is an education-domain AI platform engineering portfolio project.
It predicts post-day-27 course withdrawals from historical OULAD enrollment data.
The learner-support output is advisory and always reviewed by educators.
A later service drafts rubric-aligned assignment feedback for educator approval.
Week 1 delivers a reproducible leakage-aware prediction baseline.
The platform will evolve into a versioned ML pipeline and model-serving API.
Infrastructure goals include AWS ECS/EC2, monitoring, CI/CD, and benchmark evidence.
Public OULAD data and synthetic assignments only; never upload real learner records.
Run the Week 1 smoke check with `uv run python -m edupulse.smoke`.