import streamlit as st
import qrcode
from PIL import Image
import io
import base64

# Placeholder function to simulate image upload and get URL
def upload_image_and_get_url(file):
    # Simulate uploading the image and returning a URL
    # In practice, you should use an actual service to upload the image
    # and return the URL of the uploaded image.
    return "https://example.com/path/to/image.png"

# Function to generate QR code from text
def generate_qr_code_from_text(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    return qr_img

# Function to generate QR code from image file URL
def generate_qr_code_from_image_url(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    return qr_img

# Main function to run the Streamlit application
def main():
    st.title("QR Code Generator")

    st.sidebar.header("Generate QR Code")
    option = st.sidebar.selectbox(
        "Choose an option",
        ["Text", "Image"]
    )

    if option == "Text":
        text_input = st.text_area("Enter text to generate QR code")
        if st.button("Generate QR Code"):
            if text_input:
                qr_img = generate_qr_code_from_text(text_input)
                
                # Convert PIL Image to bytes
                buf = io.BytesIO()
                qr_img.save(buf, format='PNG')
                byte_im = buf.getvalue()
                
                st.image(byte_im, caption="Generated QR Code", use_column_width=True)
            else:
                st.warning("Please enter some text.")

    elif option == "Image":
        image_file = st.file_uploader("Upload an image file", type=['jpg', 'png', 'jpeg'])
        if image_file is not None:
            if st.button("Generate QR Code"):
                try:
                    # Upload the image and get the URL
                    url = upload_image_and_get_url(image_file)
                    
                    # Generate QR code from the URL
                    qr_img = generate_qr_code_from_image_url(url)
                    
                    # Convert PIL Image to bytes
                    buf = io.BytesIO()
                    qr_img.save(buf, format='PNG')
                    byte_im = buf.getvalue()
                    
                    st.image(byte_im, caption="Generated QR Code", use_column_width=True)
                except ValueError as e:
                    st.error(f"Error generating QR Code: {e}")

if __name__ == "__main__":
    main()
