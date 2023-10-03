import re

def load_experiment_settings(path_of_command_file:str) -> dict:
    #load experiment settings
    setting_path = path_of_command_file
    with open(setting_path) as f:
        settings = f.read()
    matches=re.findall(r'(\w+)=(\S+)', settings) #キーと値のペアを取得
    tmp_dict = {key: value for key, value in matches}

    # dict itemのうち、"'something'" のような文字列を 'something' に変換
    experiment_settings = {}
    for key, value in tmp_dict.items():
        after = re.findall(r'["\'](.*?)["\']', value)
        print(after)
        if(len(after) == 0):
            experiment_settings[key] = value
        else:
            experiment_settings[key] = after[0]
    
    return experiment_settings