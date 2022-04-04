from asyncio import coroutine
import streamlit as st


#st.title("WELCOME TO YOLOH")
#title_alignment = """<style>WELCOME TO YOLOH {text-align: center}</style>"""
#st.markdown(title_alignment, unsafe_allow_html=True)
st.markdown("<h1 style = 'text-align: center; color: Yellow;'>WELCOME TO YOLOH</h1>", unsafe_allow_html = True)



#st.subheader("Mandatory")

with st.form('Form1'):
        
        col1, col2 = st.columns(2)   
        
        with col1:
            st.subheader('Life Insurance')
            selection = st.selectbox('Do You Have a Life Insurance Policy?', ['SELECT', 'YES', 'NO'])
            submitted0 = st.form_submit_button('Submit')

        counts = 0 
        if selection == 'YES':
            counts = counts + 8.0
        else:
            counts = counts + 0   
        
        with col2:
            #a = st.write(count)
            st.metric(label="Projected SAFEX Score", value= counts,  delta_color="inverse")


with st.form('Form01'):
        col1, col2 = st.columns(2)

        with col1:
            
            st.subheader('Health & Well-being')
            selection1 = st.selectbox('Do You Have a Medical Insurance Policy?', ['SELECT', 'YES', 'NO'])
            selection11 = st.selectbox('Do You Have Dental Policy?', ['SELECT', 'YES', 'NO'])
            selection12 = st.selectbox('Do You Have Vision Policy?', ['SELECT', 'YES', 'NO'])
            submitted1 = st.form_submit_button('Submit')

        count = 0
         
        if selection1 == 'YES':
            count = count + 8.0
        else:
           count = count + 0
        if selection11 == 'YES':
            count = count + 4.0
        else:
            count = count + 0
        if selection12 == 'YES':
            count = count + 4.0
        else:
            count = count + 0    

        with col2:
            #a = st.write(count)
            st.metric(label="Projected SAFEX Score", value= counts + count, delta = count,  delta_color="normal")
                           
        
        
#st.subheader("Depends")

with st.form('Form2'):
       col1, col2 = st.columns(2)
       with col1:
           st.subheader('Pets')
           selection2 = st.selectbox('Do You Have  Pet?', ['SELECT', 'YES', 'NO']) 
           
           if selection2 == 'YES':
               selection21 = st.selectbox('Do You Have  Pet Insurance?', ['SELECT', 'YES', 'NO'])
    
               count1 = 0
               if selection21 == 'YES':
                   count1 = count1 + 3.0
               elif selection21 == 'NO':
                   count1 = count1 + 0
               elif selection21 == 'SELECT':
                   count1 = count1 + 0 
               else:
                   pass          
           elif selection2 == 'NO':
               count1 = 0
           elif selection2 == 'SELECT':
               count1 = 0
           else:
               pass 
           submitted02 = st.form_submit_button('Submit')        
               
       with col2:
           new_counts = counts + count + count1
           #b = st.write(new_count)
           st.metric(label="Projected SAFEX Score", value= new_counts, delta = count + count1, delta_color="normal")         


with st.form('Form02'):
       col1, col2 = st.columns(2)
       with col1:                
           st.subheader('Valuables')   
           selection22 = st.selectbox('Do You Own any Valuables More than $500?',['SELECT', 'YES', 'NO'])
         
           if selection22 == 'YES':
               selection23 = st.selectbox('Do You Have  Insurance Associated With It?', ['SELECT', 'YES', 'NO'])

               count11 = 0

               if selection23 == 'YES':
                   count11 = count11 + 3.0
               elif selection23 == 'NO':
                   count11 = count11 + 0
               elif selection23 == 'SELECT':
                   count11 = count11 + 0 
               else:
                   pass          
           elif selection22 == 'NO':
               count11 = 0
           elif selection22 == 'SELECT':
               count11 = 0
           else:
               pass
           submitted2 = st.form_submit_button('Submit') 

       with col2:
           new_count = counts + count + count1 + count11
           #b = st.write(new_count)
           st.metric(label="Projected SAFEX Score", value= new_count, delta = count + count1 + count11, delta_color="normal")



#st.subheader("Optional")

with st.form('Form3'):
       col1, col2 = st.columns(2)
       with col1:
           st.subheader('Warranty')
           selection4 = st.selectbox('Do You Have Expenssive Electronic Items ?', ['SELECT', 'YES', 'NO'])
           #selection5 = st.selectbox('Do You Have Warranty Associated With It ?',['SELECT', 'YES', 'NO'])
           #submitted3 = st.form_submit_button('Submit')
           if selection4 == 'YES':
               selection5 = st.selectbox('Do You Have Warranty Associated With It?', ['SELECT', 'YES', 'NO'])
               
               count12 = 0

               if selection5 == 'YES':
                   count12 = count12 + 0.5
               elif selection5 == 'NO':
                   count12 = count12 + 0
               elif selection5 == 'SELECT':
                   count12 = count12 + 0 
               else:
                   pass          
           elif selection4 == 'NO':
               count12 = 0
           elif selection4 == 'SELECT':
               count12 = 0
           else:
               pass
           submitted2 = st.form_submit_button('Submit')



       with col2:
           new_count1 = new_count + count12
           #c = st.write(new_count1) 
           st.metric(label="Projected SAFEX Score", value= new_count1, delta = count + count1 + count11 + count12, delta_color="normal")

# Age bracket score
score = new_count1 * 2.0            
st.text('Your Probable Safex Score:  {}'.format(new_count1))

 
st.text('75% of people in your age bracket have the score of {}'.format(score))


def header(url):
     st.markdown(f'<p style="background-color:#FFFFE0;color:#9DC209;font-size:20px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
url = 'The ideal score for a person similar to your profile lies in the range of 70 - 80'
header(url)


if new_count1 < 80:
    st.text('Please upload your documents to get your accurate SAFEX score.') 
    st.text('Our recommendation engine will further assist you to improve your score')
    st.text('and INSURE your happiness.')

uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
     bytes_data = uploaded_file.read()
     st.write("filename:", uploaded_file.name)
     st.write(bytes_data)


 


 