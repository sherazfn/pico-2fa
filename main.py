import subprocess
import time

def start_2fa_otp_generator():
    try:
        subprocess.run(["python3", "path/to/2fa-otp-generator.py"])  # Replace with the actual path to your 2fa-otp-generator.py
    except Exception as e:
        print(f"Error starting 2fa-otp-generator: {e}")

if __name__ == "__main__":
    print("Starting Raspberry Pi Pico main program.")

    try:
        while True:
            start_2fa_otp_generator()
            print("Restarting 2fa-otp-generator in 60 seconds...")
            time.sleep(60)  # Adjust the sleep duration as needed
    except KeyboardInterrupt:
        print("Exiting Raspberry Pi Pico main program.")
