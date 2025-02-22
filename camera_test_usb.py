import cv2

print("Starting camera test...")

# Use /dev/video0 (your main camera node)
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

print("Camera opened successfully.")

# Set MJPG format for better compatibility
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)  # Set to 30 FPS

# Verify camera properties
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cap.get(cv2.CAP_PROP_FOURCC)
fourcc_str = "".join([chr((int(fourcc) >> 8 * i) & 0xFF) for i in range(4)])

print(f"Camera properties set: width={width}, height={height}, fps={fps}, fourcc={fourcc_str}")

# Create a named window
cv2.namedWindow('USB Camera', cv2.WINDOW_NORMAL)

# Resize the window
cv2.resizeWindow('USB Camera', 1280, 960)  # Set the desired window size

print("Starting capture loop...")

while True:
    ret, frame = cap.read()
    print(f"Frame capture status: {ret}")
    if not ret:
        print("Failed to grab frame")
        break

    # Rotate the frame 180 degrees
    frame = cv2.rotate(frame, cv2.ROTATE_180)

    cv2.imshow('USB Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Check if the window is closed
    if cv2.getWindowProperty('USB Camera', cv2.WND_PROP_VISIBLE) < 1:
        break

print("Releasing camera and closing windows.")
cap.release()
cv2.destroyAllWindows()
print("Done.")