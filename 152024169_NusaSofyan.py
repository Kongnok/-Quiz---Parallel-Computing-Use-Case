import concurrent.futures
import time

# Task A: Simulating a data analysis task
def perform_data_analysis():
    print("[Task A] Starting data analysis...")
    time.sleep(2) # Simulating time taken to process data
    print("[Task A] Data analysis completed.")
    return "Analysis Data"

# Task B: Simulating a report generation task
def generate_pdf_report():
    print("[Task B] Starting PDF report generation...")
    time.sleep(3) # Simulating time taken to generate a file
    print("[Task B] PDF report generated.")
    return "Report.pdf"

# Task C: Simulating an I/O task like sending emails
def send_notifications():
    print("[Task C] Sending email notifications to users...")
    time.sleep(1) # Simulating time taken to communicate with a server
    print("[Task C] Notifications sent.")
    return "Emails Sent"

def main():
    start_time = time.time()
    print("--- Starting Task Parallelism Execution ---\n")

    # Using ThreadPoolExecutor to run completely different tasks concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # Submit different functions (tasks) to the executor
        future_a = executor.submit(perform_data_analysis)
        future_b = executor.submit(generate_pdf_report)
        future_c = executor.submit(send_notifications)

        # Retrieve results as they finish
        result_a = future_a.result()
        result_b = future_b.result()
        result_c = future_c.result()

    print("\n--- All Tasks Completed ---")
    print(f"Total execution time: {time.time() - start_time:.2f} seconds")
    
    # If this was strictly sequential, it would take 2 + 3 + 1 = 6 seconds.
    # Because of task parallelism, it should only take roughly as long as the longest task (~3 seconds).

if __name__ == "__main__":
    main()