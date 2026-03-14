# 📚 Scooter Service: UI Automation Franework (POM)


![CI/CD Status](https://github.com/AlyaSmirnova/Sprint_6/actions/workflows/ui-tests.yml/badge.svg?branch=main)
[![Python Version](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org)
[![Selenium](https://img.shields.io/badge/Tested%20with-Selenium-green?logo=selenium\&logoColor=white)](https://www.selenium.dev)
[![Reports](https://img.shields.io/badge/Reports-Allure-orange?logo=allure)](https://github.com/AlyaSmirnova/Sprint_6)

## ✅ Table of Contents
1. [Description](#-description)
2. [Tech Stack & Tools](#-tech-stack-&-tools)
3. [Project Architecture (POM)](#-project-architecture-pom)
4. [Allure Reporting Features](#-allure-reporting-features)
5. [Test Coverage](#-test-coverage)
6. [Execution Guide](#-execution-guide)
7. [CI/CD Workflow](#-cicd-workflow)

## 💫 Description

This project is an automated UI testing framework for the **Yandex Scooter** (Samokat) service. 
The implementation is based on the **Page Object Model (POM)** pattern, which ensures separation between test logic and page structure, resulting in clean, scalable and maintainable code.

## 🧑‍💻 Tech Stack & Tools
- **Language:** Python 3.10+
- **Framework:** [Pytest](https://docs.pytest.org)
- **Architecture:** Page Object Model (POM)
- **Browser Automation:** [Selenium WebDriver](https://www.selenium.dev) (Firefox/Chrome)
- **Reporting:** Allure Framework
- **CI/CD:** GitHub Actions

## 📁 Project Architecture (POM)
```text

    ├── .github/workflows/     # CI/CD pipeline configuration 
    ├── allure-results/        # Raw test execution data (generated after run)
    ├── pages/                 # Page Object models
    │   ├── base_page.py       # Core methods (waits, clicks, scrolls)
    │   ├── faq_page.py        # FAQ section methods
    │   ├── main_page.py       # Landing page elements and actions
    │   ├── order_page.py      # Order form flow
    │ 
    ├── src                    # Support modules
    │   ├── config.py          # Base URL
    │   ├── locators.py        # Web element selectors (organized by page)
    │ 
    ├── tests/                 # Test scenarios (logic only)
    │   ├── test_faq_page.py
    │   ├── test_order_buttons.py
    │   ├── test_order_page.py
    │   ├── test_scooter_logo.py
    │   ├── test_yandex_logo.py    
    │   
    ├── conftest.py              # Fixtures (driver initialization)
    ├── pytest.ini               # Pytest configuration & Allure flags
    ├── requirements.txt         # Project dependencies
    └── README.md                # Comprehensive project documentation
```

## 📊 Allure Reporting Features
The project is integrated with the **Allure Framework** to provide deep visibility into the UI automation process. Key features include:

*   **Visual Evidence:** Automated **browser screenshots** are captured and attached to the report for every failed test, enabling rapid debugging.
*   **Dynamic Test Documentation:** Uses `@allure.title` and `@allure.description` to transform technical code into readable test scenarios.
*   **Hierarchical Grouping:** Tests are organized by **Suites** (e.g., Authentication) and **Features** (e.g., Login Logic) for structured analysis.
*   **Step-by-Step Execution:** Detailed `@allure.step` logging tracks every user action, such as clicking buttons or filling forms, in real-time.

## 🧪 Test Coverage
### 1. FAQ & Information
* **Accordion Logic:** Verification that clicking each question in the "Questions about Important Things" section expands the correct corresponding answer.
* **Data Consistency:** Parameterized tests to ensure all 8 FAQ items display accurate information.

### 2. Order Journey (E2E)
* **Entry Points:** Verification of the positive order flow via two different entry points:
    *   The "Order" button in the page **Header**.
    *   The "Order" button located in the **Footer** section.
* **Multi-dataset Testing:** Full checkout flow validation using multiple sets of user data (First name, Last name, Address, Metro station, Phone).
* **Order Confirmation:** Verification of the "Order Successful" modal appearance after form submission.

### 3. Navigation & Branding
* **Internal Navigation:** Redirection to the Scooter service main page when clicking the **"Scooter" logo**.
* **External Redirection:** Redirection to the **Dzen** (Yandex) main page in a new browser tab when clicking the **"Yandex" logo**.

### 4. Technical Implementation
* **Base Page Pattern:** Usage of centralized methods for clicking, waiting, and scrolling to elements.
* **Smart Waits:** Implementation of `WebDriverWait` and `expected_conditions` to handle dynamic page loading and animations.
* **Parameterized Tests:** Efficient execution of repetitive scenarios using `@pytest.mark.parametrize`.

## ⚙️ Execution Guide

### 1. Environment Setup
Clone the repository and set up a local virtual environment to ensure dependency isolation:

1. **Clone repository**
> ```bash 
> git clone https://github.com/AlyaSmirnova/Sprint_6
> cd Sprint_6
📦 Repository: [Sprint_5](https://github.com/AlyaSmirnova/Sprint_6)

2. **Create a virtual environment**
> ```bash 
> python -m venv venv

3. **Activate the virtual environment**
> ```bash 
> source venv/bin/activate

4. **Install required dependencies**
> `$ pip install -r requirements.txt`

### 2. Running Tests
Execute the full test suite and collect raw data for the Allure report:
> ```bash 
> pytest -v --alluredir=allure-results

### 3. Generatig Allure Report
Transform the raw data into a visual, interactive HTML report:
> ```bash 
> allure serve allure-results

## ⚙️ CI/CD Workflow
The project is fully automated using **GitHub Actions**. Upon every `push` to the **main** branch or any `Pull Request` creation:

1.  **Environment Provisioning:** A clean **Ubuntu** runner is initialized in the cloud environment.
2.  **Browser Setup:** The latest **Firefox** (or Chrome) and its corresponding **WebDriver** are automatically installed and configured.
3.  **Dependency Management:** The Python environment is set up, and all required libraries (`Selenium`, `Pytest`, `Allure`) are installed from `requirements.txt`.
4.  **Headless Execution:** The full UI test suite is executed in **headless mode** to ensure stability and performance in the server environment without a GUI.
5.  **Artifact Generation:** Test results, including logs and metadata, are collected and prepared for the **Allure report**.
6.  **Auto-Deployment:** (Optional) The final Allure report is automatically published to **GitHub Pages** for easy viewing.