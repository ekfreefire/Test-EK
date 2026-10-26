import os

facebook = {
    "Username": "your_facebook_username",
    "Email": "your_facebook_email",
    "Profile": "your_facebook_profile_link",
}

gmail = {
    "Gmail": "your_gmail_address",
    "Recovery Email": "your_recovery_email",
}

def show_details(title, details):
    print("\n" + "=" * 30)
    print(title)
    print("=" * 30)
    for key, value in details.items():
        print(f"{key}: {value}")
    input("\nফিরতে Enter চাপো...")

while True:
    os.system("clear")
    print("""
╔════════════════════════════╗
║            EK              ║
║      PERSONAL MANAGER      ║
╚════════════════════════════╝
""")
    print("[1] Facebook Details")
    print("[2] Gmail Details")
    print("[3] Exit")

    choice = input("\nSelect Option: ").strip()

    if choice == "1":
        show_details("FACEBOOK DETAILS", facebook)
    elif choice == "2":
        show_details("GMAIL DETAILS", gmail)
    elif choice == "3":
        break
    else:
        input("ভুল অপশন! Enter চাপো...")
