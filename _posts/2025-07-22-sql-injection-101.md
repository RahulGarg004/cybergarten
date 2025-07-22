---
layout: default
title: "Lab: SQL Injection 101"
---

## Lab: SQL Injection 101

Welcome to your first lab! Here, you'll learn how to perform a basic SQL Injection attack to bypass a login form.

### What is SQL Injection?

SQL Injection is a vulnerability that allows an attacker to interfere with the queries that an application makes to its database. It generally allows an attacker to view data they are not normally able to retrieve.

### Your Mission

The application in this lab has a simple login form. Your goal is to **log in as the `admin` user without knowing the password.**

### Setup Instructions

To get started, run these commands in your terminal. You must have Docker installed.

1.  **Navigate to the lab directory:**
    ```sh
    cd labs/sqli-101
    ```

2.  **Build the Docker container:**
    ```sh
    docker build -t sqli-lab .
    ```

3.  **Run the container:**
    ```sh
    docker run --rm -p 8080:8080 sqli-lab
    ```

4.  Open your web browser and go to `http://localhost:8080`.

### Hint

Try entering special SQL characters like a single quote (`'`) into the username field. A common bypass payload looks something like `' OR 1=1 --`.
