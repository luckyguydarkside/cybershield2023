import os
import hashlib
import time

# Function to compute the hash of a file
def hash_file(filepath):
    """Generate SHA256 hash of the given file."""
    hash_sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        # Read file in chunks to avoid memory overload
        for byte_block in iter(lambda: f.read(4096), b""):
            hash_sha256.update(byte_block)
    return hash_sha256.hexdigest()

# Function to monitor changes in files
def monitor_directory(directory):
    """Monitor a directory for changes in file hashes."""
    file_hashes = {}
    while True:
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                current_hash = hash_file(filepath)
                if filename in file_hashes:
                    if file_hashes[filename] != current_hash:
                        print(f"File changed: {filename}")
                file_hashes[filename] = current_hash
        time.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
    # Specify the directory to monitor
    directory_to_monitor = '/path/to/directory'
    print(f"Monitoring changes in: {directory_to_monitor}")
    monitor_directory(directory_to_monitor)