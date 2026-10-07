# Streamlit Documentation: https://docs.streamlit.io/


import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image  # to deal with images (PIL: Python imaging library)

# TEXT ELEMENTS
# Title/Text
st.title("This is a title")
st.text("This is some text.")

st.markdown("Streamlit is **_really_ cool** :+1:")  # Here, we use ** to make the word bold, _(underscore) to make it italic, and :(colon) :+1: to display a thumbs-up emoji.
st.markdown("# This is a markdown")  # Here, #(hashtag) is used to create a main heading, so "This is a markdown" is displayed as a large heading.
st.markdown("## This is a markdown")  # Here, we use two hashtag symbols, to create a second-level heading. So, "This is a markdown" is displayed as a smaller heading.
st.markdown("### This is a markdown")  # Here, we use three hashtag symbols, to create a third-level heading.

st.header('This is a header')  # is used to add a header to our Streamlit application. Here, "This is a header" is the text that we passed into the function to display on the page.
st.subheader('This is a subheader')  # is used to add a subheader to our Streamlit application. It is smaller than a main header and is useful for organizing different sections of the page.


st.success('This is a success message! green')  # is used to display a success message. For example, here, "This is a success message!" is displayed to let the user know that an operation was successful.
st.info('This is a purely informational message')  # is used to display an informational message.For example, here, "This is a purely informational message" is displayed to provide some information to the user.
st.error("This is an error.")  # is used to display an error message. For example, here, "This is an error." is displayed to let the user know that an error has occurred.
st.warning("This is a warning message!")  # is used to display a warning message. For example, here, "This is a warning message!" is displayed to warn the user about a potential problem or issue.
st.exception("NameError('name there is not defined')")  # is used to display an exception message. For example, here, "NameError('name there is not defined')" is displayed to show the details of an exception that has occurred.


st.help(range)

st.write("Hello :sunglasses:")
st.write(range(10))

# Add image
img = Image.open("images.jpeg")  # First, we open the image using the Image.open() function from the PIL library.
st.image(img, caption="cattie", width=300)  # Then, we use st.image() to display the image in our Streamlit application.
#  The caption parameter adds a text below the image, and width=300 sets the image width to 300 pixels.

# Add video
# my_video = open("ml.mov",'rb')  # First, we open the video file by specifying the local file path in binary mode using open().
# st.video(my_video)  # Then, we pass the video file to st.video() to display and play the video in our Streamlit app.


# Add youtube video
st.video("https://www.youtube.com/watch?v=uHKfrz65KSU")  # We can add a YouTube video to our app by simply providing its URL.

st.checkbox("Up and Down")  # Here, we create a checkbox with a label "Up and Down".
cbox = st.checkbox("Hide and Seek")  # Here, we create a checkbox and assign its value to the variable cbox.
# If the user selects the checkbox, cbox becomes True; otherwise, it becomes False.

if cbox:
    st.write("hide")
else:
    st.write("seek")
status = st.radio("Select a color",("blue-mavi","orange","yellow-sari"))  # Here, we create a radio button with three options: blue, orange, and yellow. And selected option is assigned to the variable status.
st.write("My favorite color is ", status)  # Finally, we display the selected option using the st.write() function.

st.button("Click me")  # Here, we create a button with the label "Click me".


if st.button("Press me") :  # When the user clicks the Press me button, st.button() returns True, so the code inside the if statement is executed.
    st.success("Analysis results are ready!")  #  In this example, a success message is displayed using st.success().

    
occupation = st.selectbox("Your Occupation", ["Programmer", "DataScientist", "Ph.Doctor"])  # The user can select one option from the dropdown list. The selected option is stored in the occupation variable.
st.write("Your Occupation is ", occupation)  # then we display it using st.write().


multi_select = st.multiselect("Select multiple numbers",[1,2,3,4,5])  # Here, we create a multiselect widget with five options. Unlike a radio button or a selectbox, the user can select more than one option.
st.write(f"You selected {len(multi_select)} number(s)")  # Here, we use len() to count how many numbers are selected.
st.write("Your selection are", multi_select)  # Then, we display the selected numbers.
for i in range(len(multi_select)):  # Finally, we use a for loop to display each selected number separately.
    st.write(f"Your {i+1}. selection is {multi_select[i]}")




option1 = st.slider("Select a number", min_value=5, max_value=70, value=34, step=5)  # Here, the user can select a number between 5 and 70. The default value is 30, and the value increases or decreases by 5. And the selected number is assigned to variable option1.
option2 = st.slider("Select a number", min_value=0.2, max_value=30.2, value=5.2, step=0.2)  # Here we use decimal numbers. The user can select a value between 0.2 and 30.2. The default value is 5.2, and the value increases or decreases by 0.2. And selected value is assigned to the option2.

result = option1*option2  # We multiply the two selected values
st.write("multiplication of two options is:",result)  # and display the result using st.write()


name = st.text_input("Enter your name", placeholder="Your name here")  # Here, we create a text input where the user can enter their name. And the entered name is stored in the name variable.
if st.button("Submit"):  # And here, when the user clicks the Submit button,
    st.write("Hello {}".format(name.title()))  # a greeting message will be displayed with the user's name.
      # The title() method makes the first letter of each word uppercase.



number = st.number_input("Insert a number", value=0)  # st.number_input("select a number", min_value, max_value, value, step)
#  Here, the user can enter or select a number, and the value is stored in the number variable. We can also set the minimum, maximum, default, and step values.
st.write("The current number is ", number)  # Finally, we display the current value using st.write().



st.code("import pandas as pd")  # Here, we display a line of Python code using st.code()
st.code("import pandas as pd\nimport numpy as np")  # We can also display multiple lines of code. Here \n is used to start a new line.



with st.echo():  # The code inside the with block is displayed in the Streamlit app and also executed.
    import pandas as pd
    import numpy as np
    df = pd.DataFrame({"a":[1,2,3], "b":[4,5,6]})
    df


import datetime  # First, we import the datetime module.
today = st.date_input("Today is", datetime.datetime.now())  # Then, we use st.date_input() to display a date picker. In the first example, we use the current date as the default value. And selected date is stored in today variable.
date = st.date_input("Enter the date")  # In the second example, the user can select a date from the calendar.

the_time = st.time_input("The time is", datetime.time(8, 45))  # Here, we create a time input with 8:45 as the default time.
hour = st.time_input(str(pd.Timestamp.now()))  # Here, the user can select a time from the time picker, and the selected time is stored in the hour variable.
st.write("Hour is", hour)  # hour variable is displayed using st.write().
st.write("day is", today)

st.button("Click me2")

st.sidebar.title("Sidebar title")  # Adds a large title to the sidebar.
st.sidebar.header("Sidebar header")  # Adds a header below title.

a = st.sidebar.slider("input1",0,5,2,1)  # The first slider allows the user to select a value between 0 and 5. And selected value is assigned to a variable.
x = st.sidebar.slider("input2")  #  The second slider uses Streamlit's default slider settings. And selected value is assigned to b.
st.write("# sidebar input result")  # Finally, we multiply the two selected values and display the result with a header on the main page.
st.success(a*x)


df = pd.read_csv("Advertising.csv")
st.table(df.head())


st.write(df.head())  # displays the first five rows. It is interactive and you can sort.
st.write(df.isnull().sum()) # another example: displays the number of missing values in each column of df.


st.dataframe(df.describe().T)



import pickle  # First, we import the pickle library. We use it to save and load Python objects, including machine learning models.
filename = "my_model"  # Here, we specify the name of our saved model file.
model = pickle.load(open(filename, "rb"))  # Here, we load the saved model into the model variable. And we will use it later to make predictions.


TV = st.sidebar.number_input("TV:",min_value=5, max_value=300)  # This creates a number input for the TV feature. The user can enter a value between 5 and 300.
radio = st.sidebar.number_input("radio:",min_value=1, max_value=50, step=1)  # User can enter a value for radio feature between 1 and 50.
newspaper = st.sidebar.number_input("newspaper:",min_value=0, max_value=120)  # User can enter a value for newspaper feature between 0 and 120.


my_dict = {"TV":TV,  # First, we create a dictionary containing the three feature values.
           "radio":radio,
           "newspaper":newspaper}


df = pd.DataFrame.from_dict([my_dict])  # Then, we convert the dictionary into a Pandas DataFrame.
st.table(df)

predict = st.button("Predict")  # Here we create a button called "Predict". When the user clicks it, predict becomes True.
result = model.predict(df)  # Here, we use the trained model to make a prediction using our DataFrame. The prediction is stored in the result variable.
if predict :  # If the user clicks the Predict button, we display the prediction result on the screen.
      st.success(result[0])


st.balloons()