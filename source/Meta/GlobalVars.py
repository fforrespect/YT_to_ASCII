vars_fp = "../resources/GlobalVars.txt"

var_dict = {}

with open(vars_fp) as vars_file:
    for line in vars_file.readlines():
        if line[0] == "#" or len(line) <= 2:
            continue
        else:
            data = line.replace("\n", "").split(" ")
            print(data)
            if data[0] == "int":
                var_dict[data[1]] = int(data[2])
            elif data[0] == "str":
                var_dict[data[1]] = str(data[2])[1:-1]

video_url = var_dict["video_url"]

video_fp = var_dict["video_fp"]
video_name = var_dict["video_name"]

audio_fp = var_dict["audio_fp"]

frames_fp = var_dict["frames_fp"]
frame_ext = var_dict["frame_ext"]

strings_fp = var_dict["strings_fp"]

delimiter = var_dict["delimiter"]


fps = var_dict["fps"]
skip = var_dict["skip"]
width = var_dict["width"]
