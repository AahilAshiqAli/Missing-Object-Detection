import cv2
import numpy as np

def detect_objects(image_name, desired_class=None, confidence_threshold=0.2, nms_threshold=0.4):
    net = cv2.dnn.readNet("Detection/far/yolov4-tiny.weights", "Detection/far/yolov4-tiny.cfg")
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    image_path = "Detection/far/" + image_name
    image = cv2.imread(image_path)
    blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    net.setInput(blob)
    outs = net.forward(output_layers)
    class_labels = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat", "traffic light",
                    "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow",
                    "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee",
                    "skis", "snowboard", "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard",
                    "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple",
                    "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa",
                    "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard",
                    "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase",
                    "scissors", "teddy bear", "hair drier", "toothbrush"]

    # Process detections
    boxes = []
    confidences = []
    class_ids = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > confidence_threshold:
                center_x = int(detection[0] * image.shape[1])
                center_y = int(detection[1] * image.shape[0])
                w = int(detection[2] * image.shape[1])
                h = int(detection[3] * image.shape[0])
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indices = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, nms_threshold)

    detections = []
    if len(indices) > 0:
        for i in indices.flatten():
            x, y, w, h = boxes[i]
            class_label = class_labels[class_ids[i]]
            if desired_class is None or class_label == desired_class:
                confidence = confidences[i]
                detections.append((class_ids[i], confidence, (x, y, w, h)))

                cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                label = f"{class_label}: {confidence:.2f}"
                cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    save_path = "static/" + image_name
    try:
        cv2.imwrite(save_path, image)
        print(f"Image saved successfully at: {save_path}")
    except Exception as e:
        print(f"Error saving image: {e}")

    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    label11 = []
    # Print the detected objects
    for idx, (class_id, confidence, bbox) in enumerate(detections, start=1):
        class_label = class_labels[class_id]
        label11.append(class_label)
        print(f"Object {idx}: {class_label} (confidence: {confidence:.2f})")

    return label11, save_path

# Example usage:
# detect_objects("example.jpg", desired_class="keys")
