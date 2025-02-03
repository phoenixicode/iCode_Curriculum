import os
import pyautogui
import time
from tkinter import Tk, Label, Entry, Button, Text, END
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Disable PyAutoGUI fail-safe feature (not recommended)
pyautogui.FAILSAFE = False  # WARNING: Disabling this feature can lead to unintended actions.

# Google Drive API Setup
def get_drive_service():
    SCOPES = ['https://www.googleapis.com/auth/drive']
    SERVICE_ACCOUNT_FILE = credentials_path_entry.get()
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    return build('drive', 'v3', credentials=credentials)

# Google Slides API Setup
def get_slides_service():
    SCOPES = ['https://www.googleapis.com/auth/presentations']
    SERVICE_ACCOUNT_FILE = credentials_path_entry.get()
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    return build('slides', 'v1', credentials=credentials)

def create_presentation(slides_service, title="Image Presentation"):
    presentation = slides_service.presentations().create(body={"title": title}).execute()
    return presentation['presentationId']

def upload_image_to_drive(drive_service, image_path):
    file_metadata = {'name': os.path.basename(image_path), 'mimeType': 'image/png'}
    media = MediaFileUpload(image_path, mimetype='image/png')
    uploaded_file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    drive_service.permissions().create(
        fileId=uploaded_file['id'],
        body={'type': 'anyone', 'role': 'writer'}
    ).execute()
    return f"https://drive.google.com/uc?id={uploaded_file['id']}"

def add_image_to_slide(slides_service, presentation_id, image_url, slide_index):
    width = 720
    height = 406.56
    presentation = slides_service.presentations().get(presentationId=presentation_id).execute()
    slides = presentation.get('slides')

    while len(slides) < slide_index:
        slide_id = f"slide_{len(slides) + 1}"
        slides_service.presentations().batchUpdate(
            presentationId=presentation_id,
            body={'requests': [{
                'createSlide': {
                    'objectId': slide_id,
                    'slideLayoutReference': {'predefinedLayout': 'BLANK'}
                }
            }]}
        ).execute()
        slides = slides_service.presentations().get(presentationId=presentation_id).execute().get('slides')

    slide_id = slides[slide_index - 1]['objectId']
    requests = [{
        'createImage': {
            'url': image_url,
            'elementProperties': {
                'pageObjectId': slide_id,
                'size': {
                    'width': {'magnitude': width, 'unit': 'PT'},
                    'height': {'magnitude': height, 'unit': 'PT'}
                }
            }
        }
    }]
    slides_service.presentations().batchUpdate(
        presentationId=presentation_id, body={'requests': requests}
    ).execute()

def autoss(o_f, region, buttonCord, delay, pages, progress_callback):
    
    os.makedirs(o_f, exist_ok=True)
    time.sleep(5)
    for i in range(1, pages + 1):
        os.system('osascript -e \'tell application "Google Chrome" to activate\'')
        screenshot = pyautogui.screenshot(region=region)
        screenshot_path = os.path.join(o_f, f"page_{i}.png")
        screenshot.save(screenshot_path)
        progress_callback(i, pages)  # Update progress
        print(f"Captured page {i}: {screenshot_path}")
        time.sleep(1)  # Added delay before clicking
        pyautogui.click(buttonCord)
        time.sleep(delay)

def update_progress(current, total):
    status_text.delete(1.0, END)  # Clear previous text
    status_text.insert(END, f"Progress: {current}/{total} pages captured.\n")

def start_process():
    try:
        output_folder = output_folder_entry.get()
        region = (int(region_x_entry.get()), int(region_y_entry.get()), int(region_width_entry.get()), int(region_height_entry.get()))
        button_coord = (int(button_x_entry.get()), int(button_y_entry.get()))
        pages = int(pages_entry.get())

        # Bring the Google window to the front using osascript
        os.system('osascript -e \'tell application "Google Chrome" to activate\'')  # Activate the Google window
        time.sleep(1)  # Wait for the window to be ready

        # Take screenshots
        autoss(output_folder, region, button_coord, 10, pages, update_progress)

        # Upload images to Google Slides
        images_folder = output_folder
        slides_service = get_slides_service()
        drive_service = get_drive_service()
        presentation_id = create_presentation(slides_service)

        for image_file in sorted(os.listdir(images_folder)):
            if image_file.endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(images_folder, image_file)
                if image_file.startswith('page_'):
                    page_number = int(image_file.split('_')[1].split('.')[0])
                    image_url = upload_image_to_drive(drive_service, image_path)
                    status_text.insert(END, f"Uploading image {page_number}/{pages}...\n")  # Show upload progress
                    add_image_to_slide(slides_service, presentation_id, image_url, page_number)

        drive_service.permissions().create(
            fileId=presentation_id,
            body={'type': 'anyone', 'role': 'writer'}
        ).execute()

        status_text.insert(END, f"All images uploaded to presentation: https://docs.google.com/presentation/d/{presentation_id}\n Copy and paste this link in browser")
    
    except Exception as e:
        status_text.insert(END, f"Error: {str(e)}\n")  # Display error message

# Create the main window
root = Tk()
root.title("Mayank Koli's PPT Maker")

# Input fields with default values
Label(root, text="Output Folder:").grid(row=0, column=0)
output_folder_entry = Entry(root)
output_folder_entry.insert(0, "/Users/gadgetzone/Pictures/Output")  # Default value
output_folder_entry.grid(row=0, column=1)

Label(root, text="Region X:").grid(row=1, column=0)
region_x_entry = Entry(root)
region_x_entry.insert(0, "293")  # Default value
region_x_entry.grid(row=1, column=1)

Label(root, text="Region Y:").grid(row=2, column=0)
region_y_entry = Entry(root)
region_y_entry.insert(0, "180")  # Default value
region_y_entry.grid(row=2, column=1)

Label(root, text="Region Width:").grid(row=3, column=0)
region_width_entry = Entry(root)
region_width_entry.insert(0, "1331")  # Default value
region_width_entry.grid(row=3, column=1)

Label(root, text="Region Height:").grid(row=4, column=0)
region_height_entry = Entry(root)
region_height_entry.insert(0, "747")  # Default value
region_height_entry.grid(row=4, column=1)

Label(root, text="Button X:").grid(row=5, column=0)
button_x_entry = Entry(root)
button_x_entry.insert(0, "1882")  # Default value
button_x_entry.grid(row=5, column=1)

Label(root, text="Button Y:").grid(row=6, column=0)
button_y_entry = Entry(root)
button_y_entry.insert(0, "966")  # Default value
button_y_entry.grid(row=6, column=1)

Label(root, text="Credentials JSON Path:").grid(row=7, column=0)
credentials_path_entry = Entry(root)
credentials_path_entry.insert(0, "path/to/credentials.json")  # Default value
credentials_path_entry.grid(row=7, column=1)

Label(root, text="Number of Pages:").grid(row=8, column=0)
pages_entry = Entry(root)
pages_entry.insert(0, "2")  # Default value
pages_entry.grid(row=9, column=1)  # Corrected row index

# Start button
start_button = Button(root, text="Start", command=start_process)
start_button.grid(row=10, columnspan=2)  # Adjusted row index

# Status display
status_text = Text(root, height=10, width=50)
status_text.grid(row=11, columnspan=2)

# Run the application
root.mainloop()
