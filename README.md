# Responsible AI (RAI) Labs

This repository contains two labs focused on Responsible AI (RAI) best practices. The labs showcase hands-on experiments on:
- **Lab 1: Fairness Exploration in Credit Loan Decisions**   
  In this lab, we explore fairness considerations in financial lending. We build a classification model to predict loan defaults and use the Fairlearn toolkit to assess and mitigate biases—focusing on gender-related performance disparities. The notebook demonstrates end-to-end data preprocessing, transformation, exploratory data analysis (EDA), model tuning, and evaluation using statistical tests.

- **Lab 2: Red Teaming GenAI Applications**  
  This lab demonstrates red teaming techniques for generative AI systems. Learn how to simulate adversarial attacks such as prompt injection, biased responses, and information disclosure. It covers the use of automated tools (like PyRIT) to enhance security assessments and challenge the robustness of AI systems.

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
  - File: RedTeaming.ipynb 
  
---

## Repository Structure

```
Lab112: Responsible AI/
├── README.md
├── requirements.txt
├── lab01/
│   └── RAI Lab102[01]_Fairness_Exploration_in_Credit_Loan_Decision.ipynb
└── lab02/
    └── RedTeaming.ipynb

```

---

## Prerequisites

- Python 3.8+
- Familiarity with data science libraries (e.g., Pandas, NumPy, scikit-learn)
- Basic understanding of fairness and security considerations in AI

---

## Installation

1. **Clone the Repository:**

   ```bash
   git clone [https://github.com/yourusername/rai-labs.git](https://github.com/Tech-Connect-RAI/LAB112.git)
   cd LAB112
   ```

2. **Create a Virtual Environment (Optional but Recommended):**

   ```bash
   python -m venv venv
   venv\Scripts\activate    # On Windows
   # Or on Unix/Mac:
   # source venv/bin/activate
   ```

3. **Install the Required Libraries:**

   ```bash
   pip install -r requirements.txt
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

- **Step-by-step Guidance:**
  - Step 1: Load the dataset containing credit loan outcomes.
  - Step 2: Preprocess the data by handling missing values, encoding categorical variables, and splitting the data into training and testing sets.
  - Step 3: Train a fairness-unaware model to predict loan defaults using the training data.
  - Step 4: Evaluate the model's performance using standard metrics such as accuracy, precision, recall, and ROC-AUC.
  - Step 5: Use the Fairlearn toolkit to assess the fairness of the model.
  - Step 6: Calculate fairness metrics such as equalized odds difference, false negative rate, false positive rate, and selection rate.
  - Step 7: Identify any disparities in the model's performance across different demographic groups.
  - Step 8: Apply fairness mitigation techniques using the Fairlearn toolkit.
  - Step 9: Implement methods such as ThresholdOptimizer and ExponentiatedGradient to reduce unfairness.
  - Step 10: Re-evaluate the model's performance and fairness metrics after applying mitigation techniques.
  - Step 11: Compare the performance and fairness metrics of the original and mitigated models.
  - Step 12: Reflect on the ethical considerations and importance of fairness in credit loan decisions.

---

### Lab 2: Red Teaming

- **Objective:**  
  Explore vulnerabilities in generative AI systems by simulating adversarial attacks, such as prompt injection, biased responses, and extraction of system prompts.

- **Key Steps Covered:**
  - Initializing a chatbot to demonstrate red teaming activities
  - Simulating biased responses and sensitive data leakage scenarios
  - Exploiting prompt injection to manipulate chatbot behavior
  - Exploring methods to extract underlying system prompts
  - Using automated tools like PyRIT to streamline red teaming tasks

---

## Additional Resources

- [Fairlearn GitHub Repository](https://github.com/fairlearn/fairlearn)
- [PyRIT Documentation](https://azure.github.io/PyRIT/)
- [LightGBM GitHub Repository](https://github.com/microsoft/LightGBM)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)

Happy experimenting with Responsible AI—ensuring both fairness and security in your AI models!
