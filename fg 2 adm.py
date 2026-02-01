import streamlit as st
import pandas as pd
import psycopg2

st.title("FG Public School No 2 (Boys) Jhelum Cantt")
st.header("Admission Form for 2026")
st.write("Kindly Enter required data carefully and correct in all feilds")
st.write("Double Check before pressing :green[***Save Data***]")
st.info("Please after pressing :green[***Save Data***] Note :yellow[***Tracking Number***] for Future Correspondance!!!")
st.write("\n\n")

name = st.text_input("Enter Student Name : ")
f_name = st.text_input("Enter Student\'s Father Name :")
bform = st.text_input("Enter Your Child Computerise B-Form Number Without Dashes :",placeholder='1234512345671',max_chars=13)
cnic = st.text_input("Enter Father\'s CNIC No Without Dashes :",placeholder='1234512345671',max_chars=13)
catg =  st.selectbox("Select Father\'s Profession Catagory:",options=['Army Person','Retrd Army Personal','FGEI\'s Employee','Civilian','Defense Paid','Federal Govt Employee','Provincial Govt Employee','Private Job','Own Bussiness','Un Employeeed'])
c = st.selectbox("Select Class for which you want to apply Admission:",options=['Pre-I','1st','2nd','3rd','4th','5th','6th','7th','8th','9th'])
g = st.radio("Select Gender : ",options=['Male','Female'])
phno = st.text_input("Enter Your Mobile No :",placeholder='0300xxxxxxx',max_chars=11)
whtsapp_no = st.text_input("Enter Your Whatsapp No :",placeholder='0300xxxxxxx',max_chars=11)
dob = st.date_input("Select Your Date of Birth :",value='2005-01-01',min_value='2005-01-01',max_value='2023-12-31')
adress = st.text_area("Enter Your Current Address : ")
padress = st.text_area("Enter Your Permanent Address : ")

btn = st.button("Save Data")

if btn:
    if name=='':
        st.warning("Please Enter :blue[***Student Name***]!!!")
    if f_name=='':
        st.warning("Please Enter :blue[***Father Name***]!!!")
    
    if bform=='':
        st.warning("Please Enter Your :blue[***B-Form No***]!!!")
    if not bform.isdigit():
        st.warning("B-Form should only contain :blue[***NUMBER***] value!!!")
    if not len(bform) == 13:
        st.warning("CNIC No Must contain :blue[***13 digits***]!!!")

    if cnic=='':
        st.warning("Please Enter Your :blue[***CNIC No***]!!!")
    if not cnic.isdigit():
        st.warning("CNIC No should only contain :blue[***NUMBER***] value!!!")
    if not len(cnic) == 13:
        st.warning("B-Form Must contain :blue[***13 digits***]!!!")

    if phno=='':
        st.warning("Please Enter Your :blue[***Mobile No***]!!!")
    if not phno.isdigit():
        st.warning("Mobile No should only contain :blue[***NUMBER***] value!!!")
    if not len(phno) == 11:
        st.warning("Mobile No Must contain :blue[***11 digits***]!!!")

    if whtsapp_no=='':
        st.warning("Please Enter Your :blue[***Whatsapp No***]!!!")
    if not whtsapp_no.isdigit():
        st.warning("Whatsapp No should only contain :blue[***NUMBER***] value!!!")
    if not len(whtsapp_no) == 11:
        st.warning("Whatsapp No Must contain :blue[***11 digits***]!!!")

    if adress=='':
        st.warning("Please Enter Your :blue[***Current Address***]!!!")
    if padress=='':
        st.warning("Please Enter Your :blue[***Permanent Address***]!!!")

    if name and f_name and dob and whtsapp_no and phno and adress and padress:
        # Fetch variables
        USER = "postgres"
        PASSWORD = "Usman@34203"
        HOST = "db.rouuqdhamfyhyzbzfehb.supabase.co"
        PORT = 5432
        DBNAME = "postgres"

        # Connect to the database
        try:
            connection = psycopg2.connect(
                user=USER,
                password=PASSWORD,
                host=HOST,
                port=PORT,
                dbname=DBNAME
            )
            print("Connection successful!")
            
            # Create a cursor to execute SQL queries
            cursor = connection.cursor()
            
            # Correct INSERT query using parameterized values
            insert_query = """
                INSERT INTO public.data 
                ("BFORM No","Student Name","Father Name","CNIC No","Catagory","Class","Gender",
                "Mobile Number","Whatsapp Number","Date of Birth","Current Address","Parmanent Address")
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING "BFORM No";
            """
            
            values = (bform, name, f_name, cnic, catg, c, g, phno, whtsapp_no, dob, adress, padress)
            
            cursor.execute(insert_query, values)
            connection.commit()   # commit the transaction
            result = cursor.fetchone()
            
            # Now get total row count
            cursor.execute("SELECT COUNT(*) FROM public.data;")
            total_rows = cursor.fetchone()[0]
            

            if result:
                st.success("✅ Record Entered Successfully with BFORM No:", result[0])
                st.info("📊 Your Tracking No is 202603:", total_rows)

            
            # Close the cursor and connection
            cursor.close()
            connection.close()
            print("Connection closed.")

        except Exception as e:
            print(f"Failed to connect: {e}")
            st.error(f"Failed to connect: {e}")
            st.info("For More Information!!!")
            st.info("Please Contact 0544920233")
            st.info("or write us at fgps2bjlm@gmail.com")

    else:
        st.warning("All Feidls are Mandatory, Some Data is Missing, Please Re Enter!!!")