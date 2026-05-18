# Pickle Rick Writeup

Platform: TryHackMe  
Room: Pickle Rick  
Link: https://tryhackme.com/room/picklerick  
Target: <target_ip>

This write-up covers the “Pickle Rick” room on TryHackMe, which is a beginner-friendly challenge focused on basic web exploitation and privilege escalation.

The goal of the room is to explore the target machine, find vulnerabilities, and retrieve hidden “ingredients” by gaining higher levels of access.

In this write-up, I go through the steps I took, including scanning the target, finding useful information on the website, and using that information to get a shell and escalate privileges.

The tools I used include Nmap for scanning, Gobuster for directory discovery, and a web browser for interacting with the application.

I’ll also briefly explain why I used certain commands and what I was looking for at each step.

# 1. Reconnaissance

I started by scanning the target machine using Nmap to identify open ports and available services.

nmap -sC -sV <target_ip>

This scan showed that two ports were open:

Port 22 (SSH)
Port 80 (HTTP) 

The presence of SSH means that remote login might be possible if valid credentials are found. However, since no credentials were available at this stage, it wasn’t immediately useful.

Port 80 was running a web server, which suggested that the web application could be the main entry point into the system.

Based on this, I decided to focus on exploring the website first, while keeping SSH in mind in case I found credentials later.
   
# 2. Web Enumeration


   
4. Exploitation
5. Privilege Escalation
