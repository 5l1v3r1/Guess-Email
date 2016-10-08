import time

if __name__ == "__main__":
    first_name, last_name, domain = get_person_info()
    wait_time = 2 # Wait 2 seconds in between calls

    for perm in get_email_permutations(first_name, last_name, domain):
        

def get_person_info():
    first_name = input("Enter subject's first name: ")
    last_name = input("Enter subject's last name: ")
    domain = input("Enter email domain: ")

    while domain[-4 :] not in TLDs:
        domain = input("Please re-enter email domain, including the top-level domain (e.g. .com, .net, etc.): ")

    return (first_name, last_name, domain)

def get_email_permutations(first_name, last_name, domain):
    """Given first name, last name, and a domain, returns a list of possible email
       permutations to try guessing.

       first_name: str
       last_name: str
       domain: str
    """
    f, l, d = first_name, last_name, domain

    # Example: John Smith, domain.com
    perms = [f,              # john@domain.com
             l,              # smith@domain.com
             f[0] + l,       # jsmith@domain.com
             f + "." + l,    # john.smith@domain.com
             f + l,          # johnsmith@domain.com
             f + "_" + l,    # john_smith@domain.com
             f + l[0],       # johns@domain.com
             f[0] + l[0],    # js@domain.com
             f[0] + "." + l] # j.smith@domain.com

    return [email + "@" + domain for email in perms]


