from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import io, datetime

def generate_pdf(case_desc, category, analysis, results, lawyers):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, topMargin=0.8*inch)
    styles = getSampleStyleSheet()
    story = []

    # Title - Classic Black
    title_style = ParagraphStyle("title", fontSize=24, fontName="Helvetica-Bold",
                                  textColor=colors.black, spaceAfter=6)
    story.append(Paragraph("LexMatch AI — Legal Case Report", title_style))
    story.append(Paragraph(f"Generated: {datetime.datetime.now().strftime('%d %B %Y, %I:%M %p')}",
                            ParagraphStyle("sub", fontSize=10, textColor=colors.HexColor("#4a5568"))))
    story.append(Spacer(1, 20))

    # Case Description
    story.append(Paragraph("Your Case Profile", styles["Heading2"]))
    story.append(Paragraph(f"<b>Category:</b> {category.title()}", styles["Normal"]))
    story.append(Paragraph(case_desc, styles["Normal"]))
    story.append(Spacer(1, 16))

    # AI Assessment
    story.append(Paragraph("AI Legal Assessment", styles["Heading2"]))
    assessment_data = [
        ["Case Strength", analysis.get("caseStrength", "—")],
        ["Relevant Law", analysis.get("relevantLaw", "—")],
        ["Likely Outcome", analysis.get("likelyOutcome", "—")],
        ["Urgent Action", analysis.get("urgentAction", "—")],
        ["Timeline", analysis.get("timeline", "—")],
    ]
    t = Table(assessment_data, colWidths=[2*inch, 4*inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,-1), colors.HexColor("#f8fafc")), # Very light grey
        ("FONTNAME", (0,0), (0,-1), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 10),
        ("TEXTCOLOR", (0,0), (-1,-1), colors.black),
        ("GRID", (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ("PADDING", (0,0), (-1,-1), 8),
    ]))
    story.append(t)
    story.append(Spacer(1, 8))
    story.append(Paragraph(analysis.get("summary", ""), styles["Normal"]))
    story.append(Spacer(1, 16))

    # Matched Cases
    story.append(Paragraph("Top Matched Legal Precedents", styles["Heading2"]))
    case_data = [["#", "Case Title", "Court", "Match %", "Outcome"]]
    for i, c in enumerate(results[:5]):
        case_data.append([
            str(i+1), c["title"][:40], c["court"][:20],
            f"{c['matchScore']}%", c["outcome"]
        ])
    ct = Table(case_data, colWidths=[0.4*inch, 2.5*inch, 1.5*inch, 0.8*inch, 1.2*inch])
    ct.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#1a202c")), # Charcoal header
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 9),
        ("GRID", (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ("PADDING", (0,0), (-1,-1), 6),
    ]))
    story.append(ct)
    story.append(Spacer(1, 16))

    # Recommended Lawyers
    story.append(Paragraph("Recommended Verified Advocates", styles["Heading2"]))
    
    if lawyers and len(lawyers) > 0:
        top_lawyer = lawyers[0]
        lawyer_data = [
            ["Name", top_lawyer.get("name", "N/A")],
            ["Specialization", top_lawyer.get("specialization", "N/A")],
            ["Phone", top_lawyer.get("phone", "Search Online")],
            ["Address", top_lawyer.get("address", top_lawyer.get("city", "N/A"))],
        ]
        lt = Table(lawyer_data, colWidths=[1.5*inch, 4.5*inch])
        lt.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (0,-1), colors.HexColor("#f8fafc")),
            ("FONTNAME", (0,0), (0,-1), "Helvetica-Bold"),
            ("FONTSIZE", (0,0), (-1,-1), 10),
            ("TEXTCOLOR", (0,0), (-1,-1), colors.black),
            ("GRID", (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
            ("PADDING", (0,0), (-1,-1), 8),
        ]))
        story.append(lt)

    doc.build(story)
    buffer.seek(0)
    return buffer