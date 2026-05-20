<img width="864" height="631" alt="image" src="https://github.com/user-attachments/assets/ce1d95ff-e132-419e-9404-04723a02a497" /># Automated Reconnaissance Toolkit

# Overview 

This project is a simple automated reconnaissance workflow designed to streamline the initial information-gathering phase of penetration testing. It focuses on discovering subdomains, identifying live hosts, and performing basic service enumeration.

The goal of this project is to replicate a realistic early-stage penetration testing workflow and reduce manual effort during reconnaissance.

# Objectives

Automate subdomain enumeration for a target domain
Identify live hosts and exposed services
Perform lightweight port scanning and HTTP probing

# Tools Used

This project integrates commonly used penetration testing tools:

Subfinder – subdomain enumeration
Nmap – port and service scanning
Gobuster – web directory enumeration

# Workflow 

The tool performs reconnaissance in the following order:

1. Subdomain Enumeration
Discover subdomains associated with the target domain using Subfinder.
2. Port & Service Scanning
Perform service detection and scan top ports using Nmap.
3. Web Directory Enumeration
Identify hidden directories and endpoints using Gobuster.
4. Output Storage
Save all results into structured files for later manual analysis.

# Usage

Run the script and enter a target domain when prompted:
```bash
python3 recon.py
```

Example input:
```
Enter target domain: example.com
```

![Example input](example-input.png)

# Example output

1. Subdomain Enumeration

![Subdomain Enumeration](subdomain-enum.png)

No subdomains were discovered for the tested domain, which is expected for inactive or placeholder domains like example.com.

2. Nmap Scan

![Nmap Scan](nmap-scan.png)

3. Gobuster Scan

![Gobuster Scan](gobuster-scan.png)

# Output structure

After execution, results are saved in the following format:
results/
 ├── subdomains.txt
 ├── nmap.txt
 ├── gobuster.txt

![Output structure](output-structure.png)

# Key Learning Outcomes

Understanding of the reconnaissance phase in penetration testing
Practical use of security enumeration tools
Automation of repetitive security tasks
Basic workflow design for penetration testing pipelines
Structured output handling for analysis
