## EduTech Analyser is a Website which solves real time problem for teachers regarding to the students in the class this website targets to teachers as the audience and focus on the student marks and performance 

## Outline
1. Introduction<br>
1.1.1  Future Development
2. Uses of Application<br>
3. Tech Stacks<br>
4. Work Flow<br>
5. Useful Code Snippets<br>
6. How to Use the Website<br>
7. Type of Inputs<br>
8. Version Control<br>
9. Gallery<br>
10. Conclusion<br>

## Introduction 
In the ever-evolving landscape of education, the need for efficient tools to support educators and students has never been greater. Enter EduTech Analyser, a revolutionary website designed to transform the way educators identify and assist students who may need additional support to excel academically.

EduTech Analyser serves as a powerful ally for educators by simplifying the process of assessing student performance. This user-friendly website takes the data in the form of a CSV file, typically containing the student list and their corresponding academic records. Its primary mission? To pinpoint students who may be struggling academically, often referred to as "dull" or "low-performing" students.

What sets EduTech Analyser apart is its ability to delve deep into the data and extract invaluable insights. By identifying the lowest marks achieved by students, this innovative tool calculates the exact percentage needed to reach an above-average performance level. Armed with this knowledge, educators gain a clear understanding of the challenges each student faces and can tailor their teaching methods accordingly.Furthermore, EduTech Analyser goes one step further by providing insightful remarks and suggestions for teachers. These recommendations offer a guide on how to provide the necessary care and attention to help students reach their full potential. Whether it's extra tutoring, personalized lesson plans, or additional resources, EduTech Analyser equips educators with the information they need to make informed decisions and provide targeted support.

In a world where data-driven decision-making is key to effective education, EduTech Analyser emerges as an indispensable tool, facilitating the journey toward academic excellence for every student. Join us in exploring the vast potential of this website, where technology and education converge to shape a brighter future for learners of all backgrounds and abilities.

## Future Development
If required time is allocated then we can develop this website to the peaks by integrating blockchain and make it paid version and little secure 
I have a Idea to integrate some mechine learning algorithm for segguestions for teacher to get the correct one for perticular students according to the present dataset in the internet we came to the decision to make the website with boundaries 

## Uses of Application 
EduTech Analyser offers versatile applications for both educational institutions and individuals. In schools and educational settings, this tool serves as a valuable asset for teachers and administrators. It simplifies the process of identifying underperforming students, enabling timely interventions to support their academic growth. Additionally, EduTech Analyser provides a comprehensive overview of student performance, aiding in data-driven decision-making for curriculum enhancements and resource allocation.

For individuals, such as parents or private tutors, the application offers a means to closely monitor the academic progress of their children or students. This valuable insight into a student's strengths and weaknesses empowers personalized learning plans and the delivery of targeted assistance. EduTech Analyser bridges the gap between educators and learners, fostering an environment where every student has the opportunity to thrive.


## Tech Stacks 
1.Flsk (Backend Development) <br>
2.Jinja2 (frontend Development) <br>
3.Pandas (Dataset Processing and Modification)<br>
4.Notion Pages (Documentation of code)<br>
5.Cloud Deployment<br>

## WorkFlow
<img src='https://github.com/saiguptha2003/EduTech_Analyser/blob/main/work_flow.png'>

## Code Snippets
```python

import pandas as pd

# Function to calculate the percentage needed to improve above average
def getPercentageToImproveAboveAverage(average, marks):
    return 100 * ((average / marks) - 1)

```

```python
def get_dull_students(numberOfSubjects, file_path):
    ub_1_mean=dataset['sub-1'].mean()
            sub_2_mean=dataset['sub-2'].mean()
            sub_3_mean=dataset['sub-3'].mean()
            sub_4_mean=dataset['sub-4'].mean()
            sub_5_mean=dataset['sub-5'].mean()
            sub_6_mean=dataset['sub-6'].mean()
            below_mean_all_subjects=dataset[(dataset['sub-1'] < sub_1_mean) & (dataset['sub-2'] < sub_2_mean) & (dataset['sub-3'] < sub_3_mean) & (dataset['sub-4'] < sub_4_mean) & (dataset['sub-5'] < sub_5_mean) & (dataset['sub-6'] < sub_6_mean)]
            below_mean_sub_1=dataset[(dataset['sub-1'] < sub_1_mean)]
            below_mean_sub_2=dataset[(dataset['sub-2'] < sub_2_mean)]
            below_mean_sub_3=dataset[(dataset['sub-3'] < sub_3_mean)]
            below_mean_sub_4=dataset[(dataset['sub-4'] < sub_4_mean)]
            below_mean_sub_5=dataset[(dataset['sub-5'] < sub_5_mean)]
            below_mean_sub_6=dataset[(dataset['sub-6'] < sub_6_mean)]
            unique_students_sub_1= below_mean_sub_1.merge(below_mean_all_subjects, on=list(below_mean_sub_1.columns), how='left', indicator=True).query('_merge == "left_only"').drop(columns=['_merge'])
            unique_students_sub_2= below_mean_sub_2.merge(below_mean_all_subjects, on=list(below_mean_sub_2.columns), how='left', indicator=True).query('_merge == "left_only"').drop(columns=['_merge'])
            unique_students_sub_3= below_mean_sub_3.merge(below_mean_all_subjects, on=list(below_mean_sub_3.columns), how='left', indicator=True).query('_merge == "left_only"').drop(columns=['_merge'])
            unique_students_sub_4= below_mean_sub_4.merge(below_mean_all_subjects, on=list(below_mean_sub_4.columns), how='left', indicator=True).query('_merge == "left_only"').drop(columns=['_merge'])
            unique_students_sub_5= below_mean_sub_5.merge(below_mean_all_subjects, on=list(below_mean_sub_5.columns), how='left', indicator=True).query('_merge == "left_only"').drop(columns=['_merge'])
            unique_students_sub_6= below_mean_sub_6.merge(below_mean_all_subjects, on=list(below_mean_sub_6.columns), how='left', indicator=True).query('_merge == "left_only"').drop(columns=['_merge'])
            unique_students_sub_1=unique_students_sub_1.drop(['sub-2','sub-3','sub-4','sub-5','sub-6'], axis=1)
            unique_students_sub_2=unique_students_sub_2.drop(['sub-1','sub-3','sub-4','sub-5','sub-6'], axis=1)
            unique_students_sub_3=unique_students_sub_3.drop(['sub-1','sub-2','sub-4','sub-5','sub-6'], axis=1)
            unique_students_sub_4=unique_students_sub_4.drop(['sub-1','sub-2','sub-3','sub-5','sub-6'], axis=1)
            unique_students_sub_5=unique_students_sub_5.drop(['sub-1','sub-2','sub-3','sub-4','sub-6'], axis=1)
            unique_students_sub_6=unique_students_sub_6.drop(['sub-1','sub-2','sub-3','sub-4','sub-5'], axis=1)
            unique_students_sub_1['percentage to increase']=unique_students_sub_1.apply(lambda x: getPercentageToImproveAboveAverage(sub_1_mean,x['sub-1']), axis=1)
            unique_students_sub_2['percentage to increase']=unique_students_sub_2.apply(lambda x: getPercentageToImproveAboveAverage(sub_1_mean,x['sub-2']), axis=1)
            unique_students_sub_3['percentage to increase']=unique_students_sub_3.apply(lambda x: getPercentageToImproveAboveAverage(sub_1_mean,x['sub-3']), axis=1)
            unique_students_sub_4['percentage to increase']=unique_students_sub_4.apply(lambda x: getPercentageToImproveAboveAverage(sub_1_mean,x['sub-4']), axis=1)
            unique_students_sub_5['percentage to increase']=unique_students_sub_5.apply(lambda x: getPercentageToImproveAboveAverage(sub_1_mean,x['sub-5']), axis=1)
            unique_students_sub_6['percentage to increase']=unique_students_sub_6.apply(lambda x: getPercentageToImproveAboveAverage(sub_1_mean,x['sub-6']), axis=1)
            return (below_mean_all_subjects,unique_students_sub_1,unique_students_sub_2,unique_students_sub_3,unique_students_sub_4,unique_students_sub_5,unique_students_sub_6,sub_1_mean,sub_2_mean,sub_3_mean,sub_4_mean,sub_5_mean,sub_6_mean)
```

```python
sub_2_mean=dataset['sub-2'].mean()
```
```python

unique_students_sub_6.drop(['sub-1','sub-2','sub-3','sub-4','sub-5'], axis=1)

```
## How to use Websitef
<a href="">Click here to Watch the demo Video</a>

## Type of Inputs<br>
1.Email <br>
2.Count of Subjects <br>
3.CSV File for Processing <br>
4.Little patience 😁 <br>

## Version Control
GitClone LInk:https://github.com/saiguptha2003/EduTech_Analyser.git<br>
Zip_file Link:gh repo clone saiguptha2003/EduTech_Analyser<br>
cli link: git@github.com:saiguptha2003/EduTech_Analyser.git<br>
Contact EMail: saiguptha2003@gmail.com<br>

## Gallery
Just Visit the Deployment Link]

## Conclusion
In a world driven by data and technology, EduTech Analyser emerges as a vital tool for fostering academic success. With its user-friendly interface and powerful capabilities, this application bridges the gap between educators, students, and parents. For educational institutions, it streamlines the process of student assessment, enabling timely interventions to boost performance and enhance overall teaching practices. Meanwhile, for individuals, it empowers parents and private tutors to provide personalized support, fostering a nurturing learning environment for every student.

EduTech Analyser is a testament to the positive impact technology can have on education. By simplifying the complex task of student performance analysis, it paves the way for a brighter future, where each student's unique potential can be realized. As we navigate the ever-evolving landscape of education, this application stands as a beacon of innovation and collaboration, uniting all stakeholders in the pursuit of academic excellence.


# Cloud Deployment Link 
<a href="https://edutech-tmlv.onrender.com/">https://edutech-tmlv.onrender.com/</a>
