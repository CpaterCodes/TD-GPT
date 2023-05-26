# TDGPT: Test Driven GPT

## Project rationale

In the wake of chatGPT and in turn GPT-4, many developers are either
concerned about being replaced outright by LLM AI or are considering use of 
LLM AI to implement the functionality they desire. 
Moreover, many developers are considering simply automating the writing of
tests for the code that they already have or are already developing.

Conversely, others are concerned about the limitations of AI-generated code 
given the provided prompts, in particular with regards to proper testing
practice: indeed, the role of generative AI in software development
remains controversial and warrants healthy skepticism.

But there's another possibility: what if, instead of generating tests for
our code, LLMs can generate code given sufficiently sophisticated tests?

Results and observations in this area will be tracked, so watch this space!

---

## Objectives and Observations 

1. Inanna, Utu! (FizzBuzz in all but name): 
```
Goal: Can we create a form of FizzBuzz, without explicitly mentioning it?

Status: Handles divisibles of 3, 5, 15. Must handle others.

Observations:

The GPT model can intuit branching logic and anticipate some obvious edge 
cases, but also adheres strictly to the requirements of the tests.
In some builds without tests for divisibles of neither 3 nor 5, the 
function will return "". In others, it will (more appropriately) return 
str(n). 
Overall, the model implements nothing more or less than the code under 
test: this requires careful test design.
```

