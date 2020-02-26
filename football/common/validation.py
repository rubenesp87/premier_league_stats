
def valid_legend(row):
    # Validate order legend
    if row[1] != "Date":
        return False
    if row[2] != "HomeTeam":
        return False
    if row[3] != "AwayTeam":
        return False
    if row[4] != "FTHG":
        return False
    if row[5] != "FTAG":
        return False
    if row[6] != "FTR":
        return False
    if row[7] != "HTHG":
        return False
    if row[8] != "HTAG":
        return False
    if row[9] != "HTR":
        return False
    if row[10] != "Referee":
        return False
    if row[11] != "HS":
        return False
    if row[12] != "AS":
        return False
    if row[13] != "HST":
        return False
    if row[14] != "AST":
        return False
    if row[15] != "HF":
        return False
    if row[16] != "AF":
        return False
    if row[17] != "HC":
        return False
    if row[18] != "AC":
        return False
    if row[19] != "HY":
        return False
    if row[20] != "AY":
        return False
    if row[21] != "HR":
        return False
    if row[22] != "AR":
        return False
    return True
