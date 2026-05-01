# What is Burp Suite?

It’s a man-in-the-middle (MITM) proxy tool that lets you:
    - Intercept HTTP/HTTPS traffic
    - Modify requests/responses
    - Automate vulnerability scanning
    - Perform manual exploitation

# What it does?

Burp sits between:
 *Your Browser ↔ Burp Proxy ↔ Target Website*
You configure your browser to send traffic to Burp (usually 127.0.0.1:8080).
Why this matters:
    - You see everything the browser sends/receives
    - You can edit requests before they hit the server

# Main Burp Suite Tools

## 1. 🧭 Proxy

This is the heart of Burp.
Features:
    - Intercept requests (pause & edit)
    - View raw HTTP/HTTPS traffic
    - Modify headers, cookies, parameters

## 2. 🔎 Target

Displays site structure (like a sitemap)
Shows discovered endpoints
Helps map attack surface

3. 📡 Repeater

Your best friend for manual testing.
What it does:
    - Send the same request repeatedly
    - Modify payloads easily
    - Analyze responses
Use cases:
    - Testing SQL injection
    - Checking authentication bypass
    - Tweaking API calls

## 4. ⚔️ Intruder

Used for automation and brute force attacks
Attack Types:
    - Sniper (one payload position)
    - Battering ram (same payload everywhere)
    - Pitchfork (multiple payload sets)
    - Cluster bomb (all combinations)
Use cases:
    - Password brute force
    - Fuzzing parameters
    - Discovering hidden values

## 5. 🧪 Scanner (Pro only)

Automates vulnerability detection.
Finds:
    - SQL Injection
    - XSS
    - CSRF
    - SSRF
    - Open redirects
    - Misconfigurations

## 6. 🔬 Decoder

Encode/decode data (Base64, URL encoding, etc.)

## 7. 🔧 Comparer

Compare two responses
Spot subtle differences

## 8. 🎯 Sequencer

Tests randomness of tokens (e.g., session IDs)

## 9. 🧬 Extender

Add plugins (called extensions)
Written in Python, Java, etc.
Popular extensions:
    - Autorize (auth testing)
    - Logger++
    - Active Scan++

# Burp Suite Highlight Suggestions

- Red: for identified issues
- Yellow: being somehow related to issues
- Blue: things that we wanna follow up later on
- Gray: to identify end point of doing something like clicking a picture or a button
