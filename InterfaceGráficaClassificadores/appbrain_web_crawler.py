import ipywidgets as widgets
from IPython.display import display
import cv2
import numpy as np
import requests
from PIL import Image
from io import BytesIO

# Function to change image color to red
def red_color_image(image):
    red_image = np.array(image)
    red_image[:,:,1:] = 0
    return Image.fromarray(red_image)

# Function to change image color to colored
def colored_image(image):
    return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)

# Function to check if word is present in text
def check_word_in_text(word, text):
    return word.lower() in text.lower()

# Function to handle submit button click event
def submit_text(sender):
    submitted_text = text_field.value
    
    # Check each word in the grid
    for i, word in enumerate(words):
        if check_word_in_text(word, submitted_text):
            # Change image to colored
            images[i].value = colored_image(images[i].value)
        else:
            # Change image to red
            images[i].value = red_color_image(images[i].value)

# Create text field and submit button
text_field = widgets.Textarea(placeholder='Enter your text here...')
submit_button = widgets.Button(description='Submit')

# Attach event handler to submit button
submit_button.on_click(submit_text)

# Define words and corresponding images (URLs)
words = ['cat', 'dog', 'tree', 'car', 'house', 'flower', 'bird', 'sun', 'moon', 'star', 'book', 'computer']
image_urls = [
    'https://image.shutterstock.com/image-vector/vector-illustration-cat-260nw-1383388400.jpg',
    'https://image.shutterstock.com/image-vector/dog-260nw-587085707.jpg',
    'https://image.shutterstock.com/image-vector/isolated-tree-260nw-249064791.jpg',
    'https://image.shutterstock.com/image-vector/car-top-view-260nw-1003556240.jpg',
    'https://image.shutterstock.com/image-vector/house-cartoon-icon-isolated-on-260nw-1556755203.jpg',
    'https://image.shutterstock.com/image-vector/set-tropical-flowers-leaves-bouquets-260nw-1135454432.jpg',
    'https://image.shutterstock.com/image-vector/vector-bird-icon-on-white-260nw-724861495.jpg',
    'https://image.shutterstock.com/image-vector/cute-sun-clouds-vector-illustration-260nw-194973064.jpg',
    'https://image.shutterstock.com/image-vector/abstract-cartoon-moon-isolated-on-260nw-1663501006.jpg',
    'https://image.shutterstock.com/image-vector/cute-little-star-icon-vector-260nw-718498673.jpg',
    'https://image.shutterstock.com/image-vector/stack-books-colorful-vector-icon-260nw-1092867575.jpg',
    'https://image.shutterstock.com/image-vector/cartoon-computer-laptop-flat-vector-260nw-1511644336.jpg'
]

# Create image widgets from URLs
images = []
for url in image_urls:
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img_widget = widgets.Image(value=cv2.imencode('.png', np.array(img))[1].tostring(), format='png', width=100, height=100)
    images.append(img_widget)

# Arrange images in a grid layout
grid = widgets.GridBox(images, layout=widgets.Layout(grid_template_columns="repeat(4, 100px)"))

# Display interface
display(text_field)
display(submit_button)
display(grid)
