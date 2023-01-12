import split_gif
import combine_frames

def main():
    print("Welcome to the Animation Tool")
    print("1. Split gif")
    print("2. Combine frames")
    choice = input("Enter your choice: ")

    if choice == "1":
        gif_path = input("Enter the path of the gif file: ")
        output_folder = input("Enter the path of the output folder: ")
        split_gif.split_gif(gif_path, output_folder)
    elif choice == "2":
        input_folder = input("Enter the path of the input folder: ")
        output_folder = input("Enter the path of the output folder: ")
        output_format = input("Enter the desired output format (gif or mp4): ")
        fps_amount = float(input("Enter the desired amount of FPS: "))
        combine_frames.combine_frames(input_folder, output_folder, output_format, fps_amount)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
