HomeTeam_HT_Score = int(input("Enter the home team halftime score: "))
AwayTeam_HT_Score = int(input("Enter the away team halftime score: "))

HomeTeam_FT_Score = int(input("Enter the home team fulltime score: "))
AwayTeam_FT_Score = int(input("Enter the away team halftime score: "))

TotalGoalsAfterHalfTime = (HomeTeam_FT_Score + AwayTeam_FT_Score) - (HomeTeam_HT_Score + AwayTeam_HT_Score)
print(TotalGoalsAfterHalfTime)