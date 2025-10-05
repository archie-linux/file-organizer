import os
import random

TEST_DIR = os.path.expanduser("test_dir")
os.makedirs(TEST_DIR, exist_ok=True)

# File extensions based on categories
extensions = [".jpg", ".png", ".txt", ".pdf", ".mp4", ".zip", ".mp3", ".exe", ".docx"]

# Generate random files
for i in range(50):
    ext = random.choice(extensions)
    file_path = os.path.join(TEST_DIR, f"file_{i}{ext}")
    with open(file_path, "w") as f:
        f.write("Sample data")

print(f"✅ Test directory created at {TEST_DIR}")

