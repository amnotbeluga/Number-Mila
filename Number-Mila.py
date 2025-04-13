import os
import json
import requests

CONFIG_FILE = "config.json"

# --- Load or Save Config ---
def load_or_create_config():
    # Check if the config file exists
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
        return config  # Return loaded config without print statements here
    else:
        print("⚠️ Config file not found. Please enter your API keys:")
        config = {
            "NUMVERIFY_API_KEY": input("Numverify API Key: ").strip(),
            "OPENCAGE_API_KEY": input("OpenCage API Key: ").strip()
        }
        # Save the configuration to the file
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f)
        return config

# --- Phone Number Lookup ---
def lookup_phone_number(number, config):
    numverify_url = f"https://apilayer.net/api/validate?access_key={config['NUMVERIFY_API_KEY']}&number={number}"
    opencage_url = f"https://api.opencagedata.com/geocode/v1/json?q={number}&key={config['OPENCAGE_API_KEY']}"
    
    # Perform the Numverify lookup
    try:
        numverify_response = requests.get(numverify_url)
        numverify_data = numverify_response.json()
        if numverify_data.get("valid"):
            print(f"Valid Number: {number}")
            print(f"Country: {numverify_data.get('country_name')}")
            print(f"Location: {numverify_data.get('location')}")
            # Extract latitude and longitude from Numverify if available
            lat = numverify_data.get("latitude")
            lng = numverify_data.get("longitude")
            print(f"Latitude (from Numverify): {lat}")
            print(f"Longitude (from Numverify): {lng}")
        else:
            print(f"Invalid phone number: {number}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Numverify: {e}")

    # Perform the OpenCage lookup (example using the phone number as query)
    try:
        opencage_response = requests.get(opencage_url)
        opencage_data = opencage_response.json()
        if opencage_data['results']:
            print(f"Latitude (from OpenCage): {opencage_data['results'][0]['geometry']['lat']}")
            print(f"Longitude (from OpenCage): {opencage_data['results'][0]['geometry']['lng']}")
            print(f"Formatted Address: {opencage_data['results'][0]['formatted']}")
        else:
            # If no location data is found, fall back to Numverify lat/lng
            print("No location data found for this number from OpenCage.")
            if lat and lng:
                print(f"Using fallback location (from Numverify):")
                print(f"Latitude: {lat}")
                print(f"Longitude: {lng}")
            else:
                print("No location data available.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from OpenCage: {e}")

# --- Main Program ---
def main():
    # Load or create the config file with API keys
    config = load_or_create_config()
    
    # Print success message once after config is loaded or created
    print("🔑 API keys loaded successfully.")
    
    print("🔍 Please enter a phone number for lookup:")

    # Loop to continuously ask for a phone number
    while True:
        number = input("Enter phone number (or type 'exit' to quit): ").strip()
        
        if number.lower() == 'exit':
            print("Exiting the program...")
            break
        elif number:  # Check if the user input is not empty
            lookup_phone_number(number, config)
        else:
            print("⚠️ Please enter a valid phone number.")

    print("Thank you for using the Phone Number Lookup Bot!")

# --- Run the Program ---
if __name__ == "__main__":
    main()

