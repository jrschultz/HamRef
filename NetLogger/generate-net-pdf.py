import argparse
import json
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_pdf(json_filepath, output_filename="net_log_report.pdf"):
    # Load JSON data from the specified input file
    try:
        with open(json_filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading JSON file '{json_filepath}': {e}")
        return

    # Setup document geometry (Letter size, 0.5-inch margins -> printable width = 540pt)
    doc = SimpleDocTemplate(
        output_filename, 
        pagesize=letter,
        rightMargin=36, 
        leftMargin=36,
        topMargin=36, 
        bottomMargin=36
    )
    story = []
    styles = getSampleStyleSheet()
    
    # Custom Typography Styles
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.HexColor('#050f03'),
        spaceAfter=4
    )
    subtitle_style = ParagraphStyle(
        'SubtitleStyle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#4a5568'),
        spaceAfter=12
    )
    heading_style = ParagraphStyle(
        'HeadingStyle',
        parent=styles['Heading2'],
        fontSize=13,
        textColor=colors.HexColor('#226c13'),
        spaceBefore=14,
        spaceAfter=6
    )

    # Header Section
    app_name = data.get('app', 'Net Logger')
    story.append(Paragraph(f"{app_name} - Archive Report", title_style))
    
    # Parse timestamps safely
    net_info = data.get('net', {})
    start_time_raw = net_info.get('startTime', '')
    
    # Extract Net Date and Start Time
    if 'T' in start_time_raw:
        net_date = start_time_raw.split('T')[0]
        start_time_short = start_time_raw.split('T')[1][:8]
    else:
        net_date = start_time_raw[:10] if len(start_time_raw) >= 10 else "N/A"
        start_time_short = start_time_raw
    
    # Format End Time with UTC appended if present
    end_time_raw = net_info.get('endTime')
    if end_time_raw and 'T' in end_time_raw:
        end_time_short = end_time_raw.split('T')[1][:8] + " UTC"
    else:
        end_time_short = "Ongoing / Active"

    export_time_raw = data.get('exportedAt', '')
    export_time_formatted = export_time_raw.replace('T', ' ')[:19] if export_time_raw else "N/A"

    # Metadata row: Net Date, Start, End, and Exported At (Net Status omitted)
    meta_text = (
        f"<b>Net Date:</b> {net_date} | "
        f"<b>Start:</b> {start_time_short} UTC | "
        f"<b>End:</b> {end_time_short} | "
        f"<b>Exported At:</b> {export_time_formatted} UTC"
    )
    story.append(Paragraph(meta_text, subtitle_style))
    story.append(Spacer(1, 5))

    # --- Section: Net Check-Ins Log ---
    story.append(Paragraph("Net Check-Ins Log", heading_style))
    checkin_headers = ["Time (UTC)", "Call Sign", "Name", "Location", "Role", "Comment"]
    checkin_rows = [checkin_headers]
    
    checkins = net_info.get('checkins', [])
    for item in checkins:
        time_raw = item.get('time', '')
        time_str = time_raw.split('T')[1][:8] if 'T' in time_raw else time_raw
        role = "Net Control" if item.get('isNCS', False) else "Check-in"
        checkin_rows.append([
            time_str,
            item.get('call', ''),
            item.get('name', ''),
            item.get('location', ''),
            role,
            item.get('comment', '')
        ])

    # Table width total: 65 + 65 + 65 + 95 + 75 + 175 = 540 pt
    t_checkins = Table(checkin_rows, colWidths=[65, 65, 65, 95, 75, 175])
    t_checkins.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#226c13')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        ('TOPPADDING', (0, 0), (-1, 0), 6),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f7fafc')]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e0')),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 5),
        ('TOPPADDING', (0, 1), (-1, -1), 5),
    ]))
    story.append(t_checkins)

    # Build PDF
    doc.build(story)
    print(f"PDF successfully generated: {output_filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert MJARC Net Logger JSON export into a formatted PDF archive.")
    parser.add_argument("json_file", help="Path to the input JSON log file")
    parser.add_argument("-o", "--output", default="net_log_report.pdf", help="Output PDF filename (default: net_log_report.pdf)")
    
    args = parser.parse_args()
    generate_pdf(args.json_file, args.output)
