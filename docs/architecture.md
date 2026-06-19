# Architecture

## Overview

AI Deep Research Assistant is a multi-agent system built using the OpenAI Agents SDK.

The system automates the research workflow from planning and information gathering to report generation and email delivery.

## Components

### Planner Agent

Generates structured web search plans from the user's query.

### Search Agent

Executes web searches and summarizes findings.

### Writer Agent

Creates a detailed markdown report from research results.

### Email Agent

Converts the report into email format and sends it using SendGrid.

### Research Manager

Coordinates the complete workflow between all agents.

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
Final Report