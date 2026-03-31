import time

class ShadowToken:
    def __init__(self):
        # Tracking authorized session telemetry
        self.registry = {
            "admin_jesse": {"last_ip": "108.26.x.x", "loc": "Flint, MI", "ts": time.time()}
        }

    def inspect_access_token(self, user, current_ip, current_loc):
        """
        Detects 'Impossible Travel' and Session Hijacking.
        """
        print(f"[*] Shadow-Token: Auditing access request for {user}...")
        record = self.registry.get(user)
        
        if record:
            # Calculate time since last activity
            elapsed = (time.time() - record['ts']) / 60 # Minutes
            
            # If location changed but time elapsed is too short for travel
            if current_loc != record['loc'] and elapsed < 60:
                print(f"[!!!] HIJACK DETECTED: {user} moved from {record['loc']} to {current_loc} in {elapsed:.1f} mins.")
                print("[!] EMERGENCY: Revoking OAuth Token and freezing account.")
                return "ACCESS_DENIED_REVOKED"
        
        print(f"[+] Access Granted: Identity verified for {current_loc}.")
        return "ACCESS_GRANTED"

if __name__ == "__main__":
    guardian = ShadowToken()
    # Testing a suspicious login attempt (Simulating travel from Flint to London in 0 mins)
    guardian.inspect_access_token("admin_jesse", "192.168.1.50", "London, UK")
