import random
import functools

# =====================================================================
# STUDENT INPUTS
# =====================================================================
LAST_NAME = "CULATA"
SEED_NUM = 8               # Replace with the last digit of your ID
FAVORITE_ARTIST = "ARIANA GRANDE"

# =====================================================================
# REQUIREMENT 5: DECORATOR DEFINITION
# =====================================================================
def pipeline_monitor(func):
    """Decorator to monitor and log performance of the processing pipeline."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f" -> [Execution Log] Pipeline initializing execution context for block: '{func.__name__}'")
        result = func(*args, **kwargs)
        print(f" -> [Execution Log] Block '{func.__name__}' successfully yielded control back.")
        return result
    return wrapper

# =====================================================================
# REQUIREMENT 3: GENERATOR FUNCTION
# =====================================================================
def stream_telemetry_data(last_name, seed, artist):
    """Generates and streams data chunks simulating infinite live tracking telemetry."""
    combined_seed = seed + sum(ord(c) for c in last_name) + sum(ord(c) for c in artist)
    random.seed(combined_seed)
    
    # Simulating a dynamic real-time stream of 12 incoming packets
    for i in range(12):
        if random.random() < 0.15:
            yield "MALFORMED_PACKET" # Intentional invalid entry
        else:
            yield round(random.uniform(50.0, 200.0), 2)

# =====================================================================
# REQUIREMENT 7: RECURSIVE ERROR ISOLATION
# =====================================================================
def isolate_abnormal_anomaly(reading_value, risk_threshold=160.0):
    """Recursively traces back deep system metrics when an anomaly is triggered."""
    if reading_value <= risk_threshold:
        return f"Stabilized at safety zone index {reading_value}"
    
    # Shift baseline metrics recursively to find lower bounds
    new_metric = round(reading_value - 15.5, 2)
    return isolate_abnormal_anomaly(new_metric, risk_threshold)

# =====================================================================
# REQUIREMENT 2 & 6: PIPELINE MODULES AND EXCEPTION HANDLING
# =====================================================================
@pipeline_monitor
def process_telemetry_pipeline(telemetry_generator):
    """Consumes streamed generator records and filters them through lambda limits."""
    # REQUIREMENT 4: LAMBDA EXPRESSION FOR TRANSFORM/FILTERING
    # Converts readings from Celsius to Fahrenheit, filters out entries below 120F
    c_to_f = lambda c: round((c * 9/5) + 32, 2)
    
    processed_records = []
    valid_count = 0
    invalid_count = 0
    anomalies_detected = 0
    execution_log = []
    
    for raw_reading in telemetry_generator:
        try:
            # Check for non-numeric data structures explicitly
            if isinstance(raw_reading, str):
                raise ValueError("Anomalous textual payload token encountered")
                
            # Perform clean functional lambda conversion
            fahrenheit_val = c_to_f(raw_reading)
            valid_count += 1
            
            # Identify abnormal operational conditions (> 300°F)
            if fahrenheit_val > 300.0:
                anomalies_detected += 1
                recursive_trace = isolate_abnormal_anomaly(fahrenheit_val, risk_threshold=300.0)
                execution_log.append(f"ALERT: Abnormality detected ({fahrenheit_val}°F) -> {recursive_trace}")
                status = "ABNORMAL"
            else:
                status = "VALID"
                
            processed_records.append({"Raw": raw_reading, "Transformed": fahrenheit_val, "Status": status})
            
        except ValueError as e:
            invalid_count += 1
            execution_log.append(f"ERROR: Dropped bad payload entry string. Reason: {e}")
            
    summary_metrics = {
        "Valid Count": valid_count,
        "Invalid Count": invalid_count,
        "Anomalies Found": anomalies_detected
    }
    
    return processed_records, summary_metrics, execution_log

# =====================================================================
# MAIN DESCRIPTOR RUNTIME
# =====================================================================
def main():
    # Instantiate the data stream generator
    telemetry_stream = stream_telemetry_data(LAST_NAME, SEED_NUM, FAVORITE_ARTIST)
    
    # Process pipeline architecture
    results, metrics, logs = process_telemetry_pipeline(telemetry_stream)
    
    # =====================================================================
    # DISPLAY ASSESSMENT DATA (Matches Page 15-16 Layout Exactly)
    # =====================================================================
    print("\n" + "="*70)
    print("             EXERCISE 3: INTELLIGENT MONITORING PIPELINE REPORT")
    print("="*70)
    
    print("\n[Student-Specific Inputs]:")
    print(f" Name: {LAST_NAME} | Seed: {SEED_NUM} | Target Artist: {FAVORITE_ARTIST}")
    
    print("\n[Generated Telemetry Data Stream Chunks]:")
    print(" Active Generator Streaming Session initialized successfully.")
    
    print("\n[Processed Results Table]:")
    for idx, item in enumerate(results):
        print(f"  Item #{idx+1:02d} | Input Metric: {item['Raw']:<6} °C -> Fahrenheit Core: {item['Transformed']:<6} °F [{item['Status']}]")
        
    print("\n[Recursive Analysis Diagnostics]:")
    print(f" Total Anomaly Intercepts Executed: {metrics['Anomalies Found']}")
    
    print("\n[Execution Log Trackers]:")
    for log_line in logs:
        print(f"  * {log_line}")
        
    print("\n[Final Diagnostic Summary Output]:")
    print(f" Total Stream Packets Scanned : {metrics['Valid Count'] + metrics['Invalid Count']}")
    print(f" Clean System Logs Parsed     : {metrics['Valid Count']}")
    print(f" Anomalous Drops Isolated     : {metrics['Invalid Count']}")
    print(f" System Health Assessment      : COMPLETE.")
    print("="*70)

if __name__ == "__main__":
    main()
