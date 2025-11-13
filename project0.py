import pyotp
import time

def check_knowledge_factor():
    print("\n--- Step 1: Password Verification ---")
    correct_password = "WTM2025"
    entered_password = input("Enter your password: ")

    if entered_password == correct_password:
        print("Password verified successfully.")
        return True
    else:
        print("Incorrect password.")
        return False


def check_possession_factor():
    print("\n--- Step 2: Authenticator Code Verification ---")
    user_secret_key = "JBSWY3DPEHPK3PXP"
    totp = pyotp.TOTP(user_secret_key)

    print(f"(For demo) Current TOTP: {totp.now()}")
    entered_code = input("Enter the 6-digit code from your Authenticator app: ")

    if totp.verify(entered_code):
        print("TOTP code verified successfully.")
        return True
    else:
        print("Invalid TOTP code.")
        return False


def main():
    print("=== Women Techmakers: Two-Factor Authentication Demo ===")

    if check_knowledge_factor():
        if check_possession_factor():
            print("\nAccess Granted. Welcome.")
        else:
            print("\nAccess Denied: Invalid TOTP code.")
    else:
        print("\nAccess Denied: Invalid password.")


if __name__ == "__main__":
    main()
