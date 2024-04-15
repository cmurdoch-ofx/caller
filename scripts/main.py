import json
import os


def main():

    missing_config = "File 'principle_engineers_data.csv' is not listed in the filename_to_value dictionary. Skipping."

    json_data = [{
            "team": "SRE",
            "template": "default",
            "summary": "Team tag config missing for Deprecating Lambdas job",
            "description": missing_config
    }]

    json_string = json.dumps(json_data)

    os.environ['JSON_INPUT'] = json_string

    print('Environment variable JSON_INPUT set to')
    print(os.environ['JSON_INPUT'])


if __name__ == "__main__":
    main()