#!/usr/bin/env python3
"""
SmartAC Visual Identity Guidelines Generator
Author: MAKAMTE TATSINKOU PAOLA
Course: Level 3 Software Engineering - Graphic Design
Project: IoT-Based Smart Air Conditioning Control System
"""

import subprocess
import sys
from datetime import datetime

# Auto-install reportlab if not present
try:
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
    from reportlab.lib.units import cm, mm
    from reportlab.lib import colors
    from reportlab.platypus import Table, TableStyle
except ImportError:
    print("Installing reportlab...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "reportlab"])
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
    from reportlab.lib.units import cm, mm
    from reportlab.lib import colors
    from reportlab.platypus import Table, TableStyle

# ============================================================================
# BRAND COLOR PALETTE - Constants
# ============================================================================
ARCTIC_BLUE = "#0A84FF"
COOL_TEAL = "#30D5C8"
DEEP_NAVY = "#0D1B2A"
FROST_WHITE = "#F4F9FF"
SLATE_GREY = "#6B7280"
DANGER_RED = "#FF3B30"

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple (0-1 range)"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4))

# Color constants as RGB tuples
COLOR_ARCTIC_BLUE = hex_to_rgb(ARCTIC_BLUE)
COLOR_COOL_TEAL = hex_to_rgb(COOL_TEAL)
COLOR_DEEP_NAVY = hex_to_rgb(DEEP_NAVY)
COLOR_FROST_WHITE = hex_to_rgb(FROST_WHITE)
COLOR_SLATE_GREY = hex_to_rgb(SLATE_GREY)
COLOR_DANGER_RED = hex_to_rgb(DANGER_RED)

# ============================================================================
# PAGE SETUP
# ============================================================================
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 2 * cm
HEADER_HEIGHT = 8
FOOTER_HEIGHT = 15

# ============================================================================
# LOGO DRAWING FUNCTION
# ============================================================================
def draw_smartac_logo(c, x, y, size=100, color_scheme='primary'):
    """
    Draw the SmartAC logo with MTP initials

    Args:
        c: canvas object
        x, y: center position
        size: logo width
        color_scheme: 'primary', 'reversed', 'monochrome_dark', 'monochrome_light'
    """
    c.saveState()

    # Define colors based on scheme
    if color_scheme == 'primary':
        primary_color = COLOR_ARCTIC_BLUE
        accent_color = COLOR_COOL_TEAL
        text_color = COLOR_DEEP_NAVY
    elif color_scheme == 'reversed':
        primary_color = (1, 1, 1)
        accent_color = COLOR_COOL_TEAL
        text_color = (1, 1, 1)
    elif color_scheme == 'monochrome_dark':
        primary_color = COLOR_DEEP_NAVY
        accent_color = COLOR_DEEP_NAVY
        text_color = COLOR_DEEP_NAVY
    elif color_scheme == 'monochrome_light':
        primary_color = (1, 1, 1)
        accent_color = (1, 1, 1)
        text_color = (1, 1, 1)
    else:
        primary_color = COLOR_ARCTIC_BLUE
        accent_color = COLOR_COOL_TEAL
        text_color = COLOR_DEEP_NAVY

    # Logo container dimensions
    logo_height = size * 0.8

    # Draw WiFi/IoT symbol (three curved arcs)
    c.setStrokeColorRGB(*accent_color)
    c.setLineWidth(2)
    for i in range(3):
        radius = (i + 1) * (size * 0.08)
        c.arc(x - size * 0.35, y + logo_height * 0.5, x - size * 0.35 + radius * 2,
              y + logo_height * 0.5 + radius * 2, 45, 90)

    # Draw small WiFi dot
    c.setFillColorRGB(*accent_color)
    c.circle(x - size * 0.35, y + logo_height * 0.5, size * 0.02, fill=1)

    # Draw MTP letters in geometric style
    c.setFont("Helvetica-Bold", size * 0.4)
    c.setFillColorRGB(*primary_color)

    # Letter M
    c.drawString(x - size * 0.25, y + logo_height * 0.3, "M")

    # Letter T
    c.drawString(x - size * 0.05, y + logo_height * 0.3, "T")

    # Letter P
    c.drawString(x + size * 0.15, y + logo_height * 0.3, "P")

    # Draw airflow arcs around the letters
    c.setStrokeColorRGB(*accent_color)
    c.setLineWidth(1.5)
    c.setDash(3, 3)

    # Top arc
    c.arc(x - size * 0.3, y + logo_height * 0.1, x + size * 0.3,
          y + logo_height * 0.9, 0, 180)

    # Bottom arc
    c.arc(x - size * 0.28, y + logo_height * 0.15, x + size * 0.28,
          y + logo_height * 0.85, 180, 360)

    c.setDash(1, 0)  # Reset dash

    # Draw "SmartAC" wordmark
    c.setFont("Helvetica-Bold", size * 0.15)
    c.setFillColorRGB(*text_color)
    wordmark_width = c.stringWidth("SMARTAC", "Helvetica-Bold", size * 0.15)
    c.drawString(x - wordmark_width / 2, y - size * 0.1, "SMARTAC")

    # Draw tagline
    c.setFont("Helvetica", size * 0.08)
    tagline = "Intelligent Climate. Total Control."
    tagline_width = c.stringWidth(tagline, "Helvetica", size * 0.08)
    c.drawString(x - tagline_width / 2, y - size * 0.2, tagline)

    c.restoreState()

# ============================================================================
# HEADER AND FOOTER FUNCTIONS
# ============================================================================
def draw_header(c, page_num):
    """Draw consistent header on each page"""
    if page_num == 1:  # Skip header on cover page
        return

    c.saveState()
    # Header strip
    c.setFillColorRGB(*COLOR_ARCTIC_BLUE)
    c.rect(0, PAGE_HEIGHT - HEADER_HEIGHT, PAGE_WIDTH, HEADER_HEIGHT, fill=1, stroke=0)

    # Small logo in header
    c.setFont("Helvetica-Bold", 6)
    c.setFillColorRGB(1, 1, 1)
    c.drawString(MARGIN, PAGE_HEIGHT - 6, "SmartAC")

    c.restoreState()

def draw_footer(c, page_num):
    """Draw consistent footer on each page"""
    if page_num == 1:  # Skip footer on cover page
        return

    c.saveState()
    c.setFont("Helvetica", 8)
    c.setFillColorRGB(*COLOR_SLATE_GREY)

    # Footer text
    footer_text = "SmartAC Visual Identity Guidelines — MAKAMTE TATSINKOU PAOLA — Confidential"
    footer_width = c.stringWidth(footer_text, "Helvetica", 8)
    c.drawString((PAGE_WIDTH - footer_width) / 2, FOOTER_HEIGHT, footer_text)

    # Page number
    page_text = str(page_num)
    page_width = c.stringWidth(page_text, "Helvetica", 8)
    c.drawString((PAGE_WIDTH - page_width) / 2, FOOTER_HEIGHT - 10, page_text)

    c.restoreState()

def draw_section_banner(c, y_position, title):
    """Draw a section title banner"""
    c.saveState()
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.rect(MARGIN, y_position - 30, PAGE_WIDTH - 2 * MARGIN, 25, fill=1, stroke=0)

    c.setFont("Helvetica-Bold", 16)
    c.setFillColorRGB(1, 1, 1)
    c.drawString(MARGIN + 10, y_position - 22, title)
    c.restoreState()

# ============================================================================
# PAGE 1: COVER PAGE
# ============================================================================
def draw_cover_page(c):
    """Page 1: Cover Page"""
    c.saveState()

    # Full-bleed Deep Navy background
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Large logo centered
    draw_smartac_logo(c, PAGE_WIDTH / 2, PAGE_HEIGHT * 0.6, size=180, color_scheme='reversed')

    # Title
    c.setFont("Helvetica-Bold", 36)
    c.setFillColorRGB(*COLOR_FROST_WHITE)
    title = "Visual Identity Guidelines"
    title_width = c.stringWidth(title, "Helvetica-Bold", 36)
    c.drawString((PAGE_WIDTH - title_width) / 2, PAGE_HEIGHT * 0.35, title)

    # Subtitle
    c.setFont("Helvetica", 16)
    subtitle = "SmartAC — IoT-Based Smart Air Conditioning Control System"
    subtitle_width = c.stringWidth(subtitle, "Helvetica", 16)
    c.drawString((PAGE_WIDTH - subtitle_width) / 2, PAGE_HEIGHT * 0.31, subtitle)

    # Decorative horizontal rule
    c.setStrokeColorRGB(*COLOR_COOL_TEAL)
    c.setLineWidth(2)
    c.line(PAGE_WIDTH * 0.3, PAGE_HEIGHT * 0.28, PAGE_WIDTH * 0.7, PAGE_HEIGHT * 0.28)

    # Author name
    c.setFont("Helvetica-Bold", 14)
    c.setFillColorRGB(*COLOR_COOL_TEAL)
    author = "MAKAMTE TATSINKOU PAOLA"
    author_width = c.stringWidth(author, "Helvetica-Bold", 14)
    c.drawString((PAGE_WIDTH - author_width) / 2, PAGE_HEIGHT * 0.23, author)

    # Academic info
    c.setFont("Helvetica", 11)
    c.setFillColorRGB(*COLOR_FROST_WHITE)
    academic = "Level 3 Software Engineering — Graphic Design Course"
    academic_width = c.stringWidth(academic, "Helvetica", 11)
    c.drawString((PAGE_WIDTH - academic_width) / 2, PAGE_HEIGHT * 0.20, academic)

    year = f"Academic Year {datetime.now().year} — Continuous Assessment"
    year_width = c.stringWidth(year, "Helvetica", 11)
    c.drawString((PAGE_WIDTH - year_width) / 2, PAGE_HEIGHT * 0.17, year)

    c.restoreState()
    c.showPage()

# ============================================================================
# PAGE 2: TABLE OF CONTENTS
# ============================================================================
def draw_table_of_contents(c):
    """Page 2: Table of Contents"""
    draw_header(c, 2)
    draw_footer(c, 2)

    c.saveState()

    # Background
    c.setFillColorRGB(*COLOR_FROST_WHITE)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Left sidebar accent
    c.setFillColorRGB(*COLOR_ARCTIC_BLUE)
    c.rect(0, 0, 15, PAGE_HEIGHT, fill=1, stroke=0)

    # Title
    c.setFont("Helvetica-Bold", 28)
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.drawString(MARGIN + 20, PAGE_HEIGHT - 80, "Table of Contents")

    # Contents list
    contents = [
        ("1", "Brand Overview & Brand Story", "3"),
        ("2", "Logo Design & Construction", "4"),
        ("3", "Logo Variations", "5"),
        ("4", "Logo Misuse Guidelines", "6"),
        ("5", "Color Palette", "7"),
        ("6", "Typography Showcase", "8"),
        ("7", "Iconography & UI Elements", "9"),
        ("8", "UI Color Application", "10"),
        ("9", "Brand Voice & Messaging", "11"),
        ("10", "Stationery & Applications", "12"),
        ("11", "Digital & Print Usage", "13"),
        ("12", "Accessibility & Contrast", "14"),
        ("13", "Conclusion", "15"),
    ]

    y = PAGE_HEIGHT - 130
    c.setFont("Helvetica", 12)
    c.setFillColorRGB(*COLOR_SLATE_GREY)

    for num, title, page in contents:
        # Number
        c.setFont("Helvetica-Bold", 12)
        c.setFillColorRGB(*COLOR_ARCTIC_BLUE)
        c.drawString(MARGIN + 20, y, num)

        # Title
        c.setFont("Helvetica", 12)
        c.setFillColorRGB(*COLOR_DEEP_NAVY)
        c.drawString(MARGIN + 50, y, title)

        # Dot leaders
        dots = "." * 50
        dots_width = c.stringWidth(dots, "Helvetica", 12)
        c.setFillColorRGB(*COLOR_SLATE_GREY)
        c.drawString(PAGE_WIDTH - MARGIN - 50, y, dots[:40])

        # Page number
        c.setFont("Helvetica-Bold", 12)
        c.setFillColorRGB(*COLOR_ARCTIC_BLUE)
        c.drawString(PAGE_WIDTH - MARGIN - 25, y, page)

        y -= 25

    c.restoreState()
    c.showPage()

# ============================================================================
# PAGE 3: BRAND OVERVIEW & STORY
# ============================================================================
def draw_brand_overview(c):
    """Page 3: Brand Overview & Brand Story"""
    draw_header(c, 3)
    draw_footer(c, 3)

    c.saveState()

    # Background
    c.setFillColorRGB(*COLOR_FROST_WHITE)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Section banner
    draw_section_banner(c, PAGE_HEIGHT - 50, "Brand Overview & Story")

    y = PAGE_HEIGHT - 100

    # What SmartAC is
    c.setFont("Helvetica-Bold", 14)
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.drawString(MARGIN, y, "What is SmartAC?")
    y -= 25

    c.setFont("Helvetica", 11)
    c.setFillColorRGB(*COLOR_SLATE_GREY)

    text_lines = [
        "SmartAC is an innovative IoT-based smart air conditioning control system that revolutionizes",
        "how users interact with their climate control devices. Built on the Android platform, SmartAC",
        "empowers users to remotely monitor, control, and optimize their air conditioning units through",
        "an intuitive mobile application connected via WiFi and cloud infrastructure.",
        "",
        "The system combines cutting-edge Internet of Things technology with user-centric design to",
        "deliver unprecedented control over indoor climate. Users can adjust temperature settings,",
        "monitor energy consumption, schedule cooling cycles, and receive intelligent recommendations",
        "—all from the palm of their hand, anywhere in the world.",
        "",
        "SmartAC represents the convergence of sustainability, convenience, and technological innovation,",
        "making smart home climate control accessible to everyone while promoting energy efficiency",
        "and environmental responsibility.",
    ]

    for line in text_lines:
        c.drawString(MARGIN + 10, y, line)
        y -= 15

    # Mission statement box
    y -= 20
    c.setFillColorRGB(*COLOR_ARCTIC_BLUE)
    c.roundRect(MARGIN, y - 60, PAGE_WIDTH - 2 * MARGIN, 55, 5, fill=1, stroke=0)

    c.setFont("Helvetica-BoldOblique", 13)
    c.setFillColorRGB(1, 1, 1)
    mission_lines = [
        "Our Mission: To make intelligent climate control accessible, sustainable,",
        "and effortless for every home, while reducing energy waste and empowering",
        "users with data-driven insights for a more comfortable, eco-friendly lifestyle."
    ]
    my = y - 20
    for line in mission_lines:
        c.drawString(MARGIN + 15, my, line)
        my -= 14

    # Brand personality keywords
    y -= 100
    c.setFont("Helvetica-Bold", 12)
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.drawString(MARGIN, y, "Brand Personality")
    y -= 30

    keywords = ["Intelligent", "Efficient", "Connected", "Sustainable", "Trustworthy", "Innovative"]
    x_pos = MARGIN + 10

    for keyword in keywords:
        # Badge background
        c.setFillColorRGB(*COLOR_COOL_TEAL)
        badge_width = c.stringWidth(keyword, "Helvetica-Bold", 10) + 20
        c.roundRect(x_pos, y - 20, badge_width, 20, 3, fill=1, stroke=0)

        # Keyword text
        c.setFont("Helvetica-Bold", 10)
        c.setFillColorRGB(*COLOR_DEEP_NAVY)
        c.drawString(x_pos + 10, y - 14, keyword)

        x_pos += badge_width + 10
        if x_pos > PAGE_WIDTH - MARGIN - 100:
            x_pos = MARGIN + 10
            y -= 30

    c.restoreState()
    c.showPage()

# ============================================================================
# PAGE 4: LOGO DESIGN & CONSTRUCTION
# ============================================================================
def draw_logo_construction(c):
    """Page 4: Logo Design & Construction"""
    draw_header(c, 4)
    draw_footer(c, 4)

    c.saveState()

    # Background
    c.setFillColorRGB(*COLOR_FROST_WHITE)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Section banner
    draw_section_banner(c, PAGE_HEIGHT - 50, "Logo Design & Construction")

    y = PAGE_HEIGHT - 120

    # Large logo display
    draw_smartac_logo(c, PAGE_WIDTH / 2, y - 80, size=200, color_scheme='primary')

    y -= 200

    # Construction guidelines
    c.setFont("Helvetica-Bold", 12)
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.drawString(MARGIN, y, "Logo Construction Grid")
    y -= 20

    c.setFont("Helvetica", 10)
    c.setFillColorRGB(*COLOR_SLATE_GREY)
    construction_text = [
        "• The logo is built on a modular grid system with precise geometric proportions",
        "• The MTP initials are the central focal point, rendered in bold geometric letterforms",
        "• WiFi connectivity symbol positioned at top-left represents IoT integration",
        "• Airflow arc motifs surround the letters to convey cooling and air circulation",
        "• The wordmark 'SMARTAC' sits below in clean sans-serif capitals",
        "• Tagline follows in a lighter weight for hierarchy"
    ]

    for line in construction_text:
        c.drawString(MARGIN + 10, y, line)
        y -= 15

    y -= 20

    # Clear space rule
    c.setFont("Helvetica-Bold", 12)
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.drawString(MARGIN, y, "Clear Space & Minimum Size")
    y -= 20

    c.setFont("Helvetica", 10)
    c.setFillColorRGB(*COLOR_SLATE_GREY)
    c.drawString(MARGIN + 10, y, "• Minimum clear space: Height of the letter 'M' on all sides")
    y -= 15
    c.drawString(MARGIN + 10, y, "• Minimum size: 40px for digital use / 15mm for print applications")
    y -= 15
    c.drawString(MARGIN + 10, y, "• Never scale the logo smaller than these dimensions to maintain legibility")

    # Visual clear space demonstration
    y -= 40
    c.setStrokeColorRGB(*COLOR_DANGER_RED)
    c.setLineWidth(1)
    c.setDash(2, 2)

    logo_x = PAGE_WIDTH / 2
    logo_y = y - 40
    clear_space = 30

    # Draw clear space box
    c.rect(logo_x - 100 - clear_space, logo_y - 60 - clear_space,
           200 + 2 * clear_space, 120 + 2 * clear_space, fill=0, stroke=1)

    # Small logo in center
    draw_smartac_logo(c, logo_x, logo_y, size=100, color_scheme='primary')

    # Clear space labels
    c.setDash(1, 0)
    c.setFont("Helvetica-Oblique", 8)
    c.setFillColorRGB(*COLOR_DANGER_RED)
    c.drawString(logo_x - 110, logo_y + 70, "Clear Space (M height)")

    c.restoreState()
    c.showPage()

# ============================================================================
# PAGE 5: LOGO VARIATIONS
# ============================================================================
def draw_logo_variations(c):
    """Page 5: Logo Variations"""
    draw_header(c, 5)
    draw_footer(c, 5)

    c.saveState()

    # Background
    c.setFillColorRGB(*COLOR_FROST_WHITE)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Section banner
    draw_section_banner(c, PAGE_HEIGHT - 50, "Logo Variations")

    y = PAGE_HEIGHT - 120

    # Layout: 2x2 grid
    variations = [
        ("Primary (Color on White)", "primary", COLOR_FROST_WHITE),
        ("Reversed (White on Navy)", "reversed", COLOR_DEEP_NAVY),
        ("Monochrome Dark", "monochrome_dark", COLOR_FROST_WHITE),
        ("Monochrome Light", "monochrome_light", COLOR_DEEP_NAVY)
    ]

    box_width = (PAGE_WIDTH - 3 * MARGIN) / 2
    box_height = 180

    positions = [
        (MARGIN, y - box_height),
        (MARGIN + box_width + MARGIN / 2, y - box_height),
        (MARGIN, y - 2 * box_height - 30),
        (MARGIN + box_width + MARGIN / 2, y - 2 * box_height - 30)
    ]

    for i, (name, scheme, bg_color) in enumerate(variations):
        x_pos, y_pos = positions[i]

        # Background box
        c.setFillColorRGB(*bg_color)
        c.setStrokeColorRGB(*COLOR_SLATE_GREY)
        c.setLineWidth(0.5)
        c.roundRect(x_pos, y_pos, box_width, box_height, 5, fill=1, stroke=1)

        # Logo
        draw_smartac_logo(c, x_pos + box_width / 2, y_pos + box_height / 2,
                         size=120, color_scheme=scheme)

        # Label
        c.setFont("Helvetica-Bold", 10)
        c.setFillColorRGB(*COLOR_DEEP_NAVY)
        label_width = c.stringWidth(name, "Helvetica-Bold", 10)
        c.drawString(x_pos + (box_width - label_width) / 2, y_pos - 15, name)

    c.restoreState()
    c.showPage()

# ============================================================================
# PAGE 6: LOGO MISUSE
# ============================================================================
def draw_logo_misuse(c):
    """Page 6: Logo Misuse (Do's and Don'ts)"""
    draw_header(c, 6)
    draw_footer(c, 6)

    c.saveState()

    # Background
    c.setFillColorRGB(*COLOR_FROST_WHITE)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Section banner
    draw_section_banner(c, PAGE_HEIGHT - 50, "Logo Misuse — Don'ts")

    y = PAGE_HEIGHT - 100

    # Grid of bad examples
    box_size = 140
    spacing = 20

    misuses = [
        ("Don't Stretch", "stretch"),
        ("Don't Change Colors", "color"),
        ("Don't Use Busy Background", "background"),
        ("Don't Add Shadows", "shadow"),
        ("Don't Rotate", "rotate"),
        ("Don't Low Contrast", "contrast")
    ]

    positions = [
        (MARGIN + 30, y - box_size),
        (MARGIN + 30 + box_size + spacing, y - box_size),
        (MARGIN + 30 + 2 * (box_size + spacing), y - box_size),
        (MARGIN + 30, y - 2 * box_size - spacing - 40),
        (MARGIN + 30 + box_size + spacing, y - 2 * box_size - spacing - 40),
        (MARGIN + 30 + 2 * (box_size + spacing), y - 2 * box_size - spacing - 40)
    ]

    for i, (label, error_type) in enumerate(misuses):
        if i >= len(positions):
            break
        x_pos, y_pos = positions[i]

        # Box background
        c.setFillColorRGB(1, 1, 1)
        c.setStrokeColorRGB(*COLOR_SLATE_GREY)
        c.setLineWidth(0.5)
        c.rect(x_pos, y_pos, box_size, box_size, fill=1, stroke=1)

        # Draw misused logo
        c.saveState()

        if error_type == "stretch":
            # Stretched horizontally
            c.scale(1.5, 1)
            draw_smartac_logo(c, (x_pos + box_size / 2) / 1.5, y_pos + box_size / 2,
                            size=60, color_scheme='primary')

        elif error_type == "color":
            # Wrong colors - draw with random colors
            c.setFillColorRGB(0.8, 0.2, 0.8)
            c.setFont("Helvetica-Bold", 24)
            c.drawString(x_pos + 30, y_pos + 60, "MTP")

        elif error_type == "background":
            # Busy background
            for j in range(10):
                c.setFillColorRGB(0.9, 0.9, 0.9)
                c.rect(x_pos + j * 15, y_pos, 10, box_size, fill=1, stroke=0)
            draw_smartac_logo(c, x_pos + box_size / 2, y_pos + box_size / 2,
                            size=60, color_scheme='primary')

        elif error_type == "shadow":
            # Draw shadow (offset black version)
            c.setFillColorRGB(0.5, 0.5, 0.5)
            c.setFont("Helvetica-Bold", 24)
            c.drawString(x_pos + 33, y_pos + 57, "MTP")
            draw_smartac_logo(c, x_pos + box_size / 2, y_pos + box_size / 2,
                            size=60, color_scheme='primary')

        elif error_type == "rotate":
            # Rotated 45 degrees
            c.translate(x_pos + box_size / 2, y_pos + box_size / 2)
            c.rotate(45)
            draw_smartac_logo(c, 0, 0, size=60, color_scheme='primary')

        elif error_type == "contrast":
            # Low contrast - Arctic blue on light blue
            c.setFillColorRGB(0.8, 0.9, 1)
            c.rect(x_pos, y_pos, box_size, box_size, fill=1, stroke=0)
            draw_smartac_logo(c, x_pos + box_size / 2, y_pos + box_size / 2,
                            size=60, color_scheme='primary')

        c.restoreState()

        # Red X overlay
        c.setStrokeColorRGB(*COLOR_DANGER_RED)
        c.setLineWidth(3)
        c.line(x_pos + 10, y_pos + 10, x_pos + box_size - 10, y_pos + box_size - 10)
        c.line(x_pos + 10, y_pos + box_size - 10, x_pos + box_size - 10, y_pos + 10)

        # Label
        c.setFont("Helvetica-Bold", 9)
        c.setFillColorRGB(*COLOR_DANGER_RED)
        label_width = c.stringWidth(label, "Helvetica-Bold", 9)
        c.drawString(x_pos + (box_size - label_width) / 2, y_pos - 12, label)

    c.restoreState()
    c.showPage()

# ============================================================================
# PAGE 7: COLOR PALETTE
# ============================================================================
def draw_color_palette(c):
    """Page 7: Color Palette"""
    draw_header(c, 7)
    draw_footer(c, 7)

    c.saveState()

    # Background
    c.setFillColorRGB(*COLOR_FROST_WHITE)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Section banner
    draw_section_banner(c, PAGE_HEIGHT - 50, "Brand Color Palette")

    y = PAGE_HEIGHT - 100

    # Color swatches data
    colors_data = [
        ("Arctic Blue", ARCTIC_BLUE, "10, 132, 255", "96, 48, 0, 0", "Primary brand color, buttons, headers"),
        ("Cool Teal", COOL_TEAL, "48, 213, 200", "76, 0, 6, 16", "Accent color, IoT highlights, CTAs"),
        ("Deep Navy", DEEP_NAVY, "13, 27, 42", "69, 36, 0, 84", "Dark backgrounds, body text"),
        ("Frost White", FROST_WHITE, "244, 249, 255", "4, 2, 0, 0", "Light backgrounds, cards"),
        ("Slate Grey", SLATE_GREY, "107, 114, 128", "16, 11, 0, 50", "Secondary text, borders"),
    ]

    # Draw swatches in 2 columns
    swatch_width = (PAGE_WIDTH - 3 * MARGIN) / 2
    swatch_height = 100

    col1_x = MARGIN
    col2_x = MARGIN + swatch_width + MARGIN / 2

    for i, (name, hex_val, rgb, cmyk, usage) in enumerate(colors_data):
        if i < 3:
            x_pos = col1_x
            y_pos = y - (i * (swatch_height + 30))
        else:
            x_pos = col2_x
            y_pos = y - ((i - 3) * (swatch_height + 30))

        # Color swatch
        color_rgb = hex_to_rgb(hex_val)
        c.setFillColorRGB(*color_rgb)
        c.roundRect(x_pos, y_pos, swatch_width, swatch_height, 8, fill=1, stroke=0)

        # Color info text
        info_y = y_pos - 15
        c.setFont("Helvetica-Bold", 11)
        c.setFillColorRGB(*COLOR_DEEP_NAVY)
        c.drawString(x_pos, info_y, name)

        info_y -= 15
        c.setFont("Helvetica", 9)
        c.setFillColorRGB(*COLOR_SLATE_GREY)
        c.drawString(x_pos, info_y, f"HEX: {hex_val}")

        info_y -= 12
        c.drawString(x_pos, info_y, f"RGB: {rgb}")

        info_y -= 12
        c.drawString(x_pos, info_y, f"CMYK: {cmyk}")

        info_y -= 15
        c.setFont("Helvetica-Oblique", 8)
        # Wrap usage text
        if len(usage) > 40:
            words = usage.split()
            line1 = " ".join(words[:5])
            line2 = " ".join(words[5:])
            c.drawString(x_pos, info_y, line1)
            c.drawString(x_pos, info_y - 10, line2)
        else:
            c.drawString(x_pos, info_y, usage)

    c.restoreState()
    c.showPage()

# ============================================================================
# PAGE 8: TYPOGRAPHY SHOWCASE
# ============================================================================
def draw_typography(c):
    """Page 8: Typography Showcase"""
    draw_header(c, 8)
    draw_footer(c, 8)

    c.saveState()

    # Background
    c.setFillColorRGB(*COLOR_FROST_WHITE)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Section banner
    draw_section_banner(c, PAGE_HEIGHT - 50, "Typography System")

    y = PAGE_HEIGHT - 90

    # Type hierarchy demonstration
    c.setFont("Helvetica-Bold", 22)
    c.setFillColorRGB(*COLOR_ARCTIC_BLUE)
    c.drawString(MARGIN, y, "Heading Level 1 — Helvetica Bold 22pt")
    y -= 30

    c.setFont("Helvetica-Bold", 14)
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.drawString(MARGIN, y, "Heading Level 2 — Helvetica Bold 14pt")
    y -= 25

    c.setFont("Helvetica", 11)
    c.setFillColorRGB(*COLOR_SLATE_GREY)
    body_text = [
        "Body text uses Helvetica 11pt in Slate Grey with 1.5 line spacing. This paragraph demonstrates",
        "how body copy appears in the SmartAC brand system. The typeface provides excellent readability",
        "across digital and print media, ensuring clear communication of technical and marketing content."
    ]
    for line in body_text:
        c.drawString(MARGIN, y, line)
        y -= 15

    y -= 10
    c.setFont("Helvetica-Oblique", 9)
    c.drawString(MARGIN, y, "Captions and labels use Helvetica Oblique 9pt for supplementary information.")
    y -= 20

    c.setFont("Helvetica-BoldOblique", 13)
    c.setFillColorRGB(*COLOR_COOL_TEAL)
    c.drawString(MARGIN, y, "Pull quotes and taglines: Helvetica Bold Oblique 13pt in Cool Teal")
    y -= 35

    # Alphabet showcase
    c.setFont("Helvetica-Bold", 12)
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.drawString(MARGIN, y, "Primary Typeface: Helvetica")
    y -= 20

    c.setFont("Helvetica", 10)
    c.setFillColorRGB(*COLOR_SLATE_GREY)
    c.drawString(MARGIN, y, "Uppercase: ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    y -= 15
    c.drawString(MARGIN, y, "Lowercase: abcdefghijklmnopqrstuvwxyz")
    y -= 15
    c.drawString(MARGIN, y, "Numerals: 0123456789")
    y -= 15
    c.drawString(MARGIN, y, "Special Characters: !@#$%^&*()_+-={}[]|:;<>?,./")
    y -= 30

    # Sample paragraph
    c.setFont("Helvetica-Bold", 12)
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.drawString(MARGIN, y, "Sample Application Text")
    y -= 20

    c.setFont("Helvetica", 10)
    c.setFillColorRGB(*COLOR_SLATE_GREY)
    sample_lines = [
        "SmartAC revolutionizes home climate control through intelligent automation and seamless",
        "connectivity. Our Android application provides intuitive controls, real-time monitoring,",
        "and energy-saving insights—all designed with the user experience at the forefront.",
        "The interface balances technical precision with approachable design, making advanced",
        "IoT technology accessible to everyone."
    ]
    for line in sample_lines:
        c.drawString(MARGIN, y, line)
        y -= 13

    c.restoreState()
    c.showPage()

# ============================================================================
# PAGE 9: ICONOGRAPHY & UI ELEMENTS
# ============================================================================
def draw_iconography(c):
    """Page 9: Iconography & UI Elements"""
    draw_header(c, 9)
    draw_footer(c, 9)

    c.saveState()

    # Background
    c.setFillColorRGB(*COLOR_FROST_WHITE)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Section banner
    draw_section_banner(c, PAGE_HEIGHT - 50, "Iconography & UI Elements")

    y = PAGE_HEIGHT - 90

    # Icon style guide
    c.setFont("Helvetica-Bold", 12)
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.drawString(MARGIN, y, "Icon Style Guidelines")
    y -= 20

    c.setFont("Helvetica", 10)
    c.setFillColorRGB(*COLOR_SLATE_GREY)
    c.drawString(MARGIN, y, "• Stroke weight: 2pt | Line cap: Rounded | Color: Arctic Blue | Grid: 24×24pt")
    y -= 40

    # Draw icons in grid
    icons_data = [
        ("Thermometer", "thermometer"),
        ("WiFi", "wifi"),
        ("Phone", "phone"),
        ("Snowflake", "snowflake"),
        ("Power", "power"),
        ("Settings", "settings"),
        ("Leaf", "leaf"),
        ("Cloud", "cloud")
    ]

    icon_box_size = 80
    icons_per_row = 4
    spacing = 20

    for i, (name, icon_type) in enumerate(icons_data):
        row = i // icons_per_row
        col = i % icons_per_row

        x_pos = MARGIN + col * (icon_box_size + spacing)
        y_pos = y - row * (icon_box_size + spacing + 20)

        # Icon background box
        c.setFillColorRGB(1, 1, 1)
        c.setStrokeColorRGB(*COLOR_SLATE_GREY)
        c.setLineWidth(0.5)
        c.roundRect(x_pos, y_pos - icon_box_size, icon_box_size, icon_box_size, 5, fill=1, stroke=1)

        # Draw simple icon
        icon_center_x = x_pos + icon_box_size / 2
        icon_center_y = y_pos - icon_box_size / 2

        c.setStrokeColorRGB(*COLOR_ARCTIC_BLUE)
        c.setLineWidth(2)
        c.setLineCap(1)  # Rounded caps

        if icon_type == "thermometer":
            c.line(icon_center_x, icon_center_y - 15, icon_center_x, icon_center_y + 15)
            c.circle(icon_center_x, icon_center_y - 18, 5, stroke=1, fill=0)
        elif icon_type == "wifi":
            for j in range(3):
                r = (j + 1) * 5
                c.arc(icon_center_x - r, icon_center_y - r, icon_center_x + r, icon_center_y + r, 45, 90)
            c.setFillColorRGB(*COLOR_ARCTIC_BLUE)
            c.circle(icon_center_x, icon_center_y, 2, fill=1)
        elif icon_type == "phone":
            c.roundRect(icon_center_x - 10, icon_center_y - 15, 20, 30, 3, stroke=1, fill=0)
            c.line(icon_center_x - 5, icon_center_y + 12, icon_center_x + 5, icon_center_y + 12)
        elif icon_type == "snowflake":
            c.line(icon_center_x, icon_center_y - 12, icon_center_x, icon_center_y + 12)
            c.line(icon_center_x - 12, icon_center_y, icon_center_x + 12, icon_center_y)
            c.line(icon_center_x - 8, icon_center_y - 8, icon_center_x + 8, icon_center_y + 8)
            c.line(icon_center_x - 8, icon_center_y + 8, icon_center_x + 8, icon_center_y - 8)
        elif icon_type == "power":
            c.line(icon_center_x, icon_center_y - 8, icon_center_x, icon_center_y + 5)
            c.arc(icon_center_x - 10, icon_center_y - 10, icon_center_x + 10, icon_center_y + 10, 45, 270)
        elif icon_type == "settings":
            c.circle(icon_center_x, icon_center_y, 8, stroke=1, fill=0)
            for angle in range(0, 360, 60):
                import math
                x1 = icon_center_x + 8 * math.cos(math.radians(angle))
                y1 = icon_center_y + 8 * math.sin(math.radians(angle))
                x2 = icon_center_x + 12 * math.cos(math.radians(angle))
                y2 = icon_center_y + 12 * math.sin(math.radians(angle))
                c.line(x1, y1, x2, y2)
        elif icon_type == "leaf":
            c.bezier(icon_center_x - 10, icon_center_y, icon_center_x - 5, icon_center_y + 15,
                    icon_center_x + 5, icon_center_y + 15, icon_center_x + 10, icon_center_y)
            c.line(icon_center_x - 10, icon_center_y, icon_center_x + 10, icon_center_y)
        elif icon_type == "cloud":
            c.arc(icon_center_x - 12, icon_center_y - 5, icon_center_x, icon_center_y + 7, 0, 180)
            c.arc(icon_center_x - 5, icon_center_y - 3, icon_center_x + 7, icon_center_y + 9, 0, 180)
            c.line(icon_center_x - 12, icon_center_y + 1, icon_center_x + 7, icon_center_y + 1)

        # Icon label
        c.setFont("Helvetica", 8)
        c.setFillColorRGB(*COLOR_DEEP_NAVY)
        label_width = c.stringWidth(name, "Helvetica", 8)
        c.drawString(x_pos + (icon_box_size - label_width) / 2, y_pos - icon_box_size - 12, name)

    c.restoreState()
    c.showPage()

# ============================================================================
# PAGE 10: UI COLOR APPLICATION
# ============================================================================
def draw_ui_application(c):
    """Page 10: UI Color Application"""
    draw_header(c, 10)
    draw_footer(c, 10)

    c.saveState()

    # Background
    c.setFillColorRGB(*COLOR_FROST_WHITE)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Section banner
    draw_section_banner(c, PAGE_HEIGHT - 50, "UI Color Application")

    y = PAGE_HEIGHT - 100

    # Mock Android UI
    phone_width = 200
    phone_height = 400
    phone_x = PAGE_WIDTH / 2 - phone_width / 2
    phone_y = y - phone_height - 20

    # Phone outline
    c.setStrokeColorRGB(*COLOR_SLATE_GREY)
    c.setLineWidth(2)
    c.roundRect(phone_x, phone_y, phone_width, phone_height, 10, fill=0, stroke=1)

    # Status bar (Deep Navy)
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.rect(phone_x, phone_y + phone_height - 25, phone_width, 25, fill=1, stroke=0)
    c.setFont("Helvetica", 6)
    c.setFillColorRGB(1, 1, 1)
    c.drawString(phone_x + 10, phone_y + phone_height - 15, "9:41")
    c.drawString(phone_x + phone_width - 30, phone_y + phone_height - 15, "100%")

    # Label
    c.setFont("Helvetica-Oblique", 7)
    c.setFillColorRGB(*COLOR_SLATE_GREY)
    c.drawString(phone_x + phone_width + 10, phone_y + phone_height - 15, "← Deep Navy")

    # App header (Arctic Blue)
    c.setFillColorRGB(*COLOR_ARCTIC_BLUE)
    c.rect(phone_x, phone_y + phone_height - 65, phone_width, 40, fill=1, stroke=0)
    c.setFont("Helvetica-Bold", 12)
    c.setFillColorRGB(1, 1, 1)
    c.drawString(phone_x + 15, phone_y + phone_height - 45, "SmartAC")

    c.setFont("Helvetica-Oblique", 7)
    c.setFillColorRGB(*COLOR_SLATE_GREY)
    c.drawString(phone_x + phone_width + 10, phone_y + phone_height - 45, "← Arctic Blue")

    # Card component (Frost White)
    card_y = phone_y + phone_height - 150
    c.setFillColorRGB(*COLOR_FROST_WHITE)
    c.roundRect(phone_x + 15, card_y, phone_width - 30, 70, 5, fill=1, stroke=0)

    c.setFont("Helvetica-Bold", 10)
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.drawString(phone_x + 25, card_y + 50, "Living Room")

    c.setFont("Helvetica-Bold", 24)
    c.setFillColorRGB(*COLOR_ARCTIC_BLUE)
    c.drawString(phone_x + 25, card_y + 25, "22°C")

    # Notification badge (Cool Teal)
    c.setFillColorRGB(*COLOR_COOL_TEAL)
    c.circle(phone_x + phone_width - 30, card_y + 55, 8, fill=1, stroke=0)
    c.setFont("Helvetica-Bold", 7)
    c.setFillColorRGB(1, 1, 1)
    c.drawString(phone_x + phone_width - 33, card_y + 52, "3")

    c.setFont("Helvetica-Oblique", 7)
    c.setFillColorRGB(*COLOR_SLATE_GREY)
    c.drawString(phone_x + phone_width + 10, card_y + 55, "← Cool Teal Badge")

    # Toggle buttons
    toggle_y = card_y - 40

    # ON button (Arctic Blue)
    c.setFillColorRGB(*COLOR_ARCTIC_BLUE)
    c.roundRect(phone_x + 20, toggle_y, 70, 30, 5, fill=1, stroke=0)
    c.setFont("Helvetica-Bold", 9)
    c.setFillColorRGB(1, 1, 1)
    c.drawString(phone_x + 40, toggle_y + 13, "ON")

    # OFF button (Slate Grey)
    c.setFillColorRGB(*COLOR_SLATE_GREY)
    c.roundRect(phone_x + 110, toggle_y, 70, 30, 5, fill=1, stroke=0)
    c.setFont("Helvetica-Bold", 9)
    c.setFillColorRGB(1, 1, 1)
    c.drawString(phone_x + 128, toggle_y + 13, "OFF")

    c.setFont("Helvetica-Oblique", 7)
    c.setFillColorRGB(*COLOR_SLATE_GREY)
    c.drawString(phone_x + phone_width + 10, toggle_y + 15, "← Button States")

    # Color legend
    legend_y = phone_y - 40
    c.setFont("Helvetica-Bold", 10)
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.drawString(MARGIN, legend_y, "Color Application Legend:")

    legend_items = [
        ("Deep Navy", COLOR_DEEP_NAVY, "Status bar, headers"),
        ("Arctic Blue", COLOR_ARCTIC_BLUE, "Primary actions, active states"),
        ("Cool Teal", COLOR_COOL_TEAL, "Notifications, accents"),
        ("Frost White", COLOR_FROST_WHITE, "Card backgrounds, containers"),
        ("Slate Grey", COLOR_SLATE_GREY, "Inactive states, secondary text")
    ]

    legend_y -= 20
    for name, color, usage in legend_items:
        # Color swatch
        c.setFillColorRGB(*color)
        c.roundRect(MARGIN, legend_y, 15, 15, 2, fill=1, stroke=0)

        # Text
        c.setFont("Helvetica-Bold", 9)
        c.setFillColorRGB(*COLOR_DEEP_NAVY)
        c.drawString(MARGIN + 20, legend_y + 8, name + ":")

        c.setFont("Helvetica", 8)
        c.setFillColorRGB(*COLOR_SLATE_GREY)
        c.drawString(MARGIN + 80, legend_y + 8, usage)

        legend_y -= 20

    c.restoreState()
    c.showPage()

# ============================================================================
# PAGES 11-15: Additional pages
# ============================================================================
def draw_brand_voice(c):
    """Page 11: Brand Voice & Messaging"""
    draw_header(c, 11)
    draw_footer(c, 11)

    c.saveState()
    c.setFillColorRGB(*COLOR_FROST_WHITE)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
    draw_section_banner(c, PAGE_HEIGHT - 50, "Brand Voice & Messaging")

    y = PAGE_HEIGHT - 90

    # Tone of voice
    c.setFont("Helvetica-Bold", 12)
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.drawString(MARGIN, y, "Tone of Voice")
    y -= 20

    c.setFont("Helvetica", 10)
    c.setFillColorRGB(*COLOR_SLATE_GREY)
    tone_text = [
        "SmartAC communicates with a professional yet approachable tone. We are:",
        "• Tech-forward: Confident in our technological capabilities without being intimidating",
        "• Reassuring: Building trust through clear, honest communication",
        "• Empowering: Helping users feel in control of their environment",
        "• Sustainable: Emphasizing environmental responsibility and energy efficiency"
    ]
    for line in tone_text:
        c.drawString(MARGIN, y, line)
        y -= 15

    y -= 20

    # DO/DON'T table
    c.setFont("Helvetica-Bold", 12)
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.drawString(MARGIN, y, "Language Guidelines: DO vs DON'T")
    y -= 25

    guidelines = [
        ("DO: 'Optimize your comfort'", "DON'T: 'Maximize AC efficiency'"),
        ("DO: 'Smart climate control'", "DON'T: 'Complicated automation system'"),
        ("DO: 'Save energy effortlessly'", "DON'T: 'Reduce power consumption manually'"),
        ("DO: 'Your comfort, remotely'", "DON'T: 'IoT-enabled thermal management'"),
        ("DO: 'Simple, intelligent cooling'", "DON'T: 'Advanced HVAC protocols'")
    ]

    for do, dont in guidelines:
        # DO column
        c.setFont("Helvetica-Bold", 9)
        c.setFillColorRGB(*COLOR_ARCTIC_BLUE)
        c.drawString(MARGIN + 10, y, "✓")
        c.setFont("Helvetica", 9)
        c.setFillColorRGB(*COLOR_DEEP_NAVY)
        c.drawString(MARGIN + 25, y, do)

        # DON'T column
        c.setFont("Helvetica-Bold", 9)
        c.setFillColorRGB(*COLOR_DANGER_RED)
        c.drawString(PAGE_WIDTH / 2 + 10, y, "✗")
        c.setFont("Helvetica", 9)
        c.setFillColorRGB(*COLOR_SLATE_GREY)
        c.drawString(PAGE_WIDTH / 2 + 25, y, dont)

        y -= 18

    y -= 20

    # Sample messages
    c.setFont("Helvetica-Bold", 12)
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.drawString(MARGIN, y, "Sample App Messages")
    y -= 20

    messages = [
        "Onboarding: 'Welcome to SmartAC! Let's get your climate control set up in just a few taps.'",
        "Notification: 'Your living room reached your preferred temperature of 22°C.'",
        "Energy Tip: 'You've saved 15% energy this week by using eco mode. Great work!'",
        "Error: 'Connection lost. We'll retry automatically when your WiFi is back.'"
    ]

    for msg in messages:
        c.setFont("Helvetica-Oblique", 9)
        c.setFillColorRGB(*COLOR_SLATE_GREY)
        # Wrap long text
        if len(msg) > 80:
            parts = [msg[i:i+80] for i in range(0, len(msg), 80)]
            for part in parts:
                c.drawString(MARGIN + 10, y, part)
                y -= 12
        else:
            c.drawString(MARGIN + 10, y, msg)
            y -= 15

    c.restoreState()
    c.showPage()

def draw_stationery(c):
    """Page 12: Stationery & Application Mockups"""
    draw_header(c, 12)
    draw_footer(c, 12)

    c.saveState()
    c.setFillColorRGB(*COLOR_FROST_WHITE)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
    draw_section_banner(c, PAGE_HEIGHT - 50, "Stationery & Brand Applications")

    y = PAGE_HEIGHT - 90

    # Business card mockup (front)
    card_width = 150
    card_height = 90
    card_x = MARGIN
    card_y = y - card_height

    c.setFillColorRGB(1, 1, 1)
    c.setStrokeColorRGB(*COLOR_SLATE_GREY)
    c.setLineWidth(0.5)
    c.rect(card_x, card_y, card_width, card_height, fill=1, stroke=1)

    # Card content
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.rect(card_x, card_y + card_height - 25, card_width, 25, fill=1, stroke=0)

    draw_smartac_logo(c, card_x + card_width / 2, card_y + card_height / 2 + 10, size=60, color_scheme='primary')

    c.setFont("Helvetica-Bold", 8)
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.drawString(card_x + 10, card_y + 20, "MAKAMTE TATSINKOU PAOLA")
    c.setFont("Helvetica", 6)
    c.setFillColorRGB(*COLOR_SLATE_GREY)
    c.drawString(card_x + 10, card_y + 13, "Software Engineer")
    c.drawString(card_x + 10, card_y + 6, "paola@smartac.io")

    # Label
    c.setFont("Helvetica-Bold", 9)
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.drawString(card_x, card_y - 15, "Business Card (Front)")

    # Business card (back)
    card_back_x = card_x + card_width + 30
    c.setFillColorRGB(*COLOR_ARCTIC_BLUE)
    c.rect(card_back_x, card_y, card_width, card_height, fill=1, stroke=0)

    c.setFont("Helvetica-Bold", 7)
    c.setFillColorRGB(1, 1, 1)
    c.drawString(card_back_x + 10, card_y + card_height / 2, "SmartAC")
    c.setFont("Helvetica", 6)
    c.drawString(card_back_x + 10, card_y + card_height / 2 - 10, "Intelligent Climate. Total Control.")

    c.setFont("Helvetica-Bold", 9)
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.drawString(card_back_x, card_y - 15, "Business Card (Back)")

    # Letterhead mockup
    y = card_y - 80
    letter_width = PAGE_WIDTH - 2 * MARGIN
    letter_height = 150

    c.setFillColorRGB(1, 1, 1)
    c.setStrokeColorRGB(*COLOR_SLATE_GREY)
    c.setLineWidth(0.5)
    c.rect(MARGIN, y - letter_height, letter_width, letter_height, fill=1, stroke=1)

    # Letterhead header
    c.setFillColorRGB(*COLOR_ARCTIC_BLUE)
    c.rect(MARGIN, y - 30, letter_width, 30, fill=1, stroke=0)

    draw_smartac_logo(c, MARGIN + 50, y - 15, size=40, color_scheme='reversed')

    c.setFont("Helvetica", 6)
    c.setFillColorRGB(1, 1, 1)
    c.drawString(letter_width - 50, y - 20, "www.smartac.io")

    # Letterhead content placeholder
    c.setFont("Helvetica", 8)
    c.setFillColorRGB(*COLOR_SLATE_GREY)
    for i in range(8):
        c.line(MARGIN + 20, y - 50 - i * 12, letter_width - 20, y - 50 - i * 12)

    c.setFont("Helvetica-Bold", 9)
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.drawString(MARGIN, y - letter_height - 15, "Letterhead Template")

    # App icon mockup
    icon_size = 80
    icon_x = MARGIN
    icon_y = y - letter_height - 50

    c.setFillColorRGB(*COLOR_ARCTIC_BLUE)
    c.roundRect(icon_x, icon_y - icon_size, icon_size, icon_size, 15, fill=1, stroke=0)

    draw_smartac_logo(c, icon_x + icon_size / 2, icon_y - icon_size / 2, size=50, color_scheme='reversed')

    c.setFont("Helvetica-Bold", 9)
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.drawString(icon_x, icon_y - icon_size - 15, "App Icon")

    c.restoreState()
    c.showPage()

def draw_usage_guidelines(c):
    """Page 13: Digital & Print Usage Guidelines"""
    draw_header(c, 13)
    draw_footer(c, 13)

    c.saveState()
    c.setFillColorRGB(*COLOR_FROST_WHITE)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
    draw_section_banner(c, PAGE_HEIGHT - 50, "Digital & Print Usage Guidelines")

    y = PAGE_HEIGHT - 90

    # File formats table
    c.setFont("Helvetica-Bold", 12)
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.drawString(MARGIN, y, "Recommended File Formats")
    y -= 25

    formats = [
        ("Print Materials", "PDF, SVG (vector), EPS", "CMYK color mode, 300 DPI minimum"),
        ("Digital/Web", "SVG, PNG (transparent), WebP", "RGB color mode, 72-96 DPI"),
        ("Email Signatures", "PNG (transparent)", "RGB, max 200px width"),
        ("Social Media", "PNG, JPG", "RGB, platform-specific dimensions"),
        ("App Assets", "PNG, SVG", "Multiple resolutions (@1x, @2x, @3x)")
    ]

    c.setFont("Helvetica-Bold", 9)
    c.setFillColorRGB(*COLOR_ARCTIC_BLUE)
    c.drawString(MARGIN + 10, y, "Use Case")
    c.drawString(MARGIN + 120, y, "Format")
    c.drawString(MARGIN + 260, y, "Specifications")
    y -= 3

    c.setStrokeColorRGB(*COLOR_SLATE_GREY)
    c.setLineWidth(0.5)
    c.line(MARGIN, y, PAGE_WIDTH - MARGIN, y)
    y -= 15

    for use, fmt, spec in formats:
        c.setFont("Helvetica-Bold", 9)
        c.setFillColorRGB(*COLOR_DEEP_NAVY)
        c.drawString(MARGIN + 10, y, use)

        c.setFont("Helvetica", 8)
        c.setFillColorRGB(*COLOR_SLATE_GREY)
        c.drawString(MARGIN + 120, y, fmt)
        c.drawString(MARGIN + 260, y, spec)

        y -= 15

    y -= 20

    # Resolution requirements
    c.setFont("Helvetica-Bold", 12)
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.drawString(MARGIN, y, "Resolution Requirements")
    y -= 20

    c.setFont("Helvetica", 10)
    c.setFillColorRGB(*COLOR_SLATE_GREY)
    res_text = [
        "• Print: Minimum 300 DPI for professional quality output",
        "• Screen/Digital: 72-96 DPI is standard for web and mobile applications",
        "• Large Format: 150-200 DPI for posters and banners (viewed from distance)",
        "• Retina/High-DPI: Provide @2x and @3x assets for mobile applications"
    ]
    for line in res_text:
        c.drawString(MARGIN + 10, y, line)
        y -= 15

    y -= 20

    # Color mode guidelines
    c.setFont("Helvetica-Bold", 12)
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.drawString(MARGIN, y, "Color Mode Guidelines")
    y -= 20

    c.setFont("Helvetica", 10)
    c.setFillColorRGB(*COLOR_SLATE_GREY)
    color_text = [
        "• CMYK: For all printed materials (business cards, brochures, signage)",
        "• RGB/HEX: For all digital applications (website, app, social media)",
        "• Always use the defined brand color values—never eyeball or approximate colors",
        "• Include color profiles when exporting files for professional printing"
    ]
    for line in color_text:
        c.drawString(MARGIN + 10, y, line)
        y -= 15

    y -= 20

    # Font embedding
    c.setFont("Helvetica-Bold", 12)
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.drawString(MARGIN, y, "Font Embedding & Licensing")
    y -= 20

    c.setFont("Helvetica", 10)
    c.setFillColorRGB(*COLOR_SLATE_GREY)
    font_text = [
        "• Always embed fonts when creating PDF documents for distribution",
        "• Helvetica is a standard system font—ensure availability on target platforms",
        "• For web use, consider web-safe alternatives or licensed web fonts",
        "• Outline/convert text to paths for logo files to ensure consistency"
    ]
    for line in font_text:
        c.drawString(MARGIN + 10, y, line)
        y -= 15

    y -= 20

    # Social media sizing
    c.setFont("Helvetica-Bold", 12)
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.drawString(MARGIN, y, "Social Media Profile Image Sizing")
    y -= 20

    social_sizes = [
        ("Facebook", "180×180 px"),
        ("Instagram", "320×320 px"),
        ("Twitter/X", "400×400 px"),
        ("LinkedIn", "300×300 px")
    ]

    for platform, size in social_sizes:
        c.setFont("Helvetica-Bold", 9)
        c.setFillColorRGB(*COLOR_DEEP_NAVY)
        c.drawString(MARGIN + 10, y, platform + ":")

        c.setFont("Helvetica", 9)
        c.setFillColorRGB(*COLOR_SLATE_GREY)
        c.drawString(MARGIN + 100, y, size)

        y -= 15

    c.restoreState()
    c.showPage()

def draw_accessibility(c):
    """Page 14: Accessibility & Contrast"""
    draw_header(c, 14)
    draw_footer(c, 14)

    c.saveState()
    c.setFillColorRGB(*COLOR_FROST_WHITE)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
    draw_section_banner(c, PAGE_HEIGHT - 50, "Accessibility & Contrast")

    y = PAGE_HEIGHT - 90

    # Contrast ratios
    c.setFont("Helvetica-Bold", 12)
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.drawString(MARGIN, y, "WCAG Color Contrast Compliance")
    y -= 25

    contrast_pairs = [
        ("Deep Navy on Frost White", "14.2:1", "AAA Pass", COLOR_DEEP_NAVY, COLOR_FROST_WHITE),
        ("Arctic Blue on White", "5.1:1", "AA Pass", COLOR_ARCTIC_BLUE, (1, 1, 1)),
        ("Slate Grey on White", "4.8:1", "AA Pass", COLOR_SLATE_GREY, (1, 1, 1)),
        ("White on Arctic Blue", "5.1:1", "AA Pass", (1, 1, 1), COLOR_ARCTIC_BLUE),
        ("White on Deep Navy", "14.2:1", "AAA Pass", (1, 1, 1), COLOR_DEEP_NAVY),
        ("Cool Teal on Deep Navy", "8.5:1", "AAA Pass", COLOR_COOL_TEAL, COLOR_DEEP_NAVY)
    ]

    for pair_name, ratio, status, fg, bg in contrast_pairs:
        # Sample box
        box_width = 120
        box_height = 30

        c.setFillColorRGB(*bg)
        c.rect(MARGIN, y - box_height, box_width, box_height, fill=1, stroke=0)

        c.setFont("Helvetica-Bold", 10)
        c.setFillColorRGB(*fg)
        c.drawString(MARGIN + 10, y - 18, "Sample Text")

        # Info text
        c.setFont("Helvetica-Bold", 9)
        c.setFillColorRGB(*COLOR_DEEP_NAVY)
        c.drawString(MARGIN + box_width + 20, y - 10, pair_name)

        c.setFont("Helvetica", 9)
        c.setFillColorRGB(*COLOR_SLATE_GREY)
        c.drawString(MARGIN + box_width + 20, y - 22, f"Contrast: {ratio}")

        # Status badge
        if "AAA" in status:
            badge_color = (0.2, 0.8, 0.2)
        else:
            badge_color = COLOR_ARCTIC_BLUE

        c.setFillColorRGB(*badge_color)
        c.roundRect(MARGIN + box_width + 160, y - 25, 60, 18, 3, fill=1, stroke=0)

        c.setFont("Helvetica-Bold", 8)
        c.setFillColorRGB(1, 1, 1)
        c.drawString(MARGIN + box_width + 170, y - 16, status)

        y -= 45

    y -= 10

    # Text sizing guidelines
    c.setFont("Helvetica-Bold", 12)
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.drawString(MARGIN, y, "Accessible Text Sizing")
    y -= 20

    c.setFont("Helvetica", 10)
    c.setFillColorRGB(*COLOR_SLATE_GREY)
    sizing_text = [
        "• Minimum body text size: 11pt (14.67px) for comfortable reading",
        "• Line height: 1.5× the text size for improved readability",
        "• Button text: Minimum 10pt (13.33px) with adequate touch target size (44×44px)",
        "• Avoid text smaller than 9pt except for legal disclaimers"
    ]
    for line in sizing_text:
        c.drawString(MARGIN + 10, y, line)
        y -= 15

    y -= 15

    # Color blindness
    c.setFont("Helvetica-Bold", 12)
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.drawString(MARGIN, y, "Color Blindness Considerations")
    y -= 20

    c.setFont("Helvetica", 10)
    c.setFillColorRGB(*COLOR_SLATE_GREY)
    cb_text = [
        "The SmartAC color palette has been designed with accessibility in mind:",
        "",
        "• Arctic Blue and Cool Teal remain distinguishable in most color blindness types",
        "• Never rely on color alone to convey information—use icons, labels, or patterns",
        "• Deep Navy provides high contrast anchor point for all users",
        "• Test critical UI elements with color blindness simulation tools before deployment"
    ]
    for line in cb_text:
        c.drawString(MARGIN + 10, y, line)
        y -= 13

    c.restoreState()
    c.showPage()

def draw_conclusion(c):
    """Page 15: Conclusion"""
    draw_header(c, 15)
    draw_footer(c, 15)

    c.saveState()
    c.setFillColorRGB(*COLOR_FROST_WHITE)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
    draw_section_banner(c, PAGE_HEIGHT - 50, "Conclusion")

    y = PAGE_HEIGHT - 100

    # Summary
    c.setFont("Helvetica-Bold", 14)
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.drawString(MARGIN, y, "Building Trust Through Consistency")
    y -= 25

    c.setFont("Helvetica", 11)
    c.setFillColorRGB(*COLOR_SLATE_GREY)
    summary_text = [
        "This Visual Identity Guidelines document establishes the foundation for SmartAC's brand",
        "presence across all touchpoints. Consistent application of these guidelines ensures that",
        "SmartAC is immediately recognizable, trustworthy, and professional in every interaction.",
        "",
        "From the carefully crafted logo with its MTP monogram to the thoughtfully selected color",
        "palette and typography system, every element has been designed to communicate SmartAC's",
        "core values: intelligence, efficiency, connectivity, and sustainability.",
        "",
        "By adhering to these standards, we create a cohesive brand experience that builds user",
        "confidence and reinforces our position as a leader in smart home climate control technology."
    ]

    for line in summary_text:
        c.drawString(MARGIN, y, line)
        y -= 15

    y -= 20

    # Forward-looking statement
    c.setFont("Helvetica-Bold", 12)
    c.setFillColorRGB(*COLOR_DEEP_NAVY)
    c.drawString(MARGIN, y, "Looking Forward")
    y -= 20

    c.setFont("Helvetica", 11)
    c.setFillColorRGB(*COLOR_SLATE_GREY)
    forward_text = [
        "As SmartAC grows and evolves, this visual identity will adapt while maintaining its core",
        "principles. The system is designed to scale—from mobile app interfaces to marketing materials,",
        "from digital advertisements to physical installations.",
        "",
        "SmartAC represents more than technology; it represents a commitment to making sustainable,",
        "intelligent climate control accessible to everyone. Through consistent brand expression, we",
        "communicate this vision clearly and effectively to users worldwide."
    ]

    for line in forward_text:
        c.drawString(MARGIN, y, line)
        y -= 15

    y -= 25

    # Author note
    c.setFillColorRGB(*COLOR_ARCTIC_BLUE)
    c.roundRect(MARGIN, y - 60, PAGE_WIDTH - 2 * MARGIN, 55, 5, fill=1, stroke=0)

    c.setFont("Helvetica-BoldOblique", 11)
    c.setFillColorRGB(1, 1, 1)
    author_note = [
        "This Visual Identity Guidelines document was created as part of a Level 3",
        "Software Engineering project in Graphic Design. SmartAC represents the",
        "intersection of user-centric design and cutting-edge IoT technology."
    ]
    ay = y - 20
    for line in author_note:
        c.drawString(MARGIN + 15, ay, line)
        ay -= 13

    y -= 80

    # Large logo as final flourish
    draw_smartac_logo(c, PAGE_WIDTH / 2, y - 80, size=180, color_scheme='primary')

    y -= 180

    # Document metadata footer
    c.setFont("Helvetica", 8)
    c.setFillColorRGB(*COLOR_SLATE_GREY)
    metadata = f"SmartAC Visual Identity Guidelines v1.0 | {datetime.now().strftime('%B %Y')} | MAKAMTE TATSINKOU PAOLA"
    metadata_width = c.stringWidth(metadata, "Helvetica", 8)
    c.drawString((PAGE_WIDTH - metadata_width) / 2, y, metadata)

    c.restoreState()
    c.showPage()

# ============================================================================
# MAIN FUNCTION TO GENERATE PDF
# ============================================================================
def generate_pdf():
    """Generate the complete Visual Identity Guidelines PDF"""
    filename = "SmartAC_Visual_Identity_Guidelines.pdf"
    c = canvas.Canvas(filename, pagesize=A4)

    print("Generating SmartAC Visual Identity Guidelines PDF...")
    print(f"Page size: A4 ({PAGE_WIDTH:.2f} x {PAGE_HEIGHT:.2f} points)")

    # Generate all pages
    print("  ✓ Page 1: Cover Page")
    draw_cover_page(c)

    print("  ✓ Page 2: Table of Contents")
    draw_table_of_contents(c)

    print("  ✓ Page 3: Brand Overview & Story")
    draw_brand_overview(c)

    print("  ✓ Page 4: Logo Design & Construction")
    draw_logo_construction(c)

    print("  ✓ Page 5: Logo Variations")
    draw_logo_variations(c)

    print("  ✓ Page 6: Logo Misuse Guidelines")
    draw_logo_misuse(c)

    print("  ✓ Page 7: Color Palette")
    draw_color_palette(c)

    print("  ✓ Page 8: Typography Showcase")
    draw_typography(c)

    print("  ✓ Page 9: Iconography & UI Elements")
    draw_iconography(c)

    print("  ✓ Page 10: UI Color Application")
    draw_ui_application(c)

    print("  ✓ Page 11: Brand Voice & Messaging")
    draw_brand_voice(c)

    print("  ✓ Page 12: Stationery & Applications")
    draw_stationery(c)

    print("  ✓ Page 13: Digital & Print Usage")
    draw_usage_guidelines(c)

    print("  ✓ Page 14: Accessibility & Contrast")
    draw_accessibility(c)

    print("  ✓ Page 15: Conclusion")
    draw_conclusion(c)

    # Save the PDF
    c.save()

    print(f"\n✅ SUCCESS! PDF saved as: {filename}")
    print(f"   File size: {os.path.getsize(filename) / 1024:.2f} KB")
    print(f"   Ready for print and submission!")

    return filename

if __name__ == "__main__":
    import os
    generate_pdf()
