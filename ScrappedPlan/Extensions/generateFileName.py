from datetime import datetime

def generate_filename(base_filename, start_date, end_date):
    # Parse the dates
    start_dt = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%S%z")
    end_dt = datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%S%z")

    # Format the dates
    start_str = start_dt.strftime("%Y-%m-%d")
    end_str = end_dt.strftime("%Y-%m-%d")

    # Generate the new filename
    new_filename = base_filename.replace("_.csv", f"_{start_str}_{end_str}.csv")
    return new_filename