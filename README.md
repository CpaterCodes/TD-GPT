# TDGPT: Test Driven GPT

## Project rationale

In the wake of models such as GPT-3.5/4 and applications such as chatGPT, 
many developers are either concerned about being replaced outright by LLM AI
or are considering use of LLM AI to implement the functionality they desire.

Moreover, many developers are considering simply automating the writing of
tests for the code that they already have or are already developing.

Conversely, others are concerned about the limitations of AI-generated code 
given the provided prompts, in particular with regards to proper testing
practice: indeed, the role of generative AI in software development
remains controversial and warrants healthy skepticism.

But there's another possibility: what if, instead of generating tests for
our code, LLMs can generate code given sufficiently sophisticated tests?
In theory, development could be "test driven" with a hands-off approach to
the source code altogether (this is, of course, in theory.)

Results and observations in this project will be noted.
It must be considered that the present project is as much concerned with 
the power of TDD as it is with the power of LLMs to generate code. Moreover,
the present project is as much a form of play as an investigation: I invite
others to try this endeavour for themselves!

---

## Objectives and Observations 

### 1. Inanna, Utu! (FizzBuzz in all but name): 

**Goal:**

Can we create 'FizzBuzz', without explicitly mentioning it?

**Status:**

Complete! (For now...)

**Observations:**

- GPT can intuit branching logic; adheres strictly to test requirements.
- Without tests for divisibles of neither 3 nor 5, handling varies.
- I.e. Between returning `""` and `str(n)`
- Tests will now have anonymising names, with which builds still work.
- Nonetheless, names could play a valid role in real world "TD-GPT".
- Subsequent problems will be more novel/complex in their nature. 

- Overall, this project is an exercise in careful test design.

### 2. Modelling a Cell

**Goal**:

Starting with a simple model of a cell: with a weight, volume and some 
basic behaviours. Alan Kay had a backgroud in biology, after all.

**Status:**

To Start.

**Obserations:**

- Todo...


