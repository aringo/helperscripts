#!/usr/bin/env python3

import subprocess
from PIL import Image, ImageDraw, ImageFont, ImageColor
import textwrap
import argparse
import re

def run_command_and_capture_output(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

def text_to_image(command, text, font_path='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', font_size=14, output_path='output.png', width=120, line_spacing=4, max_lines=50, bg_color=(0, 0, 0), text_color=(255, 255, 255), command_color=(0, 255, 0)):
    # Ensure the command is always at the top
    lines = [f"$ {command}"] + text.split('\n')
    # Limit the number of lines to fit in the image
    lines = lines[:max_lines] if len(lines) > max_lines else lines
    wrapped_lines = []
    for line in lines:
        wrapped_lines.extend(textwrap.wrap(line, width=width))

    font = ImageFont.truetype(font_path, font_size)
    max_width = max(font.getbbox(line)[2] for line in wrapped_lines)
    total_height = sum(font.getbbox(line)[3] - font.getbbox(line)[1] + line_spacing for line in wrapped_lines)

    image = Image.new('RGB', (max_width, total_height), color=bg_color)
    draw = ImageDraw.Draw(image)

    y_text = 0
    for i, line in enumerate(wrapped_lines):
        bbox = font.getbbox(line)
        width, height = bbox[2], bbox[3] - bbox[1]
        color = command_color if i == 0 else text_color
        draw.text((0, y_text), line, font=font, fill=color)
        y_text += height + line_spacing

    image.save(output_path)

def clean_command(command):
    return re.sub(r'\W+', '', command)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Capture terminal output and save as an image.")
    parser.add_argument('-c', '--command', required=True, help='Command to run')
    parser.add_argument('-o', '--output', help='Output image file')
    parser.add_argument('-w', '--width', type=int, default=120, help='Width of the text wrap')
    parser.add_argument('-l', '--line_spacing', type=int, default=4, help='Line spacing')
    parser.add_argument('-m', '--max_lines', type=int, default=50, help='Maximum number of lines')
    parser.add_argument('--bg_color', type=str, default='black', help='Background color (name or hex)')
    parser.add_argument('--text_color', type=str, default='white', help='Text color (name or hex)')
    parser.add_argument('--command_color', type=str, default='yellow', help='Command text color (name or hex)')

    args = parser.parse_args()

    command = args.command
    output = run_command_and_capture_output(command)

    output_file = args.output if args.output else f"{clean_command(command)}.png"

    bg_color = ImageColor.getrgb(args.bg_color)
    text_color = ImageColor.getrgb(args.text_color)
    command_color = ImageColor.getrgb(args.command_color)

    text_to_image(command, output, output_path=output_file, width=args.width, line_spacing=args.line_spacing, max_lines=args.max_lines, bg_color=bg_color, text_color=text_color, command_color=command_color)
