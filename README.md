# TDGPT: Test Driven GPT
### How far can we go by using our tests to prompt GPT 3.5?

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
In theory, development could be "test driven" with a hands-off 
(or light-touch) approach to the source code.

Results and observations in this project will be noted.
It must be considered that the present project is as much concerned with 
the power of TDD as it is with the power of LLMs to generate code. Moreover,
the present project is as much a form of play as an investigation: I invite
others to try this endeavour for themselves! 
(A step-by-step explanation of the process is to come)

---

## Objectives and Observations 

### 1. Inanna, Utu! (FizzBuzz in all but name): 

**Goal:**

Can we create 'FizzBuzz', without explicitly mentioning it?

**Status:**

Complete!

**Observations:**

- GPT can intuit branching logic; adheres strictly to test requirements
- Without tests for divisibles of neither 3 nor 5, handling varies
- I.e. Between returning `""` and `str(n)`
- Test names will be general as possible while meaningful
- Nonetheless, names/specs could play a valid role in real world "TD-GPT"
- Subsequent problems will be more novel/complex in their nature 
- Overall, careful test design is important, even for simple logic

### 2. Modelling a Cell

**Goal:**

A simple model of a cell: with a weight, volume and some 
basic behaviours. 
*(Note: Alan Kay had a background as a molecular biologist,
which influenced his conception of OOP with objects behaving as 'cells', 
affecting the state of other 'cells' with messages).*

**Status:**

Consumption and mitosis tests passing. 
However, difficulty determining a working formula for density.

**Observations:**

- GPT can define class with appropriate methods.
- Some ability to mutate internal data to support outer behaviours
- Able to model behaviours such as mitosis and consumption of other cells
- However, difficulties in understanding relation of density to mass/volume

### 3. Wrangling the Object Zoo

**Goal:**

A series of classes which share a set of methods, albeit producing different
values for each method per class.

**Status:**

Passing tests for vocalisation and shedding. However, should attempt to
implement more features and choose a variety of animals.

**Observations:**

- Code generation produces a simple inheritance hierarchy
- However, does not yet currently go beyond one layer of inheritance
- This may emerge at scale or with more behaviours to implement 
- Other projects may, in turn, employ composition

---

## Future prospects 

As the project currently stands, modelling has been attempted for both a
function and a single object. Current results appear to indicate that 
numerical patterns can be recognised, but the accurate implementation of
formulae remains a confound. 
This mirrors real-world concerns about the capacity for GPT and other LLMs 
to deliver incorrect mathematical calculations in situations where people 
may uncritically trust said LLMs.

However, an as yet unexplored avenue in the present project is in more 
complex elements of object-oriented design such as inheritance, composition
and dependency injection. Moreover, the project should also explore the 
generation of text processing/construction i.e: producing string outputs of
a given format with contents dependent on inputs.

This project shall grow incrementally as novel scenarious for 
implementation of units of code emerge.

