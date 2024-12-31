from typing import Dict, List
from utils.dictionary import Dictionary
from faker import Faker
class DataGenerator:
    def __init__(self):
        self.max_field_count = 20
        
    def setter(self, data_dict: List[Dict[str, str]], field_name: str, field_type: str):
        # Check if the number of fields exceeds the max limit
        if not self.check(len(data_dict)):
            raise Exception("Maximum number of fields exceeded, Get Premium")
        
        # Append a dictionary with field name and field type
        data_dict.append({field_name: field_type})
        
    def check(self, field_count: int) -> bool:
        # Return whether the field count exceeds the max allowed fields
        return field_count <= self.max_field_count
        
    def translate(self,data_dict:List[Dict[str, str]])->List[Dict[str, str]]:
        # Placeholder for future translation logic
        translated_data_dict = []
        dictionary = Dictionary()
        for field in data_dict:
            for key,value in field.items():
                print(key,value)
                translated_data_dict.append({key:dictionary.get(value)})
        return translated_data_dict
        
    def generate(self,translated_data_dict:List[Dict[str, str]],records_count:int) -> List[Dict[str, str]]:
        # Placeholder for future generation logic
        fake = Faker()

        data = []
        for i in range(records_count):
            record = {}
            for field in translated_data_dict:
                for key,value in field.items():
                        record[key] = eval(f"fake.{value}")
                        # data.append({key:})
            data.append(record)
        return data
    def download(self):
        # Placeholder for future download logic
        pass
    
    # def main(self):
    #     # Ask the user for the number of fields
    #     field_count = int(input("Enter the number of fields:"))
    #     records_count = int(input("Enter the number of records to generate:"))
    #     # Initialize an empty list to hold the fields
    #     data_dict: List[Dict[str, str]] = []
        
    #     # Collect data for each field
    #     for i in range(field_count):
    #         field_name = input(f"Enter the name for field {i + 1}: ")
    #         field_type = input(f"Enter the type for field {i + 1}: ")
    #         self.setter(data_dict, field_name, field_type)
        
    #     # Output the final list of fields
    #     print("Data fields added:", data_dict)
    #     translated_data_dict = self.translate(data_dict)
    #     print("Translated data fields:",translated_data_dict)
    #     fake_data = self.generate(translated_data_dict,records_count)
    #     print("Generated fake data:",fake_data)
