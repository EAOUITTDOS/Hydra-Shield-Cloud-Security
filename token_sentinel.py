import time

class TokenSentinel:
    def __init__(self):
        self.active_sessions = {
            "user_jesse": {"ip": "108.26.x.x", "location": "Flint, MI", "last_seen": time.time()}
        }

    def validate_session(self, user_id, current_ip, current_location):
        print(f"[*] Token-Sentinel: Validating session for {user_id}...")
        session = self.active_sessions.get(user_id)
        
        if not session:
            return "NEW_SESSION"

        # Logic for "Impossible Travel" detection
        if current_location != session['location']:
            time_diff = (time.time() - session['last_seen']) / 60 # minutes
            if time_diff < 30: # If they "moved" locations in under 30 mins
                print(f"[!!!] HIJACK ALERT: Impossible Travel detected for {user_id}!")
                print(f"[!] Original: {session['location']} | New: {current_location}")
                return "REVOKE_TOKEN"

        print("[+] Session validated. User behavior consistent.")
        return "AUTHORIZED"

if __name__ == "__main__":
    sentinel = TokenSentinel()
    # Mocking a hijack attempt from a different location
    status = sentinel.validate_session("user_jesse", "192.168.1.1", "Unknown_Location")
    if status == "REVOKE_TOKEN":
        print("[!] SECURITY ACTION: Token blacklisted and session terminated.")
