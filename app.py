import streamlit as st
st.set_page_config(page_title='RAYHAN', page_icon = ':rat:', initial_sidebar_state = 'auto')

class about:
  def write():
      """Used to write the about page in the app.py file"""
      st.title("Un Esprit Curieux - A curious mind! :sleuth_or_spy:")
      st.markdown(
              """## Who Am I?
  "_I am a Random Forest in the World of Overfitting_"
  A Data Scientist with 5 years of experience in solving Business Problems, 
  a constant learner and a firm believer of experimentation over expertise. 
  Always on the lookout for new technologies, I am passionate about designing Data driven solutions which are easy, economical and can be scaled.
  
  **Abhishek Gupta**\n
  **Data Science | Business Analytics | Project Management **
  [**LinkedIn**](https://www.linkedin.com/in/abhishek-gupta-/) | [**Email**](mailto:abhishek.2.gupta@uconn.edu)
  ## The Project
  I came across **Streamlit** last week while looking for solution to host python apps on AWS EC2. 
  The Framework  boasts of being the easiest and the fastest way of creating interactive apps, and after spending just a 
  few hours creating this interactive resume, I can vouch for that. 
  Check out my [**GitHub**]() for the implementation. Reach out to me for any project or a simple discussion on Streamlit.
  Also check out their [**page**](https://www.streamlit.io/) for more more information and updates.
  Also check out this amazing implementation of Streamlit by [**Marc Skov Madsen**](http://awesome-streamlit.org/) for streamlit inspiration.
  """,
              unsafe_allow_html=True,
          )
      hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
      st.markdown(hide_streamlit_style, unsafe_allow_html=True)  
#====================================================================================================================
class edu:
  def write():
      """Used to write the page in the app.py file"""
      st.title("Education :books:")
      st.markdown(
              """### University of Connecticut School of Business

  **Master of Science in Business Analytics and Project Management | May 2020** | [**UConn**](https://www.business.uconn.edu/)\n
  GPA 4.00/4.00 | Beta Gamma Sigma Honoree 
  **Courses ** \n
  - Statistics in Business Analytics \n
  - Big Data Analytics with Hadoop \n
  - Business Decision Modelling \n
  - Predictive Analytics \n
  - Data Mining and Business Analytics \n
  - Introduction to Project Management \n
  - Advanced Business Analytics and Project Management \n
  - Adaptive Business Intelligence \n
  - Project Risk and Cost Management \n
  - Project Leadership and Communication \n
  ### Distance Learning
  **University of Michigan | June 2020** | [Credential](https://coursera.org/share/eb4b7f377b485efe57dafbf0ef9e9178)\n
  - Applied Text Mining
  **Deeplearning.ai | April 2020** | [Credential](https://coursera.org/share/a07ae8b31a11a44f30fe4f77d6d6c0cc)\n
  - Structuring Machine Learning Projects
  **A Cloud Guru| February 2020** | [Credential](https://verify.acloud.guru/5F4E6B310B93)\n
  - AWS certified cloud practitioner 2020
  ### Manipal Institute of Technology
  **Bachelors of Technology in Mechanical Engineering | May 2015** | [**MIT**](https://manipal.edu/mit.html)\n
  GPA 8.54/10.00 
  **Courses **\n
  - Essentials of management\n
  - Engineering Economics and Management \n
  - Object Oriented Programming \n
  - Business Communications \n
  - Operational Research
  """,
              unsafe_allow_html=True,
          )
      hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
      st.markdown(hide_streamlit_style, unsafe_allow_html=True)  
#======================================================================================================================      
class skills:
  def write():
      """Used to write the page in the app.py file"""
      st.title("Skills :hammer_and_wrench:")
      st.markdown(
              """## Languages
  - R
  - Python
  - SQL 
  - VBA
  ## Platforms and Libraries
  - **SAS** - JMP, Enterprise Miner and Enterprise Guide
  - **MS Office** - Excel, Powerpoint, Project, Word
  - **Python** - Pandas, Numpy, Skicit Learn,Scipy, NLTK, Tensorflow, Keras, Streamlit, Dash, Plotly, Matplotlib, Seaborn, etc.
  - **R** - Shiny, Dplyr
  - **SQL** - MS SQL, PostgreSQL,HIVE, HANA, Teradata 
  - Tableau
  - PowerBI
  - Qlik View
  - JIRA, Confluence
  ## Analytical Skills
  - Statistical Data Analysis
  - Data Wrangling
  - Hypothesis Testing
  - Machine Learning
  - Natural Language Processing
  - Web Scraping
  ## AWS Stack
  - EC2
  - Lambda
  - S3
  - RDS - Redshift, Aurora, MS SQL
  - Dynamo DB
  - Sagemaker
  - Lex, Polly
  - Cloudfront
  - IAM
              
  _I am a Random Forest in the World of Overfitting_
  """,
              unsafe_allow_html=True,
  )
      hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
      st.markdown(hide_streamlit_style, unsafe_allow_html=True)
#======================================================================================================================      
class projects:
  def write():
      """Used to write the page in the app.py file"""
      st.title("Projects - :male-construction-worker: ")
      st.markdown(
              """### Graduate Consultant, LIMRA | Aug 2019 – Dec 2019
              
  **Life insurance Policy Lapse Study [AWS Sagemaker, S3, Python, MS Project]**
  - Performed exploratory data analysis on 9.6 million records of aggregated data about “premium persistency” and analyzed the frequency and causes of lapses using Tableau
  - Built XGBoost classification model with 83% precision, 76% recall using AWS Sagemaker to predict customer churn 
              
  ### Decision Scientist, Mu Sigma Inc.| July 2015 - Dec 2020
  **Web Application for a Major US Retailer [SQL- Teradata, HANA, HIVE, Agile-JIRA]**
  - Managed agile teams working on development of a web-based Business Intelligence dashboard to rate ~51k vendors based on key performance indicators like OTIF and In-stock Metrics
  - Led a team of five analysts to develop SQL queries, calculation views and stored procedures to extract data for front-end visualizations
  **Sales and revenue reporting for a US Technology giant [Excel, VBA, SSIS-ETL]**
  - Developed multiple Power BI and Excel dashboards explaining sales and revenues across different business units.
  - Performed Extract Transform Load of data files from several Data Sources to feed the DataCube backend for the reports
  - Created data quality dashboard using VBA and excel to accurately identify data discrepancy issues between reports reducing the time for manual verification by 90%
  **Predicting potential product complaints [Regex, NLP, Random Forest]**
  - Processed customer complaints data using regex and NLP to identify common topics and establish a cause effect relationship with quality control tests’ data from a refrigerator assembly line
  - Created a scalable tool on SAS Visual Analytics to speed up identifying issues during production, leading to 25% improvement in parts availability during assembly
  ### Academic Projects [(GitHub)](https://github.com/alphadatagamma)
  **The Cricket Project [BeautifulSoup, Regex, AWS Sagemaker, S3, Redshift, Tableau]**
  - Used BeautifulSoup and Regex to scrape cricket data for 10 countries and ~6000 players using AWS Sagemaker and EC2 
  - Created a data warehouse in AWS Redshift, and a tableau dashboard to visualize key trends
  **Advance House Price Prediction in Python [Kaggle Top 2%, Stacked Regression]**
  - Created a custom stacked regression model to predict sale price for 1500 houses and achieved a low RMSE of 0.11 for the final model and a top 2% rank on the leaderboard
  **IBM Attrition Analysis and Prediction [Python, Tableau, Decision Trees]**
  - Performed exploratory data analysis and external research to identify the mix of drivers affecting employee attrition rates  
  - Created a classification model using Decision trees and Gradient Boosting to identify employees that are likely to leave, so that the company can have a strategy for employee engagement
              
  """,
              unsafe_allow_html=True,
          )
      hide_streamlit_style = """
              <style>
              #MainMenu {visibility: hidden;}
              footer {visibility: hidden;}
              </style>
              """
      st.markdown(hide_streamlit_style, unsafe_allow_html=True)        
#======================================================================================================================
class recommendations:
  def write():
      """Used to write the page in the app.py file"""
      st.title("Recommendations :memo:")
      st.markdown(
              """### Anantha Krishna Rajpurohit
  **Senior Analyst | Boston Consulting Group(BCG) | April 5, 2020** | [**LinkedIn**](https://www.linkedin.com/in/anantha-krishna-rajpurohit/)\n
  Abhishek joined as a fresher into the team. He brings in a lot of energy into the team and gives his 
  100%. He was reliable to finish the job at hand and actively reach out for help from peers and managers. 
  Always looked to up-skill on a regular basis and actively looked for new skills in the analytics space. 
  Since then he grew over three years at Mu Sigma to be able to move on the bigger responsibilities, 
  mentoring juniors, managing modules and delivering high quality results. With his recent addition of MS 
  in business analytics, I recommend him for any position that require depth in analytics, 
  reliability and project management skills
  
  ### Abhinav Dasgupta
  **Deputy Director | Myntra Jabong | April 5, 2020** | [**LinkedIn**](https://www.linkedin.com/in/abhinav-dasgupta-a0670422/)  \n
  Abhishek was part of the team working with a leading manufacturing giant which I was leading. 
  Abhishek brought a great sense of maturity and work ethic coupled with excellent analytical skills 
  to the team and ensured we constantly created a good experience for the client stakeholders. 
  We solved some of the most complex problems for the business and he was pivotal in making it happen. 
  In addition, he has a continuous zeal to learn and improve himself, which was also reflected in his 
  decision to pursue masters in the area of analytics. I really enjoyed working with Abhishek 
  during his time at Mu Sigma and think he will be a top asset to any team that he will be part of.
  ### Tara Chamberlain
  **Senior Operations Manager| AT&T | February 5, 2020** | [**LinkedIn**](https://www.linkedin.com/in/tara-chamberlain-832b991a/)  \n
  Abhishek was a member of my Capstone team at UCONN and proved to be an invaluable asset. He was not 
  only adept at all data cleaning, modeling, and visualization methods that our team utilized, but
  also took the lead in our research. He ended up uncovering key information that no one, not even our 
  professor or sponsors, was aware of. The team that I run at my current company doesn't 
      have any openings, but it we did, I would be happy to have him join our organization.
  """,
  unsafe_allow_html=True
  )
      hide_streamlit_style = """
              <style>
              #MainMenu {visibility: hidden;}
              footer {visibility: hidden;}
              </style>
              """
      st.markdown(hide_streamlit_style, unsafe_allow_html=True)   
#======================================================================================================================
PAGES = {
    "About": about,
    "Education" : edu,
    "Skills": skills,
    "Projects": projects,
    "Recommendations": recommendations
}

def main():
    """Main function of App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]
    
    with st.spinner(f"Loading {selection} ..."):
        page.write()

    st.sidebar.title("Hire Me")
    st.sidebar.info(
        """
        If you are looking to hire a Data Scientist, 
        [email me](mailto:abhishek.2.gupta@uconn.edu) or reach out 
        to me on [LinkedIn](https://www.linkedin.com/in/abhishek-gupta-/)
    """)
    st.sidebar.title("Additional Info")
    st.sidebar.info(
        "This an interactive streamlit app completely created with Python's latest library **streamlit** "
        "Do reach out to me on [LinkedIn](https://www.linkedin.com/in/abhishek-gupta-/) or "
        "at [Mail me](mailto:abhishek.2.gupta@uconn.edu) to know more. "
        "Also check the [source code](https://github.com/alphadatagamma/Streamlit-Resume-App) here. "  

    )
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
