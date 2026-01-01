# Port Scanner (Python)

A simple Python-based TCP port scanner built as part of my Cyber Security learning journey.
This script demonstrates basic network enumeration concepts using sockets.

## Description

This tool scans a predefined list of common ports on a target IP address or hostname
and reports whether each port is open or closed.

It is designed for educational purposes and hands-on practice in networking
and penetration testing fundamentals.

## Features

- TCP port scanning using Python sockets
- Custom timeout handling
- Clean and readable console output
- Beginner-friendly and easy to extend

## Scanned Ports

The script currently scans the following common ports:

- 21  (FTP)
- 22  (SSH)
- 80  (HTTP)
- 443 (HTTPS)

## Usage

Run the script using Python:

```bash
python port_scanner.py
