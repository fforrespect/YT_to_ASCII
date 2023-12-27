import cv2


def download(from_path, to_path):
    # file = [x for x in os.listdir(from_path) if x[-1] == "4"][0]
    file = from_path

    vid_cap = cv2.VideoCapture(file)
    success, image = vid_cap.read()

    frame = 0

    while success:
        cv2.imwrite(f"{to_path}frame%d.jpg" % frame, image)
        success, image = vid_cap.read()
        frame += 1

    print("All frames created")
