from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.contrib.auth.decorators import login_required
from login.models import booking, iscurrent, isoverdue, item, itemlocation, itemstatus, itemtype, reservedstatus


# Django report system using reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
import io

@login_required
def report_view(request):
    # Create a file-like buffer to receive PDF data
    buffer = io.BytesIO()

    # Create a canvas for the PDF report
    p = canvas.Canvas(buffer, pagesize=letter)

    # Set the title and draw it
    p.setFont("Helvetica-Bold", 18)
    p.drawString(1 * inch, 10.5 * inch, "Inventory Report")

    # Draw a line separator
    p.line(1 * inch, 10 * inch, 8 * inch, 10 * inch)

    # Set the font for the report content
    p.setFont("Helvetica", 12)

   # Fetch data from the databases
    bookings = booking.objects.all()
    current_items = iscurrent.objects.filter(status=True)
    overdue_items = isoverdue.objects.filter(status=True)
    all_items = item.objects.all()
    item_locations = itemlocation.objects.all()
    item_statuses = itemstatus.objects.all()
    item_types = itemtype.objects.all()
    reserved_statuses = reservedstatus.objects.all()

    # Prepare the report content
    report_content = [
        "Current Inventory Status:",
    ]
    for item in current_items:
        report_content.append(f"- {item.item_name} ({item.item_type.type_name})")

    report_content.extend([
        "",
        "Overdue Items:",
    ])
    for item in overdue_items:
        report_content.append(f"- {item.item_name} ({item.item_type.type_name})")


    # Draw the report content with line spacing
    text_object = p.beginText(1 * inch, 10 * inch)
    line_height = 0.25 * inch
    for line in report_content:
        text_object.textLine(line)
        text_object.moveCursor(0, -line_height)
    p.drawText(text_object)

    # Close the PDF object cleanly
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='inventory_report.pdf')