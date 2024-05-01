from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.contrib.auth.decorators import login_required
from equipment.models import Booking, Item

# Django report system using reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
import io

@login_required
def report(request):
    if request.user.is_superuser:
        return render(request, 'report/report.html')
    else:
        # http response saying error 403 access denied
        return HttpResponse('403 Error: Access Denied')

def download(request):
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
    current_bookings = Booking.objects.filter(isCurrent__isCurrent=True)
    overdue_bookings = Booking.objects.filter(isOverdue__isOverdue=True)

    # Prepare the report content
    report_content = [
        "Current Inventory Status:",
    ]
    for item in Item.objects.all():
        if item not in [booking.item for booking in current_bookings]:
            report_content.append(f"- {item.name} ({item.itemtype.type})")

    report_content.extend([
        "",
        "Overdue Items:",
    ])
    for booking in overdue_bookings:
        report_content.append(f"- {booking.item.name} ({booking.item.itemtype.type})")

    # Set the initial y position for drawing text
    y_position = 9.5 * inch

    # Draw the report content with line spacing
    for line in report_content:
        if y_position < 0.5 * inch:
            # Start a new page if the current page is full
            p.showPage()
            p.setFont("Helvetica", 12)
            p.drawString(1 * inch, 10.5 * inch, "Inventory Report (Continued)")
            p.line(1 * inch, 10 * inch, 8 * inch, 10 * inch)
            y_position = 9.5 * inch
        p.drawString(1 * inch, y_position, line)
        y_position -= 0.25 * inch

    # Close the PDF object cleanly
    p.save()

    # Get the value of the BytesIO buffer and write it to the response
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='inventory_report.pdf')
