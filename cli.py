import argparse
from datetime import datetime

from agent import run_agent_sync
from pdf_exporter import export_markdown_to_pdf


def main():
    parser = argparse.ArgumentParser(
        description="Pegasus CLI — Headless Market Research Engine"
    )
    parser.add_argument(
        "topic",
        type=str,
        help="Research topic (e.g. 'AI semiconductor market overview')",
    )
    parser.add_argument(
        "--pdf",
        action="store_true",
        help="Export report as PDF instead of Markdown",
    )
    parser.add_argument(
        "--out",
        type=str,
        default="Pegasus_Report",
        help="Output filename without extension",
    )

    args = parser.parse_args()

    print(f"[PEGASUS] Running research on: {args.topic}")
    report_md = run_agent_sync(args.topic)

    title = f"Pegasus Intelligence Report: {args.topic}"

    if args.pdf:
        filename = args.out + ".pdf"
        export_markdown_to_pdf(
            filename=filename,
            title=title,
            markdown_text=report_md,
        )
        print(f"[PEGASUS] PDF report saved to {filename}")
    else:
        filename = args.out + ".md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n")
            f.write(report_md)
        print(f"[PEGASUS] Markdown report saved to {filename}")


if __name__ == "__main__":
    main()
