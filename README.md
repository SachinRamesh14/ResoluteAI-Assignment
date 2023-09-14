## Title
ResoluteAI - facegenie assignment

## Description

This automation testing project demonstrates how to automate web testing using Selenium WebDriver with Python. It includes sample test scripts, configurations, and guidelines for running automated tests.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

1. Clone this repository:

   ```shell
   git clone https://github.com/SachinRamesh14/ResoluteAI-Assignment.git
   cd selenium-automation
   ```

2. Install the required Python packages:

   ```shell
   pip install -r requirements.txt
   ```

3. Download and install the appropriate WebDriver for your browser (e.g., Chrome WebDriver or Firefox WebDriver). Add the WebDriver executable to your system's PATH.

## Usage

1. Modify the `config.py` file to specify your test environment and configurations, such as the URL, browser choice, and test data.

2. Write your test scripts in the `tests/` directory using Python and Selenium WebDriver. You can use the sample test scripts as a reference.

3. To run a test, use the following command:

   ```shell
   pytest -v -s testCases
   ```

4. View test results and logs in the `logs/` directory.
