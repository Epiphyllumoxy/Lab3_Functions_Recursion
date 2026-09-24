import random
import functools

# =====================================================================
# STUDENT INPUTS (Configure these)
# =====================================================================
LAST_NAME = "CULATA"
SEED_NUM = 8
FAVORITE_ARTIST = "ARIANA GRANDE" 

# =====================================================================
# REQUIREMENT 4: DECORATOR DEFINITION
# =====================================================================
def diagnostic_logger(func):
    """Decorator to record execution details in the Execution Log."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f" - [Execution Log] Starting system diagnostic via '{func.__name__}'...")
        result = func(*args, **kwargs)
        print(f" - [Execution Log] '{func.__name__}' completed processing successfully.")
        return result
    return wrapper

# =====================================================================
# REQUIREMENT 1: STUDENT-SPECIFIC DATA GENERATION
# =====================================================================
def generate_equipment_readings(last_name, seed, artist):
    """Generates deterministic pseudo-random equipment readings."""
    # Seed based on combination of inputs
    combined_seed = seed + sum(ord(c) for c in last_name) + sum(ord(c) for c in artist)
    random.seed(combined_seed)
    
    # Mix of valid integers, floats, and intentional invalid string payloads
    raw_pool = []
    for _ in range(8):
        raw_pool.append(str(round(random.uniform(10.0, 150.0), 2)))
    raw_pool.extend(["ERR_OVERHEAT", "null", "999.99", "-45.2"]) # Invalid tokens
    random.shuffle(raw_pool)
    return raw_pool

# =====================================================================
# REQUIREMENT 2 & 3: REUSABLE FUNCTIONS & EXCEPTION HANDLING
# =====================================================================
def validate_reading(reading_str):
    """Validates the input string token and returns a clean float if sound."""
    # Strict boundary checks
    val = float(reading_str)
    if val < 0 or val > 500:
        raise ValueError(f"Value {val} out of hardware threshold constraints (0-500)")
    return val

def classify_condition(value):
    """Classifies equipment condition based on numeric metrics."""
    if value < 40.0:
        return "OPTIMAL / LOW LOAD"
    elif 40.0 <= value <= 110.0:
        return "NORMAL OPERATING RANGE"
    else:
        return "CRITICAL WARNING / HIGH LOAD"

@diagnostic_logger
def run_diagnostic_system(raw_data):
    """Processes, filters, and reports diagnostic findings."""
    valid_results = {}
    validation_summary = {"Valid": 0, "Invalid": 0}
    
    print("\n--- Diagnostic Processing Activity ---")
    for raw_item in raw_data:
        try:
            # Attempt validation
            clean_val = validate_reading(raw_item)
            condition = classify_condition(clean_val)
            valid_results[raw_item] = {"Value": clean_val, "Condition": condition}
            validation_summary["Valid"] += 1
            print(f"Token '{raw_item}': VALID -> {condition}")
        except (ValueError, TypeError) as error:
            # Handle anomalous signals without crashing
            validation_summary["Invalid"] += 1
            print(f"Token '{raw_item}': INVALID -> Reason: {error}")
            
    return valid_results, validation_summary

# =====================================================================
# REQUIREMENT 5: MAIN EXECUTION AND SUMMARY DISPLAY
# =====================================================================
def main():
    raw_readings = generate_equipment_readings(LAST_NAME, SEED_NUM, FAVORITE_ARTIST)
    
    # Run the decorated logic
    diagnostic_data, summary_counts = run_diagnostic_system(raw_readings)
    
    # Formatted Printout matching the assessment blocks on Page 14
    print("\n" + "="*60)
    print("                 ASSESSMENT DATA SUMMARY")
    print("="*60)
    print(f"\n[Generated Equipment Data]:\n{raw_readings}")
    
    print(f"\n[Validation Results]:\n{summary_counts}")
    
    print("\n[Diagnostic Results]:")
    for token, details in diagnostic_data.items():
        print(f"  * Reading: {details['Value']:<7} | Condition: {details['Condition']}")
        
    print("\n[Final Output]:")
    if diagnostic_data:
        avg_load = sum(d['Value'] for d in diagnostic_data.values()) / len(diagnostic_data)
        print(f"System Check Complete. Overall Core Average Load Metric: {avg_load:.2f}")
    print("="*60)

if __name__ == "__main__":
    main()
