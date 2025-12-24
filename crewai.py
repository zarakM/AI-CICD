from crewai.tasks.hallucination_guardrail import HallucinationGuardrail
from crewai import LLM

# Basic usage - will use task's expected_output as context
guardrail = HallucinationGuardrail(
    llm=LLM(model="gpt-4o-mini")
)

# With explicit reference context
context_guardrail = HallucinationGuardrail(
    context="AI helps with various tasks including analysis and generation.",
    llm=LLM(model="gpt-4o-mini")
)