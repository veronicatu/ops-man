db = db.getSiblingDB("campaigns");
for(i=0; i < 2000; i++){
db.donations.find({contributor_occupation:"INVESTMENT BANKER"}).sort({amount:-1}).toArray();
db.donations.find({contributor_occupation:"INVESTMENT BANKER"}).toArray();
db.donations.find({contributor_occupation:"INVESTMENT BANKER"}).sort({candidate_name:1}).toArray();
};
