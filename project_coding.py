import pandas as pd
import numpy as np

insurance = pd.read_csv("insurance.csv")
ages = insurance["age"]
sexes = insurance["sex"]
bmis = insurance["bmi"]
num_children = insurance["children"]
smoker_status = insurance["smoker"]
regions = insurance["region"]
charges = insurance["charges"]

print(insurance)


class PatientsInfo:
    def __init__(self, ages, sexes, bmis, num_children, 
                    smoker_status, regions, charges):
            self.ages = ages
            self.sexes = sexes
            self.bmis = bmis
            self.num_children = num_children
            self.smoker_status = smoker_status
            self.regions = regions
            self.charges = charges



    def average_age(self):
        total_age = 0
        for i in self.ages:
            total_age += i
        average_age = round(total_age/len(self.ages),1)
        print("The average age of the patients is: " + str(average_age))

    def smokers_percentage(self):
        smoker_count = 0
        for i in self.smoker_status:
            if i== "yes":
                smoker_count += 1
            else:
                continue
        smoker_count_perc = round(smoker_count/len(self.smoker_status) * 100,2)
        print(str(smoker_count_perc) + "% of patients are smokers")

    def sex_count(self):
        males = 0
        females = 0
        for sex in self.sexes:
            if sex == "female":
                females += 1
            else:
                males += 1
        print("There are " + str(males) + " male patiets and " + str(females) + " female patients")

    def unique_regions(self):
        unique_regions = []
        for region in self.regions:
            if region not in unique_regions: 
                unique_regions.append(region)
        print( "All patients belong to one of these regions:" + str(unique_regions))

    def average_charge(self):
        total_charge = 0
        for charge in self.charges:
            total_charge += charge
        average_charges = round(total_charge/(len(self.charges)),2)
        print("The average charge for patients is: " + str(average_charges) + " dollars")

    def create_dictionary(self):
        self.patients_dictionary = {}
        self.patients_dictionary["age"] = self.ages
        self.patients_dictionary["sex"] = self.sexes
        self.patients_dictionary["bmi"] = self.bmis
        self.patients_dictionary["children"] = self.num_children
        self.patients_dictionary["smoker"] = self.smoker_status
        self.patients_dictionary["regions"] = self.regions
        self.patients_dictionary["charges"] = self.charges
        return self.patients_dictionary


# Instance of Class

patients_analysis = PatientsInfo(ages, sexes, bmis, num_children, smoker_status, regions, charges)

# Testing of class functions

patients_analysis.smokers_percentage()
patients_analysis.sex_count()
patients_analysis.average_age()
patients_analysis.unique_regions()
patients_analysis.average_charge()
patients_analysis.create_dictionary()