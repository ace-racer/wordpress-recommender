# An application to recommend articles from a Wordpress blog based on user's query using semantic search

## [Install Poetry](https://python-poetry.org/docs/) - Version 1.4.2

## Virtual environment management with Poetry

1. Create Python virtual environment using Poetry: `poetry install`
2. Start Poetry shell: `poetry shell`
3. Exit Poetry shell: `exit`

## How to run the application
- See the make commands as described in the steps below

### Pre-requisites:
- Python and Poetry are set up
- `make` is installed to be able to run commands from terminal, else run the commands from the make file directly in the terminal after supplying the required arguments
- Adjust the below environment variables before running any of the below steps if required:
    - `DATA_LOC`: Location where all the application data will be stored. By default, it is stored in a `data` folder in the current directory. This folder will be created if it does not exist during creation.
    - HuggingFace key (free) to use their inference endpoints to generate embeddings using Sentence Transformer models. Export the key to an environment variable called `HF_KEY` before creating or querying the index as shown in the steps below.

### Steps
1. Download all content from the target Wordpress blog, e.g.:  `make download-content sitemap_url="https://synergychronicler.wordpress.com/sitemap.xml"`
2. Create index after content is downloaded, e.g.: `export HF_KEY="hf_ywerwe..."` then `make generate-index sitemap_url="https://synergychronicler.wordpress.com/sitemap.xml"`
3. Query index, e.g.: `export HF_KEY="hf_ywerwe..."` then `make query-index sitemap_url="https://synergychronicler.wordpress.com/sitemap.xml" query="How are the AI regulations different in different parts of the world?"`
4. TODO

## Roadmap
- [X] Implement download content given a Wordpress sitemap and write downloaded content to a CSV file for further processing
- [X] Use a combination of langchain for content/text splitting options, sentence transformers to generate embeddings and Chroma to store the embeddings with metadata.
Apply this on the downloaded content and store the Chroma index to disk for now.
- [X] Create a query application, that given some metadata filters and text query will provide a ranked list of articles (e.g. top 5) from the Blog
- [ ] Evaluate the ranked list of articles that are returned by the approach
- [ ] Enhance the application to create social media posts using Large Language Models that use the contents from the blog
- [ ] Create a hosted product that can be used by others via Wordpress plugins

## Technical enhancements
- [X] Publish as a package to PyPI
- [ ] Add unit tests
- [ ] Write a build pipeline and use GitHub actions to trigger build process on code push and PR
