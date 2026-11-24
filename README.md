# Scope3 - procurement-matching
NLP-based matching of procurement descriptions with emission-factor sectors for Scope 3 accounting.
# Automated Scope 3 Emissions Estimation – Procurement Data Matching

## Project overview

This project explores how natural language processing (NLP) techniques can support Scope 3 greenhouse gas accounting by automatically matching procurement descriptions with relevant economic sectors in an emission-factor database.

The project addresses a common challenge in spend-based emissions accounting: procurement records often contain unstructured text descriptions, making it difficult to consistently classify purchases and associate them with appropriate emission factors.

A Python pipeline was developed to compare three text-matching approaches and generate candidate sector classifications for human review.

## Objectives

- Process and clean procurement descriptions.
- Extract greenhouse gas emission factors from the US EPA USEEIO database.
- Compare classical text-matching techniques with semantic embeddings.
- Evaluate matching performance using manually assigned reference classifications.
- Generate a reproducible matching workflow with a human-review stage.

## Methodology

### 1. Data preparation

A synthetic procurement dataset containing 25 transactions was created to simulate purchasing activities.

The reference database was extracted from the US EPA USEEIO model and contains 402 sector-level greenhouse gas coefficients.

### 2. Text-matching approaches

Three approaches were implemented:

- Fuzzy matching: compares text based on character-level similarity using RapidFuzz.
- TF-IDF: represents descriptions through word importance and compares them using cosine similarity.
- Semantic embeddings: uses the Sentence Transformers model `all-MiniLM-L6-v2` to identify similarities in meaning.

### 3. Benchmarking

The three approaches were compared against manually assigned reference classifications.

| Method              | Top-1 accuracy | Top-3 accuracy |
| ------------------- | -------------: | -------------: |
| Fuzzy matching      |             8% |            12% |
| TF-IDF              |            36% |            44% |
| Semantic embeddings |            60% |            72% |

### 4. Human-review workflow

The semantic matching approach generates the three most similar sector candidates for each procurement transaction.

The workflow also calculates:

- Similarity score.
- Difference between the best and second-best candidate scores.
- Review priority.

A review template allows a human reviewer to approve or correct the suggested classification.

## Technologies

- Python
- Pandas and NumPy
- RapidFuzz
- Scikit-learn
- Sentence Transformers
- PyTorch
- Google Colab

## Project limitations

The procurement dataset is synthetic and does not represent actual ETH Zurich purchases.

The emission factors were extracted from the US EPA USEEIO model. They represent US economic sectors and are denominated in USD. Since the procurement data represents a Swiss purchasing context, the factors cannot be directly multiplied by the expenditure amounts to produce reliable emissions estimates.

The matching results are also preliminary: the manually assigned reference classifications are limited to 25 transactions, and the benchmark does not constitute an independent validation study.

A real-world implementation would require geographically and economically compatible emission factors, a larger validated dataset, and further testing with actual procurement records.

## Data sources

- US Environmental Protection Agency (EPA), USEEIO model: [EPA USEEIO](https://www.epa.gov/land-research/us-environmentally-extended-input-output-useeio-model)

