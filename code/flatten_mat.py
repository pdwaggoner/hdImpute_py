def flatten_mat(cor_mat, return_mat=False):
    if not isinstance(cor_mat, pd.DataFrame):
        raise ValueError("cor_mat must be a Pandas DataFrame")

    ut = np.triu_indices_from(cor_mat, k=1)

    all_cor_mat = pd.DataFrame({
        'row': [cor_mat.index[i] for i in ut[0]],
        'column': [cor_mat.index[j] for j in ut[1]],
        'cor': [cor_mat.iloc[i, j] for i, j in zip(ut[0], ut[1])]
    })
    all_cor_mat = all_cor_mat.sort_values(by='cor', ascending=False)

    if return_mat:
        print(all_cor_mat)

    # interweave cols for batch creation
    df_x = all_cor_mat[['row']].rename(columns={'row': 'col'})
    df_y = all_cor_mat[['column']].rename(columns={'column': 'col'})

    print("Flattened and ranked")

    # create new df, ordered by correlation
    ranked = pd.concat([df_x, df_y]).drop_duplicates(subset='col')
    ranked = ranked.reset_index(drop=True)

    return ranked