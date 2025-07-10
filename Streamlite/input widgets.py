
import streamlit as st
# 1. Checkbox
st.title('This app show input widgets')

agree = st.checkbox('I agree')
if agree:
    st.write('Great!')

#2. Radio Button
genre = st.radio(
    "What's your favorite movie genre?",
    ('Comedy', 'Drama', 'Documentary')
)

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")

#3. Selectbox

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)
st.write('You selected:', option)
#4. Multiselect
options = st.multiselect(
    'What are your favorite colors?',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red']  # default selections
)
st.write('You selected:', options)
#5. Slider
age = st.slider('How old are you?', 0, 130, 25)  # min, max, default
st.write("I'm ", age, 'years old')
#6. Text Input
name = st.text_input('What is your name?')  
st.write('Hello, ', name, '!')
#7. Text Area       
text = st.text_area('What do you want to say?')
st.write('You wrote:', text)
#8. Date Input          
import datetime
today = st.date_input("Today's date", datetime.date.today())                    
st.write('The current date is:', today)

#9. Time Input
import datetime     
time = st.time_input('Set an alarm for', datetime.time(8, 45))  # default time
st.write('Alarm set for:', time)                        
#10. File Uploader
uploaded_file = st.file_uploader("Choose a file", type=['csv', 'txt'])      
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.read()
    st.write(bytes_data)
#11. Button
if st.button('Say hello'):
    st.write('Hello there!')            
#12. Color Picker

color = st.color_picker('Pick A Color', '#00f900')  # default color
st.write('The current color is', color)             
