
def valid_legend(row):
    # Validate order legend
    field_error = []
    if row[1] != "Date":
        field_error.append(row[1])
    if row[2] != "HomeTeam":
        field_error.append(row[2])
    if row[3] != "AwayTeam":
        field_error.append(row[3])
    if row[4] != "FTHG":
        field_error.append(row[4])
    if row[5] != "FTAG":
        field_error.append(row[5])
    if row[6] != "FTR":
        field_error.append(row[6])
    if row[7] != "HTHG":
        field_error.append(row[7])
    if row[8] != "HTAG":
        field_error.append(row[8])
    if row[9] != "HTR":
        field_error.append(row[9])
    if row[10] != "Referee":
        field_error.append(row[10])
    if row[11] != "HS":
        field_error.append(row[11])
    if row[12] != "AS":
        field_error.append(row[12])
    if row[13] != "HST":
        field_error.append(row[13])
    if row[14] != "AST":
        field_error.append(row[14])
    if row[15] != "HF":
        field_error.append(row[15])
    if row[16] != "AF":
        field_error.append(row[16])
    if row[17] != "HC":
        field_error.append(row[17])
    if row[18] != "AC":
        field_error.append(row[18])
    if row[19] != "HY":
        field_error.append(row[19])
    if row[20] != "AY":
        field_error.append(row[20])
    if row[21] != "HR":
        field_error.append(row[21])
    if row[22] != "AR":
        field_error.append(row[22])
    if len(field_error) > 0:
        raise Exception('Field error: ' + ', '.join(field_error))
    return True
