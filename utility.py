
import pandas as pd

def getPercentageToImproveAboveAverage(average,marks):
    return 100*((average/marks)-1)

def get_dull_students(numberOfSubjects,file_path):
    import pandas as pd
    dataset=pd.read_csv(file_path)
    sub_1_mean=dataset['sub-1'].mean()
    sub_2_mean=dataset['sub-2'].mean()
    sub_3_mean=dataset['sub-3'].mean()
    sub_4_mean=dataset['sub-4'].mean()
    below_mean_all_subjects=dataset[(dataset['sub-1'] < sub_1_mean) & (dataset['sub-2'] < sub_2_mean) & (dataset['sub-3'] < sub_3_mean) & (dataset['sub-4'] < sub_4_mean)]
    below_mean_sub_1=dataset[(dataset['sub-1'] < sub_1_mean)]
    below_mean_sub_2=dataset[(dataset['sub-2'] < sub_2_mean)]
    below_mean_sub_3=dataset[(dataset['sub-3'] < sub_3_mean)]
    below_mean_sub_4=dataset[(dataset['sub-4'] < sub_4_mean)]
    unique_students_sub_1= below_mean_sub_1.merge(below_mean_all_subjects, on=list(below_mean_sub_1.columns), how='left', indicator=True).query('_merge == "left_only"').drop(columns=['_merge'])
    unique_students_sub_2= below_mean_sub_2.merge(below_mean_all_subjects, on=list(below_mean_sub_2.columns), how='left', indicator=True).query('_merge == "left_only"').drop(columns=['_merge'])
    unique_students_sub_3= below_mean_sub_3.merge(below_mean_all_subjects, on=list(below_mean_sub_3.columns), how='left', indicator=True).query('_merge == "left_only"').drop(columns=['_merge'])
    unique_students_sub_4= below_mean_sub_4.merge(below_mean_all_subjects, on=list(below_mean_sub_4.columns), how='left', indicator=True).query('_merge == "left_only"').drop(columns=['_merge'])
    unique_students_sub_1=unique_students_sub_1.drop(['sub-2','sub-3','sub-4'], axis=1)
    unique_students_sub_2=unique_students_sub_2.drop(['sub-1','sub-3','sub-4'], axis=1)
    unique_students_sub_3=unique_students_sub_3.drop(['sub-1','sub-2','sub-4'], axis=1)
    unique_students_sub_4=unique_students_sub_4.drop(['sub-1','sub-2','sub-3'], axis=1)
    unique_students_sub_1['percentage to increase']=unique_students_sub_1.apply(lambda x: getPercentageToImproveAboveAverage(sub_1_mean,x['sub-1']), axis=1)
    unique_students_sub_2['percentage to increase']=unique_students_sub_2.apply(lambda x: getPercentageToImproveAboveAverage(sub_1_mean,x['sub-2']), axis=1)
    unique_students_sub_3['percentage to increase']=unique_students_sub_3.apply(lambda x: getPercentageToImproveAboveAverage(sub_1_mean,x['sub-3']), axis=1)
    unique_students_sub_4['percentage to increase']=unique_students_sub_4.apply(lambda x: getPercentageToImproveAboveAverage(sub_1_mean,x['sub-4']), axis=1)
    return (below_mean_all_subjects,unique_students_sub_1,unique_students_sub_2,unique_students_sub_3,unique_students_sub_4,sub_1_mean,sub_2_mean,sub_3_mean,sub_4_mean)
        

