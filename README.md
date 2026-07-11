# AI Deep Research Assistant

## Overview

AI Deep Research Assistant is a multi-agent research system built using the OpenAI Agents SDK.

The application automates the complete research lifecycle:

1. Research planning
2. Web information gathering
3. Report generation
4. Email delivery

The system uses specialized AI agents coordinated through a central Research Manager to produce detailed research reports from a single user query.

---

## Features

* Multi-agent architecture
* Automated research planning
* Parallel web search execution
* Structured AI outputs using Pydantic
* Long-form report generation
* OpenAI tracing support
* Email delivery via SendGrid
* Interactive Gradio interface

---

## Architecture

The project consists of four specialized agents:

### Planner Agent

Generates a structured research plan from the user's query.

Responsibilities:

* Analyze research objective
* Generate targeted search queries
* Create a search strategy
* Prepare downstream research workflow

### Search Agent

Executes web searches and summarizes findings.

Responsibilities:

* Gather relevant information
* Summarize search results
* Provide research context
* Support concurrent search execution

### Writer Agent

Produces a comprehensive research report.

Responsibilities:

* Synthesize research findings
* Generate structured markdown reports
* Create executive summaries
* Suggest follow-up research topics

### Email Agent

Delivers generated reports through email.

Responsibilities:

* Convert reports into HTML format
* Generate email-friendly output
* Send reports using SendGrid

---

## Workflow

User Query

↓

Planner Agent

↓

Search Agent

↓

Writer Agent

↓

Email Agent

↓

Final Research Report

---

## Screenshots

### Application Interface

![Application UI](docs/screenshots/ui.png)

### Generated Research Report

![Research Report](docs/screenshots/report.png)

### OpenAI Trace

![OpenAI Trace](docs/screenshots/trace.png)

---

## Project Structure

```text
app/
│
├── main.py

core/
│
├── research_manager.py

research_agents/
│
├── planner_agent.py
├── search_agent.py
├── writer_agent.py
├── email_agent.py

docs/
│
├── screenshots
├── architecture.md
├── setup.md

examples/
│
└── sample_report_1.md

README.md
pyproject.toml
```

---
## Documentation

- [Architecture](docs/architecture.md)
- [Setup Guide](docs/setup.md)


## Technology Stack

The project leverages the OpenAI Agents SDK to orchestrate specialized AI agents that collaborate to automate end-to-end research workflows.

* Python
* OpenAI Agents SDK
* Gradio
* Pydantic
* AsyncIO
* SendGrid

---

## Future Improvements

* Citation generation
* PDF export support
* Research history tracking
* Multi-model support
* Knowledge base integration
* Advanced report templates

---

## Status

This project demonstrates the implementation of a multi-agent research assistant using the OpenAI Agents SDK, including automated research planning, web search, report generation, and email delivery.

## Author

**Pratik Mirajkar**

AI Engineer | Generative AI Developer | Multi-Agent Systems Enthusiast
