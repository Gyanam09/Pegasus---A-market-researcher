import re
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER


def sanitize_text(text: str) -> str:
    """
    Make text safe for ReportLab Paragraph:
    - Remove HTML tags
    - Remove Markdown table pipes
    - Replace <br> with newlines
    - Remove unsupported markup
    """

    # Replace <br> and <br/> with newline
    text = re.sub(r"<br\\s*/?>", "\n", text, flags=re.IGNORECASE)

    # Remove remaining HTML tags
    text = re.sub(r"<[^>]+>", "", text)

    # Remove markdown bold/italics
    text = text.replace("**", "").replace("__", "").replace("*", "")

    # Remove markdown table pipes
    text = re.sub(r"\\|+", " ", text)

    return text.strip()


def export_markdown_to_pdf(filename, title, markdown_text):
    """
    Converts Markdown-based report into a safe, professional PDF.
    """

    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50,
    )

    styles = getSampleStyleSheet()

    styles.add(
        ParagraphStyle(
            name="TitleStyle",
            fontSize=20,
            alignment=TA_CENTER,
            spaceAfter=30,
        )
    )

    styles.add(
        ParagraphStyle(
            name="HeaderStyle",
            fontSize=14,
            spaceBefore=20,
            spaceAfter=10,
            leading=18,
            fontName="Helvetica-Bold",
        )
    )

    styles.add(
        ParagraphStyle(
            name="BodyStyle",
            fontSize=10.5,
            leading=15,
            spaceAfter=10,
        )
    )

    story = []

    # ---------- Title ----------
    story.append(Paragraph(sanitize_text(title), styles["TitleStyle"]))
    story.append(Spacer(1, 0.3 * inch))

    # ---------- Content ----------
    for raw_line in markdown_text.splitlines():
        line = sanitize_text(raw_line)

        if not line:
            story.append(Spacer(1, 0.15 * inch))
            continue

        # Section headers
        if raw_line.startswith("## "):
            story.append(Spacer(1, 0.2 * inch))
            story.append(
                Paragraph(
                    sanitize_text(raw_line.replace("## ", "")),
                    styles["HeaderStyle"],
                )
            )
            continue

        # Bullet points
        if raw_line.startswith("- "):
            bullet = "• " + sanitize_text(raw_line[2:])
            story.append(Paragraph(bullet, styles["BodyStyle"]))
            continue

        # Normal paragraph
        story.append(Paragraph(line, styles["BodyStyle"]))

    doc.build(story)
