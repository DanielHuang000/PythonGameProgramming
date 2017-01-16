import GoogleClassroomPowerSchoolLib as G

G.ActivitiesNames(G.OriGoogleData('GoogleActivities.csv'))
Data1 = G.OriPowerSchoolData()
G.UpdatePowerSchool(Data1,G.OriGoogleData('GoogleActivities.csv'))
