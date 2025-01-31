import pandas as pd
import joblib

model = joblib.load("E:/Projects/Car_Evaluation_Project/artifacts/model.joblib")


def preprocess_input(input_dict):
    expected_columns = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety']

    df = pd.DataFrame(0, columns=expected_columns, index=[0])

    for key, value in input_dict.items():
        if key == 'buying' and value == 'vhigh':
            df['buying'] = 3
        elif key == 'buying' and value == 'high':
            df['buying'] = 2
        elif key == 'buying' and value == 'med':
            df['buying'] = 1
        elif key == 'buying' and value == 'low':
            df['buying'] = 0

        if key == 'maint' and value == 'vhigh':
            df['maint'] = 3
        elif key == 'maint' and value == 'high':
            df['maint'] = 2
        elif key == 'maint' and value == 'med':
            df['maint'] = 1
        elif key == 'maint' and value == 'low':
            df['maint'] = 0

        if key == 'doors' and value == '2':
            df['doors'] = 2
        elif key == 'doors' and value == '3':
            df['doors'] = 3
        elif key == 'doors' and value == '4':
            df['doors'] = 4
        elif key == 'doors' and value == '5more':
            df['doors'] = 5

        if key == 'persons' and value == '2':
            df['persons'] = 2
        elif key == 'persons' and value == '4':
            df['persons'] = 4
        elif key == 'persons' and value == 'more':
            df['persons'] = 5

        if key == 'lug_boot' and value == 'small':
            df['lug_boot'] = 0
        elif key == 'lug_boot' and value == 'med':
            df['lug_boot'] = 1
        elif key == 'lug_boot' and value == 'big':
            df['lug_boot'] = 2

        if key == 'safety' and value == 'low':
            df['safety'] = 0
        elif key == 'safety' and value == 'med':
            df['safety'] = 1
        elif key == 'safety' and value == 'high':
            df['safety'] = 2


    return df

def print_proper_output(int):
    if int == 0:
        return "Unaccurate"
    elif int == 1:
        return "Accurate"
    elif int == 2:
        return "Good"
    elif int == 3:
        return "Very Good"



def predict(input_dict):
    input_df = preprocess_input(input_dict)

    prediction = model.predict(input_df)

    return prediction