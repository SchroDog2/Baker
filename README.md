## Nvidia Lambda Setup
# download uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# create venv
uv venv
source .venv/bin/activate

# env args
export HF_TOKEN=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

# install build tools
sudo apt update && sudo apt install ninja-build -y
sudo apt update && sudo apt install python3.11 python3.11-venv -y

# install
python3.11 -m venv --upgrade-deps venv
source venv/bin/activate

# initialize ilab
ilab config init
ilab model download
ilab model serve

# softlinks
ln -s /home/ubuntu/.local/share/instructlab/datasets ./datasets
ln -s ~/.config/instructlab/config.yaml ./config.yaml
ln -s ~/.local/share/instructlab/taxonomy ./taxonomy

# copy taxonomy
cp -r my-taxonomy/ /home/ubuntu/.local/share/instructlab/taxonomy
ilab taxonomy diff

## Generate qna.yaml for Walleye Capital
- generate qna.yaml using chatgpt and place in taxonomy finance category
- use python `wikipedia` and download walleye content in baker repo
```bash
(baker) jyu@JiaboAlienware:~/code/baker$ python ../wikipedia-markdown-generator/wiki-to-md.py Walleye_Capital
Markdown file created: md_output/Walleye_Capital.md
```

# generate synthetic data
ilab data generate
