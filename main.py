import split_gif
import combine_frames

def main():
    print("FRAMEMASTER")
    print("1. Split gif")
    print("2. Combine frames")
    choice = input("Enter your choice: ")

    if choice == "1":
        gif_path = input("Enter the file PATH: ")
        output_folder = input("Enter the output PATH: ")
        split_gif.split_gif(gif_path, output_folder)
    elif choice == "2":
        input_folder = input("Enter the input PATH: ")
        output_folder = input("Enter the output PATH: ")
        output_format = input("Enter the format (GIF / MP4): ")
        fps_amount = float(input("Enter the amount of FPS: "))
        combine_frames.combine_frames(input_folder, output_folder, output_format, fps_amount)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
