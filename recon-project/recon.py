import subprocess
import os

os.makedirs("results", exist_ok=True)

target = input("Enter target domain: ").strip()

def run_command(cmd):
    """Runs a shell command safely and returns output."""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"[ERROR] {e}"

print("\n[+] Subdomain enumeration...")

subdomains = run_command([
    "subfinder", "-d", target, "-silent"
])

if not subdomains.strip():
    print("[!] No subdomains found.")

print(subdomains)

with open("results/subdomains.txt", "w") as f:
    f.write(subdomains)

print("\n[+] Nmap scan...")

nmap = run_command([
    "nmap", "-sV", "--top-ports", "20", target
])

print(nmap)

with open("results/nmap.txt", "w") as f:
    f.write(nmap)

print("\n[+] Web directory scan...")

gobuster = run_command([
    "gobuster", "dir",
    "-u", f"http://{target}",
    "-w", "/usr/share/wordlists/dirb/common.txt",
    "-q"
])

print(gobuster)

with open("results/gobuster.txt", "w") as f:
    f.write(gobuster)

print("\n[+] Recon complete. Results saved in /results folder.")
