#実行時引数にファイルパスを取る
import sys
import os
import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, help='', default='.')
    args = parser.parse_args()
    return args

if __name__=='__main__':
    args = create_parser()
    print(args.path)

    #パスを絶対パスに変換
    target_path=os.path.abspath(args.path)
    print(target_path)

    #target_path直下に /checkpoints ディレクトリと/settingsディレクトリが存在することを確認
    if not os.path.isdir(target_path + '/checkpoints') or not os.path.isdir(target_path + '/settings'):
        print('Error: There is no checkpoints directory or settings directory in the target path.')
        sys.exit()  
    else:
        print('OK')
    
    #target_path直下に /reports/ディレクトリが存在しない場合は作成
    os.makedirs(target_path + '/reports', exist_ok=True)

    #notebookファイルを target_path/reports/ にコピー
    notebook_dir = os.path.dirname(os.path.abspath(__file__)) + '/report_utils'
    ipynb_files = [f for f in os.listdir(notebook_dir) if f.endswith('.ipynb')]
    print("notebook_dir: ", notebook_dir)
    print(ipynb_files)