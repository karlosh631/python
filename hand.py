import subprocess

def scan_wifi_networks():
    """Scan for available Wi-Fi networks using PowerShell."""
    try:
        # Use PowerShell to list available Wi-Fi networks
        command = "netsh wlan show networks"
        result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
        if result.returncode == 0:
            print("Available Wi-Fi Networks:")
            print(result.stdout)
            return result.stdout
        else:
            print("Failed to scan Wi-Fi networks.")
            return None
    except Exception as e:
        print(f"Error scanning Wi-Fi networks: {e}")
        return None

def connect_to_wifi(ssid, password):
    """Connect to a WPA2-secured Wi-Fi network using PowerShell."""
    try:
        # Create an XML profile for the Wi-Fi network
        profile_name = f"{ssid}_profile"
        xml_profile = f"""
        <?xml version="1.0"?>
        <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
            <name>{profile_name}</name>
            <SSIDConfig>
                <SSID>
                    <name>{ssid}</name>
                </SSID>
            </SSIDConfig>
            <connectionType>ESS</connectionType>
            <connectionMode>auto</connectionMode>
            <MSM>
                <security>
                    <authEncryption>
                        <authentication>WPA2PSK</authentication>
                        <encryption>AES</encryption>
                        <useOneX>false</useOneX>
                    </authEncryption>
                    <sharedKey>
                        <keyType>passPhrase</keyType>
                        <protected>false</protected>
                        <keyMaterial>{password}</keyMaterial>
                    </sharedKey>
                </security>
            </MSM>
        </WLANProfile>
        """

        # Save the XML profile to a temporary file
        with open("wifi_profile.xml", "w") as f:
            f.write(xml_profile)
