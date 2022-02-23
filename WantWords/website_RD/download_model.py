import gdown


def download(file_id,output):
    url = f'https://drive.google.com/uc?id={file_id}'
    gdown.download(url, output, quiet=False)

download("1lyB8Xy7HzOeKYfzLmh96wpb0YJ8FGUws",'data_inUse1_en.npy')
download("1PGrmE-DhHmTEtCFmVCvRbDgJF8JnHrUB",'data_inUse1.npy')
download("18bhT131bLUaTNyyOoAsLPKfpYdTqj5zg",'data_inUse2_en.npy')
download("1AuYCZNpIyWSAcVvEQBmMZoF0n92VPNij",'data_inUse2.npy')
download("17-gov1ElBBl36W1KQSEp5gCChhU-HW78",'data_inUse3.npy')
download("1DC58EVkCC5g8rpa_GESEdL2YH9-W8-58",'En.model')
download("1UHdb7FedCWolUW0s2wc2IjJetR5N2NJP",'wd_def_for_website_En.json')
download("1PnAobFpR0-3j-GyD9ufaThezMzf8szFq",'wd_def_for_website_zh.json')
download("1zm1nqOvMmScNj43TTShJdJvo2d1j-GQq",'word_synsetWords.txt')
download("1WtQam0NpQV_GCewWQXpyALYOVgMHECq3",'word2synset_synset.txt')
download("1uz9Q-BxQREXiQDqwz6FacuulGAj5tK27",'Zh.model')
