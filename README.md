## Nvidia Lambda Setup
# download uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# create venv
uv venv
source .venv/bin/activate

# env args
export HF_TOKEN=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

# initialize ilab
ilab config init

ilab model download
ilab model serve

## Generate qna.yaml for Walleye Capital
- generate qna.yaml using chatgpt and place in taxonomy finance category
- use python `wikipedia` and download walleye content in baker repo
```bash
(baker) jyu@JiaboAlienware:~/code/baker$ python ../wikipedia-markdown-generator/wiki-to-md.py Walleye_Capital
Markdown file created: md_output/Walleye_Capital.md
```
