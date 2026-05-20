# Steel Mountain Writeup

Platform: TryHackMe  
Room: Pickle Rick  
Link: [https://tryhackme.com/room/steelmountain](https://tryhackme.com/room/steelmountain)
Target: <target_ip>

# 1. Reconnaissance

I started with a default Nmap scan to quickly identify open ports and services:

```bash
nmap -sC -sV -Pn <target_ip>
```
This scan identified multiple Windows services including HTTP, SMB, and RPC. A web service was discovered on port 80.

To ensure no services were missed, I followed up with a full port scan:

```bash
nmap -p- -Pn <TARGET_IP>
```

The scan revealed that port 8080 was running: HttpFileServer version 2.3

![Nmap scan](nmap-scan.png)

This service is known to have publicly available vulnerabilities.

# 2. Web Enumeration

Visiting the web server on port 80 revealed a company webpage containing an “Employee of the Month” section. By inspecting the image, I identified the employee as:

Bill Harper

# 3. Service Enumeration

Accessing the service in a browser confirmed it was a file-sharing web interface:

```bash
http://<TARGET_IP>:8080
```

![HttpFileServer](hfs.png)

# 4. Vulnerability Research

Using Searchsploit, I identified a known Remote Code Execution vulnerability affecting this service:

```bash
searchsploit HttpFileServer
```

![searchsploit HttpFileServer](sploit-hfs.png)

This revealed an exploit targeting HttpFileServer 2.3.x, associated with CVE-2014-6287, which allows remote command execution via a crafted HTTP request.

A Python exploit script (49125.py) was identified and reviewed. The exploit works by injecting commands into the vulnerable search parameter of the web application.

# 5. Exploitation Preparation & Execution

The exploit was executed with the following format:

```bash
python3 stlmtn.py <RHOST> 8080 "whoami"
```

The script generates a malicious HTTP request targeting the vulnerable parameter:

```bash
http://<TARGET_IP>:8080/?search=%00{.+exec|whoami.}
```

This confirmed that the target is vulnerable to remote command execution via the file server.

# 6. Initial Access

After identifying a vulnerable instance of HttpFileServer running on port 8080, I used the Metasploit framework to exploit a known Remote Code Execution vulnerability (CVE-2014-6287).

The exploit module was configured with the target IP address, service port, and attacker callback parameters (LHOST and LPORT). Upon execution, Metasploit delivered a payload through a crafted HTTP request to the vulnerable search parameter.

This resulted in successful code execution on the target system and the establishment of a Meterpreter session.

# 7. Privilege Escalation
