import json

def calculate_savings():
    print("--- AI Clipper Cost Calculator (2025) ---")
    
    # Load the data
    try:
        with open('data/tools.json', 'r') as f:
            tools = json.load(f)
    except FileNotFoundError:
        print("Error: data/tools.json not found.")
        return

    # User input simulation
    hours_needed = 10 
    print(f"\nScenario: You need to process {hours_needed} hours of video per month.\n")

    print(f"{'Tool':<15} | {'Cost':<10} | {'Status'}")
    print("-" * 40)

    for tool in tools:
        cost = 0
        status = "Expensive"
        
        # Simple logic to determine cost effectiveness
        if tool['price_monthly'] == 0 and "90 Hours" in tool['free_tier']:
            cost = 0
            status = "✅ BEST VALUE"
        else:
            # Assuming standard overage costs if not free
            cost = tool['price_monthly']
            status = "❌ Paid Only"

        print(f"{tool['name']:<15} | ${cost:<9} | {status}")

    print("\nRecommendation: Switch to the free tier tools to save ~$360/year.")

if __name__ == "__main__":
    calculate_savings()
