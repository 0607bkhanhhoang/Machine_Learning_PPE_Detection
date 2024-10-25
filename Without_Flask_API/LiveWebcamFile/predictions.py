import os
from ultralytics import YOLO

# Initialize YOLO with the Model Name
model = YOLO("best.pt")

try:
    # Perform segmentation and get results
    results = model.predict(source="0", show=True, conf=0.15)

    # Initialize a variable to store the number of PPE_Hat detections
    ppe_hat_count = 0

    # Loop over each result to extract relevant information
    for result in results:
        # Loop over each detected object in the result
        for cls, box in zip(result.boxes.cls, result.boxes):
            # Assuming 'PPE_Hat' is the label for hats, check the class label
            if result.names[int(cls)] == ' PPE_Insurance vest':
                ppe_hat_count += 1
                print(ppe_hat_count)

    # Print the total number of PPE_Hat detected
    print("Total PPE_Hat detected: ", ppe_hat_count)

except Exception as e:
    print(f"An error occurred: {e}")
