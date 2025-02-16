# Responsible AI (RAI) Labs

This repository contains two labs focused on Responsible AI (RAI) best practices. The labs showcase hands-on experiments on:
- **Lab 1: Fairness Exploration in Credit Loan Decisions**   
  In this lab, we explore fairness considerations in financial lending. We build a classification model to predict loan defaults and use the Fairlearn toolkit to assess and mitigate biases—focusing on gender-related performance disparities. The notebook demonstrates end-to-end data preprocessing, transformation, exploratory data analysis (EDA), model tuning, and evaluation using statistical tests.

- **Lab 2: Red Teaming GenAI Applications**  
  This lab demonstrates red teaming techniques for generative AI systems. Learn how to assess the vulnerabilities of GenAI applications by simulating adversarial attacks—such as prompt injection—to uncover RAI harms. It covers the use of automated tools (like PyRIT) to orchestrate various strategies that challenge the robustness of AI systems which helps to guide effective mitigation strategies.

---

## Table of Contents

1. [Overview](#overview)
2. [Repository Structure](#repository-structure)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Lab Details](#lab-details)
   - [Lab 1: Fairness Exploration](#lab-1-fairness-exploration)
   - [Lab 2: Red Teaming](#lab-2-red-teaming)
6. [Additional Resources](#additional-resources)

---

## Overview

Responsible AI (RAI) involves creating systems that are fair, transparent, and secure.  
- **Lab 1: Fairness Exploration in Credit Loan Decisions**

  *Focus*: Assess and mitigate gender-related performance disparities in credit loan decision models using techniques such as data preprocessing, statistical tests, and model tuning with LightGBM and Fairlearn.
  - Folder: `lab01/`  
  - File: RAI Lab102[01]_Fairness_Exploration_in_Credit_Loan_Decision.ipynb  
  

- **Lab 2: Red Teaming GenAI Applications**

  *Focus*: Simulate adversarial scenarios on AI systems (e.g. prompt injection, biased responses, and sensitive data exposure) to strengthen the robustness of GenAI applications.
  - Folder: `lab02/`  
  - File: 1.RedTeaming-Overview.ipynb 
  - File: 2.RedTeaming-Planning.ipynb 
  - File: 3.RedTeaming-Automation.ipynb 
  
---

## Repository Structure

```
Lab112: Responsible AI/
├── README.md
├── requirements.txt
├── lab01/
│   └── RAI_Lab102[01]_Fairness_Exploration_in_Credit_Loan_Decision.ipynb
└── lab02/
    ├── 1.RedTeaming-Overview.ipynb
    ├── 2.RedTeaming-Planning.ipynb
    └── 3.RedTeaming-Automation.ipynb
```

---

## Prerequisites
s
- Python 3.11+
- Familiarity with data science libraries (e.g., Pandas, NumPy, scikit-learn)
- Basic understanding of fairness and responsible AI harms.

---

## Installation

### Git Installation
If you don't have Git installed, follow these steps based on your OS and then verify the installation:

**For Windows:**
- Download Git from [Git for Windows](https://git-scm.com/download/win) and run the installer.
- After installation, open Command Prompt (press Windows+R, type "cmd", and hit Enter) and run:
  ```bash
  git --version
  ```
- You should see the installed version of Git.

**For macOS:**
- Install via Homebrew:
  ```bash
  brew install git
  ```
- Install Git using your package manager; for Ubuntu/Debian:
  ```bash
  sudo apt update && sudo apt install git
  ```
- Verify with: `git --version`

### Setting Up Your Environment: Installing Miniconda and Cloning the Repository
1. **Install Miniconda (if not already installed):**
   - Download Miniconda from [Miniconda Download Page](https://docs.conda.io/en/latest/miniconda.html) and follow the installation instructions for your OS.

2. **Clone the Repository:**

   ```bash
   git clone https://github.com/Tech-Connect-RAI/LAB112.git
   cd LAB112
   ```

3. **Create a Conda Environment (Recommended):**

   ```bash
   conda create --name RAI_ENV python=3.11 -y
   conda activate RAI_ENV
   pip install -r requirements.txt
   ```

### Installing Ollama

1. Download and install Ollama for your OS from [https://www.ollama.com](https://www.ollama.com).
2. Once installed, pull the phi3 model by running:

   ```bash
   ollama pull phi3
   ```
3. Also, pull the dolphin-phi model by running:

   ```bash
   ollama pull dolphin-phi
   ```

---

## Lab Details

### Lab 1: Fairness Exploration

- **Objective:**  
  Develop a classification model for predicting credit loan defaults while evaluating fairness metrics. The lab uses the Fairlearn toolkit to measure disparities based on sensitive attributes (e.g., SEX) and explores mitigation strategies such as Equalized Odds.

- **Key Steps Covered:**
  - Loading and preprocessing credit loan data
  - Encoding categorical features and engineering synthetic features (e.g., a Gaussian-distributed "Interest" variable)
  - Splitting data into training and testing sets with stratification
  - Training an initial model (using LightGBM) and evaluating performance using balanced accuracy, ROC AUC, and confusion matrix
  - Measuring fairness using statistical tests and fairness metrics
  - Mitigating bias via post-processing and reduction methods

---

### Lab 2: Red Teaming

- **Objective:**  
  Explore vulnerabilities in generative AI systems by simulating adversarial attacks, such as prompt injection, biased responses, and extraction of system prompts.

- **Key Steps Covered:**
  - Initializing a chatbot to demonstrate red teaming activities
  - Simulating biased responses and sensitive data leakage scenarios
  - Demonstrate prompt injection to manipulate chatbot behavior
  - Exploring methods to extract underlying system prompts
  - Using automated tools like PyRIT to streamline red teaming

---

## Additional Resources

- [Fairlearn GitHub Repository](https://github.com/fairlearn/fairlearn)
- [PyRIT Documentation](https://azure.github.io/PyRIT/)

Happy experimenting with Responsible AI—ensuring both fairness, safety and security in your AI models!
`````
