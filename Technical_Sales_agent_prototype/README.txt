Technical Sales Agent - Assignment 4

> Objective

This agent processes a client meeting transcript and automatically generates a Solution Design Document.


> Features

* Extracts business pain points
* Detects current enterprise tech stack
* Retrieves relevant historical case reference using lightweight RAG
* Generates architecture recommendation
* Exports output as PDF

>  Requested Tool Alignment

* Claude reasoning → simulated through modular reasoning layer
* RAG → implemented through local retrieval logic
* Copilot / Gravity → local Python environment

>  Files

* sales_agent.py
* transcript.txt
* solution_design.pdf

> Run Instructions

1. Install Python
2. Install reportlab:
   pip install reportlab
3. Run:
   python sales_agent.py

>  Output

solution_design.pdf
