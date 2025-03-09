from djitellopy import Tello
import cv2
import time

# Initialize the drone
drone = Tello()

try:
    # Connect to the drone
    drone.connect()
    print(f"Battery Level: {drone.get_battery()}%")

    # Start video streaming
    drone.streamon()
    time.sleep(2)  # Allow the stream to stabilize

    # Define the crowd detection function
    def detect_crowd(frame):
        # Load pre-trained model and configuration for crowd/person detection (e.g., YOLO, SSD)
        net = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'res10_300x300_ssd_iter_140000.caffemodel')

        # Preprocess the frame for detection
        blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104.0, 177.0, 123.0))
        net.setInput(blob)
        detections = net.forward()

        # Count people in the frame
        person_count = 0
        height, width = frame.shape[:2]
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.5:  # Minimum confidence threshold
                # Extract coordinates of the detection box
                box = detections[0, 0, i, 3:7] * [width, height, width, height]
                (startX, startY, endX, endY) = box.astype("int")

                # Draw the detection box
                cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)

                # Increment person count
                person_count += 1

        # Display the person count on the frame
        cv2.putText(frame, f"Persons Detected: {person_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        return frame, person_count

    # Start drone video stream
    cv2.namedWindow("Drone Camera")
    frame_reader = drone.get_frame_read()

    while True:
        # Get the current frame
        frame = frame_reader.frame
        if frame is None:
            print("Waiting for video frame...")
            time.sleep(0.5)
            continue

        # Detect crowd in the frame
        processed_frame, count = detect_crowd(frame)

        # Display the frame
        cv2.imshow("Drone Camera", processed_frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Safely land the drone and release resources
    try:
        print("Landing the drone...")
        drone.land()
    except Exception as land_error:
        print(f"Failed to land the drone: {land_error}")

    # Stop video streaming
    drone.streamoff()
    cv2.destroyAllWindows()
