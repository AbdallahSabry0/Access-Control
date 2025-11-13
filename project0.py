import pyotp
import time
# FACTOR 1: KNOWLEDGE (Password)
def check_knowledge_factor():
    """Simulates checking the 'Something You Know' factor."""
    print("\n--- FACTOR 1: KNOWLEDGE (Password) ---")
    
    # Predefined correct password
    correct_password = "WTM2025"
    
    # Get password input from the user
    entered_password = input("Enter your password: ")
    11
    # Compare input with the stored password
    if entered_password == correct_password:
        print("✅ Password check successful.")
        return True
    else:
        print("❌ Incorrect password.")
        return False


# FACTOR 2: POSSESSION (TOTP Code)
def check_possession_factor():
    """Simulates checking the 'Something You Have' (TOTP Code) factor."""
    print("\n--- FACTOR 2: POSSESSION (Authenticator Code) ---")

    # Create or use a predefined secret key
    user_secret_key = "JBSWY3DPEHPK3PXP"  # Example secret key
    totp = pyotp.TOTP(user_secret_key)

    # Show current TOTP (for testing/demo purposes)
    print(f"(For demo) Current TOTP: {totp.now()}")

    # Get user input for the TOTP code
    entered_code = input("Enter the 6-digit code from your Authenticator app: ")

    # Validate user’s TOTP
    if totp.verify(entered_code):
        print("✅ TOTP Code check successful.")
        return True
    else:
        print("❌ TOTP Code incorrect.")
        return False


# MAIN PROGRAM FLOW
def main():
    print("=== Women Techmakers: Two-Factor Authentication Demo ===")
    
    # Step 1: Check the first factor (Knowledge)
    password_ok = check_knowledge_factor()
    
    # Step 2: Proceed to possession factor only if first passes
    if password_ok:
        possession_ok = check_possession_factor()
        if possession_ok:
            print("\n🎉 Access Granted! Welcome!")
        else:
            print("\n🚫 Access Denied: Invalid TOTP Code.")
    else:
        print("\n🚫 Access Denied: Invalid Password.")


# Run the program
if __name__ == "__main__":
    main()
