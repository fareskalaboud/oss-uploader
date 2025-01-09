import os
import oss2
from tqdm import tqdm

# Configure your OSS credentials
ACCESS_KEY_ID = 'your-access-key-id'
ACCESS_KEY_SECRET = 'your-access-key-secret'
ENDPOINT = 'example.aliyuncs.com'
BUCKET_NAME = 'my-bucket-name'

# Initialize the OSS bucket
auth = oss2.Auth(ACCESS_KEY_ID, ACCESS_KEY_SECRET)
bucket = oss2.Bucket(auth, ENDPOINT, BUCKET_NAME)

def scan_directory(base_dir):
    """Recursively scans a directory and returns a list of file paths and directories."""
    file_list = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    return file_list

def upload_to_oss(local_base_dir, bucket_base_dir, file_list):
    """Uploads files to Alibaba Cloud OSS, maintaining the folder structure."""
    progress_bar = tqdm(total=len(file_list), desc="Uploading files", unit="file")
    
    for local_file in file_list:
        # Determine the relative path for maintaining the folder structure
        relative_path = os.path.relpath(local_file, local_base_dir)
        oss_path = os.path.join(bucket_base_dir, relative_path).replace('\\', '/')  # Use OSS-friendly paths
        
        try:
            bucket.put_object_from_file(oss_path, local_file)
            progress_bar.set_postfix({"status": "Success", "file": relative_path})
        except Exception as e:
            progress_bar.set_postfix({"status": "Failed", "file": relative_path, "error": str(e)})
        finally:
            progress_bar.update(1)
    
    progress_bar.close()

if __name__ == "__main__":
    # Specify the local directory to copy and the target bucket base directory
    local_directory = os.getcwd()
    bucket_base_directory = "files"

    # Scan the local directory to get all file paths
    print("Scanning directory...")
    all_files = scan_directory(local_directory)
    total_files = len(all_files)
    print(f"Total files found: {total_files}")

    # Upload files to OSS
    upload_to_oss(local_directory, bucket_base_directory, all_files)
    print("Upload completed.")
