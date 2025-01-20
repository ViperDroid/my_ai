import gzip
import shutil

# Path to the .gz file (use raw string or forward slashes)
gz_file = r"G:\template websites\myAi\kddcup.data.gz"  # Raw string
# OR
# gz_file = "G:/template websites/myAi/kddcup.data.gz"  # Forward slashes

# Path to the output file (use raw string or forward slashes)
output_file = r"G:\template websites\myAi\kddcup.data"  # Raw string
# OR
# output_file = "G:/template websites/myAi/kddcup.data"  # Forward slashes

# Extract the .gz file
try:
    with gzip.open(gz_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    print(f"Extracted {gz_file} to {output_file}")
except Exception as e:
    print(f"Error extracting {gz_file}: {e}")