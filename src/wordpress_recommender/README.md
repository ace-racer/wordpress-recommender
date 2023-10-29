# Wordpress articles recommender app using Python
An application to recommend articles from a Wordpress blog based on user's query using semantic search

## Pre-requisites:
- Adjust the below environment variables before running any of the below steps if required:
    - `DATA_LOC`: Location where all the application data will be stored. By default, it is stored in a `data` folder in the current directory. This folder will be created if it does not exist during creation.
    - HuggingFace key (free) to use their inference endpoints to generate embeddings using Sentence Transformer models. Export the key to an environment variable called `HF_KEY` before creating or querying the index as shown in the steps below.
    - Override the default HuggingFace embeddings model by specifying the name in the environment variable `HF_EMBEDDINGS_MODEL_NAME`. If not provided, the `sentence-transformers/all-MiniLM-l6-v2` model is used to generate embeddings.

## How to use the CLI after installing the package from PyPI:
1. Download content: `wordpress-recommender download-content "https://learnwoo.com/post-sitemap1.xml"`
2. Build index using the downloaded content: `wordpress-recommender generate-index "https://learnwoo.com/post-sitemap1.xml"`
3. Query index built in previous step: `wordpress-recommender query-index "https://learnwoo.com/post-sitemap1.xml" --query "How are the AI regulations different in different parts of the world?"`

## Release notes:

### 0.1.1
- Initial release

### 0.1.2
- Allow client to override the default HuggingFace inference API embeddings model via the environment variable `HF_EMBEDDINGS_MODEL_NAME`
- Allow client to rebuild index by providing the option `--rebuild_index` in the CLI
- *Breaking change* Return final output as a sorted pandas dataframe with all original columns present along with a new column for the score e.g. `cosine_distance` or `cosine_similarity`
- Allow client to override the number of results returned by passing an optional `--top` parameter with an integer value

### 0.1.3
- Minor updates to docs
- Add tests
- Add GitHub Actions to publish package

