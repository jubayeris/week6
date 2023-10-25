host_names = set() 

with open("writefile.txt", "r") as file:
    for line in file:
        if line.startswith("From:"):
            parts = line.split()
            if len(parts) > 1:
                email = parts[1]
                _, domain = email.split("@", 1)
                host_names.add(domain)

for host in host_names:
    print(host)

print(f"Number of unique hosts: {len(host_names)}")
