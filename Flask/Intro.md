# 🌐 Web Server & Web Application Interaction

## 📌 Overview
A **web server** is responsible for handling client requests over the internet and delivering appropriate responses. When a user accesses a website through a browser, the request is sent using HTTP/HTTPS protocols. The web server processes this request and returns resources such as web pages, images, or data.

The web server acts as an intermediary between the client and backend systems, ensuring smooth communication.

---

## ⚙️ Web Server Responsibilities
- Receives client requests (e.g., `/home`, `/api`, `/function1`)
- Processes HTTP/HTTPS requests
- Forwards requests to the application layer
- Sends responses back to the client

> Note: A web server **cannot handle business logic on its own**

---

## 🧠 Role of Web Application (Flask)
A **web application** (e.g., built using Flask) handles the core logic of the system.

### Example Routes:
- `/home`
- `/api`
- `/function1`

The application:
- Interprets incoming requests
- Executes business logic
- Generates responses

---

## 🔌 WSGI (Web Server Gateway Interface)

WSGI acts as a **bridge** between the web server and the Python web application.

### Key Role:
- Enables communication between:
  - Web servers (Apache, AWS EC2, Azure)
  - Python applications (Flask)

### Flow:
Web Server → WSGI → Flask App → WSGI → Web Server


WSGI ensures that requests and responses are properly transferred between the server and application.

---

## ☁️ Deployment Environment

### 1. Cloud Platforms
- **AWS EC2**  
  Virtual machines for hosting and configuring servers manually.

- **Azure App Service**  
  Managed platform for deploying applications without handling infrastructure.

---

### 2. Web Server Software
- **Apache**  
  Open-source, widely used, flexible web server.

- **IIS (Internet Information Services)**  
  Microsoft’s web server for Windows environments.

---

## 🔄 Request Flow Summary

1. Client sends a request (e.g., `/home`)
2. Web server receives the request
3. Request is forwarded via WSGI
4. Flask application processes the request
5. Response is returned via WSGI
6. Web server sends the response back to the client

---

## 🧩 Architecture Summary

- **Web Server** → Handles requests & networking  
- **WSGI** → Communication bridge  
- **Flask App** → Business logic & routing  

---

## 📊 Diagram

![Architecture Diagram](https://github.com/user-attachments/assets/dc5e7bfc-e13b-4abb-9fb9-3fe78968fbad)

---
---
# 🎨 Jinja2 Template Engine
<img width="1080" height="558" alt="image" src="https://github.com/user-attachments/assets/63af99a6-79f6-46b6-bf60-498bb25dfeab" />

## 📌 Overview
**Jinja2** is a modern and powerful **web template engine** used in Python web frameworks like Flask.

It allows developers to generate dynamic HTML pages by combining:
- Static templates (HTML structure)
- Dynamic data (from databases, APIs, or models)

---

## ⚙️ How Jinja2 Works

Jinja2 takes data from various sources and injects it into HTML templates to produce a final web page.

### 🧩 Components:
- **Web Template** → Defines the structure/layout of the page
- **Data Source** → Provides dynamic content
- **Rendered Web Page** → Final output sent to the user

---

## 🔗 Data Sources

Jinja2 can receive data from multiple sources such as:
- **SQL Databases**
- **CSV Files / Sheets**
- **Machine Learning Models**
- **MongoDB (NoSQL Database)**

---

## 🧠 Role of Templates

Templates define the layout of a webpage and include placeholders for dynamic content.

### Example:

```html
<h1>{{ title }}</h1>
<p>{{ description }}</p>


Jinja2 replaces {{ }} placeholders with actual values at runtime.

