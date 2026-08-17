# Learning Notes: Introduction to AI & Python

Welcome to my learning notes for the **Introduction to AI & Python** module. Below is a structured summary of the foundational concepts of Artificial Intelligence, Machine Learning, Deep Learning, and basic programming concepts in Python.

---

## 1. Understanding Artificial Intelligence, Machine Learning, and Deep Learning

It is common to hear the terms **AI**, **ML**, and **Deep Learning** used interchangeably, but they represent nested subsets of the same field:

```
┌──────────────────────────────────────────────┐
│  ARTIFICIAL INTELLIGENCE (AI)                │
│  Systems that mimic human intelligence       │
│  ┌────────────────────────────────────────┐  │
│  │  MACHINE LEARNING (ML)                 │  │
│  │  Algorithms that learn from data       │  │
│  │  ┌──────────────────────────────────┐  │  │
│  │  │  DEEP LEARNING (DL)              │  │  │
│  │  │  Multi-layered neural networks  │  │  │
│  │  └──────────────────────────────────┘  │  │
│  └────────────────────────────────────────┘  │
└──────────────────────────────────────────────┘
```

### Key Differences at a Glance

| Parameter | Artificial Intelligence (AI) | Machine Learning (ML) | Deep Learning (DL) |
| :--- | :--- | :--- | :--- |
| **Scope** | Broadest concept; machines mimicking human intelligence. | Subfield of AI; systems learning from data patterns. | Subfield of ML; multi-layer neural networks (deep networks). |
| **Data Requirements** | Can work on rules/expert systems (no data) or statistics. | Needs thousands of data points to train mathematical models. | Needs millions of data points (very large datasets). |
| **Feature Engineering** | Hand-crafted rules by human experts. | Hand-crafted features extracted from raw data by engineers. | Automatic feature learning directly from raw data by layers. |
| **Hardware** | Works on standard CPU computers. | Works on CPUs; benefits from GPU acceleration. | Requires heavy GPU/TPU computing resources. |
| **Examples** | Chess engine (Stockfish), rule-based chatbots. | Linear Regression, Decision Trees, Spam filters. | ChatGPT (LLMs), Midjourney, Self-driving cars. |

---

## 2. Real-World Applications of AI

Artificial Intelligence is driving transformation across various sectors:

1. **Natural Language Processing (NLP)**: Large Language Models (LLMs) like GPT-4, Gemini, and Claude power smart assistants, document summarization, code generation, and translation services.
2. **Computer Vision**: Facial recognition systems, medical imaging diagnostics (detecting tumors), and defect inspection on assembly lines.
3. **Autonomous Vehicles**: Self-driving cars (Tesla, Waymo) use sensor fusion and deep neural networks to navigate traffic, read road signs, and avoid obstacles in real-time.
4. **Recommendation Systems**: Platforms like YouTube, Netflix, Spotify, and Amazon analyze user behavior and history to suggest highly relevant content and products.
5. **Healthcare & Drug Discovery**: AlphaFold (by Google DeepMind) predicts 3D protein structures, accelerating molecular biology and reducing drug design cycles from years to days.

---

## 3. Python Programming Foundations for AI

Python is the undisputed language of AI/ML due to its simple syntax, readability, and a massive ecosystem of libraries (like NumPy, Pandas, Scikit-Learn, PyTorch, and TensorFlow).

### Core Concepts

#### A. Variables & Data Types
Variables store data values in memory. In Python, you do not need to specify the type of a variable upon declaration.
```python
name = "Deep"            # String (Text)
age = 21                 # Integer (Whole Number)
learning_rate = 0.001    # Float (Decimal Number)
is_trained = True        # Boolean (True/False)
```

#### B. Control Flow (Loops & Conditionals)
Conditionals use `if`, `elif`, and `else` to perform decisions, while loops (`for` and `while`) repeat code blocks.
```python
# Conditional Logic
if age >= 18:
    print("Eligible for advanced AI courses.")
else:
    print("Recommended: Introduction to Scratch/Python.")

# Loop iteration (counting from 0 to 4)
for i in range(5):
    print(f"Iteration {i}")
```

#### C. Lists & Slicing
Lists are ordered collections of items that can be modified (mutable).
```python
frameworks = ["TensorFlow", "PyTorch", "Scikit-Learn"]
frameworks.append("Keras")      # Adds "Keras" to the end
first_two = frameworks[0:2]      # Returns ["TensorFlow", "PyTorch"]
```

#### D. Functions
Functions are reusable blocks of code that perform a specific task. They take parameters and return values.
```python
def calculate_loss(prediction, actual):
    """Calculates absolute error."""
    return abs(prediction - actual)

error = calculate_loss(0.85, 1.0)
print(f"Absolute Error: {error}") # Output: 0.15
```

---

## 4. How to Set Up Python Locally

1. **Download & Install**: Visit [python.org](https://www.python.org/downloads/) and download the latest installer for Windows. Make sure to check the box **"Add python.exe to PATH"** before clicking Install.
2. **Verify Installation**: Open PowerShell or Command Prompt and run:
   ```bash
   python --version
   pip --version
   ```
3. **Run Code**: Write Python code in a file (e.g. `main.py`) and execute it using:
   ```bash
   python main.py
   ```
