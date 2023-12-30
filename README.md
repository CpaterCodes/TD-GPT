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

## Instructions for playing around

I invite those who are interested in this approach to try it out for 
themselves. All you will need is:

- An OpenAI secret key, generated through an OpenAI account 
- Python 3.11 or higher
- Pipenv

**To install and setup:**

1. Clone this repository and navigate to it.
2. Copy `.env.example` to `.env`
3. In `.env`, set `OPENAI_KEY` to your OpenAI key.

**To run tests:**

To run tests for `InannaUtu`, for example, you can run 
`pipenv run pytest InannaUtu/test.py`. 

However, a bash script has also been provided for convenience as this is 
otherwise a verbose command. Continuing with `InannaUtu` as an example it 
can be run with `./test.sh InannaUtu/`, assuming the script has been made 
executable (`chmod +x ./test.sh`).

**To generate source code:**

For a given experiment, using `InannaUtu` once again as an example, one can
run `pipenv run python3 prompt.py InannaUtu/` to generate fresh source code 
for `InannaUtu`. However, a script is also provided for convenience and can 
be invoked with `./codegen.sh InannaUtu/` instead.

**To run your own TD-GPT experiments:**

We have established that both testing and code generation can be performed
for an experiment directory such as `InannaUtu`, `Cell` or `ObjectZoo`.

However, all that a custom directory needs to perform code generation and 
testing is a file named `test.py` containing pytest tests as if for a 
set of units of code which already exist in a neighbouring file `src.py`.
See existing `test.py` files under one of the aforementioned experiment 
directories for a visual example.

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
*Note:* 
```
Alan Kay had a background as a molecular biologist,
which influenced his conception of OOP with objects behaving as 'cells', 
affecting the state of other 'cells' with messages.
```

**Status:**

Consumption, density and mitosis tests passing. Complete!

**Observations:**

- GPT can define class with appropriate methods.
- Some ability to mutate internal data to support outer behaviours
- Able to model behaviours such as mitosis and consumption of other cells
- Difficulties understanding density in terms of 'weight', but not 'mass'
- Again, semantic elements substantially affect accuracy of implementation

### 3. Wrangling the Object Zoo

**Goal:**

A series of classes which share a set of methods, albeit producing different
values for each method per class.

**Status:**

Passing tests for vocalisation and shedding. However, should attempt to
implement more features and choose a variety of animals.

**Observations:**

- Code generation produces a simple inheritance hierarchy
- With enough subclasses, multi layer inheritance emerges
- Could also emerge with more behaviours to implement 
- Other projects may, in turn, employ composition

## Future prospects 

Future exercises in this project can explore composition-based designs or
complete software systems such as REST APIs. As such, this project may be
revisited and expanded upon in future.

