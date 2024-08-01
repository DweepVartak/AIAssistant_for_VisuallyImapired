import speech_recognition as sr
import time

# Initialize the recognizer
r = sr.Recognizer()

# Set device index (change this to the appropriate index for your microphone)
device_index = 0

def record_text():
    try:
        # Use microphone as input source
        with sr.Microphone(device_index=device_index) as source:
            print("Adjusting for ambient noise...")
            r.adjust_for_ambient_noise(source, duration=1)  # Adjust duration as needed
            print("Listening for input...")
            
            # Set pause threshold for recognizing speech
            r.pause_threshold = 1.0  # Reduced pause threshold
            
            # Reduce timeout to a more reasonable value
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            
            print("Recognizing speech...")
            
            # Using Google to recognize audio
            text = r.recognize_google(audio)
            print("Recognized text:", text)
            return text
        
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        
    except sr.UnknownValueError:
        print("Could not understand audio. Please try again.")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return None  # Return None if recognition fails

def output_text(text):
    try:
        with open("output.txt", "a") as f:
            f.write(text)
            f.write("\n")
        print("Text written to output.txt")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

# Main loop
while True:
    try:
        print("Ready for next input...")
        text = record_text()
        if text:
            output_text(text)
        time.sleep(2)  # Add a 2-second delay between iterations
    except KeyboardInterrupt:
        print("Exiting...")
        break
    except Exception as e:
        print(f"An unexpected error occurred in the main loop: {e}")
