import os
import subprocess
from tqdm import tqdm


def run_inference(img_path, output, segment_type="semantic"):
    cmd = f"/root/miniconda3/envs/foodsam/bin/python /workspaces/FoodSAM/FoodSAM/{segment_type}.py --img_path {img_path} --output {output}"
    with open("/workspaces/Datasets/nutrition5k/data/foodsam/std.txt", "a") as fh:
        process = subprocess.Popen(cmd, shell=True, stdout=fh, stderr=fh)
        process.wait()
        return process.returncode


if __name__ == "__main__":
    folder_path = "/workspaces/Datasets/nutrition5k/data/images_130"
    folder_output = "/workspaces/Datasets/nutrition5k/data/foodsam"
    segment_types = ["semantic", "panoptic"]

    for segment_type in segment_types:
        print(f"Segment type: {segment_type}")
        output = os.path.join(folder_output, segment_type)
        for img in tqdm(os.listdir(folder_path)):
            img_path = os.path.join(folder_path, img)

            if os.path.exists(os.path.join(output, img.split(".")[0])):
                continue

            returncode = run_inference(img_path=img_path, output=output, segment_type=segment_type)
            if returncode != 0:
                print(f"Error in {img_path}")
                break
