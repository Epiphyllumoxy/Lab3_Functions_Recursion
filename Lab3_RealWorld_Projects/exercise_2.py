import random

# =====================================================================
# STUDENT INPUTS
# =====================================================================
LAST_NAME = "CULATA"
SEED_NUM = 8               
FAVORITE_ARTIST = "ARIANA GRANDE"

# =====================================================================
# DATA GENERATION
# =====================================================================
def generate_fault_code(last_name, seed, artist):
    """Generates a unique deterministic numeric fault code sequence."""
    combined_seed = seed + sum(ord(c) for c in last_name) + sum(ord(c) for c in artist)
    random.seed(combined_seed)
    # Generate a unique fault threshold integer between 3 and 7
    return random.randint(3, 7)

# =====================================================================
# RECURSIVE FAULT TRACE ENGINE
# =====================================================================
def trace_fault(current_depth, termination_target, trace_history=None, logs=None):
    """
    Recursively descends system architecture levels until it strikes 
    the termination base condition target code.
    """
    if trace_history is None:
        trace_history = []
    if logs is None:
        logs = []

    # Record the diagnostic checkpoint step
    current_code = (current_depth * 13) % 101  # Synthesize a layer status identifier code
    trace_history.append(f"Layer_{current_depth}(Code:{current_code})")
    logs.append(f"Analyzing systemic boundaries at Node Level {current_depth}... Integrity Check: FAULT FOUND.")

    # REQUIREMENT 3: DEFINE AND APPLY AN APPROPRIATE BASE CONDITION
    if current_depth >= termination_target:
        logs.append(f"Termination target condition reached at Level {current_depth}. Discovered root isolation vector.")
        return current_depth, trace_history, logs

    # REQUIREMENT 2: RECURSIVE CALL SEQUENCE
    return trace_fault(current_depth + 1, termination_target, trace_history, logs)


# =====================================================================
# MAIN RUNTIME EXECUTION
# =====================================================================
def main():
    # 1. Generate unique targeting metrics
    target_fault_depth = generate_fault_code(LAST_NAME, SEED_NUM, FAVORITE_ARTIST)
    
    # 2. Execute the recursive tracer starting at root index depth 1
    total_calls, trace_path, execution_logs = trace_fault(current_depth=1, termination_target=target_fault_depth)
    
    # =====================================================================
    # DISPLAY ASSESSMENT DATA (Matches Page 14 Requirements Exactly)
    # =====================================================================
    print("\n" + "="*60)
    print("             EXERCISE 2: RECURSIVE FAULT TRACE REPORT")
    print("="*60)
    
    print(f"\n[Generated Fault Data]:")
    print(f" Target Termination Depth Identity : Level {target_fault_depth}")
    
    print(f"\n[Recursive Trace]:")
    print(" -> ".join(trace_path))
    
    # REQUIREMENT 4: COUNT THE RECURSIVE CALLS PERFORMED
    print(f"\n[Number of Recursive Calls]:")
    print(f" Total Depth Traversed / Active Call Cycles: {total_calls}")
    
    print(f"\n[Execution Log]:")
    for log in execution_logs:
        print(f"  - {log}")
        
    # REQUIREMENT 5: DISPLAY THE COMPLETE FAULT TRACE AND FINAL RESULT
    print(f"\n[Final Output]:")
    print(f" Status: SUCCESS | System isolated safely at core containment Level {total_calls}.")
    print("="*60)

if __name__ == "__main__":
    main()
