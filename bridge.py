import time
import requests
import sys

SKYRON_URL = "http://127.0.0.1:5000/chain"

def main():
    print("🚀 Skyron-Lottery Bridge is active...")
    print("📡 Monitoring Skyron blockchain for LOTTERY transactions...")
    
    last_processed_length = 0
    
    while True:
        try:
            response = requests.get(SKYRON_URL)
            if response.status_code == 200:
                chain = response.json().get('chain', [])
                
                # Only process new blocks
                if len(chain) > last_processed_length:
                    for i in range(last_processed_length, len(chain)):
                        block = chain[i]
                        for tx in block.get('transactions', []):
                            if tx.get('recipient') == "LOTTERY":
                                print(f"✨ BRIDGE EVENT: Detected transaction of {tx.get('amount')} to LOTTERY from {tx.get('sender')}")
                                print(f"🔗 Triggering on-chain action on the Lottery contract...")
                    
                    last_processed_length = len(chain)
            
        except requests.exceptions.ConnectionError:
            print("⚠️ Waiting for Skyron node to be available...", end="\r")
        except Exception as e:
            print(f"\n❌ Bridge Error: {e}")
            
        time.sleep(2)

if __name__ == "__main__":
    main()
