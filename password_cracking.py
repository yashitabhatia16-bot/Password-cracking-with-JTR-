

# Password Cracking & Security Testing

This repository contains my Week 3 cybersecurity project work, where I explored how password-protected PDF files can be tested using different password recovery tools.

I completed two practical modules as part of my cybersecurity training at NetworkWalks. Both exercises helped me understand how password hashes are extracted and how dictionary-based password attacks work.

## 📌 Project Modules

### 1. Password Cracking with John the Ripper (JTR)

**Tools used:**
- John the Ripper
- Johnny GUI
- PDF Hash Extractor

**What I did:**
- Installed and configured John the Ripper and Johnny GUI.
- Extracted the password hash from a protected PDF file.
- Saved the extracted hash in a text file.
- Loaded the hash into Johnny.
- Started a password recovery attack.
- Verified the recovered password by opening the protected PDF.

### 2. Password Cracking with NetworkWalks Tools

**Tools used:**
- NetworkWalks Hash Calculator
- NetworkWalks Password Cracker

**What I did:**
- Uploaded a password-protected PDF to the Hash Calculator.
- Extracted the PDF hash.
- Copied the complete hash into the Password Cracker.
- Ran a dictionary-based attack.
- Retrieved the matching password and verified it by opening the PDF.

## 🛠️ Tools & Resources

| Tool | Purpose |
|---|---|
| John the Ripper | Password hash cracking |
| Johnny GUI | Graphical interface for JTR |
| Hash Calculator | Extracting PDF password hashes |
| Password Cracker | Dictionary-based password recovery |

**Useful links:**
- [John the Ripper](https://www.openwall.com/john/)
- [Johnny GUI](https://openwall.info/wiki/john/johnny)
- [NetworkWalks Hash Calculator](https://networkwalks.com/hash-calculator/)
- [NetworkWalks Password Cracker](https://networkwalks.com/password-cracker/)

## 📚 What I Learned

Working on these two modules helped me understand:

- The difference between hashing and encryption.
- How password hashes can be extracted from protected PDF files.
- How dictionary attacks work.
- How tools like John the Ripper are used for password security testing.
- Why using common or weak passwords can put files at risk.

## 📸 Practical Demonstration

Screenshots of my lab work and the steps performed are included in this repository.

![nslookup output](screenshots/Johnny.png)

![nslookup output](screenshots/locked1.png)

![nslookup output](screenshots/crack1(a).png)

![nslookup output](screenshots/locked1(a).png)

![nslookup output](screenshots/locked2.png)

![nslookup output](screenshots/cracked3.png)

![nslookup output](screenshots/locked3.png)

## ⚠️ Disclaimer

This project was completed for educational purposes as part of cybersecurity training.

Password testing should only be performed on files and systems that you own or have explicit permission to test. Do not use these techniques to access someone else's private files.

---

**Project:** Week 3 – Project Modules 1 & 2  
**Training:** NetworkWalks  
**Focus:** Cybersecurity | Password Security | Ethical Hacking
