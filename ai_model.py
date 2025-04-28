import os
from google import genai
from google.genai import types

def generate(user_input):
    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY"),  # Ensure your API key is loaded from the environment
    )

    model = "gemini-2.0-flash"  # Replace this with your trained model identifier

    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""What is the address of TIP Manila?
"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""The Technological Institute of the Philippines (T.I.P.) Manila is primarily located at 363 P. Casal Street, Quiapo, Manila, 1001, Philippines. Additionally, the campus includes another building at 1338 Arlegui Street, Quiapo, Manila, 1001, Philippines. """),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""What is the telephone number of TIP Manila?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""The telephone numbers of T.I.P. Manila are:\n

*    (02) 8733-9117\n
*    (02) 7918-8476\n
*    0917-177-2566\n

 Feel free to reach out to them for any inquiries!
            """),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""What is the email address for TIP Manila?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""The email address for TIP Manila is info@tip.edu.ph"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""What undergraduate programs are offered at TIP Manila?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""T.I.P. Manila offers a variety of undergraduate programs across different fields. Here's a list of the programs available:

**College of Engineering and Architecture**
*   Bachelor of Science in Chemical Engineering
*   Bachelor of Science in Civil Engineering
*   Bachelor of Science in Computer Engineering
*   Bachelor of Science in Electrical Engineering
*   Bachelor of Science in Electronics Engineering
*   Bachelor of Science in Industrial Engineering
*   Bachelor of Science in Mechanical Engineering
*   Bachelor of Science in Architecture

**College of Computer Studies**
*   Bachelor of Science in Computer Science
*   Bachelor of Science in Information Technology
*   Bachelor of Science in Entertainment and Multimedia Computing
*   Major in:
*   Digital Animation technology
*   Game Development

**College of Business Education**
*   Bachelor of Science in Accountancy
*   Bachelor of Science in Accounting Information System
*   Bachelor of Science in Business Administration
*   Major in:
    *   Logistics and Supply Chain Management
    *   Financial Management
    *   Human Resource Management
    *   Marketing Management

**College of Arts**
*   Bachelor of Arts in English Language
*   Bachelor of Arts in Political Science

"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""Does TIP Manila offer Senior High School?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""T.I.P. Manila no longer offers Senior High School (SHS). Applicants who wish to pursue their SHS education with T.I.P. may consider enrolling at Quezon City Campus."""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""
What academic tracks are offered in the Senior High School program at TIP Manila?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""I'm sorry, TIP Manila no longer offers Senior High School.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""What are the admission requirements for freshmen at TIP Manila?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""To apply as a freshman at T.I.P. Manila, you'll generally need to prepare the following:

1. Original High School Report Card (Form 138/SF9) in Grade 12
2. PSA Birth Certificate (Original Copy)
3. Certificate of Good Moral Character
4. Two (2) copies of 2\" x 2\" recent ID pictures
 
If graduated with honors, please present Certificate of Honors as well.

**Additional Freshman Requirements**

**Filipino Graduates of Secondary Education from Philippine Secondary Schools Abroad**
1. High School Report Card (Form 138/SF9) in Grade 12 or Certificate of Completion of Secondary Education or its equivalent
2. Philippine Statistics Authority (PSA) Birth Certificate
3. Certificate of Good Moral Character (with school seal)
4. Two (2) copies of 2\"x 2\"recent picture
5. Photocopy of Philippine passport
6. Certificate of Honors / Rank, if applicable

**Filipino Graduates of Secondary Education from Foreign Schools**
1. Authenticated Scholastic Records and Certification of Graduation or Certification of Completion of Secondary Education or its equivalent
2. Certification of Equivalency from DepEd
3. Philippine Statistics Authority (PSA) Birth Certificate
4. Two (2) copies of 2\"x 2\" recent picture
5. Original and photocopy of Philippine passport / Foreign Passport
6. Authenticated Identification Certificate for Dual Citizenship under RA 9225, if holder of foreign passport

**Filipino graduates prior to S.Y. 2014-2015 who did not enroll in any tertiary institution immediately after graduation**
1. High School Report Card (Form 138)
2. Philippine Statistics Authority (PSA) Birth Certificate
3. Certification from the high school principal stating that the F137- A has not been forwarded to any tertiary institution / Affidavit of non enrollment in other HEls.
4. Certificate of Good Moral Character (with school seal)
5. Four (4) copies of 2\"x 2\" recent picture
6. Certificate of Honors / Rank, if applicable

**Filipino applicants with PEPT/ALS Certificates**
1. Examinee Report Form (ERF)/Certificate of Rating in Secondary Level
2. Completion Certificate for Secondary Level
3. Philippine Statistics Authority (PSA) Birth Certificate
4. Authenticated Diploma in Secondary Education Equivalency
5. Four (4) copies of 2\"x 2\" recent picture

For more detailed and updated information, it's always best to check the T.I.P. Manila website or contact the Admissions Office directly.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""What are the admission requirements for transferees"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""
For students who want to transfer to T.I.P. Manila, here are the requirements:

1.	Original Transfer Credentials or Honor Dismissal
2.	Official Transcript of Records or True Copy of Grades from the last school attended
3.	Certificate of Good Moral Character
4.	Copy of course Descriptions
5.	PSA Birth Certificate
6.	Two (2) copies of 2\" x 2\" recent ID pictures

For the most up-to-date and detailed information, it's advisable to visit the T.I.P. Manila website https://www.tip.edu.ph/ or directly contact the Admissions Office.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""When was TIP founded?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""The Technological Institute of the Philippines (T.I.P.) was founded in February 8, 1962. It is a private non-sectarian stock institution founded by a group of educators led by Engineer Demetrio A. Quirino, Jr. and Dr. Teresita U. Quirino. T.I.P. is committed to providing high-quality and best-value education. Leveraging on an outcomes-based educational model and globally accredited programs, T.I.P. produces graduates prepared to meet industry needs, contribute to the nation's economic development, or pursue technopreneurship to address societal challenges."""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""What were the objectives of the founders' vision?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""The founders, Engr. Demetrio A. Quirino Jr. and Dr. Teresita U. Quirino, envisioned T.I.P. to achieve the following objectives:

1.	To maintain high standards of instruction;
2.	To bring within the reach of the masses the blessings of higher education; and
3.	To cooperate with the government in the implementation of its economic and social amelioration programs.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""What courses did TIP initially offer?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""In its early years, T.I.P. primarily offered courses in:
•	Chemical Engineering
•	Civil Engineering
•	Electrical Engineering
•	Mechanical Engineering
•	Architecture

It also offered Industrial Education, Industrial Arts, Liberal Arts, High School, and various trade courses.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""Where was TIP's first located?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""T.I.P.’s first site was the Lorenzana Building in Quiapo, Manila. The school had an initial enrollment of 2,400 which steadily increased throughout the years, prompting the school to slowly but surely expand. In 1967, it set up its main site at G. Puyat Street, Quiapo, Manila."""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""When did TIP open its Manila campus?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""T.I.P Manila open in 1981, the T.I.P. P. Casal, Quiapo location was opened to accommodate the growing student population which had reached over 23,000. T.I.P. Arlegui was opened three years later across P. Casal, both areas being collectively known as the T.I.P. Manila campus. Currently, T.I.P. Manila has four (4) main buildings across the combined 2.3-hectares of the two sites."""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""Who is the current president of TIP?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""The current president of T.I.P. is Angelo Quirino Lahoz. The announcement was made by Dr. Elizabeth Quirino-Lahoz, T.I.P. Chairman, on Friday, February 21, 2025 during the school’s 63rd anniversary celebrations.

Angelo Quirino Lahoz is the firstborn son of Dr. Quirino-Lahoz and Angel Lahoz and the grandson of T.I.P. founders, Engr. Demetrio Quirino and Dr. Teresita Quirino. He previously served T.I.P. as Assistant Vice President for Administration for fifteen (15) years then as Senior Vice President and Vice Chairman for eight (8) years.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""Who is the current Chairman of the Board of TIP?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Dr. Elizabeth Quirino-Lahoz is the current Chairman of the Board of Directors of the Technological Institute of the Philippines (T.I.P.), with campuses in Manila and Quezon City.

Dr. Lahoz assumed the presidency in 2003. She succeeded Dr. Teresita U. Quirino and Engr. Demetrio A. Quirino, Jr., T.I.P. founders and first and second T.I.P. presidents, respectively.

She stepped down from her role as the third T.I.P. president on February 21, 2025, turning over the presidency to her son, third generationer Angelo Quirino Lahoz. Dr. Lahoz continues to serve as the institution's Chairman of the Board.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""What are TIP's vision and mission statements?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Here are T.I.P.'s vision and mission statements:

**Vision:**
TIP envision a better life for Filipinos by empowering our students with the best globally competitive technological education in engineering, computing, and allied disciplines.

**Mission:**
Through digitalization and innovation in academic design and delivery, T.I.P. students, faculty, staff, and industry partners work together in both traditional and online/flexible learning to transform our students to achieve optimal student outcomes:
*	Full competence in their fields of study
*	Ability to apply their competencies, mindsets, and values to serve the needs of industry or to pursue technopreneurship to solve societal problems.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""What are TIP's core values?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""The core values of T.I.P. are:

*   **Commitment to Continuous Improvement and Innovation**
The School is committed to continuously improve its services and innovate its program offerings to maintain its globally competitive edge and to ensure value addition for its stakeholders.
* **Collaborative Mindset**
Everyone continuously engages and collaborates with internal and external stakeholders to remain relevant, and attain its desired goals and objectives.
* **Community Spirit**
A strong sense of community, a willingness to cooperate in planning, realizing, and achieving goals for the common good.
* **Service Orientedness**
A culture of altruism in the context of an educational institution where work is towards helping others. Teachers unselfishly impart knowledge so students achieve full competency in their field of study. Employees and administrators serve with the knowledge that service to others is their reason for being, and the school, as a community, gives back to society.
* **Positive Attitude For Learning and Working**
Positive attitude, high emotional resiliency, a grateful heart, a healthy body, and a clean environment are ways for productive learning and working to take place.
* **Effective and Open Communication**
The School recognizes that effective communication is an integral element in the institution’s success. With this, the School also encourages two-way dialogues that shall lead to an engaged and united community under a common goal.
* **Digital Savvy**
The School integrates digitalization and technology in managing its processes and embedding them into its curriculum. This enables the School to streamline its processes and achieve digital transformation.
* **Adaptability**
The School strategically adapts to a changing environment by gathering relevant information and applying critical thinking to address multiple demands and competing priorities, thereby optimizing opportunities even in times of adversity."""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""What are TIP's core competencies?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""T.I.P.'s core competencies are:

* **COLLABORATION**
The ability to work with others and build partnerships to meet the shared objectives.
* **CONTINUING IMPROVEMENT TOWARDS TOTAL QUALITY**
A relentless drive towards the improvement of work process in order to achieve quality in all aspects of operations with the objective of delivering quality service to the School's constituents.
* **INNOVATIVENESS**
The ability to rapidly incorporate relevant changes in business practices through the creation and/or adoption of new ideas that add value in the form of increased competitiveness and sustainability and to improve facilities, laboratories and shops; creative and efficient solutions in order to provide and design facilities that are up-to-date and highly conducive to teaching, learning and working.
* **EFFICIENT AND CREATIVE MANAGEMENT**
The ability to innovate so that financial and human resources are conserved and harnessed to the fullest to ensure viability and continued delivery of quality instruction and quality administrative services.
* **AN ORGANIZATION WILLING TO LEARN AND IMPROVE**
The dynamism, openness and willingness to grow, adapt and improve by learning new and better ways of doing things. Through grit and determination, the organization does not resist the challenges brought about by new learning, new technologies, new systems, and new policies.
* **ABILITY TO ENGAGE TECHNOLOGY/DIGITAL COMPETENCY**
The integration of technology and digitalization in the management of the school and in the conduct of its operations and processes.
* **QUEST FOR EXCELLENCE**
In order to achieve excellence and exceed expectations, the quest is broken down into small steps beginning with setting personal standards higher than those of the School and for the School, and the community, to set standards higher than those of the CHED and national government."""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""What is the meaning of TIP Seal?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""A fusion of technology and traditional education. The willingness to evolve in the face of new challenges, while maintaining the same passion and steadfastness that build an institution. An institution that imbues its students with Filipino values, industry and global citizen values. An institution that transforms students into graduates who will contribute to the general welfare of society."""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""What is the meaning of TIP Logo?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""The T.I.P. logo is dominated by lines and symmetry, both important elements in engineering. Behind every great structure is the right mix of lines placed in symmetry.
 
The proportion between the gray lower block and the white upper block is 60:40 to subliminally reinforce the idea of stability. The base, which is colored black, represents a firm and strong foundation. The white dots in our new T.I.P. acronym is our non-verbal way, in visual graphic form, to suggest to the reader to read TIP as T.I.P. and not as “tip”.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""What is the contact information of tip manila admission?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""For inquiries regarding admissions at T.I.P. Manila, you can reach them through the following contact information:

**Telephone:**
    * 8733-9117 loc. 102
    * 8736-2580
    * (02) 7918-8476 loc. 102
    * 9171772566 loc. 102
    * 0917-1059581

**Email:**
    *  admissions.manila@tip.edu.ph
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""Who can we contact if there is grades or school document concerns?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""For any grades or school document concerns, you may email the Registrar of 
T.I.P. Manila: 
(02) 8736-4208 or (02) 8733-9117 or (02) 79188476 or 09171772566 loc 187
registrar.manila@tip.edu.ph
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""When is registrar open?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""The Registrar's Office at T.I.P. Manila is open during the following hours:

*   Monday to Friday: 8:00 AM to 5:00 PM
*   Saturday: 8:00 AM to 12:00 NN

Please note that these hours are subject to change. It's always a good idea to confirm with the Registrar's Office directly, especially during holidays or special events.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""When is the start of classes?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""No start date yet for SY 2025-2026. Please stay tuned to our social media pages for official announcements. 
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""What is the enrollment procedure for incoming college students?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""ENROLLMENT PROCEDURE FOR INCOMING COLLEGE STUDENTS
 
*  **Step 1:** Self-Admit - Online Registration: https://admission.tip.edu.ph/web.
*   **Step 2:**	Admission - Evaluation, Migration of Student Profile in ARIS, Printing of Admission Forms and Scholarship Forms (if applicable) at Student Recruitment Office (SRO)
*  **Step 3:**	Interview - with Security, Occupational, Health and Safety (SOHAS) and Guidance and Counseling Center (GCC)
*  **Step 4:**	Entrance Exam - this step is required for applicants with 79% or below GWA
*  **Step 5:** 	Registration - Encoding of Courses / Sections and Printing of Pre-Enrollment Form at SRO
*  **Step 6:** 	Payment of Fees at Tellering - pay at the teller and receive Official Receipt
*  **Step 7:** 	Issuance of Registration Form - Print the Official Enrollment Form at the Student Accounting Services (SAS).  
*  **Step 8:** 	Application for ID, Library Card, Orientation - Head to the Office of Student Affairs (OSA) and Library for ID and Library Card application respectively, then head to GCC to sign up for orientation.
*  **Step 9:**	Math Enhancement Program - If this step is applicable to you, please head to the Math and Physics department.
*  **Step 10:**	Medical and Dental Check-up - Head to the Medical-Dental Services (MDS) for check-up; check-up includes drug testing
*  **Step 11:**	Orientation - headed by GCC
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""What is the enrollment procedure for transferee college students?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Here's the enrollment procedure for Transferee College Students at T.I.P. Manila:

*   **Step 1:**	Self-Admit - Online Registration: https://admission.tip.edu.ph/web.
*  **Step 2:**	Admission - Evaluation, Migration of Student Profile in ARIS, Printing of Admission Forms at Student Recruitment Office (SRO)
*  **Step 3:** Interview - with Security, Occupational, Health and Safety (SOHAS), Office of Student Affairs (OSA) and Guidance Counseling Center (GCC) 
*  **Step 4:** 	Entrance Exam - required for all transferees
*  **Step 5:** 	Evaluation of Courses with Program Chair / Program Evaluator
*  **Step 6:** 	Medical and Dental Check-up - Head to the Medical-Dental Services (MDS) for check-up; check-up includes drug testing
*  **Step 7:** 	Registration - Encoding of Courses / Sections and Printing of Pre-Enrollment Form at SRO
*  **Step 8:**  	Payment of Fees at Tellering - pay at the teller and receive Official Receipt
* **Step 9:** 	Issuance of Registration Form - Print the Official Enrollment Form at the Student Accounting Services (SAS). 
* **Step 10:** 	Application for ID, Library Card, Orientation - Head to the Office of Student Affairs (OSA) and Library for ID and Library Card application respectively, then head to GCC to sign up for orientation.
* **Step 11:**  	Orientation - headed by GCC

"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""What is the online enrollment procedure for continuing college students?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Here is the online enrollment procedure for continuing college students at T.I.P. Manila:\n

**For students without concerns**
* **Step 1:**	Pre-register using your ARIS student portal
MLA: https://webmla2.tip.edu.ph/portal/student/new/public/login.php.
* **Step 2:**	Print enrollment form
* **Step 3:**	Pay at teller or via online. Official receipt can be requested onsite.\n
 
**For students with concerns (including returnees)**
* **Step 1:**	Clearance 
For students with academic probations, seek study load advice with the Guidance and Counseling Center (GCC).
For returnees, secure clearance with the Office of Student Affairs (OSA), Student Accounting Services (SAS) and Security, Occupational, Health and Safety (SOHAS) for readmission
For students with liabilities, secure clearance of liability from the concerned offices
* **Step 2:**	Pre-register using your ARIS student portal 
  MLA: https://webmla2.tip.edu.ph/portal/student/new/public/login.php.
* **Step 3:**	Advising 
Seek advice from Academic Advisers regarding courses to enroll 
Program Evaluator with validate and encode advised courses
* **Step 4:**	Print enrollment form
* **Step 5:**	Pay at teller and get official receipt
 
Reminder: Academic advisers are available onsite. The Office of the Registrar may validate courses for course credit, course equivalency, overload, simultaneous enrollment and posting of elective courses.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""How much is the total school fees (tuition and miscellaneous fees)?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Updated list of fees and discounts are available at the Student Recruitment Office.\n
                                     
*	**Trunkline:** 8733-9117 loc. 102
*	**Landline:** 8736-2580
*	**Mobile:** 0917-1059581
*	**Email:** admissions.manila@tip.edu.ph
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""What is the mode of payment of school fees?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""**MODE OF PAYMENT**\n
*	Cashier / Tellering Office at T.I.P. Campus 
*	PayApp: bit.ly/TIPOnlinePayment
*	DragonPay (If you are a current T.I.P. student, be sure to log in to your T.I.P. e-mail to access the link): https://tip.instructure.com/courses/4925/files?preview=331490
*	7/11: https://www.dragonpay.ph/dragonpay-payments-via-7-11-are-now-easier-and-faster
*	BDO online banking and over-the-counter transaction
*	Landbank online banking
 
Please note that T.I.P. does not use GCash, Maya or any other alternative payment channels and does not authorize anyone to receive any payment outside of the official channels listed above.  
 
If you have any concerns regarding payment and/or assessment, you may reach our Student Accounting Services (SAS) and Tellering Services here:

**Student Accounting Manila:** 
* 8733-9117 loc 153\n
**Tellering Manila**
* 8733-9117 loc. 155
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""Is there scholarship available at tip?"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Yes, T.I.P. offers a variety of scholarships and financial aid options. Here's a summary of some key scholarship opportunities:

**1. Engr. Demetrio A. Quirino, Jr. (EDAQ) Scholarship Grant:**
The EDAQ grant is a prestigious annual scholarship program open to highly qualified senior high school graduates who intend to enroll in any board-related engineering or architecture program. 
**Qualifications:** \n
The senior high school student must:
*	Possess a general average of 85% in the First Semester in Grade 12;
*	Have not taken any course in college prior to the examination.
**Benefits and Allowances** \n
The scholar shall be entitled to the following benefits and allowances: 
*	No fees throughout the duration of the program of study
*	Semestral stipend of P5,000.00 throughout the program of study
**Note:**
*	As long as the student maintains the grade requirements of the scholarship every term, no fees shall be paid throughout the duration of the program of study. Further, the scholar shall lose the scholarship if the student commits any infraction of the provisions of the Student Manual.
*	The scholars shall be determined through a rigid and competitive examination process. The examinations shall cover three (3) courses: Physical Sciences, Mathematics, and English.

**Scholarship Grant for Engineering and Architecture are available only at T.I.P. For the following academic programs:**
* Chemical Engineering (Manila only), 
* Civil Engineering, 
* Electrical Engineering, 
* Electronics Engineering, 
* Mechanical Engineering, and 
* Architecture. 


**2. Dr. Teresita U. Quirino (DTUQ) Scholarship Grant:**
The DTUQ grant is an honorary annual scholarship program open only to highly qualified senior high school graduates who intend to enroll in accountancy or teacher education.

**Qualifications:** 
The senior high school student must: 
*	Possess a general average of 85% in the First Semester in Grade 12; 
*	Have not taken any course in college prior to the examination.

**Benefits:**
The scholar shall be entitled to the following benefits and allowances: 
*	No fees throughout the duration of the program of study
*	Semestral stipend of P2,500.00 throughout the program of study

**Note:**
*	As long as the student maintains the grade requirements of the scholarship every term, no fees shall be paid throughout the duration of the program of study. Further, the scholar shall lose the scholarship if the student commits any infraction of the provisions of the Student Manual.
*	The scholars shall be determined through a rigid and competitive examination process. The examinations shall cover three (3) courses: Physical Sciences, Mathematics, and English. 

Scholarship Grant for Accountancy and Teacher Education available only at T.I.P.  For the following academic programs: Accountancy in TIP Manila.

**3. Entrance Scholarship and Discounts:**
 Slots are available on a first come, first serve basis. 

*   **With Highest Honors:** 100% discount on tuition for one semester only.
*   **With High Honors:** 50% discount on tuition for one semester only.
*   **With Honors or 90% or Higher GWA:** 25% discount on tuition for one semester only.

**4. Loyalty Discount for T.I.P. Senior High School Graduates:**

*   A one-time loyalty discount of Php 3,500 on top of other applicable discounts for one semester during their first college enrollment as freshmen at T.I.P.

"""),
            ],
        ),

        types.Content(
            role="user",
            parts=[types.Part.from_text(text=user_input)], 
        ),
    ]
    

    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""You are a helpful and informative chatbot for TIP Manila. You respond in a friendly and professional manner and provide accurate answers based on the information you have been trained on.
                                  If unsure and is not about TIP Manila, and also do not answer any math related questions, say "I'm sorry, I don't have information on that topic.Your name as a chatbot is yui"""),  # Custom instructions
        ],
    )

    # Initialize the response variable
    full_response = ""

    # Request content from the trained model
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        full_response += chunk.text  # Append each chunk of the response

    return full_response  # Return the complete concatenated response
