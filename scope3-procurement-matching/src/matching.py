def match_procurement_data(new_procurement_df, sector_data, model, sector_vectors):

    # Preserve the original procurement data
    data = new_procurement_df.copy()

    # Clean procurement descriptions
    data["description_clean"] = data["description"].apply(clean_text)

    # Convert descriptions into numerical embeddings
    procurement_vectors = model.encode(
        data["description_clean"].tolist(),
        convert_to_tensor=True,
        normalize_embeddings=True
    )

    # Compare procurement descriptions with the sector database
    similarity_matrix = procurement_vectors @ sector_vectors.T

    results = []

    # Find the three best sector candidates for each transaction
    for i, row in data.reset_index(drop=True).iterrows():

        scores = similarity_matrix[i].cpu().numpy()
        top_indices = scores.argsort()[-3:][::-1]

        for rank, sector_index in enumerate(top_indices, start=1):

            sector = sector_data.iloc[sector_index]

            results.append({
                "transaction_id": row["transaction_id"],
                "procurement_description": row["description"],
                "rank": rank,
                "sector_name": sector["Name"],
                "sector_id": sector["ID"],
                "similarity_score": scores[sector_index]
            })

    return pd.DataFrame(results)
