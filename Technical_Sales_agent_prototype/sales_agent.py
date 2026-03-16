from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

# -------------------------------
# Claude Reasoning Layer (Simulated)
# -------------------------------
def claude_reasoning_layer(transcript):
    pain_points = []

    if "Excel" in transcript:
        pain_points.append("Manual approval dependency")

    if "slow" in transcript.lower() or "long" in transcript.lower():
        pain_points.append("Slow reporting process")

    if "disconnected" in transcript.lower():
        pain_points.append("Disconnected enterprise systems")

    if "automation" in transcript.lower():
        pain_points.append("Need for workflow automation")

    return pain_points


# -------------------------------
# Tech Stack Detection
# -------------------------------
def detect_tech_stack(transcript):
    tech_stack = []

    if "SAP" in transcript:
        tech_stack.append("SAP")

    if "Salesforce" in transcript:
        tech_stack.append("Salesforce")

    if "Excel" in transcript:
        tech_stack.append("Excel")

    return tech_stack


# -------------------------------
# RAG Retrieval Layer
# -------------------------------
def rag_retrieve_case(transcript):
    if "SAP" in transcript and "Salesforce" in transcript:
        return "Integrated SAP and Salesforce using API gateway and workflow automation"

    elif "Excel" in transcript:
        return "Converted manual Excel approvals into digital workflow"

    else:
        return "Built centralized enterprise reporting dashboard"


# -------------------------------
# Architecture Generator
# -------------------------------
def generate_architecture(tech_stack):
    architecture = []

    if "SAP" in tech_stack and "Salesforce" in tech_stack:
        architecture.append("API integration layer between SAP and Salesforce")

    if "Excel" in tech_stack:
        architecture.append("Workflow automation replacing Excel approvals")

    architecture.append("Centralized reporting dashboard")

    return architecture


# -------------------------------
# PDF Generator
# -------------------------------
def generate_pdf(pain_points, tech_stack, architecture, reference_case):
    doc = SimpleDocTemplate("solution_design.pdf", pagesize=A4)
    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph("Solution Design Document", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 20))

    data = [
    ["Section", "Output"],
    ["Pain Points", Paragraph(", ".join(pain_points), styles['BodyText'])],
    ["Current Tech Stack", Paragraph(", ".join(tech_stack), styles['BodyText'])],
    ["Suggested Architecture", Paragraph(", ".join(architecture), styles['BodyText'])],
    ["Reference Case (RAG)", Paragraph(reference_case, styles['BodyText'])]
]



    table = Table(data,colWidths=[120, 350])
    table.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 1, colors.black)
    ]))



    elements.append(table)

    doc.build(elements)


# -------------------------------
# Main Agent Workflow
# -------------------------------
with open("transcript.txt", "r") as file:
    transcript = file.read()

pain_points = claude_reasoning_layer(transcript)
tech_stack = detect_tech_stack(transcript)
reference_case = rag_retrieve_case(transcript)
architecture = generate_architecture(tech_stack)

generate_pdf(pain_points, tech_stack, architecture, reference_case)

print("Solution Design Document Generated Successfully")