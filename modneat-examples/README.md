## 使い方

### run\_task.py
`run_task.py` は、1回のタスクを実行するためのスクリプトです。
引数として以下をとります
- `network` 実験に用いるモデル名
- `config` 実験に用いるコンフィグファイル名
- `savedir` 実験結果を保存するディレクトリ名
- `task` 実験に用いるタスク名
- `generation` 実験実行時の世代数の上限
- `run_id` 実行時ID(保存ファイル名になります)

例: `python run_task.py --network ExHebbFFN --config ./configs/exhebb_genome.ini --generation 10 --task task.xor --savedir mydir --run_id 1 `

### 指定できるネットワーク
基本的にmodneat/nn/以下に実装されているモデルを指定できます。
- `ExHebbFFN` 拡張ヘブ則により重み更新を行うフィードフォワード型のモデル
- `ExHebbRNN` 拡張ヘブ則により重み更新を行うリカレント型のモデル
- `FeedForwardNetwork` 重み更新を行わない(デフォルトの) フィードフォワード型のモデル
- `RecurrentNetwork` 重み更新を行わない(デフォルトの) リカレント型のモデル
- `ModExHebbFNN` 拡張ヘブ則 & 修飾ニューロンで重み更新を行うモデル
...

ind..という名前のモデルは拡張ヘブ則の進化パラメータ(A, B, C, D)が各ノードごとに独立に定義されていることを示す

### taskについて
`task.py`の`xor`クラスを参考にして自分のタスクを実装してください

### run\_task\_parallel.sh
`run_task_parallel.sh`は、run\_task.pyを並列実行するためのスクリプトです。
引数に実験設定をとり、複数試行を並列で実行できます。
データもそれぞれ別の名前を付けて保存されます。
指定できる引数については`run_task_parallel.sh --help`を参考にしてください

例: `bash run_task_parallel.sh --network ModIndExHebbFFN --config_file ./configs/modindexhebb_genome.ini --task task.non_static`

### m\_dパラメータの意味
`m_d`はsoltoggioの実装で修飾されていないニューロンの重みをどれだけ更新するかを指定
0なら重み更新なし、大きな値なら拡張ヘブ則で重み更新
